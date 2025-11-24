def user_live_update():
    # disable the do you want to close dialog
    root_window.tk.call("wm","protocol",".","WM_DELETE_WINDOW","destroy .")