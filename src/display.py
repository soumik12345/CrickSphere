import streamlit as st
from streamlit import header


def hover_image_html(text: str, image_url: str):
    html = """
    <style>
        .hover_img a { position:relative; }
        .hover_img a span { position:absolute; display:none; z-index:99; }
        .hover_img a:hover span { display:block; }
    </style>

    <span class="hover_img">
        <a href="#">
            """ + text + """<span>
                <img src=\"""" + image_url + """\" alt="image" height="100" />
            </span>
        </a>
    </span>
    """
    return html


def get_match_heading(match: dict, index: int):
    heading = "## Match " + str(index)
    return heading


def get_team_name_display(team: str):
    return hover_image_html(
        text=team,
        image_url='https://raw.githubusercontent.com/soumik12345/CrickSphere/master/assets/West_indies_cricket_flag.png'
    )


def display_match(match: dict, index: int):
    st.markdown(get_match_heading(match, index))
    versus_line = get_team_name_display(match['info']['teams'][0]) + ' vs '
    versus_line += get_team_name_display(match['info']['teams'][1])
    st.markdown(versus_line, unsafe_allow_html=True)
