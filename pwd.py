import os
from pathlib import Path
def main():
    path = Path(__file__).resolve()
    print(path)
    print(path.parent)

if __name__=="__main__":
    main()