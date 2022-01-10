import dotenv,os

def read_env():
    env_path = ""
    for path, dirs, files in os.walk(os.getcwd()):
        for i in files:
            if i == '.env':
                setting_path = path
                break
    dotenv.read_dotenv(setting_path)