# vamos prever a produção e dar uma olhada nos preços das ações.

from tkinter import _test


score = learner.score(X_test, Y_test) #testando o modelo de regressão linear.
forecast = learner.predict(X_lately) #conjunto que conterá os dados previstos
response = {} #criando objeto json
response['test_score'] = score 
response['forecast_set'] = forecast

print(response)