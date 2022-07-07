import ctypes
import os
import subprocess
import sys

from win32comext.shell.shell import ShellExecuteEx


def has_admin():
    if os.name != 'nt':
        return (os.environ['SUDO_USER'], True) if 'SUDO_USER' in os.environ and os.geteuid() == 0 else (
        os.environ['USERNAME'], False)

    try:
        # only windows users with admin privileges can read the C:\Windows\Temp
        temp = os.listdir(os.sep.join([os.environ.get('SystemRoot', 'C:\\Windows'), 'Temp']))
    except Exception:
        # return (os.environ['USERNAME'], False)
        return False
    else:
        # return (os.environ['USERNAME'], True)
        return True

def run_program(executable, show_console):
    ShellExecuteEx(
        fMask=0x00000040 | 0x00008000,
        hwnd=None,
        lpVerb='runas',
        lpFile=executable,
        nShow=int(show_console)
    )


def elevate(executable: str, show_console=True):
    """
    Re-launch the current process with root/admin privileges

    When run as root, this function does nothing.

    When not run as root, this function replaces the current process (Linux,
    macOS) or creates a child process, waits, and exits (Windows).

    :param show_console: (Windows only) if True, show a new console for the
        child process. Ignored on Linux / macOS.
    """
    if sys.platform.startswith("win"):
        # from elevate.windows import elevate
    # else:
    #     from elevate.posix import elevate
        run_program(os.path.abspath(executable), show_console)

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() == 0
    except:
        return False
