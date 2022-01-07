from random import randint
import plotly.express as px
import plotly.figure_factory as ff
import statistics as ss
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv('D:\Documents\school\jr\PRIVATE\Python\Project 109\StudentsPerformance.csv')
math_score = df['math score'].tolist()
#Calculating the mean and standard deviation

mean = sum(math_score)/ len(math_score)
std_deviation = ss.stdev(math_score)
median = ss.median(math_score)
mode = ss.mode(math_score)

print("Mean = ",mean)
print("Std_Deviation = ",std_deviation)
print("Median = ",median)
print("Mode = ",mode)


#Finding 1 standard deviation stard and end values, and 2 standard deviations stard and end values and 3 standard deviation start and end values
first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)


list_of_data_within_1_std_deviation = [result for result in math_score if result > first_std_deviation_start and result< first_std_deviation_end]
print(len(list_of_data_within_1_std_deviation))

list_of_data_within_2_std_deviation = [result for result in math_score if result > second_std_deviation_start and result< second_std_deviation_end]
print(len(list_of_data_within_2_std_deviation))

list_of_data_within_3_std_deviation = [result for result in math_score if result > third_std_deviation_start and result< third_std_deviation_end]
print(len(list_of_data_within_3_std_deviation))


print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_std_deviation)*100.0/len(math_score)))
print("{}% of data lies within 2 standard deviations".format(len(list_of_data_within_2_std_deviation)*100.0/len(math_score)))
print("{}% of data lies within 3 standard deviations".format(len(list_of_data_within_3_std_deviation)*100.0/len(math_score)))

fig = ff.create_distplot([math_score],["Math Score"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.show()