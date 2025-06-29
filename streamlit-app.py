import streamlit as st
import os

# Define possible ranks and suits
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
suits = ['CLUBS', 'DIAMONDS', 'HEARTS', 'SPADES']

def card_selector(label):
    col1, col2 = st.columns(2)
    with col1:
        suit = st.selectbox(f"{label} Suit", suits, key=f"{label}_suit")
    with col2:
        rank = st.selectbox(f"{label} Rank", ranks, key=f"{label}_rank")
    return suit, rank

def card_png_path(suit, rank):
    filename = f"{rank.lower()}_of_{suit.lower()}.png"
    filepath = os.path.join("CardPNGs", filename)
    if os.path.exists(filepath):
        return filepath
    else:
        return None

st.title("Texas Hold'em Hand Visualizer")

st.header("Hero's Hand")
hero1 = card_selector("Hero Card 1")
hero2 = card_selector("Hero Card 2")

st.header("Villain's Hand")
villain1 = card_selector("Villain Card 1")
villain2 = card_selector("Villain Card 2")

st.header("Board")
flop1 = card_selector("Flop 1")
flop2 = card_selector("Flop 2")
flop3 = card_selector("Flop 3")
turn = card_selector("Turn")
river = card_selector("River")

# Display cards
def display_card(label, suit, rank):
    png_path = card_png_path(suit, rank)
    if png_path:
        st.markdown(f"**{label}**", unsafe_allow_html=True)
        st.image(png_path, width=90)
    else:
        st.warning(f"{label}: Card PNG not found.")

st.subheader("Hand Display")

cols = st.columns(7)
with cols[0]:
    display_card("Hero 1", *hero1)
with cols[1]:
    display_card("Hero 2", *hero2)
with cols[2]:
    display_card("Flop 1", *flop1)
with cols[3]:
    display_card("Flop 2", *flop2)
with cols[4]:
    display_card("Flop 3", *flop3)
with cols[5]:
    display_card("Turn", *turn)
with cols[6]:
    display_card("River", *river)

cols2 = st.columns(2)
with cols2[0]:
    display_card("Villain 1", *villain1)
with cols2[1]:
    display_card("Villain 2", *villain2)