from statistics import LinearRegression
from previsao_preco_de_acoes.previsao import prepare_data
from previsao_preco_de_acoes.previsao1 import df
from previsao_preco_de_acoes.previsao import forecast_col
from previsao_preco_de_acoes.previsao import forecast_out
from previsao_preco_de_acoes.previsao import test_size

# Agora vou dividir os dados e encaixar no modelo de regressão linear.

X_train, X_test, Y_train, Y_test, X_lately = prepare_data(df, forecast_col, forecast_out, test_size); #chamando o método onde á validação cruzada e a preparação.
aprendiz = LinearRegression() #inicializando o modelo de regreção linear.

aprendiz.fit(X_train, Y_train) #treinando o modelo de regreção linear.