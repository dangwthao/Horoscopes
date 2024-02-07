import streamlit as st
import webbrowser  

# Function to open the Facebook page
def open_facebook_page():
    webbrowser.open_new_tab("https://www.facebook.com/profile.php?id=61553564769648")

# Function to show the feedback form
def show_feedback_form():
    st.header(":mailbox: Leave your feedback for us!")

    contact_form = """
            <form action="https://formsubmit.co/stellar.fbuser@gmail.com" method="POST">
             <input type="hidden" name="_captcha" value="false">
             <input type="text" name="name" placeholder="Your name" required>
             <input type="email" name="email" placeholder="Your email" required>
             <textarea name="message" placeholder="Your message here"></textarea>
             <button type="submit">Send</button>
        </form>
        """
    st.markdown(contact_form, unsafe_allow_html=True)

# Use Local CSS File
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    local_css("style/style.css")

    # Create a button to toggle between Facebook page and feedback form
    selected_option = st.radio("Select an option:", ["Contact Us", "Feedback Form"])

    if selected_option == "Contact Us":
        st.button("Go to Facebook Page", on_click=open_facebook_page)
    elif selected_option == "Feedback Form":
        show_feedback_form()
