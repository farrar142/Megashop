import os
from pathlib import Path
def env_getter():
    path = Path(__file__).resolve().parent
    print(path)
    f = open(f"{str(path.parent)}/.env","r",encoding="UTF-8")
    target = open(f"{str(path)}/.env","w",encoding="UTF-8")
    target.write(f.read())
    target.close()
    f.close()
    

if __name__=="__main__":
    main()