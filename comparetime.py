import matplotlib.pyplot as plt
import numpy as np
xData = []
x = []
yData = []
y = []
zData = []
z = []
counter = 0
start = 0
end = 0
dur = 0
for line in open("comparetime.txt"):
        counter=counter+1
	newline = line.rstrip('\n')
	line_split = newline.split(':')
	if line_split[0] == 'start time difference':
		start = counter
	elif line_split[0] == 'end time difference':
                end = counter
        elif line_split[0] == 'duration difference':
                dur = counter

counter = 0
for line in open("comparetime.txt"):
        counter=counter+1
        newline = line.rstrip('\n')
        line_split = newline.split(':')
        if counter > start and counter < end:
                xData.append(float(line_split[2]))
		x_split = line_split[1].split(' ')
                x.append(int(x_split[0]))
        elif counter > end and counter < dur:
                yData.append(float(line_split[2]))
        elif counter > dur: 
                zData.append(float(line_split[2]))
plt.bar(x,xData,alpha=0.5,color='green')
plt.show()
plt.hist(xData,color='green',alpha=0.5) 
plt.xlabel('start difference (s)') 
plt.ylabel('frequency') 
plt.title('plot of start difference') 
#plt.show()
plt.savefig('images/start_difference.png',format='png')
plt.hist(yData,facecolor='red',alpha=0.5) 
plt.xlabel('end difference (s)') 
plt.ylabel('frequency') 
plt.title('plot of end difference') 
#plt.show()
plt.savefig('images/end_difference.png',format='png')
plt.hist(zData,facecolor='blue',alpha=0.5) 
plt.xlabel('executing difference (s)') 
plt.ylabel('frequency') 
plt.title('plot of executing difference') 
#plt.show()
plt.savefig('images/executing_difference.png',format='png')
