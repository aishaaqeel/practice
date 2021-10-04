

'''
NAME:Srushti Sulgudle
ROLL NO.:3460
C No.:C22019221459
ASSIGNMENT NO.:3
PROBLEM STATEMENT: Write a python code that loads any dataset and perform basic operations and plot the graph(bar graph,scatter graph,pie chart,etc).
'''


import matplotlib.pyplot as plt
import csv


country=[]
gold=[]
silver=[]
bronze=[]


#Importing data from CSV file

with open('summer.csv','r') as csvfile:
    plots=csv.reader(csvfile,delimiter=',')
    for row in plots:
        country.append(row[0])
        gold.append(int(row[1]))
        silver.append(int(row[2]))
        bronze.append(int(row[3]))

totalMedals=[gold[-1],silver[-1],bronze[-1]]
# country.remove(country[-1])
# gold.remove(gold[-1])
# silver.remove(silver[-1])
# bronze.remove(bronze[-1])

#1 Line graph
plt.plot(country,gold,color='r',label='Gold',linewidth=4)
plt.plot(country,silver,color='g',label='Silver',linewidth=4)
plt.plot(country,bronze,color='b',label='Bronze',linewidth=4)
plt.legend()
plt.title('Olympic Medals Summary')
plt.ylabel('Medals')
plt.xlabel('Country')
plt.show()

#2 Bar graph
xpos1=[1,2,3,4,5,6,7]
xpos2=[1.2,2.2,3.2,4.2,5.2,6.2,7.2]
xpos3=[1.4,2.4,3.4,4.4,5.4,6.4,7.4]
plt.bar(xpos1,gold,color='r',width=0.2,label="Gold")
plt.bar(xpos2,silver,color='g',width=0.2,label="Silver")
plt.bar(xpos3,bronze,color='b',width=0.2,label="Bronze")
plt.legend()
plt.show()


#3 Scatter plot
plt.scatter(country,gold,color='r',s=30,label='Gold Medals')
plt.scatter(country,silver,color='g',s=30,label='Silver Medals')
plt.scatter(country,bronze,color='b',s=30,label='Silver Medals')
plt.title('Olympic Golds earned by Countries')
plt.legend()
plt.show()


#Pie Charts
#1
plt.pie(totalMedals,labels=['Gold','Silver','Bronze'],autopct='%1.1f%%')
plt.title('Medal Summary')
plt.show()

#2
plt.pie(gold,labels=country,autopct='%1.1f%%')
plt.title('Olympic Golds by Countries')
plt.show()

#3
plt.pie(silver,labels=country,autopct='%1.1f%%')
plt.title('Olympic Golds by Countries')
plt.show()

#4
plt.pie(bronze,labels=country,autopct='%1.1f%%')
plt.title('Olympic Golds by Countries')
plt.show()