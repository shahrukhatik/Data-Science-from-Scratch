##matplotlib

from matplotlib import pyplot as plt

###line graph


from matplotlib import pyplot as plt
years = [1950,1960,1970,1980,1990,2000,2010]
gdp = [300.2,543.3,1075.9,2862.5,5979.6,10289.7,14958.3]
plt.plot(years, gdp, color = 'green', marker='o', linestyle='solid')
### add a title
plt.title("Nominal GDP")
## add a label
plt.ylabel("Billions of $")
plt.show()

##barcharts

movies = ["Annie Hall", "Ben-Hur","Casablanca","Gandhi","West Side Story"]
num_oscars = [5,11,3,8,10]

plt.bar(range(len(movies)), num_oscars)
plt.title("My Favorite Movies")
plt.ylabel("# of Academy Awards")
plt.xticks(range(len(movies)),movies)
plt.show()

###Bar chart - counter
from collections import Counter
grades = [83,95,91,87,70,0,85,82,100,67,73,77,0]

histogram = Counter(min(grade // 10*10,90) for grade in grades)
plt.bar([x+5 for x in histogram.keys()], ## shift bars to right by 5
        histogram.values(), ### give bars its respective correct height
        10, ##barwidth of 10
        edgecolor=(0,0,0)) ## black edges for bar
plt.axis([-5,105,0,5])
plt.xticks([10 * i for i in range[11]])
plt.xlabel("Decile")
plt.ylabel("# of Students")
plt.title("Distribution of Exam 1 Grades")
plt.show

###line charts

variance = [1,2,4,8,16,32,64,128,256]
bias_squared = [256,128,64,32,16,8,4,2,1]
total_error = [x+y for x,y in zip(variance,bias_squared)]
xs = [i for i, _ in enumerate(variance)]

plt.plot(xs,variance, 'g-', label = 'variance') ##green solid
plt.plot(xs,bias_squared,'r-.',label='bias^2') ## red dashed
plt.plot(xs,total_error,'b:',label='total errror') ##blue dotted

plt.legen(loc=9)
plt.xlabel("model complexity")
plt.xticks([])
plt.title("Bias Variance Tradeoff")
plt.show()