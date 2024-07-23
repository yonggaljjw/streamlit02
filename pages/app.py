import streamlit as st

data = [1,2,3]
url = 'https://naver.com'

# 입력화면 - HTML/CSS/JS로 최종적으로 변환
val1 = st.button("안녕1")
val2 = st.button("안녕2")
val3 = st.button("안녕3")

# 동작
if val1 :
    st.image("./data/01.png")
    
elif val2 :
    st.image("./data/02.png")
elif val3 :
    st.image("./data/03.png")
else :
    st.image("./data/01.png")

#출력화면
st.write(val1)


#.: 현재경로 \ : WINDOWS, / : MAC 으로 구분한다.