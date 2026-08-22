import winreg

from src.config import REGEDIT_SUBKEY_PATH, REGEDIT_SUCESS_INSTSALLED_SUBKEY_NAME
from lang.languages import langs

def detect_if_installed():
    subkey_exists = [True, "installed"]
    try:
        with winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, REGEDIT_SUBKEY_PATH, 0, winreg.KEY_READ) as key:
            winreg.QueryValueEx(key, REGEDIT_SUCESS_INSTSALLED_SUBKEY_NAME)
    except FileNotFoundError:
        subkey_exists = [False, 'not_installed']
    except PermissionError:
        subkey_exists = [False, 'access_denied']
    except Exception as ex:
        subkey_exists = [False, ex]

    # se não tiver permissão para acessar, então, fala ao usuário
    if subkey_exists[1] == 'access_denied':
        print(langs["en-us"]["message_access_denied"])
        input()

    elif subkey_exists[0] == False and subkey_exists[1] != "not_installed":
        print("Error:" +subkey_exists[1])

    return subkey_exists[0]