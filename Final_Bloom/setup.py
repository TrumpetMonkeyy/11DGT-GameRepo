import os
import subprocess
import sys

def install_requirements():
    req_path = os.path.join(os.path.dirname(__file__), 'requirements.txt')
    
    if os.path.exists(req_path):
        try:
            print("Installing requirements...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", req_path])
            print()
            print()
            print("Requirements installed, you can run the game now")
            os.system('pause')
        except subprocess.CalledProcessError:
            print("Failed to install requirements, please manually install the requirements from requirements.txt")
            os.system('pause')
            sys.exit(1)
    else:
        print("⚠️ requirements.txt not found.")
        os.system('pause')
        sys.exit(1)

install_requirements()
        