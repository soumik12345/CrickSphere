import streamlit as st
from src.matches.test_cricket_options import test_cricket_by_date


def test_cricket():
    test_browse_option = st.sidebar.selectbox(
        'How Would you like to search?',
        ('', 'By Date', 'By Map')
    )
    if test_browse_option == 'By Date':
        test_cricket_by_date()
    elif test_browse_option == 'By Map':
        st.warning('Under Development')


def one_day_international():
    st.warning('Under Development')
