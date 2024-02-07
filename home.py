import streamlit as st
import requests  # Import necessary libraries here
from PIL import Image
from io import BytesIO

def display_home():
    st.title("Daily Horoscopes - Home")

    zodiac_images = {
    "Aries": "https://s.net.vn/3gvx",
    "Taurus": "https://s.net.vn/k94g",
    "Gemini": "https://s.net.vn/8h7i",
    "Cancer": "https://s.net.vn/Pj7s",
    "Leo": "https://s.net.vn/jhxs",
    "Virgo": "https://s.net.vn/ZMx4",
    "Libra": "https://s.net.vn/6eRu",
    "Scorpio": "https://s.net.vn/kr84",
    "Sagittarius": "https://s.net.vn/f070",
    "Capricorn": "https://s.net.vn/T7HU",
    "Aquarius": "https://s.net.vn/9N1X",
    "Pisces": "https://s.net.vn/CXoV"
}

    def get_zodiac_sign(day, month):
        if (month == 3 and day >= 21) or (month == 4 and day <= 19):
            return "Aries"
        elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
            return "Taurus"
        elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
            return "Gemini"
        elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
            return "Cancer"
        elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
            return "Leo"
        elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
            return "Virgo"
        elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
            return "Libra"
        elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
            return "Scorpio"
        elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
            return "Sagittarius"
        elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
            return "Capricorn"
        elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
            return "Aquarius"
        else:
            return "Pisces"

    st.title("What is your Zodiac?")
    birthday = st.date_input("Your birthday:")

    if st.button("Let's Find"):
        day = birthday.day
        month = birthday.month
        zodiac_sign = get_zodiac_sign(day, month)

        if zodiac_sign in zodiac_images:
            st.write(f"{zodiac_sign}:")
            response = requests.get(zodiac_images[zodiac_sign])
            image = Image.open(BytesIO(response.content))
            st.image(image, caption=zodiac_sign, use_column_width=True)
            st.balloons()
