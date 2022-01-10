import os
from pathlib import Path
def main():
    path = Path(__file__).resolve().parent
    f = open(f"{path.parent}/.env","r","UTF-8")
    target = open(f"{path}/.env","w","UTF-8")
    target.write(f)
    target.close()
    f.close()
    

if __name__=="__main__":
    main()