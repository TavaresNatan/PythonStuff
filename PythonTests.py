def search_user(user_list, user_name):
  for user in user_list:
    if user == user_name:
      print(f'user {user_name} found')

users = ['Natan','Alan','Marcos','Thalita']

search_user(users, 'Natan')

def km_medio(ano_fab, ano_atual, km_rodados):
  return km_rodados / (ano_atual - ano_fab)


media = km_medio(2003, 2022, 15345.2)
media

import numpy as np

person_1 = np.array(['9701-2230', '12757696912', 'Natan'])
person_2 = np.array(['9868-2035', '11515616548', 'James'])
person_3 = np.array(['1234-5678', '12345678912', 'User'])

people = [person_1, person_2, person_3]
people

print(f'{people[1][2]} = {people[0]}')

import pandas as pd


dataset = pd.read_csv('db.csv', sep=';')
dataset

dataset[['Quilometragem', 'Valor']]

pessoas = ['Amanda', 'Natan', 'Eduarda', 'Thalita']

_, eu, *_ = pessoas

eu

