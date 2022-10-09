import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image
pip install openpyxl 


st.set_page_config(page_title='Survey Results')
st.header('Survey Results 2021')
st.subheader('Was the tutorial helpful?')

### --- LOAD DATAFRAME
excel_file = 'Survey_Results.xlsx'
sheet_name = 'DATA'

df = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='B:D',
                   header=3)

df_participants = pd.read_excel(excel_file,
                                sheet_name= sheet_name,
                                usecols='F:G',
                                header=3)
df_participants.dropna(inplace=True)

st.dataframe(df)

pie_chart = px.pie(df_participants,
                   title='Total number of participants',
                   values= 'Participants',
                    names = 'Departments')
st.plotly_chart(pie_chart)

df_participants.dropna(inplace=True)


image = Image.open('survey.jpg')
st.image(image, caption='Shalom',
         use_column_width=True)
#selection

department = df['Department'].unique().tolist()
ages = df['Age'].unique().tolist()

age_selection = st.slider('Age:', min_value=min(ages),
                          max_value = max(ages),
                          value= (min(ages),max(ages)))
department_selection = st.multiselect('Department:',department,
                                      default=department)
mask = (df['Age'].between(*age_selection))& (df['Department'].isin(department_selection))
number_of_results = df[mask].shape[0]
st.markdown(f'* Availabel Results:{number_of_results}*')
