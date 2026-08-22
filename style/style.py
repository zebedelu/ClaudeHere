CSS = """
    Screen {
        align: center middle;
    }

    #painel {
        width: 70;
        height: auto;
        border: round green;
        padding: 1 2;
    }

    #titulo {
        text-align: center;
        text-style: bold;
        margin-bottom: 1;
    }

    #idioma {
        margin-top: 1;
        margin-bottom: 1;
    }

    #buttons {
        height: auto;
        margin-top: 1;
        align-horizontal: center;
    }

    Button {
        margin: 0 2;
        min-width: 16;
    }

    #status {
        margin-top: 1;
        height: 1;
        text-align: center;
    }
    
    .nothing_to_remove {
        color: grey;
    }
    #install_option {
        layout: horizontal;    /* radios lado a lado DENTRO do RadioSet */
        height: auto;          /* altura ajusta ao conteúdo */
        width: auto;           /* largura ajusta ao conteúdo */
        margin-right: 4;       /* espaço entre o RadioSet e o próximo elemento */
    }
    #options_title, #cli_title, #logos_title, #language_title {
        margin-top: 2;
    }
"""