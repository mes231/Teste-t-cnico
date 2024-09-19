dic = { 'SP': 67836.43, 'RJ': 36678.66, 'MG': 29229.88, 'ES': 27165.48, 'Outros': 19849.53}
total_faturamento = sum(dic.values())
dicPercent = {}

for k, v in dic.items():
   percentual = (v / total_faturamento)*100
   dicPercent[k] = percentual

for k, v in dicPercent.items():
   print(f'O estado {k} teve uma representação de {v:.2f}% no faturamento total mensal da distribuidora.')