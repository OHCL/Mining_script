import numpy as np

data = np.loadtxt("bm.csv", skiprows=1, usecols=(0, 1, 2, 12), delimiter=",", dtype=np.float64)

coordenadas = data[:, 0:3]
cobre = data[:, 3]
cutoff = 0.1

nData = len(cobre)
promedio = np.mean(cobre)
varianza = np.var(cobre)
minimo = np.min(cobre)
maximo = np.max(cobre)

fid = open("newBlockModel.csv", "w")
fid.write("midx,midy,midz,cu\n")

for x in range(len(cobre)):
    if cobre[x] > cutoff:
        fid.write(str(coordenadas[x, 0]) + "," + str(coordenadas[x, 1]) + "," +
                  str(coordenadas[x, 2]) + "," + str(cobre[x]) + "\n")

fid.close()
#commit