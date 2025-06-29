import streamlit as st
import os

# Define possible ranks and suits
ranks = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11-JACK', '12-QUEEN', '13-KING']
suits = ['CLUB', 'DIAMOND', 'HEART', 'SPADE']

def card_selector(label):
    col1, col2 = st.columns(2)
    with col1:
        suit = st.selectbox(f"{label} Suit", suits, key=f"{label}_suit")
    with col2:
        rank = st.selectbox(f"{label} Rank", ranks, key=f"{label}_rank")
    return suit, rank

def card_svg(suit, rank):
    filename = f"{suit.upper()}-{rank}.svg"
    filepath = os.path.join("CardVectors", filename)
    if os.path.exists(filepath):
        with open(filepath, "r") as svg_file:
            svg_content = svg_file.read()
        return svg_content
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
    svg = card_svg(suit, rank)
    if svg:
        st.markdown(f"**{label}**", unsafe_allow_html=True)
        st.components.v1.html(svg, height=140)
    else:
        st.warning(f"{label}: Card vector not found.")

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