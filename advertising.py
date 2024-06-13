import pandas as pd 

publi = pd.read_csv('https://www.statlearning.com/s/Advertising.csv', index_col=0)
publi.head()

x = publi[['TV','radio', 'newspaper']]
y = publi ['sales']

print(x.shape)
print(y.shape)