"""
Manipolazione di array Numpy
"""
import numpy as np

# alcuni simboli di borsa
sym = ["MMM", "ABT", "ABBV", "ACN", "ACE", "ATVI", "ADBE", "ADT"]

sap = np.array(sym)

print('sap')
print(sap)
print('dim: {}, shape: {}, dtype: {}'.format(sap.ndim, sap.shape, sap.dtype))

# RESHAPE cambia la dimensione del numpy array
# ritorna un array bidimensionale
sap2d = sap.reshape(2, 4)

print('sap after reshape 2d')
print(sap2d)
print('dim: {}, shape: {}, dtype: {}'.format(sap2d.ndim, sap2d.shape, sap2d.dtype))

sap3d = sap.reshape(2, 2, 2)
print('sap after reshape 3d')
print(sap3d)
print('dim: {}, shape: {}, dtype: {}'.format(sap3d.ndim, sap3d.shape, sap3d.dtype))

# FLATTEN: dato un array multidimensionale, ne costruisce la versione monodimensionale
sap1d = sap2d.flatten()
print('sap2d after flatten')
print(sap1d)

# Trasporre unarray bidimensionale
print('sap2d trasposto')
print(sap2d.T)
# La funzione transpose() viene usata per trasporre un array multidimensionale
# Permuta alcuni o tutti gli assi di un array multidimensionale
# sulla base della tupla fornita come parametro
# Nel seguente esempio, il primo asse rimane "verticale", mentre gli altri 2 assi
# vengono scambiati
print('transpose fun.')
print(sap3d.transpose(0, 2, 1))
# La funzione swapaxes() esegue la trasposizione di un array multidimensionale scambiando
# i due assi passati come parametri (passando 0 e 1 equivale ad eseguire nomearray.T)
print('swapaxes fun.')
print(sap3d.swapaxes(1, 2))
