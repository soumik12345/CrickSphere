import streamlit as st
from src.matches import test_cricket, one_day_international


st.title('CrickSphere')


browse_option = st.sidebar.selectbox(
    'Which Format of the Game would you like to Experience?',
    ('', 'Test Cricket', 'One Day International')
)

if browse_option == 'Test Cricket':
    test_cricket()
elif browse_option == 'One Day International':
    one_day_international()
