import pandas as pd

d = {'one' : pd.Series([100.,200.,300.], index = ['apple', 'ball', 'clock']),
 'two' : pd.Series([111.,222.,333.,4444], index = ['apple', 'ball', 'cerill', 'dancy'])}

df = pd.DataFrame(d)
df['three'] = df['one'] * df['two']
df['flag'] = df['one']>250
df
