import streamlit as st
from streamlit_chat import message
from tester import *


st.set_page_config(page_title="OutBound Reach", page_icon=":phone:")
with st.sidebar:
    st.markdown(
        """
        <style>
        .big-font {
            font-size: 40px; /* Adjust the size as needed */
            
        }
        .small-margin {
            
            font-size: 16px; /* Size of GROQ API */
            margin-top: -30px; /* Move GROQ API closer to Steam Labs */
            font-style: italic; /* Italicize for style */
            color: gray; /* Lighter color for a subtle effect *
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown('<p class="big-font">Steam Labs ⚡</p>', unsafe_allow_html=True)
    
    st.markdown('<p class="small-margin">Powered by</p>', unsafe_allow_html=True)
    st.markdown("<style></br><br><style>", unsafe_allow_html=True)
    GROQ_API_KEY = st.sidebar.text_input('GROQ API 🔑')        
    st.file_uploader("Upload your data 📃")
    st.button("Process")
    text = st.chat_input("Enter your message")


st.markdown("""
    <style>
        body {
            overflow: hidden;
            background: radial-gradient(circle, #3b0e68 0%, #1a084e 100%);
        }
        .mic {
            position: absolute;
            top: 70%;
            left: 50%;
            margin-top:250px;   
            transform: translate(-40%, -60%);
            color: #fff;
        }
        .mic::before, .mic::after {
            content: "";
            position: absolute;
            top: 50%;
            left: 50%;
            
            transform: translate(-50%, -50%);
            border-radius: 100%;
            z-index: 2;
            box-shadow: 0 0 20px 20px #1c084f;
        }
        .mic::before {
            width: 400px;
            height: 400px;
            background-color: #1a084e;
        }
        .mic::after {
            width: 250px;
            height: 250px;
            background-color: #2f1e5f;
            animation: circle-size 0.8s linear infinite alternate;
        }
        .mic-icon {
            box-sizing: border-box;
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%) scale(5);
            display: block;
            width: 16px;
            height: 12px;
            border-bottom-left-radius: 120px;
            border-bottom-right-radius: 120px;
            border: 2px solid;
            border-top: 0;
            margin-top: 20px;
            z-index: 3;
        }
        .mic-icon::before, .mic-icon::after {
            content: "";
            display: block;
            box-sizing: border-box;
            position: absolute;
        }
        .mic-icon::before {
            width: 2px;
            height: 5px;
            top: calc(100% + 1px);
            left: 50%;
            transform: translate(-50%, 0);
            background-color: #fff;
        }
        .mic-icon::after {
            border: 2px solid;
            width: 8px;
            height: 18px;
            left: 50%;
            top: -10px;
            border-radius: 4px;
            transform: translate(-50%, 0);
        }
        .mic-shadow {
            width: 400px;
            height: 400px;
            position: absolute;
            top: 50%;
            left: 50%;
            border-radius: 100%;
            z-index: 1;
            box-shadow: 10px -55px 30px 15px #823ca6, 24px -10px 47px 10px #aab3d2, -21px -25px 97px 10px #5acee3, 51px 5px 17px 10px #1b7d8f, 3px 2px 77px 10px #f30bf5;
            animation: shadow-rotate 1.5s linear infinite;
            transform-origin: center;
        }
        @keyframes circle-size {
            from {
                width: 250px;
                height: 250px;
            }
            to {
                width: 300px;
                height: 300px;
            }
        }
        @keyframes shadow-rotate {
            from {
                transform: translate(-50%, -50%) rotate(0deg);
            }
            to {
                transform: translate(-50%, -50%) rotate(360deg);
            }
        }
    </style>

    <div class="mic">
      <i class="mic-icon"></i>
      <div class="mic-shadow"></div>
    </div>
""", unsafe_allow_html=True)

# Add custom styling for chat messages
st.markdown(
    """
    <style>
    .chat-container {
        max-width: 400px;
        margin-top:470px;
        padding: 10px;
        
    }
    .chat-message {
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 10px;
        
        max-width: 70%;
    }
    .user {
        position:relative;
        
    }
    .assistant {
        position:relative;
        right:0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Create a chat-like container
st.markdown('<div class="chat-container">', unsafe_allow_html=True)

# Add chat messages
if GROQ_API_KEY:
    if text:
        message(text)
        message("I'm good what about you ?",is_user=True)
#st.markdown('<div class="chat-message user">🤖 Hi, how are you?</div>', unsafe_allow_html=True)
#st.markdown('<div class="chat-message assistant">🚹 I\'m good</div>', unsafe_allow_html=True)

# Close chat container
st.markdown('</div>', unsafe_allow_html=True)