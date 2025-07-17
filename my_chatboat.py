import streamlit as st
import wikipedia

st.title("🤖 MY Chatbot")


if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

def get_response(user_inp):
    lower_inp = user_inp.lower()

    if "how are you" in lower_inp:
        return "I am fine, how are you?"
    elif "who built you" in lower_inp:
        return "I was built by AMCODERS."
    else:
        try:
            answer = wikipedia.summary(lower_inp, sentences=2)
            return answer
        except Exception:
            return "Something went wrong. Please try again."


user_inp = st.chat_input("How can I help you?")

if user_inp:
    st.session_state.chat_history.append(("user", user_inp))
    response = get_response(user_inp)
    st.session_state.chat_history.append(("bot", response))

for sender, message in st.session_state.chat_history:
    with st.chat_message(sender):
        st.markdown(message)
