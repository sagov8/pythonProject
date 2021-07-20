import numpy as np
from datetime import datetime

#Diferencia de tiempo de procesamiento de 1 millón de elementos
#Con listas normales en python
py_list = [i for i in range(1000000)]
start = datetime.now()
py_list = [i+3 for i in py_list]
end = datetime.now()
print(end - start)

#Con numpy
np_arr = np.array([i for i in range(1000000)])
start = datetime.now()
np_arr += 3
end = datetime.now()
print(end - start)

