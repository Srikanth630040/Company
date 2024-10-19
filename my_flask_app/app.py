from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Welcome to the Flask Application!</h1><p>Go to <a href='/htop'>/htop</a> to see system information.</p>"

@app.route('/htop', methods=['GET'])
def htop():
    # Get the server time in IST
    ist_time = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=5, minutes=30)))

    # Get the top output
    top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8')

    # Prepare the response with your name and username
    response = {
        "Name": "Srikanth Namoju",  # full name
        "Username": "srikanthnamoju06@gmail.com",  # username
        "Server Time (IST)": ist_time.strftime("%Y-%m-%d %H:%M:%S"),
        "TOP output": top_output
    }
    
    return f"""
    <h1>System Information</h1>
    <p>Name: {response['Name']}</p>
    <p>Username: {response['Username']}</p>
    <p>Server Time (IST): {response['Server Time (IST)']}</p>
    <h2>TOP output:</h2>
    <pre>{response['TOP output']}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
