import io
from ppci.api import ir_to_python, c3toir
from ppci.arch.example import SimpleTarget


def run_it():
    bsp = io.StringIO("""
    module bsp;
    public function void sleep(int ms);
    public function void putc(byte c);
    public function bool get_key(int* key);
    """)

    ircode, debug_info = c3toir(
        ['snake/game.c3', 'snake/main.c3', '../librt/io.c3'],
        [bsp], SimpleTarget())

    with open('python_snake2.py', 'w') as f:
        print('import time', file=f)
        print('import sys', file=f)
        print('import threading', file=f)
        ir_to_python(ircode, f)

        print('', file=f)
        print('def bsp_putc(c):', file=f)
        print('    print(chr(c), end="")', file=f)
        print('def bsp_get_key(x):', file=f)
        print('    return 0', file=f)
        print('def bsp_sleep(x):', file=f)
        print('    time.sleep(x*0.001)', file=f)
        print('main_main()', file=f)

    print('Now run python_snake2.py !')

run_it()