import pandas as pd
from src.modelo import treinar_detector, avaliar

data = {
    'valor': [100, 150, 120, 8000, 110, 130, 9500],
    'freq_diaria': [1, 2, 1, 15, 2, 1, 20]
}
df = pd.DataFrame(data)
df['real'] = [0, 0, 0, 1, 0, 0, 1]  

df = treinar_detector(df, ['valor', 'freq_diaria'])
avaliar(df['real'], df['js_predito'])