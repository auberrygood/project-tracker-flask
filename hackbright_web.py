"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')
    
    if not github:
        github = 'jhacks'

    first, last, github = hackbright.get_student_by_github(github)

    html = render_template("student_info.html",
                           first=first,
                           last=last,
                           github=github)
    return html
    # return f"{github} is the GitHub account for {first} {last}"

if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True, host="0.0.0.0")
