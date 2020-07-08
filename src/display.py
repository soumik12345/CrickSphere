import streamlit as st
from streamlit import header


def get_match_heading(match: dict, index: int):
    heading = "## Match " + str(index) + ": "
    heading += match['info']['teams'][0]
    heading += " vs " + match['info']['teams'][1]
    return heading


def display_match(match: dict, index: int):
    st.markdown(get_match_heading(match, index))