🔐 Caesar Cipher CLI Tool
A simple Python-based Command-Line Interface (CLI) application that performs Caesar Cipher encryption and decryption. The program allows users to input a message, choose whether to encrypt or decrypt, and specify a shift key. It uses the colorama package to provide colorful and user-friendly output.

🚀 Features
Encryption → Shift letters forward by a given key.

Decryption → Shift letters backward by a given key.

Colorful output → Uses colorama for styled text in the terminal.
table output → Uses tabulate  in the terminal.


Interactive CLI → Prompts user for action, message, and shift key.

Replay option → Continue encrypting/decrypting until the user chooses to exit.

🛠️ Installation
1.Clone the repository:
git clone https://github.com/yourusername/caesar-cipher-cli.git
cd caesar-cipher-cli

2.Install dependencies:
bash
pip install colorama
pip install tabulate

3.Run the program:
bash
python cipher.py

📊 Example Usage
bash
Type 'encrypt' for encryption, type 'decrypt' for decryption:
 encrypt
Type your message:
 hello world
Type the shift key:
 3
Here is the text after encryption: khoor zruog
Do you want to play again? Type 'yes' or 'no':
 no
Thank you for using the Caesar Cipher program. Goodbye!

📂 Project Structure
Code
caesar_cipher_cli/
    cipher.py          # Main program file
    README.md          # Documentation
    requirements.txt   # Dependencies
📌 Requirements
Python 3.10+

External package:

colorama → for colorful terminal output
tabulate → for table terminal output

🧪 Testing
Test encryption with different shift keys.

Test decryption to ensure original message is restored.

Validate handling of non-alphabet characters (spaces, punctuation).

📖 Documentation
All functions (encryption, decryption) are commented.

CLI prompts guide the user clearly.

Known limitation: Only lowercase alphabetic characters are shifted; uppercase letters remain unchanged unless extended.

🧑‍💻 Contribution
Fork the repo.

1.Create a feature branch.

2.Commit changes with meaningful messages.

3.Submit a pull request.

✅ requirements.txt
Here’s the minimal requirements.txt you can include:

Code

colorama==0.4.6

tabulate==0.10.0