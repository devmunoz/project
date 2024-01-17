import streamlit as st

import numpy as np
import pandas as pd
import requests


def main():
    # Title
    st.title("Hello Streamlit App.")

    # Text
    st.text("Hello World!")
    name = "Daniel here... :D"
    st.text("{}".format(name))

if __name__ == "__main__":
    main()