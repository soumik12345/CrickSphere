import streamlit as st
from src.data_query import load_data
from src.utils import datetime_to_str
from src.display import display_match, hover_image_html


def test_cricket_by_date():
    query_date = st.date_input('Enter Date')
    query_date = datetime_to_str(query_date)

    matches = load_data(
        db='test_cricket', collection='matches',
        query={"info.dates": query_date}
    )

    for index, match in enumerate(matches):
        display_match(match, index + 1)
        st.markdown("<hr>", unsafe_allow_html=True)
    
    #st.markdown(hover_image_html(), unsafe_allow_html=True)