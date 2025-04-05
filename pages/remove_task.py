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
    try:
        with open(FILENAME, "w") as file:
            for task in tasks:
                file.write(task + "\n")
    except Exception as e:
        st.error(f"Error saving tasks: {e}")


st.divider()

# Sidebar Navigation
with st.sidebar:
    st.header("🔍 Navigation")

    if st.button("🏠 Home"):
            st.switch_page("streamlit_to_do_list.py")
    if st.button("➕ Add Task"):
        st.switch_page("pages/add_task.py")
    if st.button("✏️ Update Task"):
        st.switch_page("pages/update_task.py")
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


# Remove Task Page
st.title("❌ Remove Task")

tasks = load_tasks()
if tasks:
    index = st.selectbox("Select a task to remove:", range(len(tasks)), format_func=lambda i: tasks[i])

    if st.button("Remove"):
        removed_task = tasks.pop(index)
        save_tasks(tasks)
        st.success(f"Task '{removed_task}' removed successfully!")
        st.rerun()
else:
    st.info("No tasks available.")

st.page_link("streamlit_to_do_list.py", label="⬅ Back to Home")
