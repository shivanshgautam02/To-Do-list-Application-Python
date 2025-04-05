import streamlit as st
import os

FOLDER_PATH = "tasks"
FILENAME = os.path.join(FOLDER_PATH, "tasks.txt")

def load_tasks():
    try:
        with open(FILENAME, "r") as file:
            return file.read().splitlines()
    except Exception as e:
        st.error(f"Error loading tasks: {e}")
        return []

def save_tasks(tasks):
    """Save updated tasks to file."""
    try:
        with open(FILENAME, "w") as file:
            for task in tasks:
                file.write(task + "\n")
    except Exception as e:
        st.error(f"Error saving tasks: {e}")




# st.divider()

# Sidebar Navigation
with st.sidebar:
    st.header("🔍 Navigation")
    
    if st.button("🏠 Home"):
        st.switch_page("streamlit_to_do_list.py")
    if st.button("➕ Add Task"):
        st.switch_page("pages/add_task.py")
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



# Update Task Page
st.title("✏️ Update Task")

tasks = load_tasks()
if tasks:
    index = st.selectbox("Select a task to update:", range(len(tasks)), format_func=lambda i: tasks[i])
    updated_text = st.text_input("Enter the updated task:", tasks[index])

    if st.button("Update"):
        if updated_text.strip():
            tasks[index] = updated_text.strip()
            save_tasks(tasks)
            st.success("Task updated successfully!")
            st.rerun()
        else:
            st.warning("Task cannot be empty.")
else:
    st.info("No tasks available.")

st.page_link("streamlit_to_do_list.py", label="⬅ Back to Home")
