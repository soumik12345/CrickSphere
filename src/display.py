import streamlit as st
from streamlit import header


def hover_image_html():
    html = """
    <style>
        .hover_img a { position:relative; }
        .hover_img a span { position:absolute; display:none; z-index:99; }
        .hover_img a:hover span { display:block; }
    </style>

    <span class="hover_img">
        <a href="./assets/West_indies_cricket_flag.png">
            Show Image<span>
                <img src="https://raw.githubusercontent.com/soumik12345/CrickSphere/master/assets/West_indies_cricket_flag.png" alt="image" height="100" />
            </span>
        </a>
    </span>
    """
    return html


def get_match_heading(match: dict, index: int):
    heading = "## Match " + str(index) + "\n"
    heading += match['info']['teams'][0]
    heading += " vs " + match['info']['teams'][1]
    return heading


def display_match(match: dict, index: int):
    st.markdown(get_match_heading(match, index))