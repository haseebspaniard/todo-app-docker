import os
import time
import logging
from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
from prometheus_flask_exporter import PrometheusMetrics

load_dotenv()

app = Flask(__name__)
metrics = PrometheusMetrics(app)
app.secret_key = os.getenv('SECRET_KEY', 'fallback-secret')

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def get_db_connection(retries=5, delay=5):
    for attempt in range(retries):
        try:
            conn = mysql.connector.connect(
                host=os.getenv('MYSQL_HOST', 'db'),
                user=os.getenv('MYSQL_USER', 'todouser'),
                password=os.getenv('MYSQL_PASSWORD', ''),
                database=os.getenv('MYSQL_DATABASE', 'tododb')
            )
            if conn.is_connected():
                logger.info("Database connection successful")
                return conn
        except Error as e:
            logger.warning(f"Attempt {attempt+1}/{retries} - DB not ready: {e}")
            time.sleep(delay)
    logger.error("Could not connect to database after all retries")
    return None

@app.route('/')
def index():
    conn = get_db_connection()
    todos = []
    if conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM todos ORDER BY created_at DESC")
        todos = cursor.fetchall()
        cursor.close()
        conn.close()
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task', '').strip()
    if task:
        conn = get_db_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO todos (task) VALUES (%s)", (task,))
            conn.commit()
            cursor.close()
            conn.close()
            logger.info(f"Task added: {task}")
    return redirect(url_for('index'))

@app.route('/complete/<int:todo_id>', methods=['POST'])
def complete(todo_id):
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE todos SET completed = NOT completed WHERE id = %s",
            (todo_id,)
        )
        conn.commit()
        cursor.close()
        conn.close()
        logger.info(f"Task {todo_id} toggled")
    return redirect(url_for('index'))

@app.route('/delete/<int:todo_id>', methods=['POST'])
def delete(todo_id):
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM todos WHERE id = %s", (todo_id,))
        conn.commit()
        cursor.close()
        conn.close()
        logger.info(f"Task {todo_id} deleted")
    return redirect(url_for('index'))

@app.route('/health')
def health():
    conn = get_db_connection(retries=1, delay=1)
    if conn:
        conn.close()
        return {"status": "healthy", "database": "connected"}, 200
    return {"status": "unhealthy", "database": "disconnected"}, 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
