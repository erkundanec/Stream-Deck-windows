from flask import Flask, render_template
import subprocess
import webbrowser

app = Flask(__name__)

# Function to handle launching applications
def launch_application(application_name):
    try:
        subprocess.Popen([application_name], shell=True)
        return "Application launched: {}".format(application_name)
    except Exception as e:
        return "Error launching application {}: {}".format(application_name, str(e))

# Function to handle system commands
def perform_system_command(command):
    try:
        subprocess.Popen(command, shell=True)
        return "System command executed: {}".format(command)
    except Exception as e:
        return "Error executing system command {}: {}".format(command, str(e))

# Function to open a specific website
def open_website(website_url):
    try:
        webbrowser.open(website_url)
        return "Website opened: {}".format(website_url)
    except Exception as e:
        return "Error opening website {}: {}".format(website_url, str(e))

@app.route('/')
def index():
    return render_template('index.html')

# Example route to launch an application
@app.route('/launch/<application_name>')
def launch_route(application_name):
    result = launch_application(application_name)
    return result

# Example route to perform a system command
@app.route('/system/<command>')
def system_route(command):
    result = perform_system_command(command)
    return result

# Example route to open a website
@app.route('/open/<website_url>')
def open_website_route(website_url):
    result = open_website(website_url)
    return result

if __name__ == '__main__':
    app.run(debug=True, host='192.168.0.7', port=12135)

