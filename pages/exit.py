import streamlit as st

st.divider()

    # Sidebar Navigation
with st.sidebar:
        st.header("🔍 Navigation")
        
        if st.button("🏠 Home"):
            st.switch_page("streamlit_to_do_list.py")


st.title("🚪 Exit Application")
st.markdown("You can close this browser tab to exit the application.")
st.page_link("streamlit_to_do_list.py", label="⬅ Back to Home")
