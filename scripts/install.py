import winreg
from src.config import REGEDIT_INSTALL_PATHS, REGEDIT_SUBKEY_PATH, UNIVERSAL_END_COMMAND, UNIVERSAL_INITIAL_COMMAND
from src.options import OPTIONS, ALIAS
from lang.languages import langs

def install_aplication(app, cli_name, mark, lang):
    try:
        RSP = REGEDIT_SUBKEY_PATH
        for n, install_instructions in enumerate(REGEDIT_INSTALL_PATHS[cli_name]):
            if not mark[n]: continue
            ii = install_instructions
            with winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, RSP+"\\"+ii[0]) as chave:
                command_name = langs[lang][ii[1]].replace("{$1}", OPTIONS[ALIAS[cli_name]]["name"])
                winreg.SetValueEx(chave, "", 0, winreg.REG_SZ, command_name)
                with winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, RSP+"\\"+ii[0]+"\\command") as chave:
                    winreg.SetValueEx(chave, "", 0, winreg.REG_SZ, UNIVERSAL_INITIAL_COMMAND+ii[2])

        with winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, RSP) as chave:
            #Colocar a chave que foi baixado com sucesso
            winreg.SetValueEx(
                chave,
                "ClaudeHereInstalledSucessful",
                0,
                winreg.REG_DWORD,
                1
            )
    except Exception as ex:
        return [False, ex]

    return [True, "sucess"]