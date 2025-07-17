import streamlit as st
import requests

st.title("🌤️ Weather App")

cities_name = [
    "Mumbai", "Delhi", "Bengaluru", "Hyderabad", "Ahmedabad", "Chennai", "Kolkata", "Surat", "Pune", "Jaipur",
    "Lucknow", "Kanpur", "Nagpur", "Indore", "Thane", "Bhopal", "Visakhapatnam", "Patna", "Vadodara", "Ghaziabad",
    "Ludhiana", "Agra", "Nashik", "Faridabad", "Meerut", "Rajkot", "Kalyan", "Vasai", "Varanasi", "Srinagar",
    "Aurangabad", "Dhanbad", "Amritsar", "Navi Mumbai", "Allahabad (Prayagraj)", "Ranchi", "Howrah", "Coimbatore",
    "Jabalpur", "Gwalior", "Vijayawada", "Jodhpur", "Madurai", "Raipur", "Kota", "Guwahati", "Chandigarh", "Solapur",
    "Hubli", "Mysore", "Tiruchirappalli", "Bareilly", "Aligarh", "Moradabad", "Tiruppur", "Noida", "Bhilai", "Guntur",
    "Jamshedpur", "Warangal", "Cuttack", "Firozabad", "Bhiwandi", "Kochi", "Bhavnagar", "Dehradun", "Durgapur",
    "Asansol", "Nanded", "Ajmer", "Ujjain", "Sangli", "Rourkela", "Mangalore", "Kolhapur", "Bokaro", "Bikaner",
    "Siliguri", "Thrissur", "Nellore", "Raurkela", "Malegaon", "Gandhinagar", "Bilaspur", "Mathura", "Kamarhati",
    "Panipat","mohali","pathankot", "Darbhanga", "Sagar", "Satara", "Junagadh", "Ambattur", "Tirunelveli", "Davanagere", "Sambalpur",
    "Shimoga", "Eluru", "Rewa", "Nizamabad", "Bhagalpur", "Kharagpur", "Haridwar", "Aizawl"
]

API_KEY = "33a070494ff0713e4f2c521458ab2aca"

choice = st.selectbox("Choose your city:", cities_name)

st.write(f"You selected: {choice}")

if choice:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={choice}&appid={API_KEY}&units=metric"
    responce = requests.get(url)

    if responce.status_code ==200:
        st.write("Weather data fetched successfully!")
        st.json(responce.json())
    else:
        st.write("Failed to fetch weather data. Please try again later.")
    
    
    st.write(f"{choice}")