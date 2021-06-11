import csv
import pandas as pd
import plotly.figure_factory as px
import statistics as st
import random



rolls = pd.read_csv('yes.csv')
rolls = rolls['scores'].tolist()



rolls.sort()



meanp = st.mean(rolls)
standardp = st.stdev(rolls)

print(standardp, meanp)

graph = px.create_distplot([rolls], ['scores'])

graph.show()
