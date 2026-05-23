# ASCII Art Generator

An interactive terminal app that renders text as colorful ASCII art using [pyfiglet](https://github.com/pwaller/pyfiglet) and [colorama](https://github.com/tartley/colorama).

## Features

- 17 built-in fonts to choose from
- 6 foreground colors
- Live preview as you type
- Save output to a `.txt` file

## Setup

```bash
pip install -r requirements.txt
python ascii_art.py
```

## Usage

| Key | Action           |
|-----|------------------|
| T   | Change text       |
| F   | Browse fonts      |
| C   | Pick color        |
| S   | Save to file      |
| Q   | Quit              |

Saved files are written to the same directory as the script and are excluded from version control via `.gitignore`.
