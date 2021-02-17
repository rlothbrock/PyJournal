#!/usr/bin/python3.8

import os


def find_uis_on_path(path):
    result = []
    for file in os.listdir(path):
        try:
            if file.split('.')[1] == 'ui' and os.path.isfile(file) and len(file.split('.')) > 1:
                result.append(file.split('.')[0])
        except:
            continue
    print(result)
    return result


def bulk_ui_compiler(path):
    uis = find_uis_on_path(path)
    for ui in uis:
        os.system("pyside2-uic {0}.ui -o {0}.py".format(ui))
        print('{0}.ui compiled to {0}.py'.format(ui))


# todo improve script execution
if __name__ == '__main__':
    bulk_ui_compiler('.')
