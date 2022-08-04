import streamlit as st
import requests
from streamlit_lottie import st_lottie
import random
import time 

st.set_page_config(layout = "wide")
body = st.container()



def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_80 = load_lottieurl("https://assets2.lottiefiles.com/private_files/lf30_ya6bnm3a.json")
lottie_intro = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_jvxwtdtp.json")
lottie_friends = load_lottieurl("https://assets7.lottiefiles.com/private_files/lf30_hxmzmij0.json")
lottie_70 = load_lottieurl("https://assets1.lottiefiles.com/private_files/lf30_vutrqlyh.json")
lottie_60 = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_SLZG2B.json")


st.title('Love meter! ❤️')
 
left_column, right_column = st.columns(2)

with left_column:
    st.write('##')
    st.write('##')
    st.markdown('Is there is girl in your class who gives you butterflies in your stomach? Have been seeing this cute guy in the coffee shop you can just not seem to take your eyes off?')
    #st.markdown('Have been seeing this cute guy in the coffee shop you can just not seem to take your eyes off?')
    st.markdown(' Type in your name and that of your crush to find out how well you guys can hit it off!')
    st.write("---")

with right_column:
    st_lottie(lottie_intro, height=300, key="intro")

st.write('##')

with st.sidebar:
    st.write('##')
    st.write('##')
    name1 = st.text_input("Your name")  
    name2 = st.text_input("The name of that 'someone special'")
    go = st.button("GO!")

def check(namethis, namethat):
    x = random.randint(40, 99)
    if x > 85:
        text = "Love is in the air, your love will last forever!"
    if x > 70 and x <=85:
        text = "Its raining hearts!"
    if x > 60 and x <=70:
        text = "Your feelings are stronger than you think!"
    if x >= 40 and x <= 60:
        text = "Umm...Sometimes its best to stay friends"
    return x, text

if go and name1 and name2:
    col1, col2, col3 = st.columns(3)
    x, y = check(name1, name2)
    my_bar = st.progress(0)

    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1)

    my_bar.empty()

    if x > 85:
        with col2:
            st.markdown("##     Love is in the air, your love will last forever!")
            st.markdown(f"<h1 style='text-align: center; color: red;'>{x}%</h1>", unsafe_allow_html=True) 
            st_lottie(lottie_80, height=300, key="love")

    if x > 70 and x <=85:
        with col2:
            st.markdown("##      Its raining hearts! You are perfect for each other")
            st.markdown(f"<h1 style='text-align: center; color: red;'>{x}%</h1>", unsafe_allow_html=True) 
            st_lottie(lottie_70, height=300, key="loveaam")

    if x > 60 and x <=70:
        with col2:
            st.markdown("##     Your feelings are stronger than you think!")
            st.markdown(f"<h1 style='text-align: center; color: red;'>{x}%</h1>", unsafe_allow_html=True) 
            st_lottie(lottie_60, height=300, key="cheriedholove")
            

    if x >= 40 and x <= 60:
        with col2:
            st.markdown("##     Umm...Sometimes its best to stay friends")
            st.markdown(f"<h1 style='text-align: center; color: red;'>{x}%</h1>", unsafe_allow_html=True) 
            st_lottie(lottie_friends, height=300, key="friends")
    
    
    
    
    
    
    
    
    
    
            
            
    
