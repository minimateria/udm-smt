import streamlit as st
import time

st.title('streamlit 超入門')

st.write('プログレスバーの表示')
'Start!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done!'

left_column, center_column, right_column = st.columns(3)
button = left_column.button('中央カラムに文字を表示')
if button:
    center_column.write('ここは中央カラム')

expander = st.expander('問合せ1')
expander.write('問合せ1の回答を書く')
expander = st.expander('問合せ2')
expander.write('問合せ2の回答を書く')
