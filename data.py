import csv
import plotly.figure_factory as ff
import pandas as pd
import random
import statistics
import plotly.graph_objects as go

df=pd.read_csv("data.csv")
data=df['temp'].tolist()
population_mean=statistics.mean(data)
fig=ff.create_distplot([data],["temp"],show_hist=False)
#fig.show()

std_deviation=statistics.stdev(data)
print("Population mean: "+str(population_mean))
print("Standard Deviation: "+str(std_deviation))

dataset=[]
for i in range(0,1000):
    random_index=random.randint(0,len(data))
    value=data[random_index]
    dataset.append(value)
mean=statistics.mean(dataset)
std_deviation=statistics.stdev(dataset)
print("The mean in: "+str(mean))
print("The Standard deviation is: "+str(std_deviation))

#funtion to t=get the mean of the given data sample
def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean

#function to plot the mean on the graph
def show_fig(mean_list):
    df=mean_list
    mean=statistics.mean(mean_list)
    print("Mwan of sampling distribution: ",mean)
    fig=ff.create_distplot([df],["temp"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="mean"))
fig.show()

#function to get the mean of 100 data points 1000 times and plot the graph
def setup():
    mean_list=[]
    for i in range(0,1000):
        set_of_mean=random_set_of_mean(100)
        mean_list.append(set_of_mean)
    show_fig(mean_list)
setup()