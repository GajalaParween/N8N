import streamlit as st

if "x" not in st.session_state:
    st.session_state["x"]=0

if st.button("click"):
    st.session_state["x"]=st.session_state["x"]+1


st.write(st.session_state["x"])