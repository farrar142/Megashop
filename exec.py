import os,sys

def argv_or_input():
    message = ""
    if len(sys.argv) >= 2:
        for i in sys.argv[1:]:
            message += i
    else:
        message = input("commit message)\n")
    return message

def main():
    container = argv_or_input()
    os.system(f"docker exec -it {container} /bin/bash")

if __name__ == "__main__":
    main()