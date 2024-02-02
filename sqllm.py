from dotenv import load_dotenv
load_dotenv() ## load all the environemnt variables

import streamlit as st
import os
import sqlite3

import google.generativeai as genai
## Configure Genai Key

genai.configure(api_key=os.getenv("Gemini"))

## Function To Load Google Gemini Model and provide queries as response

def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text

## Fucntion To retrieve query from the database

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

## Define Your Prompt
prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name travel_database and has the following tables - customers, flights, tours
    luggage. Where customers table have columns - customer_id, name, emain, phone_number and flights table have columns - flight_id, flight_number, departure_city, arrival_city
    and tours table have columns - tour_id, tour_name, start_date, end_date and luggage table have columns luggage_id, customer_id, flight_id, tour_id, weight. In 
    luggage table customer_id, flight_id, tour_id are the columns referenced from customers, flights, tours table respectively  
    \n\nFor example,\nExample 1 - Retrieve all customers and their contact information, 
    the SQL command will be something like this SELECT * FROM customers; 
    \nExample 2 - Tell me the flight details for flight FL303?, 
    the SQL command will be something like this SELECT * FROM flights where flight_number="FL303"; 
    \nExample 3 - Retrieve the total weight of luggage for a tour with id 1., 
    the SQL command will be something like this SELECT SUM(weight) AS total_weight FROM luggage WHERE tour_id = 1;
    also the sql code should not have ``` in beginning or end and sql word in output

    """
]

## Streamlit App

st.set_page_config(page_title="SQL query in Natural Language")
st.header("Gemini application to Query database in Natural-Language")

question=st.text_input("Input question to DB: ",key="input")

submit=st.button("Fetch Answer")

# if submit is clicked
if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    data=read_sql_query(response,"travel_database.db")
    st.subheader("Retrieved data is: ")
    for row in data:
        print(row)
        st.header(row)