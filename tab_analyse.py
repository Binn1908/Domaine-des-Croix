import streamlit as sl
import pandas as pd
#import pickle
import plotly.express as px
import WordCloud
import matplotlib.pyplot as plt

@sl.cache_data
def load_df():
	df1 = pd.read_pickle('df_clean1.pickle')
	df2 = pd.read_pickle('df_clean2.pickle')
	df3 = pd.read_pickle('df_clean3.pickle')
	df4 = pd.read_pickle('df_clean4.pickle')
	df = pd.concat([df1, df2, df3, df4])
	return df

df = load_df()

def tab_analyse():
	sl.title("page analyse")

	#sl.dataframe(df)

	df_country = df.groupby(by = ['country', 'code'], as_index = False)['points'].mean()
	fig = px.choropleth(df_country, locations='code', color='points', hover_name='country', title='test')
	#projection='natural earth'
	sl.plotly_chart(fig)

	wordcloud = WordCloud(width = 480, height = 480, max_font_size = 200, min_font_size = 10)
	wordcloud.generate_from_text(" ".join(df['description_clean']))
	fig, ax = plt.subplots()
	#plt.figure()
	ax.imshow(wordcloud, interpolation = "bilinear")
	plt.axis("off")
	#plt.margins(x = 0, y = 0)
	sl.pyplot(fig)
