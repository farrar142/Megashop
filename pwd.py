import os


for path, dirs, files in os.walk(os.getcwd()):
    for i in files:
        print(path)
        if i == '.env':
            setting_path = path
            break