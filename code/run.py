import subprocess
import threading
import os

# Function to install Python dependencies
def install_python_dependencies():
    requirements_path = os.path.join('..', 'requirements.txt')
    if os.path.exists(requirements_path):
        print("Installing Python dependencies...")
        subprocess.run(["pip", "install", "-r", requirements_path], check=True)
    else:
        print("No 'requirements.txt' file found, skipping Python dependency installation.")

# Function to install Next.js dependencies
def install_nextjs_dependencies():
    client_path = os.path.join("..", "code", "client")
    if os.path.exists(os.path.join(client_path, "package.json")):
        print("Installing Next.js dependencies...")
        subprocess.run(["npm", "install"], cwd=client_path, check=True)
    else:
        print("No 'package.json' found, skipping Next.js dependency installation.")

# Function to run model_save.py
def run_model_save():
    try:
        print("Running model_save.py...")
        subprocess.run(["python", "./server/model_save.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running model_save.py: {e}")

# Function to run the Flask server
def run_flask():
    try:
        print("Running Flask server...")
        subprocess.run(["python", "./server/server.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running Flask: {e}")

# Function to run the Next.js app using "npm run dev"
def run_nextjs():
    client_path = os.path.join( "client")
    try:
        subprocess.run(["npm", "run", "dev"], cwd=client_path, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running Next.js: {e}")

if __name__ == '__main__':
    # install_python_dependencies()
    # install_nextjs_dependencies()

    run_model_save()

    # Start Flask server in a separate thread
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()

    # Start Next.js frontend in the main thread
    run_nextjs()