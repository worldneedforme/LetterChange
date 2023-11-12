import streamlit as st


# if st.button('RUN AI'):
#     with st.spinner('작성중..'):


st.title('대문자변경')

content_upper = st.text_input('대문자 변경을 원하는 문자열을 입력하세요.')

result1 = content_upper.upper()
st.write(result1)



st.title('소문자변경')
content_lower = st.text_input('소문자 변경을 원하는 문자열을 입력하세요.')

result2 = content_lower.lower()
st.write(result2)
        

st.title('앞글자만 대문자')
content_capitalize = st.text_input('앞글자만 대문자로 변경을 원하는 문자열을 입력하세요.')

result3 = content_capitalize.title()
st.write(result3)


               