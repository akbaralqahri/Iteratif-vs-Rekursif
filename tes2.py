import matplotlib.pyplot as plt

def sumofpoweriterative(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum + i * i
    return sum

def sumofpowerrecursive(n):
    if n == 1:
        return 1
    else:
        return n * n + sumofpowerrecursive(n-1)

def grafik():
    rekursif = []
    iteratif = []
    n = 100

    for i in range(1, 5):
        rekursif.append(sumofpowerrecursive(n))
        n = n + n

    for i in range(1, 5):
        iteratif.append(sumofpoweriterative(n))
        n = n + n

    print(rekursif)
    print(iteratif)

    #Grafik
    plt.title("Grafik perbandingan metode rekursif dan iteratif", fontsize=15,)
    
    plt.plot(rekursif, color="red", linewidth=2.0, linestyle="-", label = 'rekursif')
    plt.plot(iteratif, color="black", linewidth=2.0, linestyle="-", label = 'iteratif')
    # plt.plot(x3, y3, color="red", linewidth=2.0, linestyle="-", label = 'bagus')
    plt.legend(frameon = False)
    plt.show()

def grafikrec():
    rekursif = []
    n = 100

    for _ in range(1, 5):
        rekursif.append(sumofpowerrecursive(n))
        n = n + n


    #Grafik
    plt.title("Grafik Metode Rekursif", fontsize=18,)
    
    plt.plot(rekursif, color="red", linewidth=2.0, linestyle="-", label = 'rekursif')
    # plt.plot(x3, y3, color="red", linewidth=2.0, linestyle="-", label = 'bagus')
    plt.legend(frameon = False)
    plt.show()

def grafikite():
    iteratif = []
    n = 100

    for _ in range(1, 5):
        iteratif.append(sumofpoweriterative(n))
        n = n + n

    #Grafik
    plt.title("Grafik Metode Iteratif", fontsize=18,)
    
    plt.plot(iteratif, color="black", linewidth=2.0, linestyle="-", label = 'iteratif')
    # plt.plot(x3, y3, color="red", linewidth=2.0, linestyle="-", label = 'bagus')
    plt.legend(frameon = False)
    plt.show()


grafikrec()
grafikite()
grafik()

