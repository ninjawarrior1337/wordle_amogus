import streamlit as st
import numpy as np
from amogus import answers_to_board, compute_valid_amogus

from wordle import solutions

st.set_page_config("Wordle Amogus")

st.title("Wordle Amogus")

st.text_input("Wordle Solution", "valve", 5, "target")

a = compute_valid_amogus(st.session_state["target"])

lb, rb = answers_to_board(a)

l, r = st.columns(2)

with l:
    st.write(lb)
with r:
    st.write(rb)