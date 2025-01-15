from flask import Flask, render_template
import csv
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('main.html')

# Get project details
def get_projects():
    projects = []
    with open('static/data/project_data.csv', 'r', encoding='utf-8-sig') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            projects.append(row)
            print(row)
    return projects

@app.route("/projects")
def projects():
    project_data = get_projects()
    return render_template('projects.html', projects=project_data)

if __name__ == "__main__":
    app.run(debug=True)