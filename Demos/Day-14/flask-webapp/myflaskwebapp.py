from flask import Flask
# Initiate the Flask application instance 

app = Flask(__name__)

# define the route for the main home page URL ("/")

@app.route("/")
def home():
    return "<h1>Hello Python Flask web app</h1><p> Welcome to Python Flask Automation </p>"

# Run the local development server with executing the script directly. 

if __name__ == "__main__":
    app.run(debug=True, port=8000)