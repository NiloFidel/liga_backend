import pandas as pd

# data = pd.read_excel(r'/home/sl/caene/lista_caene.xlsx') 
# print(data)

lista_excel = pd.read_excel(r'/home/sl/caene/lista_caene.xlsx') 

for index, fila in lista_excel.iterrows():
    print(fila['id'])
    print("-----------------------------------------------------------------")