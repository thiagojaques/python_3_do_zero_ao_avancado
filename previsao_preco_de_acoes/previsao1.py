# Agora a próxima coisa a fazer é ler os dados

from pandas import pd

df = pd.read_csv('preços.cvs')
df = df[df.simbolo == 'GOOG']