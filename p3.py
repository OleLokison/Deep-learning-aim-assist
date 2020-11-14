from win32gui import GetWindowText, EnumWindows
def enum_window_titles():
    #returns all open window class names
    def callback(handle, data):
        titles.append(GetWindowText(handle))
    titles = []
    EnumWindows(callback, None)
    return titles
print(enum_window_titles())