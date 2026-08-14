"""
Genera assets/terminal.gif: un boot Linux retro seguito da un
blocco neofetch personalizzato con le info del profilo di perox.

Basato su github-readme-terminal (x0rzavi/github-readme-terminal),
libreria "gifos" - https://github.com/x0rzavi/github-readme-terminal
"""

import gifos

LOGO = [
    r" ____  ______ ____   ___  __  __",
    r"|  _ \|  ____|  _ \ / _ \\ \/ /",
    r"| |_) | |__  | |_) | | | |\  / ",
    r"|  __/|  __| |  _ <| |_| |/  \ ",
    r"|_|   |______|_| \_\\___//_/\_\\",
]

BOOT_LINES = [
    "[ OK ] Started perox-portfolio.service",
    "[ OK ] Mounted /dev/creativity",
    "[ OK ] Loaded modules: cad, saldatore, python.so",
    "[ OK ] Reached target Robotics Multi-User",
    "",
    "perox-os login: perox",
    "Password: ****************",
    "",
    "Ultimo accesso: oggi da porfolio.perox.it",
]

NEOFETCH = [
    ("OS", "PeroxOS (Milano) x86_64"),
    ("Host", "porfolio.perox.it"),
    ("Uptime", "studente di informatica"),
    ("Focus", "automazione & robotica"),
    ("Shell", "/bin/hands-on"),
    ("Stack", "C · Python · JS/TS · SQL"),
    ("Tools", "Fusion360, EasyEDA, RobotStudio"),
    ("Printer", "Bambu Lab P1P"),
    ("Status", "\x1b[32mdisponibile\x1b[0m"),
]


def main() -> None:
    t = gifos.Terminal(
        width=760,
        height=420,
        xpad=14,
        ypad=12,
    )

    row = 1
    for line in BOOT_LINES:
        t.gen_text(text=line, row_num=row)
        row += 1

    t.gen_text(text="", row_num=row)
    row += 1

    for logo_line in LOGO:
        t.gen_text(text=f"\x1b[36m{logo_line}\x1b[0m", row_num=row)
        row += 1

    t.gen_text(text="", row_num=row)
    row += 1

    for label, value in NEOFETCH:
        t.gen_text(text=f"\x1b[35m{label:<8}\x1b[0m {value}", row_num=row)
        row += 1

    t.gen_text(text="", row_num=row)
    row += 1
    t.gen_text(text="perox@portfolio:~$ _", row_num=row, contin=True)

    t.gen_gif()


if __name__ == "__main__":
    main()
