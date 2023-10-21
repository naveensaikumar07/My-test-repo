from flask import Flask, render_template
import psycopg2

app = Flask(__name)

# Define the database connection parameters
db_host = "postgresql"  # This should match the StatefulSet name or Service name
db_name = "mydatabase"
db_user = "myuser"
db_password = "mypassword"

def get_data_from_database():
    # Write code here to fetch data from the database using psycopg2
    # Example: Use psycopg2 to execute a SELECT query

@app.route('/')
def index():
    # Fetch data from the database using your application code
    data = get_data_from_database()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

