"""
Data Labeling GUI Application

This application allows users to label text data with emotion categories and export the results as CSV.
Designed for emotion recognition and affective computing research.
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import csv
from datetime import datetime


class DataLabelingApp:
    """GUI application for labeling text data with emotion categories."""
    
    # CSV export field names
    CSV_FIELDNAMES = ["text", "label"]
    
    # Maximum text length to display in table
    MAX_TEXT_DISPLAY_LENGTH = 100
    
    def __init__(self, root):
        """Initialize the data labeling application.
        
        Args:
            root: The tkinter root window
        """
        self.root = root
        self.root.title("Text Data Labeling Tool")
        self.root.geometry("900x700")
        
        # Data storage
        self.labeled_data = []
        self.next_id = 1  # Counter for unique IDs
        
        # Emotion labels based on Ekman's basic emotions + neutral (as mentioned in README)
        self.emotion_labels = [
            "anger", "disgust", "fear", "joy", "neutral", "sadness", "surprise"
        ]
        
        self.setup_ui()
        
    def setup_ui(self):
        """Set up the user interface components."""
        # Main container
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(3, weight=1)
        
        # Title
        title_label = ttk.Label(main_frame, text="Text Data Labeling Tool", 
                                font=('Helvetica', 16, 'bold'))
        title_label.grid(row=0, column=0, columnspan=2, pady=10)
        
        # Input section
        input_frame = ttk.LabelFrame(main_frame, text="Add New Label", padding="10")
        input_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=10)
        input_frame.columnconfigure(1, weight=1)
        
        # Text input
        ttk.Label(input_frame, text="Text:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.text_input = tk.Text(input_frame, height=4, width=50, wrap=tk.WORD)
        self.text_input.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=5, padx=5)
        
        # Scrollbar for text input
        text_scrollbar = ttk.Scrollbar(input_frame, orient=tk.VERTICAL, 
                                       command=self.text_input.yview)
        text_scrollbar.grid(row=0, column=2, sticky=(tk.N, tk.S), pady=5)
        self.text_input.configure(yscrollcommand=text_scrollbar.set)
        
        # Label selection
        ttk.Label(input_frame, text="Label:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.label_var = tk.StringVar()
        self.label_combo = ttk.Combobox(input_frame, textvariable=self.label_var, 
                                        values=self.emotion_labels, state='readonly')
        self.label_combo.grid(row=1, column=1, sticky=tk.W, pady=5, padx=5)
        self.label_combo.set(self.emotion_labels[0])
        
        # Add button
        add_button = ttk.Button(input_frame, text="Add Label", command=self.add_label)
        add_button.grid(row=2, column=0, columnspan=2, pady=10)
        
        # Statistics section
        stats_frame = ttk.Frame(main_frame)
        stats_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        self.stats_label = ttk.Label(stats_frame, text="Total labeled entries: 0")
        self.stats_label.grid(row=0, column=0, sticky=tk.W)
        
        # Data display section
        display_frame = ttk.LabelFrame(main_frame, text="Labeled Data", padding="10")
        display_frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=10)
        display_frame.columnconfigure(0, weight=1)
        display_frame.rowconfigure(0, weight=1)
        
        # Treeview for displaying data
        columns = ("ID", "Text", "Label", "Timestamp")
        self.tree = ttk.Treeview(display_frame, columns=columns, show='headings', height=15)
        
        # Configure columns
        self.tree.heading("ID", text="ID")
        self.tree.heading("Text", text="Text")
        self.tree.heading("Label", text="Label")
        self.tree.heading("Timestamp", text="Timestamp")
        
        self.tree.column("ID", width=50, anchor=tk.CENTER)
        self.tree.column("Text", width=450, anchor=tk.W)
        self.tree.column("Label", width=100, anchor=tk.CENTER)
        self.tree.column("Timestamp", width=150, anchor=tk.CENTER)
        
        self.tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Scrollbars for treeview
        vsb = ttk.Scrollbar(display_frame, orient=tk.VERTICAL, command=self.tree.yview)
        vsb.grid(row=0, column=1, sticky=(tk.N, tk.S))
        self.tree.configure(yscrollcommand=vsb.set)
        
        hsb = ttk.Scrollbar(display_frame, orient=tk.HORIZONTAL, command=self.tree.xview)
        hsb.grid(row=1, column=0, sticky=(tk.W, tk.E))
        self.tree.configure(xscrollcommand=hsb.set)
        
        # Buttons section
        buttons_frame = ttk.Frame(main_frame)
        buttons_frame.grid(row=4, column=0, columnspan=2, pady=10)
        
        delete_button = ttk.Button(buttons_frame, text="Delete Selected", 
                                   command=self.delete_selected)
        delete_button.grid(row=0, column=0, padx=5)
        
        clear_button = ttk.Button(buttons_frame, text="Clear All", 
                                  command=self.clear_all)
        clear_button.grid(row=0, column=1, padx=5)
        
        export_button = ttk.Button(buttons_frame, text="Export to CSV", 
                                   command=self.export_to_csv)
        export_button.grid(row=0, column=2, padx=5)
        
    def add_label(self):
        """Add a new labeled entry to the dataset."""
        text = self.text_input.get("1.0", tk.END).strip()
        label = self.label_var.get()
        
        if not text:
            messagebox.showwarning("Warning", "Please enter some text to label.")
            return
        
        if not label:
            messagebox.showwarning("Warning", "Please select a label.")
            return
        
        # Create entry with unique ID
        entry_id = self.next_id
        self.next_id += 1
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        entry = {
            "id": entry_id,
            "text": text,
            "label": label,
            "timestamp": timestamp
        }
        
        self.labeled_data.append(entry)
        
        # Format text for display
        display_text = self._truncate_text(text, self.MAX_TEXT_DISPLAY_LENGTH)
        
        # Add to treeview
        self.tree.insert("", tk.END, values=(entry_id, display_text, label, timestamp))
        
        # Clear input
        self.text_input.delete("1.0", tk.END)
        
        # Update statistics
        self.update_stats()
        
        messagebox.showinfo("Success", "Label added successfully!")
    
    def _truncate_text(self, text, max_length):
        """Truncate text to specified length and add ellipsis if needed.
        
        Args:
            text: The text to truncate
            max_length: Maximum length before truncation
            
        Returns:
            Truncated text with ellipsis if needed
        """
        if len(text) > max_length:
            return text[:max_length] + "..."
        return text
        
    def delete_selected(self):
        """Delete the selected entry from the dataset."""
        selected_items = self.tree.selection()
        
        if not selected_items:
            messagebox.showwarning("Warning", "Please select an entry to delete.")
            return
        
        if messagebox.askyesno("Confirm", "Are you sure you want to delete the selected entry?"):
            for item in selected_items:
                values = self.tree.item(item)['values']
                entry_id = values[0]
                
                # Remove from data
                self.labeled_data = [entry for entry in self.labeled_data 
                                   if entry["id"] != entry_id]
                
                # Remove from treeview
                self.tree.delete(item)
            
            self.update_stats()
            
    def clear_all(self):
        """Clear all labeled data."""
        if not self.labeled_data:
            messagebox.showinfo("Info", "No data to clear.")
            return
        
        if messagebox.askyesno("Confirm", "Are you sure you want to clear all labeled data?"):
            self.labeled_data.clear()
            self.tree.delete(*self.tree.get_children())
            self.update_stats()
            messagebox.showinfo("Success", "All data cleared.")
            
    def update_stats(self):
        """Update the statistics display."""
        total = len(self.labeled_data)
        self.stats_label.config(text=f"Total labeled entries: {total}")
        
    def export_to_csv(self):
        """Export labeled data to a CSV file."""
        if not self.labeled_data:
            messagebox.showwarning("Warning", "No data to export.")
            return
        
        # Ask user for save location
        file_path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")],
            initialfile=f"labeled_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        )
        
        if not file_path:
            return
        
        try:
            with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=self.CSV_FIELDNAMES)
                
                writer.writeheader()
                for entry in self.labeled_data:
                    writer.writerow({
                        "text": entry["text"],
                        "label": entry["label"]
                    })
            
            messagebox.showinfo("Success", f"Data exported successfully to:\n{file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to export data:\n{str(e)}")


def main():
    """Main entry point for the application."""
    root = tk.Tk()
    app = DataLabelingApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
