import streamlit as st
import streamlit.components.v1 as components

st.title("Scroll to Section Example")

# Define a unique ID for the section to scroll to
section_id = "target-section"

# Scroll button
if st.button("Go to Target Section"):
    components.html(f"""
        <script>
            const element = document.getElementById("{section_id}");
            if (element) {{
                element.scrollIntoView({{ behavior: "smooth" }});
            }}
        </script>
    """, height=0)

# Some filler content to make the page scrollable
for i in range(30):
    st.write(f"Line {i + 1}")

# Target section with an identifiable ID
st.markdown(f"""
    <div id="{section_id}">
        <h2>This is the Target Section 👇</h2>
        <p>You have successfully scrolled here.</p>
    </div>
""", unsafe_allow_html=True)

# Add more content below
for i in range(30, 60):
    st.write(f"Line {i + 1}")
