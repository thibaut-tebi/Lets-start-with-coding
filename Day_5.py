import matplotlib.pyplot as plt
x = [ 10,20,30,40,50,60,70,80,90,100]
y = [ 10,78,30,45,20,60,30,20,90,10]

plt.plot(x,y, color= "red", linewidth= 2)
plt.xlabel(" pressure")
plt.ylabel(" height ")
plt.title(" this is a simple graph")
plt.grid( )
plt.show()
