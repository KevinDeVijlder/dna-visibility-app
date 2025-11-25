import tkinter as tk
from tkinter import ttk
import sqlite3
import os
import subprocess

DB_FILE = "dna_database.db"

def ensure_database_exists():
        if not os.path.exists("dna_database.db"):
            print("Database not found. Running setup_db.py...")

            # Run setup script
            subprocess.run(["python", "setup_db.py"], check=True)

            print("Database created successfully.")


class DNAApp:
    def __init__(self, root):
        self.root = root
        self.root.title("DNA Visibility App")

        self.show_only_visible = tk.BooleanVar(value=False)

        # Toggle Display Mode Button
        self.toggle_button = tk.Button(
            root,
            text="Show Only Visible",
            command=self.toggle_filter
        )
        self.toggle_button.pack(pady=10)

        # Create table frame
        self.table = ttk.Treeview(
            root,
            columns=("name", "custom_id", "display"),
            show="headings",
            height=15
        )
        
        self.table.heading("name", text="Name")
        self.table.heading("custom_id", text="Custom Identifier")
        self.table.heading("display", text="Display")

        self.table.column("name", width=150)
        self.table.column("custom_id", width=150)
        self.table.column("display", width=80)

        self.table.pack()

        # Bind double click to edit custom identifier
        self.table.bind("<Double-1>", self.on_double_click)

        # Save changes button
        self.save_button = tk.Button(root, text="Save Changes", command=self.save_changes)
        self.save_button.pack(pady=10)

        self.refresh_table()

        # Add New Entry button
        self.add_button = tk.Button(root, text="Add New Entry", command=self.add_new_entry)
        self.add_button.pack(pady=5)

    def connect(self):
        return sqlite3.connect(DB_FILE)

    def load_data(self):
        conn = self.connect()
        c = conn.cursor()

        if self.show_only_visible.get():
            c.execute("SELECT id, name, custom_identifier, display FROM dna_items WHERE display=1")
        else:
            c.execute("SELECT id, name, custom_identifier, display FROM dna_items")

        rows = c.fetchall()
        conn.close()
        return rows

    def refresh_table(self):
        # Clear table
        for item in self.table.get_children():
            self.table.delete(item)

        # Load rows
        rows = self.load_data()
        for row in rows:
            item_id, name, custom_id, display = row
            self.table.insert(
                "",
                "end",
                iid=item_id,
                values=(name, custom_id if custom_id else "", "Yes" if display else "No")
            )

    def toggle_filter(self):
        self.show_only_visible.set(not self.show_only_visible.get())
        if self.show_only_visible.get():
            self.toggle_button.config(text="Show All")
        else:
            self.toggle_button.config(text="Show Only Visible")

        self.refresh_table()

    def on_double_click(self, event):
        """Allow editing custom_identifier on double click."""
        item_id = self.table.focus()
        col = self.table.identify_column(event.x)

        if col == "#2":  # custom_identifier column
            old_value = self.table.set(item_id, "custom_id")

            popup = tk.Toplevel(self.root)
            popup.title("Edit Custom Identifier")

            tk.Label(popup, text="Enter new value:").pack(pady=5)

            entry = tk.Entry(popup)
            entry.insert(0, old_value)
            entry.pack(pady=5)

            def save_value():
                new_value = entry.get()
                self.table.set(item_id, "custom_id", new_value)
                popup.destroy()

            tk.Button(popup, text="Save", command=save_value).pack(pady=5)

        elif col == "#3":  # display column
            current = self.table.set(item_id, "display")
            new = "No" if current == "Yes" else "Yes"
            self.table.set(item_id, "display", new)

    def save_changes(self):
        conn = self.connect()
        c = conn.cursor()

        for item_id in self.table.get_children():
            name, custom_id, display = self.table.item(item_id, "values")

            display_val = 1 if display == "Yes" else 0

            c.execute("""
                UPDATE dna_items
                SET custom_identifier = ?, display = ?
                WHERE id = ?
            """, (custom_id, display_val, item_id))

        conn.commit()
        conn.close()
        print("Changes saved successfully.")

        self.refresh_table()

    def add_new_entry(self):
    # Popup window to add a new DNA item.#
        popup = tk.Toplevel(self.root)
        popup.title("Add New DNA Entry")

        tk.Label(popup, text="Name:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        name_entry = tk.Entry(popup)
        name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(popup, text="Custom Identifier:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        custom_entry = tk.Entry(popup)
        custom_entry.grid(row=1, column=1, padx=5, pady=5)

        display_var = tk.BooleanVar(value=True)
        display_check = tk.Checkbutton(popup, text="Display", variable=display_var)
        display_check.grid(row=2, columnspan=2, pady=5)

        def submit():
            name = name_entry.get().strip()
            custom_id = custom_entry.get().strip()
            display = 1 if display_var.get() else 0

            if not name:
                tk.messagebox.showerror("Error", "Name cannot be empty!")
                return

            # Insert into DB
            conn = self.connect()
            c = conn.cursor()
            c.execute(
                "INSERT INTO dna_items (name, display, custom_identifier) VALUES (?, ?, ?)",
                (name, display, custom_id if custom_id else None)
            )
            conn.commit()
            conn.close()

            popup.destroy()
            self.refresh_table()

        tk.Button(popup, text="Add Entry", command=submit).grid(row=3, columnspan=2, pady=10)
        
        popup.grab_set()
        popup.focus_set()
        popup.wait_window()
   
if __name__ == "__main__":
    ensure_database_exists()

    root = tk.Tk()
    app = DNAApp(root)
    root.mainloop()