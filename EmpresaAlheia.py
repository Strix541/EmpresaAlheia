import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, empty_col, col2 = st.columns([2.0, 0.1, 3.0])

with col1:
    st.image("images/906031.jpg")
with col2:
    st.title("""Orthodox Workers""")

    content1 = ("""This company consists on very hard working 
         people that can do any job you want by any means necessary
         and when i say any means its ANY means.
         We want people to know that we are very friendly. Please hire us.
         All of our companions are from different places around the world, 
         we want diversity because we are not racists."""
         
         """At our company, we take immense pride in our team of dedicated 
         and hardworking individuals, each possessing a unique set of skills 
         that enables us to tackle any job with unwavering determination. 
         When we say any means necessary, we mean it – our team is equipped 
         with the versatility and resourcefulness to overcome challenges 
         and deliver exceptional results."""
         
         """Our commitment to friendliness extends beyond the quality of our work; 
         we strive to create a welcoming and inclusive environment for our clients.
         Your satisfaction is our top priority, and we believe that a positive 
         and collaborative atmosphere fosters creativity and productivity.""")
    st.write(content1)

    content2 = ("""Thank you for taking the time to visit our website. 
                We sincerely appreciate your interest in our company and the services we offer.
                If you're seeking a dedicated and diverse team that goes above and beyond 
                to meet your needs, look no further – you've found the right place. 
                We eagerly anticipate the opportunity to work with you and demonstrate 
                the exceptional capabilities of our team. Feel free to reach out to us 
                for any inquiries or to discuss how we can contribute to the success of your projects. 
                Together, we can achieve greatness.""")
    st.write(content2)

st.title("This are our companions:")

col3, col4, col5 = st.columns([2.0, 2.1, 1.0])

df = pandas.read_csv("data.csv", sep=",")

with col3:
    for index, row in df[:4].iterrows():
        st.header(row["role"])
        st.image("images/" + row["image"])
        st.write(row["first name"] + row["last name"])
with col4:
    for index, row in df[4:8].iterrows():
        st.header(row["role"])
        st.image("images/" + row["image"])
        st.write(row["first name"] + row["last name"])
with col5:
    for index, row in df[8:12].iterrows():
        st.header(row["role"])
        st.image("images/" + row["image"])
        st.write(row["first name"] + row["last name"])
