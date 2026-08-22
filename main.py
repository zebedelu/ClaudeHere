
# 120 x 30

from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Button, Checkbox, Footer, Header, Select, Static, RadioSet, RadioButton
from textual import on

from style.style import CSS
from src.options import OPTIONS, ALIAS, LOGOS
from lang.languages import langs
from scripts.detect_installed import detect_if_installed
from scripts.install import install_aplication
from scripts.remove import remove_aplication

claude_here_installed = False

class ClaudeHere(App):
    CSS = CSS
    install_option = OPTIONS[0]["name"]
    install_option_cli = OPTIONS[0]["id"]
    language = "en-us"
    install_option_logo = "claudecode"

    def __init__(self):
        super().__init__()

    def on_mount(self):
        self.update_language()
        self.change_remove_button()

    def compose(self) -> ComposeResult:
        yield Header()

        with Vertical(id="painel"):
            yield Static("",id="language_title", classes="lang")
            yield Select(
                [
                    ("English", "en-us"),
                    ("Português", "pt-br")
                ],
                prompt="",
                value="en-us",
                allow_blank=False,
                id="config_language",
                classes="lang"
            )

            yield Static("",id="cli_title",classes="lang")
            with Horizontal(id="choice"):
                yield RadioSet(
                    *[RadioButton(
                        option["name"],
                        value=(True if n == 0 else False),
                        id="install_option_"+option["id"])
                    for n, option in enumerate(OPTIONS)],
                    id="install_option"
                )

            yield Static("Logos",id="logos_title")

            yield RadioSet(
                *[RadioButton(
                    option["name"],
                    value=(True if n == 0 else False),
                    id="logo_option_"+option["id"])
                for n, option in enumerate(LOGOS.values())],
                id="logo_option"
            )

            yield Static("",id="options_title", classes="lang")

            yield Checkbox(
                "",
                value=True,
                id="open_open",
                classes="lang mark_for_install_option"
            )

            yield Checkbox(
                "",
                value=True,
                id="open_continue",
                classes="lang mark_for_install_option"
            )

            yield Checkbox(
                "",
                value=False,
                id="open_history",
                classes="lang mark_for_install_option"
            )
            
            yield Checkbox(
                "",
                value=False,
                id="open_open_dsp",
                classes="lang mark_for_install_option"
            )

            yield Checkbox(
                "",
                value=False,
                id="open_continue_dsp",
                classes="lang mark_for_install_option"
            )

            yield Checkbox(
                "",
                value=False,
                id="open_history_dsp",
                classes="lang mark_for_install_option"
            )

            with Horizontal(id="buttons"):
                yield Button(
                    "",
                    id="exit",
                    variant="default",
                    classes="lang"
                )

                yield Button(
                    "",
                    id="remove",
                    variant="default",
                    classes="lang",
                    disabled=True
                )

                yield Button(
                    "",
                    id="install",
                    variant="success",
                    classes="lang"
                )

            yield Static("", id="status")

        yield Footer()

    def update_language(self):
        for widget in self.query(".lang"):

            message = langs[self.language][widget.id]
            message = message.replace("{$1}", self.install_option)

            if isinstance(widget, Checkbox) or isinstance(widget, Button):
                widget.label = message
            elif isinstance(widget, Static):
                widget.update(message)

    @on(RadioSet.Changed, "#logo_option")
    def change_logo(self, event: RadioSet.Changed):
        self.install_option_logo = event.pressed.id.replace("logo_option_","")

    @on(RadioSet.Changed, "#install_option")
    def change_name(self, event: RadioSet.Changed):
        self.install_option = OPTIONS[
            ALIAS[
                event.pressed.id.replace("install_option_","")
            ]
        ]["name"]
        self.install_option_cli = event.pressed.id.replace("install_option_","")
        self.update_language()

    @on(Select.Changed, "#config_language")
    def change_language(self, event):
        self.language = event.value
        self.update_language()

    @on(Button.Pressed, "#exit")
    def exit_program(self):
        self.exit()

    @on(Button.Pressed, "#install")
    def install(self):
        global claude_here_installed

        logo = ""
        mark_for_install_option = [
            widget.value for widget in self.query(".mark_for_install_option")
        ]

        success, message = install_aplication(self, self.install_option_logo, self.install_option_cli, mark_for_install_option, self.language)

        if success:
            self.query_one("#status", Static).update(langs[self.language]["concluded"])
        else:
            self.query_one("#status", Static).update(langs[self.language]["something_went_wrong"]+" "+message)

        claude_here_installed = detect_if_installed()
        self.change_remove_button()

    @on(Button.Pressed, "#remove")
    def remover(self):
        global claude_here_installed

        remove_aplication(self)

        self.query_one("#status", Static).update(langs[self.language]["removed_concluded"])

        claude_here_installed = detect_if_installed()
        self.change_remove_button()

    def change_remove_button(self):
        if claude_here_installed:
            botao = self.query_one("#remove", Button)
            botao.variant = "error"
            botao.disabled = False
            botao.remove_class("nothing_to_remove")
        else:
            botao = self.query_one("#remove", Button)
            botao.variant = "default"
            botao.disabled = True
            botao.add_class("nothing_to_remove")

if __name__ == "__main__":
    app = ClaudeHere()
    claude_here_installed = detect_if_installed()
    app.run()