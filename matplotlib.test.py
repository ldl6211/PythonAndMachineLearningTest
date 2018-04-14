from matplotlib.pyplot import *
x_value = [1,2,3,4,5]
y_value = [1,4,9,16,25]
plot(x_value,y_value, linewidth=5)
title('TITLE',fontsize=24)
xlabel('X-line',fontsize=14)
ylabel('Y-line',fontsize=14)
tick_params(axis='both', labelsize=14)
scatter(x_value,y_value,s=200,edgecolors='none',c=y_value,cmap=cm.Blues)
savefig('matplotlib.png',bbox_inches='tight')
show()
