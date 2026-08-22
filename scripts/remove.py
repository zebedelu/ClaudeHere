import winreg
from src.config import REGEDIT_INSTALL_PATHS, REGEDIT_SUBKEY_PATH
from lang.languages import langs

def remove_aplication(app):
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