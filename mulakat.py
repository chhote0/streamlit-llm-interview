import streamlit as st
import pandas as pd
import numpy as np
from transformers import pipeline
import time
import webbrowser
import requests

st.title("Karşılıklı Mülakat")


def open_main():
    url = 'http://localhost:8502'  
    webbrowser.open_new_tab(url)

st.button("Ana Sayfaya Dön", on_click=open_main)