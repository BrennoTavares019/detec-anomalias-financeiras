import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.metrics import classification_report

def treinar_detector(df, colunas_features, proporcao=0.01):
    # IsolationForest marca como -1 o que for anômalo
    modelo = IsolationForest(contamination=proporcao, random_state=42)
    predicoes = modelo.fit_predict(df[colunas_features])
    
    # Ajustando para 1 (anomalia) e 0 (normal)
    df['js_predito'] = [1 if x == -1 else 0 for x in predicoes]
    return df

def avaliar(y_real, y_pred):
    print(classification_report(y_real, y_pred, target_names=['Normal', 'Anomalia']))
