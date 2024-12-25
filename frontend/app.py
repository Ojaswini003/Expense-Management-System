import requests
import streamlit as st
from add_update_ui import add_update_tab
from analytics_ui import analytics_tab
from analytics_by_month import analytics_months_tab

API_URL="http://localhost:8000/"

st.title("Expense Management System ")

tab1,tab2,tab3=st.tabs(["Add/Update","Analytics","Analytics By Month"])

with tab1:
    add_update_tab()

with tab2:
    analytics_tab()

with tab3:
    analytics_months_tab()


