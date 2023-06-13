import streamlit as st
from PIL import Image
from collections import defaultdict
css = """
        <style>
        body {
            font-family: 'Helvetica', sans-serif;
            color: #333333;
            background: linear-gradient(135deg, #f5f7fa, #c3cfe2);
        }
        .card {
            background-color: white;
            box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.1);
            border-radius: 5px;
            padding: 20px;
            margin: 10px;
            transition: box-shadow 0.3s ease-in-out;
        }
        .card:hover {
            box-shadow: 0px 6px 20px rgba(0, 0, 0, 0.15);
        }
        .about-card {
        background-color: white;
        box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.1);
        border-radius: 5px;
        padding: 20px;
        margin: 10px;
        transition: box-shadow 0.3s ease-in-out;
        }
       .about-card:hover {
        box-shadow: 0px 6px 20px rgba(0, 0, 0, 0.15);
        }
       .search-input {
        padding: 10px;
        border-radius: 5px;
        border: 1px solid #cccccc;
        margin-bottom: 10px;
        }
            .navigation {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px;
        background-color: #ffffff;
        box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.1);
        border-radius: 5px;
        margin-bottom: 20px;
    }
    .navigation-logo {
        font-size: 24px;
        font-weight: bold;
        color: #333333;
    }
    .navigation-links {
        display: flex;
        justify-content: space-between;
        align-items: center;
        list-style: none;
    }
    .navigation-links li {
        margin-left: 15px;
    }
    .navigation-links li a {
        color: #333333;
        text-decoration: none;
        transition: color 0.3s ease-in-out;
    }
    .navigation-links li a:hover {
        color: #ff6600;
    }
    </style>
    """
import os

def set_background():
    image_path = "C:\\Users\\14243\\AppData\\Local\\Temp\\Temp1_vecteezy_abstract-boxes-background-modern-technology-with-square_8171873_81.zip\\vecteezy_abstract-boxes-background-modern-technology-with-square_8171873.jpg"
    image_style = f"""
        <style>
        body {{
            background-image: url("{image_path}");
            background-size: cover;
            background-repeat: no-repeat;
        }}
        </style>
    """
    st.markdown(image_style, unsafe_allow_html=True)

# Usage
set_background()

def homepage():
        st.title("Samantha Alejandre's Personal Website")

     # Rest of the code for the homepage...
        st.markdown("Welcome to my personal website! This is where I showcase my Python projects.")
   
        st.markdown(css, unsafe_allow_html=True)
        st.markdown("<h2>Latest Projects</h2>", unsafe_allow_html=True)
     # Display a sample project card
        with st.container():
            project_container = st.container()
            project_id = "project_1"
         
            if project_id not in st.session_state:
              st.session_state[project_id] = {
                "title": "Project Title",
                "image": "project_image.jpg",
                "description": "Project description...",
                "github_link": "https://github.com/your-username/project-repo",
                "rating": 0,
                "views": 0,
            }
        project = st.session_state[project_id]

        st.markdown(f"<h3>{project['title']}</h3>", unsafe_allow_html=True)
        st.markdown(f"![Project Image]({project['image']})")
        st.markdown(f"<p>{project['description']}</p>", unsafe_allow_html=True)
        st.markdown(f"<a href='{project['github_link']}'>GitHub</a>", unsafe_allow_html=True)
        st.markdown(f"Rating: {project['rating']} ⭐")
        st.markdown(f"Views: {project['views']}")
        # Rating system
        rating = st.selectbox("Rate this project:", range(1, 6), key=f"{project_id}_rating")
        if st.button("Submit Rating"):
            project['rating'] = rating

        # Views count
        project['views'] += 1
     

def project_page():
    st.title("Projects")
    st.markdown(css, unsafe_allow_html=True)
    # Add code to display a specific project based on user selection

    # For each project, you can use st.image() to display the image
    # and st.write() or st.markdown() to display the project title and description

    # Once a project is clicked, you can use st.button() to redirect to the project's GitHub page
    # Add a search input field
    search_query = st.text_input("Search Projects", "")

    # Display project cards based on search query
    if search_query:
        # Display filtered project cards based on search query
        st.markdown("<h2>Search Results</h2>", unsafe_allow_html=True)
        # Code to filter and display project cards based on search query
    else:
        # Display all project cards
        st.markdown("<h2>All Projects</h2>", unsafe_allow_html=True)
        # Code to display all project cards
    
def about_page():
    st.title("About")
    st.markdown(css, unsafe_allow_html=True)

    st.markdown("<div class='about-card'>"
                "<h2>About Me</h2>"
                "<p>Add your content here...</p>"
                "<h3>Certifications</h3>"
                "<ul>"
                "<li>Certificate 1</li>"
                "<li>Certificate 2</li>"
                "</ul>"
                "<h3>Contact Information</h3>"
                "<p>Email: samantha@example.com</p>"
                "<p>LinkedIn: <a href='https://www.linkedin.com/in/your-profile'>Samantha Alejandre</a></p>"
                "</div>", unsafe_allow_html=True)# Add code to display information about yourself, such as your background, skills, etc.
    # You can use st.write() or st.markdown() to display the content

def main():
    st.sidebar.title("Navigation")
   
        # Define page names and corresponding icons
    pages = {
        "Home": "🏠 Home",
        "Projects": "🚀 Projects",
        "About": "ℹ️ About",
    }

    # Get the current active page from the radio selection
    active_page = st.sidebar.radio("Go to", list(pages.keys()), index=0, format_func=lambda page: pages[page])



    if active_page == "Home":
        homepage()
    elif active_page == "Projects":
        project_page()
    elif active_page == "About":
        about_page()

if __name__ == "__main__":
    main()
