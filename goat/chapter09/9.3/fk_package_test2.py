# coding: utf-8

# 导入fk_package包，实际上就是导入包下__init__.py文件
import fk_package

# 直接使用fk_package前缀即可调用它所包含的模块内的程序单元。
fk_package.print_blank_triangle(5)
im = fk_package.Item(4.5)
print(im)
fk_package.print_multiple_chart(5)
