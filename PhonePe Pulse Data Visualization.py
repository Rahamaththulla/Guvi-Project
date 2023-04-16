#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sqlalchemy
import pymysql
from sqlalchemy import create_engine
from sqlalchemy import text
from pandas.io import sql
import mysql.connector as sql
import pandas as pd
import json
import plotly.express as px
import os
import streamlit as st
from PIL import Image
from sqlalchemy import create_engine, text 
import matplotlib.pyplot as plt
import mysql.connector as sql


mydb = sql.connect(
  host="localhost",
  user="root",
  password="Risvana123",
  database="phonepay_project"
    
  
)


mycursor = mydb.cursor(buffered=True)



def graph(Ans):
            y=st.selectbox("select  :", ["Transaction_amount","Transaction_count"])
            fig=px.choropleth(Ans,
                              geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
    featureidkey='properties.ST_NM',
    locations='alter_state',
    color=y,
    color_continuous_scale='Reds'
)
  
            fig.update_geos(fitbounds="locations", visible=False)

            return fig.show()
    
def graph1(Ans):
            y=st.selectbox("select  :", ["reg_users","app_opens"])
            fig=px.choropleth(Ans,
                              geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
    featureidkey='properties.ST_NM',
    locations='alter_state',
    color=y,
    color_continuous_scale='Reds'
)
  
            fig.update_geos(fitbounds="locations", visible=False)

            return fig.show()    
def pie_chart(ans):
    value=st.selectbox("select",["Transaction_amount","Transaction_count"])
    fig=px.pie(ans,values=value,names="Transaction_type",title=("Transaction_type vs  "+value),color_discrete_sequence=px.colors.sequential.RdBu)
    return fig.show()
def  bar_chart4(ans): 
    value1=st.selectbox("select options:",["Transaction_amount","Transaction_count"])
    fig=px.bar(ans,x="Transaction_type",y=value1,title=("Transaction_type vs"+value1),text_auto=True)
    return fig.show()
# def scatterplot(ans):
#     value2=st.selectbox("select scatter:",["Transaction_amount","Transaction_count"])
#     fig=px.scatter(ans,x="Transaction_type",y=value2)
#     return fig.show()
def  bar_chart1(ans): 
    value3=st.selectbox("register_user:",["reg_users","app_opens"])
    fig=px.bar(ans,x="year",y=value3,title=("year vs " + value3),text_auto=True)
    return fig.show()
def bar_chart2(ans4):
    value=st.selectbox("brand details",["brand_count","Percentage"])
    fig=px.bar(ans4,x="brand_name",y=value,title=("brand name  vs "+value),text_auto=True)
    return fig.show()
def bar_chart_map(ans5):
    value=st.selectbox("select:", ["Transaction_amount","Transaction_count"])
    fig=px.bar(ans5,x="alter_state",y=value,title=("alter_state vs  "+value),text_auto=True)
    return fig.show()
def bar_chart3(ans7):
    #value=st.selectbox("select:",["reg_users"])
    fig=px.bar(ans7,x="pincode",y="reg_users",title=("pincode vs reg_users"),text_auto=True)
    return fig.show()
def pie_chart1(ans6):
     
    fig=px.pie(ans6,values="reg_users",names="state",title=("district vs  reg_users"),color_discrete_sequence=px.colors.sequential.RdBu)
    return fig.show()
def bar_chart(ans8):
    value=st.selectbox("select:",["Transaction_amount","Transaction_count"])
    fig=px.bar(ans8,x="district",y=value,title=("district vs "+value),text_auto=True)
    return fig.show()                              

engine=create_engine("mysql+pymysql://root:Risvana123@localhost:3306/phonepay_project",pool_size=10, max_overflow=20)
st.title("PhonePe Pulse Data Visualization")
img=Image.open(r"G:\guvi work\PhonePe_Pulse.jpg")
image=st.image(img)
#st.set_page_config(page_title="Phonepay", page_icon=img, layout="centered", initial_sidebar_state="auto", menu_items=None)
select=st.selectbox("How would you like to see",["Year Based Data","State Based Data","District based Data"])
if select=="Year Based Data":

    myfilt=st.selectbox("select:",("transaction_data",
                                   "yearly_mobile_transaction", 
                                   "registeruser_and_applicationopendetails"))
    #myfun=st.sidebar.selectbox('Select', ['Transaction_count', 'Transaction_amount'])
    if myfilt=="transaction_data":
  #         quater=st.sidebar.number_input('quater:',1,4)
   #         if quater:
  #             with engine.begin() as conn:
  #                 query=text(f'SELECT * FROM {myfilt} where quater={quater}')
   #                 Ans=pd.read_sql_query(query,conn)

            
        submit=st.checkbox("Press to View Dataframe and charts ")
        if submit:
            #choose=st.selectbox("select:", ["transaction_data"])
            year=st.selectbox("year:",[2018,2019,2020,2021,2022])
            sq=text(f'select * from {myfilt} where year={year}')
            with engine.begin() as conn:
                ans=pd.read_sql_query(sq,conn)
                st.write("Your Selected table from SQL Database:",ans)
                #st.write(ans)
