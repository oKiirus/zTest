import csv
import pandas as pd
import plotly.figure_factory as px
import statistics as st
import random
import plotly.graph_objects as pl


rolls = pd.read_csv('yes1.csv')
rolls = rolls['scores'].tolist()






meanp = st.mean(rolls)
standardp = st.stdev(rolls)

print(standardp, meanp)


rolls2 = pd.read_csv('yes2.csv')
rolls2 = rolls2['scores'].tolist()






meanp2 = st.mean(rolls2)
standardp2 = st.stdev(rolls2)

print(standardp2, meanp2)

rolls3 = pd.read_csv('yes3.csv')
rolls3 = rolls3['scores'].tolist()






meanp3 = st.mean(rolls3)
standardp3 = st.stdev(rolls3)

print(standardp3, meanp3)

rolls4 = pd.read_csv('yes4.csv')
rolls4 = rolls4['scores'].tolist()






meanp4 = st.mean(rolls4)
standardp4 = st.stdev(rolls4)

print(standardp4, meanp4)




def hi(d):
    data1 = []
    for i in range(0, d):
        position = random.randint(0, len(rolls) - 1)
        value = rolls[position]
        data1.append(value)
    mean = st.mean(data1)
    dev = st.stdev(data1)
    
    return mean



def hello():
    data = []
    for e in range(0, 1000):
        setofmeans = hi(100)
        data.append(setofmeans)
    dev = st.stdev(data)
    mean = st.mean(data)

    graph = px.create_distplot([data], ['scores'])
    graph.add_trace(pl.Scatter(x = [mean, mean], y = [0, 0.22], mode = 'lines', name = 'mean', line = pl.scatter.Line(color = "red" )))
    graph.add_trace(pl.Scatter(x = [mean - dev, mean - dev], y = [0, 0.22], mode = 'lines', name = 'deveation 1 start', line = pl.scatter.Line(color = "white" )))
    graph.add_trace(pl.Scatter(x = [mean + dev, mean +dev], y = [0, 0.22], mode = 'lines', name = 'deveation 1 end', line = pl.scatter.Line(color = "white" )))
    graph.add_trace(pl.Scatter(x = [mean - (dev * 2), mean - (dev * 2)], y = [0, 0.22], mode = 'lines', name = 'deveation 2 start', line = pl.scatter.Line(color = "gray" )))
    graph.add_trace(pl.Scatter(x = [mean + (dev * 2), mean + (dev * 2)], y = [0, 0.22], mode = 'lines', name = 'deveation 2 end', line = pl.scatter.Line(color = "gray" )))
    graph.add_trace(pl.Scatter(x = [mean - (dev * 3), mean - (dev * 3)], y = [0, 0.22], mode = 'lines', name = 'deveation 3 start', line = pl.scatter.Line(color = "black" )))
    graph.add_trace(pl.Scatter(x = [mean + (dev * 3), mean + (dev * 3)], y = [0, 0.22], mode = 'lines', name = 'deveation 3 end', line = pl.scatter.Line(color = "black" )))
    
    graph.add_trace(pl.Scatter(x = [meanp2, meanp2], y = [0, 0.22], mode = 'lines', name = 'experiment 1', line = pl.scatter.Line(color = "green" )))
    graph.add_trace(pl.Scatter(x = [meanp3, meanp3], y = [0, 0.22], mode = 'lines', name = 'experiment 2', line = pl.scatter.Line(color = "blue" )))
    graph.add_trace(pl.Scatter(x = [meanp4, meanp4], y = [0, 0.22], mode = 'lines', name = 'experiment 3', line = pl.scatter.Line(color = "purple" )))

    graph.show()

    print(dev, mean)
    z1 = (meanp2 - mean) / dev
    z2 = (meanp3 - mean) / dev
    z3 = (meanp4 - mean) / dev

    print(z1, z2, z3)




hello()







