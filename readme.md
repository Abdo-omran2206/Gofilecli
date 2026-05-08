<div align="center">
  <img src="logo.svg" alt="GoFileCLI Logo" width="500"/>

  # GoFileCLI
  
  *The missing command-line companion for [GoFile.io](https://gofile.io/)*
  
  [![Python](https://img.shields.io/badge/python-3.6+-blue.svg?style=flat-square&logo=python&logoColor=white)](https://www.python.org)
  [![GoFile](https://img.shields.io/badge/API-GoFile-orange.svg?style=flat-square)](https://gofile.io/api)
  [![License](https://img.shields.io/badge/license-MIT-green.svg?style=flat-square)](LICENSE)
  [![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat-square)](https://github.com/yourusername/gofilecli/issues)
</div>

---

## 📖 Overview

**GoFileCLI** is a fast, visually appealing, and highly functional Python-based Command Line Interface for uploading, managing, and tracking files on [GoFile.io](https://gofile.io/). Built with simplicity and productivity in mind, it brings the full power of GoFile directly to your terminal.

## ✨ Features

- ⚡ **Blazing Fast Uploads:** Upload files seamlessly without opening a browser.
- 🗂️ **Upload History:** Automatically logs all your uploads, providing quick access to shareable links.
- 🔐 **Account Integration:** Securely manage your GoFile token to link uploads to your main account.
- 🎨 **Beautiful TUI:** Enjoy an intuitive terminal interface featuring stunning ASCII art and color-coded outputs.
- ⚙️ **Customizable Settings:** Easily tweak the application's configuration to suit your workflow.

## 🚀 Quick Start

### Prerequisites
Ensure you have **Python 3.6** or higher installed on your system.

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/gofilecli.git
   cd gofilecli
   ```

2. **Set up a virtual environment (Optional but Recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 💻 Usage

To launch the interactive CLI, run:

```bash
python main.py
```

### 🧭 Navigation Menu
Once launched, you will be greeted by the main menu:

1. **Upload File:** Opens a prompt to specify the file path for upload.
2. **View History:** Displays a historical list of all files you've uploaded, including file names and GoFile links.
3. **Account:** Allows you to input and manage your GoFile API token.
4. **Settings:** Configure application defaults (e.g., output colors, prompt behaviors).
5. **Exit:** Safely close the CLI application.

## 📂 Project Structure

```text
gofilecli/
├── art.py              # ASCII art utilities
├── main.py             # Application entry point
├── requirements.txt    # Project dependencies
├── logo.svg            # GoFileCLI Logo
├── lib/
│   ├── config.py       # Configuration management
│   └── db.py           # Local database/history management
├── screens/
│   ├── account_menu.py # Account settings UI
│   ├── history_menu.py # Upload history UI
│   ├── settings_menu.py# Settings configuration UI
│   └── upload_menu.py  # File upload UI
└── utils/
    └── ui.py           # Terminal color and formatting utilities
```

## 🤝 Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project.
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the Branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

## 🛡️ Disclaimer

This is an unofficial, community-driven client for GoFile.io. It is not affiliated with, endorsed by, or sponsored by GoFile.io. Use at your own risk.

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

<div align="center">
  <i>Built with ❤️ for the terminal lovers.</i>
</div>
