#!/usr/bin/python3.8

import os
import sys

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
        if 'main' in str.casefold(ui):
            try:
                replace_qrc_import_on(ui)  # this fixes wrong import programatically...
            except BaseException as e:
                print(e)
                continue


def replace_qrc_import_on(filename):
    try:
        qrc_compiled = sys.argv[1]
    except:
        print('     >> no qrc file provided to replace imports with... omitting')
        return
    print('     >> detected: {} ...replacing imports'.format(qrc_compiled))
    ext = qrc_compiled.split('.')[1]
    if ext != 'py':
        raise TypeError('invalid extension <{}> for import, only .py supported'.format(ext))
    import_filename = qrc_compiled.split('.')[0]
    import_template = 'import packages.UI.icons.qrc.{}\n'.format(import_filename)

    file = open(os.sep.join([os.curdir,'{}.py'.format(filename)]), 'rt')
    data = file.readlines()
    replaced_data = map(
        lambda line: import_template if 'import {}\n'.format(import_filename) in line else line, data
    )
    file.close()
    file = open(os.sep.join([os.curdir, '{}.py'.format(filename)]), 'w')
    file.write(''.join(replaced_data))
    file.close()
    return






# todo improve script execution
if __name__ == '__main__':
    bulk_ui_compiler('.')
