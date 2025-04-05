# 📋 To-Do List Application

A simple yet powerful **To-Do List Application** implemented in three different ways:

- 🖥️ **CLI (Command Line Interface)**
- 🌐 **Streamlit Web App**
- 🖼️ **PyQt GUI Application**

Manage your daily tasks efficiently with this flexible to-do list!

---

## 📌 Features
✅ Add, update, and remove tasks  
✅ View saved tasks  
✅ Persistent storage using a `tasks.txt` file  
✅ Three different interfaces for ease of use  

---

## 🏗 Project Structure

```bash
📂 To-Do List Project
├── 📁 tasks/                  
│   ├── tasks.txt               
│
├── 📁 pages/                  # Streamlit web pages 
│   ├── add_task.py            
│   ├── update_task.py        
│   ├── remove_task.py         
│   ├── exit.py                
│
├── cli_to_do_list.py          # CLI file
├── streamlit_to_do_list.py    # Streamlit web-based file
├── pyqt_to_do_list.py         # PyQt GUI-based file
├── requirements.txt                 
├── README.md 
```

---

## 🚀 How to Run

### 1️⃣ Running the **CLI Version**
```bash
python cli_to_do_list.py
```

### 2️⃣ Running the **Streamlit Web App**
```bash
streamlit run streamlit_to_do_list.py
```
> **Note:** Ensure all `.py` files are inside the `pages/` directory for proper navigation.

### 3️⃣ Running the **PyQt GUI Version**
```bash
python pyqt_to_do_list.py
```

---

## 🔧  Requirements
Install required Python libraries using:
```bash
pip install -r requirements.txt
```

---



---

## 💡 Future Enhancements
- ✅ Add a database for better storage
- ✅ Add task categories & priorities
- ✅ Implement a notification system

---

 
💬 Enjoy your To-Do List App! 🚀 😃

