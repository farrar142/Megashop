import os,sys
from datetime import datetime
def get_now():
    """
    make a string by current time
    """
    now=datetime.now()
    nows = [now.year,now.month,now.day,now.hour,now.minute,now.second]
    nowtime = ""
    for i in nows:
        nowtime = nowtime + str(i).zfill(2)
    return nowtime
def argv_or_input():
    message = ""
    if len(sys.argv) >= 2:
        for i in sys.argv[1:]:
            message += i+" "
    else:
        message = input("commit message)\n")
    return message
if __name__ == "__main__":    
    message = argv_or_input()
    if not message:
        print(message)
        os.system(f"git pull")
    else:
        f = open("newfile.txt",'w')
        f.write(f"test{get_now()}")
        f.close()
        os.system(f"git config --unset --global user.name")
        os.system(f"git config --unset --global user.email")
        os.system(f"git config --global user.name farrar142")
        os.system(f"git config --global user.email gksdjf1690@gmail.com")
        os.system(f"git config user.name farrar142")
        os.system(f"git config user.email gksdjf1690@gmail.com")
        os.system(f"git add . && git commit -m \"{message}\" && git push origin master")
        os.remove("./newfile.txt")