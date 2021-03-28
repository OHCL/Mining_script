import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt('blocks.data', usecols=(3, 12), skiprows=1, dtype=np.float)
vTon, vGrade = data[:, 0], data[:, 1]

t = np.arange(0.0, 2.0, 0.01)

z1, z2 = np.zeros(len(t)), np.zeros(len(t))

for i in range(len(t)):
    tonAcum, gradeAcum, countAcum = 0., 0., 0.
    for j in range(len(vTon)):
        if vGrade[j] > t[i]:
            tonAcum += vTon[j]
            gradeAcum += vGrade[j]
            countAcum += 1
    z1[i] = tonAcum
    z2[i] = float(gradeAcum) / float(countAcum)

i_plot=1
fig, ax1 = plt.subplots()

lns1 = ax1.plot(t, z1, 'b-', label='tonnage')
ax1.set_xlabel('Cutoff')
ax1.set_ylabel('Tonnage [MTon]', color='b')
ax1.tick_params('y', colors='b')

plt.minorticks_on()
ax1.grid(which='major', color='black', linestyle='-')
#ax1.grid(which='minor', color='black', linestyle='--')

ax2 = ax1.twinx()

lns2 = ax2.plot(t, z2, 'g-', label='grade')
ax2.set_ylabel('Copper Grade [%]', color='g')
ax2.tick_params('y', colors='g')

lns = lns1 + lns2
labs = [l.get_label() for l in lns]
plt.legend(lns, labs, loc='upper right')
plt.title('GT curve')

plt.savefig('figure' + str(i_plot), dpi=500)
plt.show()
