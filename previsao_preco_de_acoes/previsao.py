# importando todas as bibliotecas importante para a tarefa.

from np import numpy
from pd import pandas

from sklearn import preprocessing
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# função que vai preparar o conjunto de dados para ajustar facilmente no modelo de Regressão Linear


def prepare_data(df,forecast_col,forecast_out,test_size):
    label = df[forecast_col].shift(-forecast_out) #criando uma nova coluna chamada label com as últimas 5 linhas são nan
    X = np.array(df[[forecast_col]]) #criando a matriz de recursos
    X = preprocessing.scale(x) #processando a matriz de recursos
    X_lately = x[-forecast_out:] #criando a coluna que quero usar mais tarde no método de previsão
    X = X[:-forecast_out] # X que conterá o treinamento e teste
    label.dropna(inplace=True) #baixando valores
    y = np.array(label) #atribuindo Y
    X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=test_size, random_state=0) #validação cruzada

    response = [X_train, X_test, Y_train, Y_test, X_lately]
    return response
