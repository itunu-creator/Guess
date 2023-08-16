import streamlit as st
import random
from PIL import Image

img = Image.open("guess img.JPG")
st.image(img)

st.header("Guess Game")
st.subheader("your future is in your hands")

b= st.number_input("Please input a number from 1 - 6")
a= random.randint(1,6)


def game(a,b):
    if b > 6:
        return("Invalid input, please select a number between 1 and 6,step=1")
    else:
        if a == b:
            return("Correct")
        else:
            st.write(f"Your selected number is {b}")
            st.write(f"Random number is {a}")
            return("Wrong, try again")
        
if st.button("Try Your Luck"):
    st.write(game(a,b))