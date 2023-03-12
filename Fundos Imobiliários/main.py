import pandas as pd

funds = pd.read_csv('fii.csv')
funds = funds[funds['Liquidez Diária'] >= 20000.0]
funds = funds[funds['P/VPA'] < 1.0]
funds = funds[funds['Patrimônio Líq.'] >= 1e9]
funds.to_csv('funds.csv')