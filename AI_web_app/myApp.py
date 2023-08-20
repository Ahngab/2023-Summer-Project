from api.AI import AIAPI
import streamlit as st
from PIL import Image
import time


@st.cache_resource
def get_api():
    return AIAPI(font="resources/malgun.ttf")

def main():
    api = get_api()

    st.title("책 읽어주는 AI")
    st.markdown("입력한 이미지로부터 텍스트를 추출합니다.(OCR)")
    tab1, tab2 = st.tabs(['책 텍스트 추출', '텍스트 내용 요약'])
    
    #image to text
    with tab1:
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("책 텍스트 추출")
            query = st.file_uploader("이미지를 입력해주세요.")
            response = ""
            if query is not None:
                st.image(query)

        with col2:
            with st.spinner('Wait for it...'):
                response = api.query_image2text(query)
                st.subheader("추출 결과")
                st.markdown(response)

    #summarize text
    with tab2:
        st.subheader("텍스트 내용 요약")
        st.markdown("추출한 텍스트를 바탕으로 내용을 요약합니다.")
        if st.button("요약하기"):
            if response:            
                with st.spinner('Wait for it...'):
                    title, summary = api.query_text2text(response)
                    st.subheader(title)
                    st.markdown("---")
                    st.markdown(summary)


if __name__ == '__main__':
    main()