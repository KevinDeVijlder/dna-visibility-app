# DNA Visibility App

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![GitHub issues](https://img.shields.io/github/issues/KevinDeVijlder/dna-visibility-app)
![GitHub forks](https://img.shields.io/github/forks/KevinDeVijlder/dna-visibility-app)
![GitHub stars](https://img.shields.io/github/stars/KevinDeVijlder/dna-visibility-app)

A **simple Python GUI application** to manage DNA entries with customizable visibility and identifiers.  
Built with **Tkinter** and **SQLite**, it allows users to view, edit, and configure which DNA entries are shown.


## 📦 Features

- Displays DNA items with **Name** and **Custom Identifier**  
- Toggle which items are visible (`display` Yes/No)  
- Edit `custom_identifier` directly in the GUI  
- Toggle view between **Show All** and **Show Only Visible**  
- Changes are **saved directly to a local SQLite database**  
- Auto-creates the database if missing (via `setup_db.py`)  


---

## ⚡ Getting Started

### Requirements
- Python 3.x or higher

### Setup

#### 1. Clone the repository:

```bash
git clone https://github.com/KevinDeVijlder/dna-visibility-app.git
```

#### 1. Change into the cloned directory
```bash
cd dna-visibility-app
```

#### 1. Run the app with python
```bash
python app.py
```

## 🧬 Usage

- Double-click a Custom Identifier to edit it

- Double-click the Display column to toggle Yes/No

- Click Save Changes to update the database

- Click Show Only Visible / Show All to filter entries

## 🗂️ Project Structure

```bash
dna-visibility-app/
├── app.py            # Main Tkinter GUI
├── setup_db.py       # Creates and pre-fills the database
├── dna_database.db   # SQLite DB (auto-generated)
└── .gitignore
```

## 📄 License
This project is licensed under the MIT License.

## ⚠️ Disclaimer

This application is a **basic example for testing and demonstration purposes only**.  
It is **not intended for production use** or any real-world DNA analysis.  
Use at your own risk; the authors are **not responsible for any misuse or data loss**.
