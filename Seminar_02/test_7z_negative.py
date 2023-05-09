from checkout import checkout

path_dir = '/home/user/tst'
path_arx = 'arx1.7z'
path_to_dir = '/home/user/out'


def test_step7():
    # test7
    assert checkout(f"cd {path_dir}; 7z e {path_arx} -o{path_to_dir}", "ERROR: "), "Test7 Fail"


def test_step8():
    # test8
    assert checkout(f"cd {path_dir}; 7z t {path_dir, path_arx}", "Everything is Ok"), "Test8 Fail"