#                 view=st.button("view chart")
#                 if view:
                pie_chart(ans)
                bar_chart4(ans)
                #scatterplot(ans)
                
            
    if myfilt=="registeruser_and_applicationopendetails":
       # year=st.selectbox("select year:",[2018,2019,2020,2021,2022]) 
        sq=text(f'select * from {myfilt}')
        with engine.begin() as conn:
                ans=pd.read_sql_query(sq,conn)
                st.write("Your Selected table from SQL Database:",ans)
                #st.write(ans)
                view=st.button("view chart")
                if view:
                    bar_chart1(ans)
    if myfilt=="yearly_mobile_transaction":
            year=st.selectbox("select year:",[2018,2019,2020,2021,2022])  
            sq=text(f'select* from {myfilt} where year={year}') 
            with engine.begin() as conn:
                ans4=pd.read_sql_query(sq,conn)
                st.write("Your Selected table from SQL Database:",ans4)
                #st.write(ans4)
                view=st.button("view chart")
                if view:
                    bar_chart2(ans4)
                         
if select=="State Based Data": 
    
    option=st.selectbox("select   ",["state_year_based_transactions","statebased_reguser_appopens"])
    if option=="state_year_based_transactions":
        year=st.selectbox("select year",[2018,2019,2020,2021,2022])
        sql=text(f'select * from {option} where year={year}')
        with engine.begin() as conn:
            ans5=pd.read_sql_query(sql,conn)
            st.write("Your Selected table from SQL Database:",ans5)
            #st.write(ans5)
            #view=st.button("view map and chart")
            #if view:
            graph(ans5)
            bar_chart_map(ans5)
                
    if option=="statebased_reguser_appopens":
        sql=text(f'select * from {option}')
        with engine.begin() as conn:
            ans5=pd.read_sql_query(sql,conn)
            st.write("Your Selected table from SQL Database:",ans5)
            #st.write(ans5)
#             view=st.button("view map")
#             if view:
            graph1(ans5)
#     if option=='state_particular_district_transaction':
#         #sql=text(f'select * from {option}')
#         state=st.selectbox("select state", ['Andaman & Nicobar',
#                                'Andhra Pradesh',
#                                'Arunachal Pradesh',
#                                'Assam',
#                                'Bihar',
#                                'Chandigarh',
#                                'Chhattisgarh',
#                                'Dadra and Nagar Haveli and Daman and Diu', 
#                                'Delhi', 
#                                'Goa',
#                                'Gujarat', 
#                                'Haryana',
#                                'Himachal Pradesh', 
#                                'Jammu & Kashmir',
#                                'Jharkhand', 
#                                'Karnataka', 
#                                'Kerala', 
#                                'Ladakh', 
#                                'Lakshadweep',
#                                'Madhya Pradesh',
#                                'Maharashtra',
#                                'Manipur', 
#                                'Meghalaya',
#                                'Mizoram',
#                                'Nagaland', 
#                                'Odisha',
#                                'Puducherry', 
#                                'Punjab',
#                                'Rajasthan',
#                                'Sikkim', 
#                                'Tamil Nadu', 
#                                'Telangana',
#                                'Tripura',
#                                'Uttar Pradesh',
#                                'Uttarakhand',
#                                'West Bengal'])
#         st.write(state)
#         sql=text(f"select * from {option} where alter_state='{state}'")  
#         #sql=text(f"select * from state_particular_district_transaction where alter_state='Tamil Nadu'")
#         with engine.begin() as conn:
#             ans8=pd.read_sql_query(sql,conn) 
#             st.write(ans8) 
#             bar_chart(ans8)
            
if select=="District based Data":  
    option=st.selectbox("",["top_10_district_regusers","particularyear_pincode_regusers",'state_particular_district_transaction'])
    if option=="top_10_district_regusers":
        sql=text(f'select * from {option}')
        with engine.begin() as conn:
            ans6=pd.read_sql_query(sql,conn)
            st.write("Your Selected table from SQL Database:",ans6)
            #st.write(ans6)
            view=st.button("view chart")
            if view:
                pie_chart1(ans6)
    if option=="particularyear_pincode_regusers": 
        year=st.selectbox("select year:",[2018,2019,2020,2021,2022])
        sql=text(f'select * from {option} where year={year}')
        with engine.begin() as conn:
            ans7=pd.read_sql_query(sql,conn)
            st.write("Your Selected table from SQL Database:",ans7)
            view=st.button("view chart")
            if view:
                 bar_chart3(ans7)         
    if option=='state_particular_district_transaction':
        #sql=text(f'select * from {option}')
        state=st.selectbox("select state", ['Andaman & Nicobar',
                               'Andhra Pradesh',
                               'Arunachal Pradesh',
                               'Assam',
                               'Bihar',
                               'Chandigarh',
                               'Chhattisgarh',
                               'Dadra and Nagar Haveli and Daman and Diu', 
                               'Delhi', 
                               'Goa',
                               'Gujarat', 
                               'Haryana',
                               'Himachal Pradesh', 
                               'Jammu & Kashmir',
                               'Jharkhand', 
                               'Karnataka', 
                               'Kerala', 
                               'Ladakh', 
                               'Lakshadweep',
                               'Madhya Pradesh',
                               'Maharashtra',
                               'Manipur', 
                               'Meghalaya',
                               'Mizoram',
                               'Nagaland', 
                               'Odisha',
                               'Puducherry', 
                               'Punjab',
                               'Rajasthan',
                               'Sikkim', 
                               'Tamil Nadu', 
                               'Telangana',
                               'Tripura',
                               'Uttar Pradesh',
                               'Uttarakhand',
                               'West Bengal'])
        st.write("your selecting state is ",state)
        sql=text(f"select * from {option} where alter_state='{state}'")  
        #sql=text(f"select * from state_particular_district_transaction where alter_state='Tamil Nadu'")
        with engine.begin() as conn:
            ans8=pd.read_sql_query(sql,conn) 
            st.write("Your Selected table from SQL Database:",ans8)
           # st.write(ans8)
#             view=st.button("view chart")
#             if view:
            bar_chart(ans8)
