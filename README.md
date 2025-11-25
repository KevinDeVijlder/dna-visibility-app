# DNA Visibility App

A simple Python GUI application to manage DNA entries with customizable visibility and identifiers. Built with Tkinter and SQLite, it allows users to view, edit, and configure which DNA entries are shown.

## Features

Displays DNA items with Name and Custom Identifier

Toggle which items are visible (display on/off)

Edit custom_identifier directly in the GUI

Toggle view between Show All and Show Only Visible

Changes are saved directly to a local SQLite database

Auto-creates the database if missing (via setup_db.py)


---

## Getting Started
### Requirements

Python 3.x

### Setup

Clone the repository:
- git clone https://github.com/KevinDeVijlder/dna-visibility-app
- cd dna-visibility-app

### Launch the app:

python app.py

## Usage

Double-click on a Custom Identifier to edit it

Double-click on Display to toggle Yes/No

Click Save Changes to update the database

Click Show Only Visible / Show All to filter entries
