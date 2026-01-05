import streamlit as st


st.header("My App")   #streamlit.header("my app")
st.button("click me")
st.radio("Select me",["option 1","option 2"])

st.text_input("write here")
st.text_area("write here")
st.selectbox("Select",["01","02"])
st.file_uploader("upload file")
st.color_picker("pick a color")
st.camera_input("Record me")