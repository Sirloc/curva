import numpy as np
import matplotlib.pyplot as plt

cuentas_std_b1 = [1179892, 1814023, 2482286, 3190870,3962260,4826287, 5832528, 6973734, 8107617, 9019825, 9552384, 9784319, 9866010, 9899608, 9919513, 9933874,9945668, 9956382, 9965881, 9974746]

radios = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22] 

plt.plot(radios, cuentas_std_b1, '-o', color='g')
plt.xlabel('Radio de apertura [pixeles]')
plt.ylabel('Flujo [Cuentas]')
plt.title('Flujo v/s Radio de apertura')
plt.grid()
plt.savefig('./Curva-std_b1.png')
plt.show()
