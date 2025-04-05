import sys
import os
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QListWidget, QInputDialog, QMessageBox)
from PyQt6.QtGui import QFont

FOLDER_PATH = "tasks"
FILENAME = os.path.join(FOLDER_PATH, "tasks.txt")

def ensure_folder_and_file_exist():

    if not os.path.exists(FOLDER_PATH):
        os.makedirs(FOLDER_PATH)
    if not os.path.exists(FILENAME):
        open(FILENAME, "w").close()

def load_tasks():
  
    ensure_folder_and_file_exist()
    try:
        with open(FILENAME, "r") as file:
            return file.read().splitlines()
    except Exception as e:
        print("Error loading tasks:", e)
        return []

def save_tasks(tasks):

    ensure_folder_and_file_exist()
    try:
        with open(FILENAME, "w") as file:
            for task in tasks:
                file.write(task + "\n")
    except Exception as e:
        print("Error saving tasks:", e)

class ToDoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("📃 To-Do List")
        self.setGeometry(100, 100, 400, 400)

        
        self.layout = QVBoxLayout()

        # Add a label with the 📃 emoji
        self.logo_label = QLabel("📃 To-Do List")
        self.logo_label.setFont(QFont("Arial", 14, QFont.Weight.Bold))  # Customize font
        self.layout.addWidget(self.logo_label)
        
        self.task_list = QListWidget()
        self.layout.addWidget(self.task_list)
        
        self.setLayout(self.layout)

        self.load_tasks()
        
        self.add_button = QPushButton("➕ Add Task")
        self.add_button.clicked.connect(self.add_task)
        self.layout.addWidget(self.add_button)
        
        self.update_button = QPushButton("✏️ Update Task")
        self.update_button.clicked.connect(self.update_task)
        self.layout.addWidget(self.update_button)
        
        self.remove_button = QPushButton("❌ Remove Task")
        self.remove_button.clicked.connect(self.remove_task)
        self.layout.addWidget(self.remove_button)
        
        self.exit_button = QPushButton("🚪 Exit")
        self.exit_button.clicked.connect(self.close)
        self.layout.addWidget(self.exit_button)
        
        self.setLayout(self.layout)
    
    def load_tasks(self):
       
        self.task_list.clear()
        tasks = load_tasks()
        self.task_list.addItems(tasks)
    
    def add_task(self):
       
        task, ok = QInputDialog.getText(self, "Add Task", "Enter new task:")
        if ok and task.strip():
            tasks = load_tasks()
            tasks.append(task.strip())
            save_tasks(tasks)
            self.load_tasks()
    
    def update_task(self):
        
        selected_item = self.task_list.currentItem()
        if selected_item:
            new_task, ok = QInputDialog.getText(self, "Update Task", "Enter new task:", text=selected_item.text())
            if ok and new_task.strip():
                tasks = load_tasks()
                index = tasks.index(selected_item.text())
                tasks[index] = new_task.strip()
                save_tasks(tasks)
                self.load_tasks()
        else:
            QMessageBox.warning(self, "Update Task", "Please select a task to update!")
    
    def remove_task(self):
        
        selected_item = self.task_list.currentItem()
        if selected_item:
            tasks = load_tasks()
            tasks.remove(selected_item.text())
            save_tasks(tasks)
            self.load_tasks()
        else:
            QMessageBox.warning(self, "Remove Task", "Please select a task to remove!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ToDoApp()
    window.show()
    sys.exit(app.exec())
