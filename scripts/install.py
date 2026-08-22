import winreg
from src.config import REGEDIT_INSTALL_PATHS, REGEDIT_SUBKEY_PATH, UNIVERSAL_END_COMMAND, UNIVERSAL_INITIAL_COMMAND
from src.options import OPTIONS, ALIAS, LOGO_BASE_URL, LOGOS, LOGO_BASE_DIR, LOGO_FILE_NAME
from lang.languages import langs
import requests, os

def install_aplication(app, logo, cli_name, mark, lang):
    global LOGO_BASE_DIR
    # Baixar a logo
    LOGO_BASE_DIR = os.path.expandvars(LOGO_BASE_DIR)
    try:
        response = requests.get(
            LOGO_BASE_URL + LOGOS[logo]["url"],
            timeout=15
        )

        if response.status_code == 200:
            os.makedirs(LOGO_BASE_DIR, exist_ok=True)

            logo_dir = os.path.join(LOGO_BASE_DIR, LOGO_FILE_NAME)

            with open(logo_dir, "wb") as file:
                file.write(response.content)
        else:
            return [False, f"Erro HTTP: {response.status_code}"]

    except requests.exceptions.RequestException as erro:
        return [False, str(erro)]

    try:
        RSP = REGEDIT_SUBKEY_PATH
        for n, install_instructions in enumerate(REGEDIT_INSTALL_PATHS[cli_name]):
            if not mark[n]: continue
            ii = install_instructions

            # chave
            with winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, RSP+"\\"+ii[0]) as chave:
                command_name = langs[lang][ii[1]].replace("{$1}", OPTIONS[ALIAS[cli_name]]["name"])
                winreg.SetValueEx(chave, "", 0, winreg.REG_SZ, command_name)
                
                logo_dir = LOGO_BASE_DIR+LOGO_FILE_NAME
                winreg.SetValueEx(chave, "Icon", 0, winreg.REG_SZ, logo_dir)

                # /command
                with winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, RSP+"\\"+ii[0]+"\\command") as chave:
                    winreg.SetValueEx(chave, "", 0, winreg.REG_SZ, UNIVERSAL_INITIAL_COMMAND+ii[2]+UNIVERSAL_END_COMMAND)

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
        return [False, str(ex)]

    return [True, "sucess"]