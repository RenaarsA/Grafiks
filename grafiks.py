import matplotlib.pyplot as plt
#plt.style.use('bmh')

x_ass_koord=['Nav pieredzes','1-2','3-5','5-10','10']#okeāna platība
y_ass_koord=[75,85,62,35,44]#darba pieredze jauniešiem
y_ass_koord2=[45,63,68,23,56]#darba pieredze pieaugušajiem

plt.xlabel('Gadu pieredze')
plt.ylabel('Atbildējušie cilvēki')
plt.title('Darba pieredze')

plt.plot(x_ass_koord,y_ass_koord,label='jaunieši',linewidth=3,linestyle='dotted',color='pink')
plt.plot(x_ass_koord,y_ass_koord2,label='pieaugušie',linewidth=3,linestyle='dashed',color='purple')
plt.legend(loc='upper right')
plt.show()