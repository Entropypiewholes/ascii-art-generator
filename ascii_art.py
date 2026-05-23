import pyfiglet
import colorama
from colorama import Fore, Style
import os
import sys

colorama.init()

COLORS = {
    "1": (Fore.RED,     "Red"),
    "2": (Fore.GREEN,   "Green"),
    "3": (Fore.YELLOW,  "Yellow"),
    "4": (Fore.CYAN,    "Cyan"),
    "5": (Fore.MAGENTA, "Magenta"),
    "6": (Fore.WHITE,   "White"),
}

FONTS = [
    "big", "banner", "block", "bubble", "digital",
    "doom", "isometric1", "larry3d", "lean", "mini",
    "roman", "shadow", "slant", "small", "standard",
    "star_wars", "univers",
]


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def pick_font(current: str) -> str:
    clear()
    print(Fore.CYAN + "── Font Browser ──" + Style.RESET_ALL)
    print(f"Current: {Fore.YELLOW}{current}{Style.RESET_ALL}\n")
    for i, font in enumerate(FONTS, 1):
        print(f"  {i:2}. {font}")
    print()
    choice = input("Enter number (or Enter to keep current): ").strip()
    if choice.isdigit():
        idx = int(choice) - 1
        if 0 <= idx < len(FONTS):
            return FONTS[idx]
    return current


def pick_color(current_code: str) -> str:
    clear()
    print(Fore.CYAN + "── Color Picker ──" + Style.RESET_ALL)
    for key, (code, name) in COLORS.items():
        print(f"  {key}. {code}{name}{Style.RESET_ALL}")
    print()
    choice = input("Enter number (or Enter to keep current): ").strip()
    if choice in COLORS:
        return COLORS[choice][0]
    return current_code


def render(text: str, font: str, color: str) -> str:
    try:
        art = pyfiglet.figlet_format(text, font=font)
    except pyfiglet.FontNotFound:
        art = pyfiglet.figlet_format(text, font="standard")
    return color + art + Style.RESET_ALL


def save(text: str, font: str):
    plain = pyfiglet.figlet_format(text, font=font)
    filename = input("Filename (without extension): ").strip() or "output"
    path = os.path.join(os.path.dirname(__file__), filename + ".txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(plain)
    print(Fore.GREEN + f"Saved to {path}" + Style.RESET_ALL)
    input("Press Enter to continue...")


def main():
    text = "Hello!"
    font = "slant"
    color = Fore.CYAN

    while True:
        clear()
        print(render(text, font, color))
        print(Fore.WHITE + Style.DIM + f"font: {font}  |  text: {repr(text)}" + Style.RESET_ALL)
        print()
        print("  [T] Change text    [F] Change font")
        print("  [C] Change color   [S] Save to file")
        print("  [Q] Quit")
        print()
        cmd = input("Choice: ").strip().lower()

        if cmd == "t":
            clear()
            new_text = input("Enter text: ").strip()
            if new_text:
                text = new_text
        elif cmd == "f":
            font = pick_font(font)
        elif cmd == "c":
            color = pick_color(color)
        elif cmd == "s":
            save(text, font)
        elif cmd == "q":
            clear()
            print(Fore.YELLOW + "Bye!" + Style.RESET_ALL)
            sys.exit(0)


if __name__ == "__main__":
    main()
