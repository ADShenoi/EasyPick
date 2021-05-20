import streamlit as st
import pandas as pd
from pop import customMsg

st.title('EasyPick')
st.markdown('''Smartphones have snaked their way into almost every living moment of our technologically-fueled lives. More people are buying smartphones, 
and the number of options is also increasing. Choosing a smartphone from such an overwhelming list of options might get 
confusing, so we present to you EasyPick that helps you pick the best smartphone for your needs.\n
 EasyPick is a web app that can help you find your best match.\n''')
if st.button('App Tour'):
    msg = '''Instructions\n
                       Step 1. Either type in the mobile name or select from dropdown
                       Step 2. Set the price range
                       Step 3. Click on Show Values to view the details
                       Step 4. Click on Show Dataset to view the dataset'''
    customMsg(msg, 6, 'warning')
st.sidebar.title('Home')

df_s = pd.read_csv('mobile_reviews_with_analysis')
df_unique = pd.read_csv('Unique.csv')
df_unique.drop(['Unnamed: 0', 'Link'], axis=1, inplace=True)

name = ['OPPO', 'POCO', 'Infinix', 'GIONEE', 'REDMI', 'realme', 'MOTOROLA', 'SAMSUNG']

Input_mode = st.sidebar.radio("Mode of Input", ('Custom Input', 'Select from Dropdown'))
Price_range = st.sidebar.slider('Price Range', 3000, 20000, (5000, 15000), step=100)
Min, Max = Price_range
df_s = df_s[df_s.Price <= Max]
df_s = df_s[Min <= df_s.Price]
if Input_mode == 'Select from Dropdown':
    naam = st.sidebar.selectbox("Name", name)
    name_lst = []
    for names in df_s.Name.unique():
        if naam.lower() in names.lower():
            name_lst.append(names)
    for each_name in name_lst:
        df_temp = df_s[each_name == df_s.Name]
        st.write(each_name)
        price = int(df_temp.Price.unique())
        st.write('Price = ', price)
        df_review = df_temp[['Review', 'Expression']]
        df_review.set_index('Review', inplace=True)
        if st.button('Show Values of ' + each_name):
            df_values = df_temp[['Review', 'neg', 'neu', 'pos', 'compound']]
            df_values.set_index('Review', inplace=True)
            st.dataframe(df_values)
        st.table(df_review)

if Input_mode == 'Custom Input':
    Name_input = st.sidebar.text_input("Input Name")
    name_lst = []
    for names in df_s.Name.unique():
        if Name_input.lower() in names.lower():
            name_lst.append(names)
    for each_name in name_lst:
        df_temp = df_s[each_name == df_s.Name]
        st.write(each_name)
        price = int(df_temp.Price.unique())
        st.write('Price = ', price)
        df_review = df_temp[['Review', 'Expression']]
        df_review.set_index('Review', inplace=True)
        if st.button('Show Values of ' + each_name):
            df_values = df_temp[['Review', 'neg', 'neu', 'pos', 'compound']]
            df_values.set_index('Review', inplace=True)
            st.dataframe(df_values)
        st.table(df_review)
if st.sidebar.button('Show Dataset'):
    st.dataframe(df_unique)
print(st.__version__)