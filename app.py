# app.py

from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

# Define the data for the group members (moved from JavaScript to Python)
team_data = [
    {'nama': 'Sigit Tri Atmaja', 'nim': '23.83.1002', 'job': 'Ketua'},
    {'nama': 'Zhewa Alvarizi M', 'nim': '23.83.1012', 'job': 'Anggota'},
    {'nama': 'Raka Tirta Wahyudi', 'nim': '23.83.0991', 'job': 'Anggota'},
    {'nama': 'Gabriel Mahesa Surendra', 'nim': '23.83.1006', 'job': 'Anggota'},
    {'nama': 'Mohd Hafiz Al haq Haeruddin', 'nim': '22.83.0946', 'job': 'Anggota'}
]

# Define the route for the home page ('/')
@app.route('/')
def index():
    # Renders the 'index.html' template and passes the team_data to it
    # The 'index.html' will now use Jinja2 templating to display the data
    return render_template('index.html', group_data=team_data)

# Standard entry point to run the application
if __name__ == '__main__':
    # Set debug=True for easier development (reloads on file changes)
    app.run(debug=True)