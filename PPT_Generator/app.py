import streamlit as st
import requests
import subprocess
import sys

st.markdown("""
<style>
/* 3D glow animation */
@keyframes glow3D {
    0% { text-shadow: 
            0 1px 0 #ff00c8, 
            0 2px 0 #ff00c8,
            0 3px 0 #ff00c8,
            0 4px 0 #ff00c8,
            0 0 12px rgba(0, 204, 255, 0.7),
            0 0 22px rgba(0, 124, 255, 0.5); 
        transform: translateY(0); }
    50% { text-shadow: 
            0 1px 0 #00d4ff, 
            0 2px 0 #00d4ff,
            0 3px 0 #00d4ff,
            0 4px 0 #00d4ff,
            0 0 18px rgba(255, 0, 200, 0.7),
            0 0 26px rgba(255, 0, 120, 0.5);
        transform: translateY(-3px); }
    100% { text-shadow: 
            0 1px 0 #ff00c8, 
            0 2px 0 #ff00c8,
            0 3px 0 #ff00c8,
            0 4px 0 #ff00c8,
            0 0 12px rgba(0, 204, 255, 0.7),
            0 0 22px rgba(0, 124, 255, 0.5);
        transform: translateY(0); }
}

/* 3D glow title style */
.glow3d-title {
    font-size: 54px;
    font-weight: 900;
    text-align: center;
    background: linear-gradient(90deg, #ff00c8, #00d4ff);
    -webkit-background-clip: text;
    color: transparent;
    animation: glow3D 2.5s ease-in-out infinite;
    letter-spacing: 2px;
    margin-top: 25px;
    margin-bottom: 10px;
}

/* subtitle fade */
.glow3d-sub {
    text-align: center;
    font-size: 18px;
    color: rgba(255,255,255,0.85);
    margin-top: -5px;
    letter-spacing: 1px;
}
</style>

<h1 class="glow3d-title">AGENTIC POWER POINT GENERATOR</h1>
<div class="glow3d-sub">Create AI-Powered Presentations Instantly</div>
""", unsafe_allow_html=True)

st.sidebar.header(':red[Presentation Features]')
font_size= st.sidebar.slider(label="Font Size",min_value=10 , max_value=40,value =16,)
font_type=st.sidebar.selectbox("Please select a Font Style",
                               ("Calibri","Arial","Helvetica","Lato","Roboto"))

presentation_theme=st.sidebar.text_area("Please select a fornt Theme",
                               placeholder="Detail about how your presentation want to look like")

#st.title("AGENTIC POWER POINT GENERATOR")
prompt=st.text_area("Please write the details of how to create the ppt")

if st.button("generate ppt"):
    if prompt:
        response=requests.post(url="https://lopepi.app.n8n.cloud/webhook-test/76815fe0-d0d7-486b-8254-bbfbfcdd7059",
                 json={"prompt":prompt,
                       "theme":presentation_theme,
                       "fornt_size":font_size,
                       "font_type":font_type})
        if response.status_code==200:
            st.write("success")

            with open("app1.py","w") as file:
            
                file.write(response.json()["output"].strip("```python"))    ## for open the file 
            subprocess.run([sys.executable,"app1.py"])
    

    else:
        st.error("API request failed")

else:
    st.warning("Please enter PPT details")


try:
    with open("generated_presentation.pptx", 'rb') as file:
        st.download_button(label="Download Presentation",
                       data=file,
                       file_name="Presentation.pptx")
        
except FileNotFoundError:
    st.info("No presentation generated yet . Click 'Generate Presentation'first ")