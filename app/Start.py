import streamlit as st
from pathlib import Path
import sys

# Fügen Sie das Projekt-Stammverzeichnis zum sys.path hinzu
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
ROOT_DIR = current_dir.parent  # Dies geht eine Ebene höher zum Projekt-Stammverzeichnis
sys.path.append(str(ROOT_DIR))

# Importieren Sie die Seitenmodule aus app.pages
from app.components import render_footer  # Falls Sie gemeinsame Komponenten haben


# render_header()
# Titel und Einleitung
st.title("Willkommen zum Showcase Projekt für KI in Logistik und Produktion")
st.write("""
In diesem Projekt präsentieren wir vier verschiedene Anwendungsfälle aus dem Bereich KI in Logistik und Produktion. Jeder Use Case wird nach dem STAR-Schema (Situation, Task, Action, Result) vorgestellt.
Verwenden Sie die Navigation auf der linken Seite, um die verschiedenen Anwendungsfälle zu erkunden. 
""")

st.write("""Bei Fragen stehen wir Ihnen gerne zur Verfügung. """)
render_footer()
