import os

def main():
    pwd = os.getcwd()
    print(pwd)
    print(pwd.parent)

if __name__=="__main__":
    main()