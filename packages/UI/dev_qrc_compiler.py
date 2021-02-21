#!/usr/bin/python3.8

import os
import sys

def find_qrc_on_path(path):
    result = []
    for file in os.listdir(path):
        try:
            filename = file.split('.')
            if filename[1] == 'qrc' and not os.path.isdir(file) and len(filename) == 2:
                result.append(filename[0])
        except:
            continue
    print(result)
    return result


def bulk_ui_compiler(path):
    qrcs = find_qrc_on_path(path)
    for qrc in qrcs:
        processed_filename = '{1}{2}{0}'.format(qrc,path,os.sep)
        os.system("pyside2-rcc {0}.qrc -o {0}_rc.py".format(processed_filename))
        print('{0}.qrc compiled to {0}_rc.py'.format(processed_filename))


# todo improve script execution
if __name__ == '__main__':
    print('dev: sys.argv: {}'.format(sys.argv))
    try:
        path = sys.argv[1]
    except:
        path = './icons/qrc'
    finally:
        bulk_ui_compiler(path)
