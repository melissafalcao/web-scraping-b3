import pandas as pd

dados = pd.read_excel('C:/Users/flora/Downloads/testee.xlsx')

variacao = dados.loc[dados['Variação'] >= 0]
variacao.head(500)

x = variacao['Preço de ajuste anterior']
y = variacao['Preço de ajuste Atual']

%matplotlib inline
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot(x, y)

ax.set(xlabel='Preço ajuste anterior', ylabel='Preço ajuste atual)',
       title='Variação de ajuste para as variações positivas (PREGÃO)')
       
ax.grid()
plt.show()
