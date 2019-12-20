import pandas as pd
%matplotlib inline
import matplotlib.pyplot as plt

dados = pd.read_excel('C:/Users/flora/Downloads/testee.xlsx')

x = dados['Preço de ajuste Atual']
y = dados['Preço de ajuste anterior']

plt.plot(x, y)

plt.title('Ajuste Atual X Ajuste Anterior')
plt.grid(True)

plt.xlabel('Atual')
plt.ylabel('Anterior')
plt.grid(True)

plt.tight_layout()
plt.show()