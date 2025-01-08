from flask import Flask, render_template
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__,
           template_folder='../templates',
           static_folder='../static')

@app.route('/')
def home():
    """Home page route."""
    return render_template('index.html', title='Crypto News Aggregator')

if __name__ == '__main__':
    # Run the app in debug mode for development
    app.run(debug=True) 