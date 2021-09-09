from pathlib import Path
path = './dataset'
basepath = Path(path)
if __name__ == '__main__':
    print(basepath.name)
