# Web Application with uWSGI and Flask

## Description
This is a capstone assignment to demonstrate your ability to create a production-ready Python web application. You'll use Flask, uWSGI, eventlet, HTML templating, and containerization. A skeleton of the project has already been provided at `compprog_students/web_app`.

## Instructions

Complete the following steps to fulfill the assignment requirements:

1. **Python Package**
    - Create a Python package from your web application.
    - The package must be distributable as a wheel.
    - Use `pyproject.toml`, `setup.cfg`, and `tox.ini` for configuration.
    - Define an appropriate `entry_point` in `setup.cfg`.
    - Follow all applicable PEP guidelines (PEP 8, PEP 20).

2. **Flask Web Application**
    - The app must have at least one **GET** and one **POST** endpoint.
    - You must render at least one HTML page using Flask (use Jinja2 templates).
    - The page must contain user input elements such as buttons or input fields.
    - Use Flask’s `render_template()` and `request.form` as needed.

3. **Server Runtime**
    - Use **eventlet** as the runtime engine for your Flask application.
    - Ensure the app can be run using `eventlet.wsgi.server`.

4. **Containerization**
    - Containerize your application using Docker.
    - The Docker image must install the Python package and run your app using `uwsgi`.

5. **Testing**
    - Confirm that the application runs locally, correctly serving the HTML page.
    - Verify POST requests are handled and processed.
    - Confirm it works both with `tox` and inside the container.

6. **Submission**
    - All files should reside under the `compprog_students/web_app` directory.
    - Add, commit, and push everything to your main branch on GitHub.
    - Submit the URL of the GitHub repo or PR.

## Examples & Test Cases

| Action                     | Expected Result                                  |
|----------------------------|--------------------------------------------------|
| `curl http://localhost:8080/` | Returns rendered HTML with form elements        |
| Submit HTML form           | POSTs to the backend and displays new content    |
| Build Docker image         | Image builds without error                       |
| Run `tox`                  | Passes tests and builds wheel                    |

## Submission Checklist
- [ ] Package builds a wheel and installs successfully.
- [ ] Application includes at least one GET and one POST endpoint.
- [ ] HTML page is rendered with user input elements.
- [ ] Flask app uses eventlet as the server.
- [ ] Docker container builds and runs the app correctly.
- [ ] Code follows PEP 8 and PEP 20.
- [ ] Code is committed and pushed to GitHub.
- [ ] URL submitted.

## Grading Criteria

| Criteria                             | Points |
|--------------------------------------|--------|
| Flask app with GET/POST endpoints    | 5 pts  |
| Rendered HTML with user interaction  | 5 pts  |
| Uses eventlet for serving            | 4 pts  |
| Docker container builds/runs         | 4 pts  |
| Package builds as a wheel            | 3 pts  |
| Style and documentation              | 4 pts  |

**Total**: 25 points

## Resources
- [Flask Documentation](https://flask.palletsprojects.com/)
- [PEP 8](https://peps.python.org/pep-0008/)
- [PEP 20](https://peps.python.org/pep-0020/)
- [Docker Documentation](https://docs.docker.com/)
- [uWSGI Documentation](https://uwsgi-docs.readthedocs.io/)
