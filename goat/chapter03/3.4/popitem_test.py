# coding: utf-8

cars = {'AUDI': 7.9, 'BENS': 8.3, 'BMW': 8.5}
print(cars)
# 弹出字典底层存储的最后一个key-value对
print(cars.popitem()) # ('AUDI', 7.9)
print(cars) # {'BMW': 8.5, 'BENS': 8.3}
# 将弹出项的key赋值给k、value赋值给v
k, v = cars.popitem()
print(k, v) # BENS 8.3
