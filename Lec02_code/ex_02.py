import subprocess


def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    # test1
    if checkout("cd /home/zerg/tst; 7z a ../out/arx2", "Everything is Ok"):
        print("test1 SUCCESS")
    else:
        print("FAIL")
    # test2
    if checkout("cd /home/zerg/out; 7z e arx2.7z -o/home/zerg/folder1 -y", "Everything is Ok"):
        print("test2 SUCCESS")
    else:
        print("FAIL")
    # test3
    if checkout("cd /home/zerg/out; 7z t arx2.7z", "Everything is Ok"):
        print("test3 SUCCESS")
    else:
        print("FAIL")
        