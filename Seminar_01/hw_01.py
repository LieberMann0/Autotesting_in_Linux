# Написать функцию, которой передаются в качестве параметров команда и текст.
# Функция должна возвращать True, если команда успешно выполнена и текст найден
# в ее выводе и False в противном случае. Разбиение вывода использовать не нужно.

import subprocess
import re

if __name__ == '__main__':

    def func(com: str, text: str):
        result = subprocess.run(com, shell=True, stdout=subprocess.PIPE, encoding='utf 8')
        out = result.stdout        
        if result.returncode == 0:
            if re.search(text, out):
                print(True)
            else:
                print(False)
        else:
            print(False)


    func('cat /etc/os-release', 'jammy')
