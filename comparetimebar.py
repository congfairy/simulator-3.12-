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
N = len(x)
ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, xData, width, color='r')
rects2 = ax.bar(ind + width, yData, width, color='y')

# add some text for labels, title and axes ticks
ax.set_ylabel('time (s)')
ax.set_xlabel('processid')
ax.set_title('time difference')
ax.set_xticks(ind + width)
ax.set_xticklabels(x)

ax.legend((rects1[0], rects2[0]), ('start', 'end'))


def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % float(height),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

plt.savefig('images/difference.png',format='png')
