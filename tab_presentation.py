import streamlit as sl

def tab_presentation():
	sl.title("page présentation")

	tab1, tab2, tab3 = sl.tabs(["Contexte", "Méthodologie/Outils", "Code"])

	with tab1:
		sl.subheader("Objectif du projet")

	with tab2:
		sl.subheader("Les étapes")

	with tab3:
		sl.subheader("Code de l'analyse")