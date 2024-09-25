import streamlit as st
from app.components import render_header, render_footer

st.set_page_config(page_title="Kundensegmentierung", layout="wide")

# Restlicher Inhalt der Seite

st.title("Customer Segmentation Use Case")
st.header("Situation")
st.write("""
*Beschreiben Sie hier die Ausgangssituation oder das Problem, das angegangen wird.*
""")

## Task
st.header("Task")
st.write("""
*Beschreiben Sie hier die zu erfüllende Aufgabe oder das Ziel des Use Cases.*
""")

## Action
st.header("Action")
st.write("""
*Beschreiben Sie hier die Schritte oder Maßnahmen, die unternommen wurden, um die Aufgabe zu erfüllen.*
""")

## Result
st.header("Result")
st.write("""
*Beschreiben Sie hier die Ergebnisse oder den Nutzen, der durch die Aktionen erzielt wurde.*
""")

# Optional: Interaktive Elemente hinzufügen
# Beispiel:
# st.slider("Wählen Sie einen Wert", min_value=0, max_value=100, value=50)

# Footer rendern
render_footer()