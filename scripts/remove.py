import winreg
from src.config import REGEDIT_INSTALL_PATHS, REGEDIT_SUBKEY_PATH
from src.options import LOGO_FILE_NAME, LOGO_BASE_DIR
import os

def remove_aplication(app):
    global LOGO_BASE_DIR
    # Remover a logo
    LOGO_BASE_DIR = os.path.expandvars(LOGO_BASE_DIR)

    try:
        os.remove(os.path.join(LOGO_BASE_DIR, LOGO_FILE_NAME))
        os.rmdir(LOGO_BASE_DIR)
    except:
        pass

    RSP = REGEDIT_SUBKEY_PATH
    for cli in REGEDIT_INSTALL_PATHS.values():
        for uninstall_instructions in cli:
            try:
                winreg.DeleteKey(winreg.HKEY_CLASSES_ROOT, REGEDIT_SUBKEY_PATH+"\\"+uninstall_instructions[0]+"\\command")
                winreg.DeleteKey(winreg.HKEY_CLASSES_ROOT, REGEDIT_SUBKEY_PATH+"\\"+uninstall_instructions[0])
            except FileNotFoundError:
                continue
            except:
                pass

    with winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, RSP) as chave:
        #Remover a chave que foi baixado com sucesso
        winreg.DeleteValue(
            chave,
            "ClaudeHereInstalledSucessful"
        )

    return [True, "sucess"]