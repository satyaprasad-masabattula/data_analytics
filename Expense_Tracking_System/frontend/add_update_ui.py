import streamlit as st
from datetime import datetime
import requests

API_URL = 'http://localhost:8000'
def add_update_tab():
    selected_dt = st.date_input('Expense Date:',datetime(2024,8,1),label_visibility='collapsed')
    response = requests.get(f"{API_URL}/expenses/{selected_dt}")
    if(response.status_code==200):
        expense_data = response.json()
    else:
        st.error('Failed to fetch the data for {selected_dt}')
        expense_data=[]
    category_lst = ['Rent','Food','Shopping','Entertainment','Others']
    with st.form(key=f"expense_form_{selected_dt}"):
        col1,col2,col3 = st.columns(3)
        with col1:
            col1.text('Amount')
        with col2:
            col2.text('Category')
        with col3:
            col3.text('Notes')
        expense_response = []
        for i in range(5):
            if i<len(expense_data):
                amount = expense_data[i]['amount']
                category = expense_data[i]['category']
                notes = expense_data[i]['notes']
            else:
                amount = 0.0
                category = 'Shopping'
                notes = ''


            col1,col2,col3 = st.columns(3)
            with col1:
                st.number_input(label="Amount",min_value=0.0,step=1.0,value=amount,key=f'Amount_{i}_{selected_dt}',label_visibility='collapsed')
                amount_input = st.session_state[f'Amount_{i}_{selected_dt}']
            with col2:
                st.selectbox(label="Category",options=category_lst,index=category_lst.index(category),key=f'Category_{i}_{selected_dt}',label_visibility='collapsed')
                category_input = st.session_state[f'Category_{i}_{selected_dt}']
            with col3:
                notes_input = notes_text = st.text_input(label='Notes',value=notes,key=f'notes_{i}_{selected_dt}',label_visibility='collapsed')
                notes_input = st.session_state[f'notes_{i}_{selected_dt}']
            expense_response.append({'amount': amount_input,
                                    'category':category_input,
                                    'notes':notes_input})
        submit_button = st.form_submit_button()
        if submit_button:
            #st.write(expense_response)
            filter_expense = [expense for expense in expense_response if expense['amount']>0]
            #st.write(filter_expense)
            reponse = requests.post(f"{API_URL}/expenses/{selected_dt}",json=filter_expense)
            if(reponse.status_code == 200):
                st.success(f'Updated data for selected date {selected_dt}')
            else:
                st.error(f'Failed to upload data for {selected_dt}')