import streamlit as st
import os

FOLDER_PATH = "tasks"
FILENAME = os.path.join(FOLDER_PATH, "tasks.txt")

def ensure_folder_and_file_exist():
    """Ensure the folder and file exist."""
    if not os.path.exists(FOLDER_PATH):
        os.makedirs(FOLDER_PATH)
    if not os.path.exists(FILENAME):
        open(FILENAME, "w").close()

def save_tasks(tasks):
    """Save tasks to file."""
    ensure_folder_and_file_exist()
    try:
        with open(FILENAME, "w") as file:
            for task in tasks:
                file.write(task + "\n")
    except Exception as e:
        st.error(f"Error saving tasks: {e}")

def load_tasks():
    """Load tasks from file."""
    ensure_folder_and_file_exist()
    try:
        with open(FILENAME, "r") as file:
            return file.read().splitlines()
    except Exception as e:
        st.error(f"Error loading tasks: {e}")
        return []


st.divider()

    # Sidebar Navigation
with st.sidebar:
        st.header("🔍 Navigation")
        
        if st.button("🏠 Home"):
            st.switch_page("streamlit_to_do_list.py")
        if st.button("✏️ Update Task"):
            st.switch_page("pages/update_task.py")
        if st.button("❌ Remove Task"):
            st.switch_page("pages/remove_task.py")
        if st.button("🚪 Exit"):
            st.switch_page("pages/exit.py")
            st.stop()
st.sidebar.markdown("👨‍💻 **Created by:** Shivansh Gautam")
st.sidebar.markdown("🔗 **GitHub:** [Click here](https://github.com/shivanshgautam02)")



tasks = load_tasks()

# Display tasks
st.subheader("📌 Your Tasks:")
if not tasks:
    st.info("No tasks available.")
else:
    for i, task in enumerate(tasks, 1):
        st.write(f"{i}. {task}")

# Add Task Page

st.title("➕ Add Task")
new_task = st.text_input("Enter a new task:")

if st.button("Add"):
    if new_task.strip():
        tasks = load_tasks()
        tasks.append(new_task.strip())
        save_tasks(tasks)
        st.success("Task added successfully!")
        st.rerun()
    else:
        st.warning("Task cannot be empty.")

st.page_link("streamlit_to_do_list.py", label="⬅ Back to Home")  # ✅ Fixed navigation
