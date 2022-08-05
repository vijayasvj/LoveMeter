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

lottie_intro = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_jvxwtdtp.json")
lottie_95 = load_lottieurl("https://assets2.lottiefiles.com/private_files/lf30_ya6bnm3a.json")
lottie_90 = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_5Vz7xX.json")
lottie_85 = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_r063ivbm.json")
lottie_80 = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_utpGTg.json")
lottie_75 = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_ad3uxjiv.json")
lottie_70 = load_lottieurl("https://assets2.lottiefiles.com/private_files/lf30_ux98admv.json")
lottie_65 = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_vhq1t67x.json")
lottie_60 = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_rjs5bshs.json")
lottie_55 = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_DH0HdV.json")
lottie_50 = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_imcvpf0j.json")
lottie_45 = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_Dz3Jb8.json")
lottie_friends = load_lottieurl("https://assets7.lottiefiles.com/private_files/lf30_hxmzmij0.json")



st.title('Love meter! ❤️')
 
left_column, right_column = st.columns(2)

with left_column:
    st.write('##')
    st.write('##')
    st.markdown('Is there a girl in your class who gives you butterflies in your stomach? Have you been seeing this cute guy in the coffee shop you can just not seem to take your eyes off?')
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
    text = ""
    x = 92
    x = random.randint(40, 99)
    if x > 95:
        text = "Love is in the air, your love will last forever!"
    if x > 90 and x <=95:
        text = "Oo la la, you are sure to steal their heart!"
    if x > 85 and x <=90:
        text = "You are sure to sweep them off their feet!"
    if x >= 80 and x <= 85:
        text = "Cupid just shot an arrow! Love it is!"
    if x >= 75 and x <= 70:
        text = "This is the beginning of a great love story!"
    if x >= 70 and x <= 65:
        text = "You guys are definitely going to hit it off!"
    if x >= 65 and x <= 70:
        text = "What a great couple you will make!"
    if x >= 60 and x <= 65:
        text = "Love is brewing!"    
    if x >= 55 and x <= 60:
        text = "It's raining hearts!"
    if x >= 50 and x <= 55:
        text = "Your feelings are stronger than you think!"
    if x >= 45 and x <= 50:
        text = "Maybe a little effort, but a coffee date could help write a good story"
    if x >= 40 and x <= 45:
        text = "Umm...Sometimes it's best to stay friends"
    return x, text

if go and name1 and name2:
    col1, col2, col3 = st.columns(3)
    x, y = check(name1, name2)
    my_bar = st.progress(0)

    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1)

    my_bar.empty()

    if x > 95:
        with col2:
            st.markdown("##     Love is in the air, your love will last forever!")
            st.markdown(f"<h1 style='text-align: center; color: red;'>{x}%</h1>", unsafe_allow_html=True) 
            st_lottie(lottie_95, height=300, key="love95")

    if x > 90 and x <=95:
        with col2:
            st.markdown("##      Oo la la, you are sure to steal their heart!")
            st.markdown(f"<h1 style='text-align: center; color: red;'>{x}%</h1>", unsafe_allow_html=True) 
            st_lottie(lottie_90, height=300, key="loveaam")

    if x > 85 and x <=90:
        with col2:
            st.markdown("##     You are sure to sweep them off their feet!")
            st.markdown(f"<h1 style='text-align: center; color: red;'>{x}%</h1>", unsafe_allow_html=True) 
            st_lottie(lottie_85, height=300, key="cheriedholove")
            

    if x >= 80 and x <= 85:
        with col2:
            st.markdown("##     Cupid just shot an arrow! Love it is!")
            st.markdown(f"<h1 style='text-align: center; color: red;'>{x}%</h1>", unsafe_allow_html=True) 
            st_lottie(lottie_80, height=300, key="friends80")
    
    if x >= 75 and x <= 80:
        with col2:
            st.markdown("##     This is the beginning of a great love story!")
            st.markdown(f"<h1 style='text-align: center; color: red;'>{x}%</h1>", unsafe_allow_html=True) 
            st_lottie(lottie_75, height=300, key="friends74")

    if x >= 70 and x <= 75:
        with col2:
            st.markdown("##     You guys are definitely going to hit it off!")
            st.markdown(f"<h1 style='text-align: center; color: red;'>{x}%</h1>", unsafe_allow_html=True) 
            st_lottie(lottie_70, height=300, key="friends70")

    if x >= 65 and x <= 70:
        with col2:
            st.markdown("##     What a great couple you will make!")
            st.markdown(f"<h1 style='text-align: center; color: red;'>{x}%</h1>", unsafe_allow_html=True) 
            st_lottie(lottie_65, height=300, key="friends65")

    if x >= 60 and x <= 65:
        with col2:
            st.markdown("##      Love is brewing!")
            st.markdown(f"<h1 style='text-align: center; color: red;'>{x}%</h1>", unsafe_allow_html=True) 
            st_lottie(lottie_60, height=300, key="friends60")

        
    if x >= 55 and x <= 60:
        with col2:
            st.markdown("##     It's raining hearts!")
            st.markdown(f"<h1 style='text-align: center; color: red;'>{x}%</h1>", unsafe_allow_html=True) 
            st_lottie(lottie_55, height=300, key="friends60")

    if x >= 50 and x <= 55:
        with col2:
            st.markdown("##     Your feelings are stronger than you think!")
            st.markdown(f"<h1 style='text-align: center; color: red;'>{x}%</h1>", unsafe_allow_html=True) 
            st_lottie(lottie_50, height=300, key="friends60")

    if x >= 45 and x <= 50:
        with col2:
            st.markdown("##     Maybe a little effort, but a coffee date could help write a good story")
            st.markdown(f"<h1 style='text-align: center; color: red;'>{x}%</h1>", unsafe_allow_html=True) 
            st_lottie(lottie_45, height=300, key="friends60")

    if x >= 40 and x <= 45:
        with col2:
            st.markdown("##     Umm...Sometimes it's best to stay friends")
            st.markdown(f"<h1 style='text-align: center; color: red;'>{x}%</h1>", unsafe_allow_html=True) 
            st_lottie(lottie_friends, height=300, key="friends60")

    
    
    
    
    
    
    
    
            
            
    
