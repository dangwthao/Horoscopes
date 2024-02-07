import streamlit as st
import requests  
from bs4 import BeautifulSoup

# Forecast Function 
def get_horoscope_by_day(zodiac_sign: int):
    res = requests.get(
        f"https://www.horoscope.com/us/horoscopes/general/horoscope-archive.aspx?sign={zodiac_sign}")
    soup = BeautifulSoup(res.content, 'html.parser')
    data = soup.find('div', attrs={'class': 'main-horoscope'})
    return data.p.text


# def get_horoscope_by_week(zodiac_sign: int):
#     res = requests.get(
#         f"https://www.horoscope.com/us/horoscopes/general/horoscope-general-weekly.aspx?sign={zodiac_sign}")
#     print(res.content) 
#     soup = BeautifulSoup(res.content, 'html.parser')
#     data = soup.find('div', attrs={'class': 'main-horoscope'})
#     return data.p.text


def get_horoscope_by_month(zodiac_sign: int):
    res = requests.get(
        f"https://www.horoscope.com/us/horoscopes/general/horoscope-general-monthly.aspx?sign={zodiac_sign}")
    soup = BeautifulSoup(res.content, 'html.parser')
    data = soup.find('div', attrs={'class': 'main-horoscope'})
    return data.p.text


def get_horoscope_by_year(zodiac_sign: int):
    res = requests.get(
        f"https://www.horoscope.com/us/horoscopes/yearly/2024-horoscope-aries.aspx?sign={zodiac_sign}")
    soup = BeautifulSoup(res.content, 'html.parser')
    data = soup.find("section", attrs={'class': "tab-content active", 'id': "personal"})
    return data.p.text
    # if data:
 
    #     paragraph = data.find("p")

    #     if paragraph:
    #         text_content = paragraph.get_text(separator="\n")
    #         return text_content
    #     else:
    #         return "No text content found within the 'p' element."
    # else:
    #     return "Section not found."

def display_forecast():
        # Zodiac sign dropdown
        signs = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]
        selected_sign = st.selectbox("Choose Your Zodiac Sign", signs)
        zodiac_sign = signs.index(selected_sign) + 1

        # Horoscope period radio
        horoscope_period = st.radio("Choose the Horoscope Period", ["Today", "Monthly", "Yearly" ])

        # Horoscope result
        horoscope = ""
        if horoscope_period == "Today":
            
            horoscope = get_horoscope_by_day(zodiac_sign)
              
        elif horoscope_period == "Monthly":
            horoscope = get_horoscope_by_month(zodiac_sign)
        
        elif horoscope_period == "Yearly":
            horoscope = get_horoscope_by_year(zodiac_sign)

        if horoscope:
            st.success(f"{selected_sign} Horoscope for {horoscope_period.lower()} period:\n{horoscope}")
