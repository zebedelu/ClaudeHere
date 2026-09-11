CSS = """
    Screen {
        align: center middle;
    }

    #painel {
        width: 70;
        height: auto;
        max-height: 100%;
        overflow-y: auto;
        border: round green;
        padding: 2 2;
    }

    Checkbox, RadioButton, RadioSet, Button {
        border: none;
    }

    Button {
        margin: 0 2;
        min-width: 16;
    }
    
    .nothing_to_remove {
        color: grey;
    }
    #install_option {
        layout: horizontal;
        height: auto;
        width: auto;
        margin-right: 4;
    }

    #buttons {
        align: center middle;
    }
    #buttons > * {
        padding: 1 5;
    }
    
    #options_title, #cli_title, #logos_title, #buttons, #status {
        margin-top: 1;
    }

    #options, #buttons, #choice {
        height: auto;
    }

    .mark_for_install_option, #logo_option RadioButton {
        margin-top: 1;
    }
"""