import os
import sys

import psutil

from helpers import save_placeholders, load_placeholders



def restart(placeholders):
    save_placeholders(placeholders)
    for proc in psutil.process_iter():
        if proc.name() == 'cbman_listener.exe':
            p = psutil.Process(proc.pid)
            p.kill()

    os.startfile('cbman_listener.exe')


def add(placeholders, k, *v):
    placeholders[k] = ''.join(v)
    restart(placeholders)
    return placeholders


def rem(placeholders, k):
    del placeholders[k]
    restart(placeholders)
    return placeholders


def view(placeholders):
    if placeholders:
        print('Placeholders:')
        for k, v in placeholders.items():
            print(f'{k}: {v[:20]}')
    else:
        print('You have no placeholders! Add one by doing:\nadd <placeholder_name> <placeholder_value>')


def exit(placeholders):
    sys.exit(0)


CMDS = {
    'restart': restart,
    'add': add,
    'rem': rem,
    'view': view,
    'exit': exit,
}


def call_command(placeholders, cmd, *args):
    if cmd in CMDS:
        try:
            CMDS[cmd](placeholders, *args)
        except Exception as e:
            print(f'Error occured when running {cmd}:\n{e}')
    else:
        print(f'"{cmd}" could not be found!')


def main():
    phs = load_placeholders()
    print('Running Clipboard Manager')
    run = True
    while run:
        args = input('> ').split(' ')
        cmd = args.pop(0)
        call_command(phs, cmd, *args)


if __name__ == '__main__':
    main()
