import datetime
import threading

global clock_
global rerun
rerun = True


def app_clock(self, display_label):
    global clock_
    display_label.setText(datetime.datetime.now().__str__().split('.')[0])
    clock_ = threading.Timer(1, app_clock, [self, display_label])
    if rerun:
        clock_.start()


def kill_clock():
    global rerun
    rerun = False
    print('killing the clock')
    clock_.cancel()
    print('killing the clock ....done')

