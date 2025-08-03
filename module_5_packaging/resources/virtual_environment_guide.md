# Creating and Using a Virtual Environment in Python

A **virtual environment** is an isolated Python environment that allows you to install packages without affecting the system-wide Python installation.

## Steps to Create and Use a Virtual Environment

### 1. Navigate to Your Project Directory
```bash
cd /proj
```

### 2. Create the Virtual Environment
Use the `venv` module to create a virtual environment. You can name it whatever you like:
```bash
python3 -m venv example.venv
```

### 3. Activate the Virtual Environment
Activate it using the `source` command:
```bash
source example.venv/bin/activate
```

You should now see your environment name prefixed in your terminal prompt.

### 4. Use the Virtual Environment
You can now install packages and use Python as usual:
```bash
python3 -m pip install fuzzywuzzy
python3 -c "import sys; print(sys.executable)"
```

This will show the path to the Python interpreter inside the virtual environment.

### 5. Deactivate the Virtual Environment
To exit the virtual environment:
```bash
deactivate
```

This returns you to your system-wide Python interpreter.

---

Virtual environments are a best practice in Python development. They prevent dependency conflicts and help manage isolated project setups.
