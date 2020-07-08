import numpy as np
import pandas as pd
import streamlit as st
from datetime import date, timedelta
from src.data_query import load_data
from src.utils import datetime_to_str
from src.display import display_match


st.title('CrickSphere')


browse_option = st.sidebar.selectbox(
    'Which Format of the Game would you like to Experience?',
    ('', 'Test Cricket', 'One Day International')
)

if browse_option == 'Test Cricket':
    
    test_browse_option = st.sidebar.selectbox(
        'How Would you like to search?',
        ('', 'By Date', 'By Map')
    )
    
    if test_browse_option == 'By Date':
        query_date = st.date_input('Enter Date')
        query_date = datetime_to_str(query_date)
        # st.sidebar.text(type(query_date))
        # st.sidebar.text(query_date)
        matches = load_data(
            db='test_cricket', collection='matches',
            query={"info.dates": query_date}
        )
        # st.json(matches)
        # st.sidebar.text(type(matches))
        for index, match in enumerate(matches):
            display_match(match, index + 1)
            st.markdown("<hr>", unsafe_allow_html=True)
        


    
    elif test_browse_option == 'By Map':
        st.warning('Under Development')

elif browse_option == 'One Day International':
    st.warning('Under Development')
