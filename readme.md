<div align="center">
  <img src="logo.svg" alt="GoFileCLI Logo" width="500"/>
  <h1>GoFileCLI</h1>
  <p><i>The missing command-line companion for <a href="https://gofile.io/">GoFile.io</a></i></p>
  <p>
    <a href="https://www.python.org"><img src="https://img.shields.io/badge/python-3.6+-blue.svg?style=flat-square&logo=python&logoColor=white" alt="Python"/></a>
    <a href="https://gofile.io/api"><img src="https://img.shields.io/badge/API-GoFile-orange.svg?style=flat-square" alt="GoFile"/></a>
    <a href="https://github.com/Abdo-omran2206/Gofilecli/issues"><img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat-square" alt="Contributions Welcome"/></a>
  </p>
</div>

---

## 📖 Overview

**GoFileCLI** brings the convenience of the GoFile file-sharing platform straight to your terminal. Whether you're uploading files as a guest or managing them through your GoFile account, this tool provides a fast, seamless, and visually appealing experience. 

It features built-in upload history, clipboard integration, and a beautiful terminal UI powered by Python.

## ✨ Features

- **📤 Fast File Uploads**: Upload files to the best available GoFile server instantly.
- **🗂️ Upload History**: Keep track of all your uploads using a local SQLite database. View details like file size, original path, and upload timestamps.
- **🔐 Account Management**: Add your GoFile API token to upload files directly to your account folders.
- **📋 Clipboard Integration**: Easily copy download links to your clipboard with a single keystroke.
- **🎨 Beautiful UI**: Enjoy a rich terminal experience with ASCII art, colored text, and neatly formatted tables.

## 🛠️ Project Structure

```text
GoFileCLI/
├── main.py                # Main entry point of the CLI application
├── lib/
│   ├── Gofile.py          # GoFile API wrapper and logic
│   ├── config.py          # Configuration and token management
│   └── db.py              # SQLite database management for history
├── screens/
│   ├── account_menu.py    # Login/Logout and account management UI
│   ├── history_menu.py    # Upload history table and file details UI
│   ├── settings_menu.py   # Settings and history clearing UI
│   └── upload_menu.py     # File upload process UI
├── utils/
│   └── ui.py              # Helper functions for UI styling, clearing, and clipboard
├── data/                  # Auto-generated directory for SQLite database
├── config/                # Auto-generated directory for configuration JSON
└── requirements.txt       # Python dependencies
```

## ⚙️ Prerequisites

- **Python 3.6+**
- Required Python packages: `requests`, `art`, `rich`, `pyperclip`

## 🚀 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Abdo-omran2206/Gofilecli.git
   cd Gofilecli
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 💻 Usage

Start the CLI by running the main Python script:

```bash
python main.py
```

### Navigation & Options

Upon launching, you will interact with the following options:

1. **Upload File**: Provide the local file path. Once uploaded, the download link is generated and can be automatically copied to your clipboard.
2. **View History**: Access a list of all your previous uploads. Select a file ID to view its details, re-copy the download link, or delete it from history.
3. **Account**: Login using your GoFile API token to switch from "Guest" to "Active" status, allowing your uploads to be linked to your account.
4. **Settings**: Clear your local upload history database or manually toggle your account status.
5. **Exit**: Safely close the application.

> **💡 Where to get your GoFile token?**  
> Sign up at [gofile.io](https://gofile.io/), then go to your **Profile → API Token** to copy it.

## 🗄️ Local Data

GoFileCLI stores its data securely on your local machine:
- **Database**: Upload logs are stored in an SQLite database at `data/gofilecli.db`.
- **Configuration**: Your API token and account status are stored in `config/config.json`.

---

<div align="center">
  <p>Made with ❤️ by <a href="https://github.com/Abdo-omran2206">Abdo-omran2206</a></p>
  <p>If you find this tool useful, consider giving it a ⭐ on <a href="https://github.com/Abdo-omran2206/Gofilecli">GitHub</a>!</p>
</div>
