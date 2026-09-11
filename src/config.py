REGEDIT_SUBKEY_PATH = r"directory\shell"
REGEDIT_SUCESS_INSTSALLED_SUBKEY_NAME = "ClaudeHereInstalledSucessful"

# Directory Name
# Name (ID)
# Command

REGEDIT_INSTALL_PATHS = {
    "openclaude":
    [
        [
            "openclaude",
            "open_open",
            "openclaude"
        ],
        [
            "openclaude continue",
            "open_continue",
            "openclaude --continue"
        ],
        [
            "openclaude history",
            "open_history",
            "openclaude --resume"
        ],
        [
            "openclaude (dsp)",
            "open_open_dsp",
            "openclaude --dangerously-skip-permissions"
        ],
        [
            "openclaude continue (dsp)",
            "open_continue_dsp",
            "openclaude --continue --dangerously-skip-permissions"
        ],
        [
            "openclaude history (dsp)",
            "open_history_dsp",
            "openclaude --resume --dangerously-skip-permissions"
        ],
    ],
    "claudecode":
    [
        [
            "claudecode",
            "open_open",
            "claude"
        ],
        [
            "claudecode continue",
            "open_continue",
            "claude --continue"
        ],
        [
            "claudecode history",
            "open_history",
            "claude --resume"
        ],
        [
            "claudecode (dsp)",
            "open_open_dsp",
            "claude --dangerously-skip-permissions"
        ],
        [
            "claudecode continue (dsp)",
            "open_continue_dsp",
            "claude --continue --dangerously-skip-permissions"
        ],
        [
            "claudecode history (dsp)",
            "open_history_dsp",
            "claude --resume --dangerously-skip-permissions"
        ]
    ],
    "opencode":
    [
        [
            "opencode",
            "open_open",
            "opencode"
        ],
        [
            "opencode continue",
            "open_continue",
            "opencode --continue"
        ],
        [
            "opencode history",
            "open_history",
            "opencode session list"
        ],
        [
            "opencode (dsp)",
            "open_open_dsp",
            "opencode --auto"
        ],
        [
            "opencode continue (dsp)",
            "open_continue_dsp",
            "opencode --continue --auto"
        ]
    ]
}
UNIVERSAL_INITIAL_COMMAND = '"C:\Windows\System32\cmd.exe" /c "cd /d %1 && '
UNIVERSAL_END_COMMAND = '"'