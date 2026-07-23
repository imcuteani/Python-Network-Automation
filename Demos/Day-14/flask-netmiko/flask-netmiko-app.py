# This application is basically to connect a Flask web app to a network device using Netmiko, you can capture 
# user input from a web form, pass it into a Netmiko connection handler and display the command output from GNS3 
# on the webpage. 

from flask import Flask, render_template_string, request
from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoTimeoutException, NetmikoAuthenticationException

app = Flask(__name__)

# Single-file HTML template using Flask's render_template string

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
 <title> Netmiko Flask Example </title>
</head>
<body>
 <div class="container">
 <h2> Network Device Command </h2>
 <form method="POST">
  <div class="form-group">
    <label>Device Type</label>
    <input type="text" name="device_type" value="cisco_ios_telnet" required>
   </div>
  <div class="form-group">
   <label>Device host IP</label>
   <input type="text" name="ip" value="192.168.80.128" required>
  </div>
  <div class="form-group">
    <label>host port:</label>
    <input type="text" name="port" value="5008" required>
    </div>
  <div class="form-group">
  <label>Username:</label>
  <input type="text" name="username" value="admin" required>
  </div>
 <div class="form-group">
  <label>Password:</label>
  <input type="text" name="password" value="cisco123" required>
  </div>
  <div class="form-group">
    <label>Command:</label>
    <input type="text" name="password" value="show ip interface brief" required>
    </div>
    <button type="submit">Execute Command</button>
</form>

{% if output %}
<h3> Result: </h3>
<pre>{{ output }} </pre>
{% endif %}

{% if error %}
<h3> Error: </h3>
<p class="error">{{ error }}</p>
{% endif %}

</div>
</body>
</html>
  
"""
@app.route('/', methods=['GET', 'POST'])
def index():
    output = None
    error = None 

    if request.method == 'POST':
        # Extract the HTML form data
       device_type = request.form.get('device_type') 
       ip = request.form.get('ip')
       port = request.form.get('port') 
       username = request.form.get('username')
       password = request.form.get('password')
       command = request.form.get('command')

    # define the Netmiko device parameters 
    device_params = {
        'device_type': 'cisco_ios_telnet',
        'host': '192.168.80.128',
        'port': '5008',
        'username': 'admin',
        'password': 'cisco123',

    }


    try: 
        # establish SSH command with the device 
        with ConnectHandler(**device_params) as net_connect:
            net_connect.enable()
            output = net_connect.send_command("show ip interface brief", read_timeout=120)
    except NetmikoTimeoutException:
        error = f"Connection timed out to {ip}, check the device connection"
    except NetmikoAuthenticationException:
        error = f"Authentication failed, check the username and password."
    except Exception as e:
        error = f"An unexpected exception has occurred: {str(e)}"

    return render_template_string(HTML_TEMPLATE, output=output, error=error)                       


if __name__ == '__main__':
    # Run in debug mode for dev env 
    app.run(host='0.0.0.0', port=5000, debug=True)