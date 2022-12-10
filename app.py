import streamlit as st
import pandas as pd
import numpy as np
from htbuilder import HtmlElement, div, ul, li, br, hr, a, p, img, styles, classes, fonts
from htbuilder.units import percent, px
from htbuilder.funcs import rgba, rgb

st.set_option('deprecation.showfileUploaderEncoding', False)

st.header("Prediction of Drug Efficacy Using Regressor Methods")


df = pd.read_csv("ProModel.csv")
x = df.iloc[:,0:15,]
y = df.iloc[:,15,]
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x, y)


uploaded = st.file_uploader("Upload spreadsheet", type=["csv", "xlsx"])
if uploaded:
    if st.button("Predict"):
        test = pd.read_csv(uploaded)
        pred = regressor.predict(test)
        st.write("The predicted Priming value is:", pred)
        st.write("Falls within", 80,"% of confidence interval")



def image(src_as_string, **style):
    return img(src=src_as_string, style=styles(**style))


def link(link, text, **style):
    return a(_href=link, _target="_blank", style=styles(**style))(text)


def layout(*args):

    style = """
    <style>
      # MainMenu {visibility: hidden;}
      footer {visibility: hidden;}
     .stApp { bottom: 105px; }
    </style>
    """

    style_div = styles(
        position="fixed",
        left=0,
        bottom=0,
        margin=px(0, 0, 0, 0),
        width=percent(100),
        color="black",
        text_align="center",
        height="auto",
        opacity=1
    )

    style_hr = styles(
        display="block",
        margin=px(8, 8, "auto", "auto"),
        border_style="inset",
        border_width=px(2)
    )

    body = p()
    foot = div(
        style=style_div
    )(
        hr(
            style=style_hr
        ),
        body
    )

    st.markdown(style, unsafe_allow_html=True)

    for arg in args:
        if isinstance(arg, str):
            body(arg)

        elif isinstance(arg, HtmlElement):
            body(arg)

    st.markdown(str(foot), unsafe_allow_html=True)


def footer():
    myargs = [
        "Rishiikeshwer Brindha Sivakumar, Mohammad Haris, RahulKumar Shivakumar ",
        br(),
        " Team 3: George Masson University, Virginia ",
    ]
    layout(*myargs)


if __name__ == "__main__":
    footer()
