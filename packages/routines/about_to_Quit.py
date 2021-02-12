from packages.modules.app_clock import kill_clock


def about_to_quit_routine():
    kill_clock()
