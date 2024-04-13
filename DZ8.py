import pandas as pd
import random 

lst = ['robot'] * 10 
lst += ['human'] * 10 
random.shuffle(lst) 
data = pd.DataFrame({'whoAmI': lst}) 


# # # Использование pd.get_dummies() для преобразования столбца 'whoAmI' в one-hot представление
# # one_hot = pd.get_dummies(data['whoAmI'])

# # # Объединение исходного DataFrame с новыми столбцами в one-hot представлении
# # data = pd.concat([data, one_hot], axis=1)

# # # Удаление исходного столбца 'whoAmI'
# # data = data.drop('whoAmI', axis=1)

# # print(data.head())

# # Создание словаря для one-hot кодирования
# categories = data['whoAmI'].unique()
# categories.sort()  # Сортировка значений для однозначности в порядке

# # Преобразование 'whoAmI' в one-hot представление
# for cat in categories:
#     data[cat] = (data['whoAmI'] == cat).astype(int)

# # Удаление исходного столбца 'whoAmI'
# data = data.drop('whoAmI', axis=1)

# print(data.head())