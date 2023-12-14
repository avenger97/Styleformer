# Import necessary modules from Flask
from flask import Flask, render_template, request
# Import the Styleformer class from the styleformer module
from styleformer import Styleformer

# Create a Flask web application instance
app = Flask(__name__)

# Initialize the Styleformer class with a specific style (style=2, Active to Passive)
styleformer = Styleformer(style=2)

# Define a route for the root URL ("/") that supports GET and POST requests
@app.route('/', methods=['GET', 'POST'])
def index():
    # Initialize the result variable to None
    result = None
    
    # Check if the request method is POST (form submission)
    if request.method == 'POST':
        # Retrieve the sentence from the submitted form
        sentence = request.form['sentence']
        
        # Use the Styleformer instance to transfer the sentence to passive style
        result = styleformer.transfer(sentence)
    
    # Render the 'index.html' template with the result to display on the web page
    return render_template('index.html', result=result)

# Run the Flask application if this script is executed
if __name__ == '__main__':
    app.run(debug=True)
