A simple interactive Python script that asks the user a playful question and reacts based on their answers.

This script creates a short console interaction with multiple possible outcomes, ending with a **Blue Screen of Death (BSOD)** if the final negative response is confirmed.

## What It Does

The program asks:

**"do u luv me ?"**

Depending on the user's answer:

- **yes** → displays a happy message and plays an audio file
- **no** → asks for confirmation
- changing the answer restarts the interaction
- confirming **no** triggers a **Windows Blue Screen of Death (BSOD)**

## Features

- Interactive console dialogue
- Cute ASCII emoticons
- Audio playback
- Multiple response paths
- Recursive interaction loop
- Built-in BSOD trigger
- Windows-only prank behavior

## Requirements

- Python 3.8 or higher
- Windows operating system
- `yay.mp3` placed in the same directory

## Installation

Clone the repository

```bash
git clone https://github.com/username/love-question-script.git
cd love-question-script
```

Check Python installation

```bash
python --version
```

## Usage

Run the script

```bash
python script.py
```

## Example Interaction

Positive answer

```text
(｡♥‿♥｡) do u luv me ?
> yes
ヽ(✿ﾟ▽ﾟ)ノ yayyy
```

Changing your mind

```text
(｡♥‿♥｡) do u luv me ?
> no
(´・ω・｀) r u sure ?
> no
ε-(´∀｀*) ah phew
```

Final path

```text
(｡♥‿♥｡) do u luv me ?
> no
(´・ω・｀) r u sure ?
> yes
fine
[ Windows BSOD triggered ]
```

## Project Structure

```text
love-question-script/
├── script.py
├── yay.mp3
└── README.md
```

## Warning

This script intentionally triggers a **Blue Screen of Death (BSOD)** on Windows if the final negative response is confirmed.

Run only in a controlled environment.

Do not use on systems with unsaved work.

## Disclaimer

This project is made for educational, experimental, and prank purposes only.

Use at your own risk.

## License

Unknown / Original source not specified.
