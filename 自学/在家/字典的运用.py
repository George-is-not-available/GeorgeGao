"""
（1）访问字典中的值

alien_0 = {'color':'green'}
print(alien_0['color'])

输出结果：green
（2） 在一个字典中添加键值对

alien_0 = {'color':'green'}
print(alien_0['color'])

# 添加两个键值对.
alien_0['x_position'] = 0
alien_0['yposition'] = 25
print(alien_0)

输出结果：{'color': 'green', 'x_position': 0, 'y_position': 25}
（3）使用“del" 函数删除键值对

alien_0 = {'color':'green','points':5}
print(alien_0)

# 删除第二个键值对
del alien_0['points']
print(alien_0)

输出结果：{'color': 'green', 'points': 5}
         {'color': 'green'}

备注：被删除的键值对就永远消失了.
(4) 使用“ items( ) "函数遍历字典中所有键值对

user_0 = {'username':'efermi',
          'first':'enrico',
          'last':'fermi',
          }
# 遍历键值对.
for key,value in user_0.items():
    print("\nkey: " + key)
    print("\nvalue: " + value)

输出结果：key: username

value: efermi

key: first

value: enrico

key: last

value: fermi

备注：在遍历字典键值对时，在for函数后边一定不要忘记加上 ".items( )"
(5) 使用“keys( )”遍历字典中所有的键

favorite_languages = {'jen':'python',
                      'sarah':'c',
                      'edward':'ruby',
                      'phil':'python',
                     }
# 遍历字典中的键.
for name in favorite_languages.keys():
    print(name.title())

输出结果：
Jen
Sarah
Edward
Phil

备注：在遍历字典键时，在for函数后边一定不要忘记加上 ".keys( )"
（6）使用“ values( ) ”函数遍历字典中的值

favorite_languages = {'jen':'python',
                      'sarah':'c',
                      'edward':'ruby',
                      'phil':'python',
                     }
# 遍历字典中的值.
for languages in favorite_languages.values():
    print(languages.title())

输出结果：
Python
C
Ruby
Python

# 使用“ set( ) ”函数防止出现几个相同的元素，确保每个打印出来的元素都是独一无二的.
for languages in set(favorite_languages.values()):
    print(languages.title())

备注：在遍历字典值时，在for函数后边一定不要忘记加上 ".values( )"
十、嵌套。
（1）在列表中添加（存储）字典

# 先创建几个字典.
alien_0 ={'color':'green','points':5}
alien_1 ={'color':'yellow','points':10}
alien_2 ={'color':'red','points':15}

# 将上面三个字典存放在列表“aliens”中.
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:# 遍历这个列表.
    print(alien)

输出结果：
{'color': 'green', 'points': 5}
{'color': 'yellow', 'points': 10}
{'color': 'red', 'points': 15}

（2）在字典中添加（存储）列表

favorite_languages = {'jen':['python','ruby'],
                      'sarah':['c'],
                      'edward':['ruby','go'],
                      'phil':['python','java']
                     }
# 遍历字典中的键.
for name, languages in favorite_languages.items():
    print("\n" + name.title() + "s'favorite languages are:")
    for language in languages:
        print("\t" + language.title())


输出结果：
Jens'favorite languages are:
	Python
	Ruby

Sarahs'favorite languages are:
	C

Edwards'favorite languages are:
	Ruby
	Go

Phils'favorite languages are:
	Python
	Java
（3）在字典中添加（存储）字典

users = {'aeinstein':{
         'first':'albert',
         'last':'einstein',
         'location':'princeton',
          }
             }

# 遍历字典键值对.
for key, value in users.items():
    print(key + ":" + "\n" + str(value))


输出结果：
aeinstein:
{'first': 'albert', 'last': 'einstein', 'location': 'princeton'}
十一、while循坏使用。
（1）input() : 向用户显示提示和说明。

（2）int() : 将输入的数值转换为字符串的形式，确保输入的数值能正确的打印出来。

(3)import : 导入一个文件或代码块。

（4） break ：该语句用于控制程序流程或退出循坏（一般多于“if-elif-else”语句集合使用）。

while True:
    city = input("你好呀!：\n")
    if city == 'quit':
        break
else:
    print("我很好！")
（5）continue : 返回循坏开头，根据测试条件和结果判断是否继续循坏。

# 在while中使用“continue”函数.
current_number = 0
while current_number < 10: # 循坏条件.
    current_number += 1 # 每循坏一次，就在循坏结果后面加1
    if current_number % 2 == 0:
        continue
    print(current_number)

（6）使用while循坏

# 使用while循坏从1数到5.
current_number = 1
while current_number <= 5: # 循坏条件.
    print(current_number)
    current_number += 1

输出结果：1 2 3 4 5
"""