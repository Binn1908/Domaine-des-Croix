import streamlit as sl
from PIL import Image
from tab_home import tab_home
from tab_presentation import tab_presentation
from tab_analyse import tab_analyse

with sl.sidebar:

	affiche = Image.open('logo.png')
	sl.sidebar.image(affiche)

	tabs = {'Home': tab_home,
		'Présentation': tab_presentation,
		'Analyse/Dataviz': tab_analyse
		}

	tab_selection = sl.radio('Menu', list(tabs.keys()))

tabs[tab_selection]()

sl.divider()

sl.caption('**Etude de marché vin** - by [Chinnawat Wisetwongsa](https://linkedin.com/in/wisetwongsa/)')
