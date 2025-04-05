import streamlit as st
import os

# File path setup
FOLDER_PATH = "tasks"
FILENAME = os.path.join(FOLDER_PATH, "tasks.txt")

def ensure_folder_and_file_exist():
    """Ensure the tasks folder and file exist."""
    if not os.path.exists(FOLDER_PATH):
        os.makedirs(FOLDER_PATH)
    if not os.path.exists(FILENAME):
        open(FILENAME, "w").close()

def load_tasks():
    """Load tasks from file."""
    ensure_folder_and_file_exist()
    try:
        with open(FILENAME, "r") as file:
            return file.read().splitlines()
    except Exception as e:
        st.error(f"Error loading tasks: {e}")
        return []

# Home Page
def main():
    st.set_page_config(page_title="To-Do List", layout="centered")
    st.title("📋 To-Do List App")
    st.markdown("Manage your tasks easily with this simple To-Do List app!")


    tasks = load_tasks()

    # Display tasks
    st.subheader("📌 Your Tasks:")
    if not tasks:
        st.info("No tasks available.")
    else:
        for i, task in enumerate(tasks, 1):
            st.write(f"{i}. {task}")


    st.divider()

    # Sidebar Navigation
    with st.sidebar:
        st.header("🔍 Navigation")
        
        if st.button("➕ Add Task"):
            st.switch_page("app_pages/add_task.py")
        if st.button("✏️ Update Task"):
            st.switch_page("app_pages/update_task.py")
        if st.button("❌ Remove Task"):
            st.switch_page("app_pages/remove_task.py")
        if st.button("🚪 Exit"):
            st.stop()
    # st.sidebar.markdown("👨‍💻 **Created by:** Shivansh Gautam")
    # st.sidebar.markdown("🔗 **GitHub:** [Click here](https://github.com/your-github-username)")


    # Navigation Buttons on Main Page
    st.subheader("📂 Manage Tasks")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("➕ Add Task "):
            st.switch_page("app_pages/add_task.py")

    with col2:
        if st.button("✏️ Update Task "):
            st.switch_page("app_pages/update_task.py")

    with col3:
        if st.button("❌ Remove Task "):
            st.switch_page("app_pages/remove_task.py")

    with col4:
        if st.button("🚪 Exit "):
            st.stop()

    st.divider()


    # Project Details
    st.subheader("📢 About This Project")
    st.markdown("""
    - This is a simple **To-Do List Application** built using **Streamlit** and **Python**.
    - Users can **add, update, remove, and view tasks** in a structured way.
    - The data is stored in a **tasks.txt** file inside a folder for persistence.
    """)

    st.markdown("👨‍💻 **Created by:** Shivansh Gautam")
    st.markdown("🔗 **GitHub:** [Click here](https://github.com/your-github-username)")


if __name__ == "__main__":
    main()
