import subprocess


def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False


def test_step1():
    # test1
    assert checkout("cd /home/zerg/tst; 7z a ../out/arx2", "Everything is Ok"), "test1 FAIL"


def test_step2():
    # test2
    assert checkout("cd /home/zerg/out; 7z e arx2.7z -o/home/zerg/folder1 -y", "Everything is Ok"), "test2 FAIL"


def test_step3():
    # test3
    assert checkout("cd /home/zerg/out; 7z t arx2.7z", "Everything is Ok"), "test3 FAIL"
    