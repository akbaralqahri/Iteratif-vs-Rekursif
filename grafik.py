import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

angles = np.arange(0, 3*np.pi, 0.1) # siapkan nilai sudut
sindata = np.sin(angles) # siapkan nilai sinus sudutnya

def kualitas():
  #rekursif
  x1 = [5050, 20100, 80200, 320400]
  
  #iteratif
  x2 = [100, 200, 400, 800]
    
  #Grafik
  plt.title("Grafik perbandingan metode rekursif dan iteratif", fontsize=18,)
  plt.plot(x1, color="red", linewidth=2.0, linestyle="-", label = 'rekursif')
  plt.plot(x2, color="black", linewidth=2.0, linestyle="-", label = 'iteratif')
  # plt.plot(x3, y3, color="red", linewidth=2.0, linestyle="-", label = 'bagus')  
  plt.legend(frameon=False)  
  plt.show()
  animation.FuncAnimation(plt.gcf(), kualitas, interval=1000)

kualitas()