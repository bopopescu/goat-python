# coding: utf-8

# 两次导入module1，并指定其别名为md
import module1 as md
import module1 as md
print(md.my_book)
md.say_hi('Charlie')
user = md.User('孙悟空')
print(user)
user.walk()