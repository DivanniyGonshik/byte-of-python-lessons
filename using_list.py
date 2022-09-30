#Это мой список покупок

shopList =['яблоки', 'манго', 'морковь', 'бананы']

print('я долден сделать ',len(shopList), "покупок.")

print('Покупки:', end=" ")
for item in shopList:
    print(item, end=' ')

print('\nТакже нужно купить риса.')
shopList.append("рис")
print('теперь мой список покупок таков:', shopList)

print('отсортирую-ка я свой список')
shopList.sort()
print("отсортированный список покупок выглядит так:", shopList)

print('первое что мне нужно купить это', shopList[0])
