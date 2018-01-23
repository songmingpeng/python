#!/usr/bin/python
#coding:utf-8
import re

'''
###### re.compile(strPattern[, flag]):

pattern=re.compile(r'hello')
match=pattern.match('hello world!')

if match:
    print(match.group())

m=re.match(r'hello','hello world!')
print(m.group(),'sec')


#### Match
m = re.match(r'(\w+) (\w+)(?P<sign>.*)', 'hello world!')
 
print "m.string:", m.string
print "m.re:", m.re
print "m.pos:", m.pos
print "m.endpos:", m.endpos
print "m.lastindex:", m.lastindex
print "m.lastgroup:", m.lastgroup
 
print "m.group(1,2):", m.group(1, 2)
print "m.groups():", m.groups()
print "m.groupdict():", m.groupdict()
print "m.start(2):", m.start(2)
print "m.end(2):", m.end(2)
print "m.span(2):", m.span(2)
print r"m.expand(r'\2 \1\3'):", m.expand(r'\2 \1\3')


#### split(string[, maxsplit]) | re.split(pattern, string[, maxsplit]): 
p = re.compile(r'\d+')
print p.split('one1two2three3four4')


#### findall(string[, pos[, endpos]]) | re.findall(pattern, string[, flags]): 
p=re.compile(r'\d+')
print ( p.findall('one1two2three3four4') )



##projectname='wawa333'
##r = re.match('^[A-Za-z0-9]+$', projectname) and True or False
ss=re.match(r'^([1-9]\d*)(,\d+)*$','10,2,10') and True or False
print(ss)
'''
##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++##
# re→ (...) 被括起来的表达式将作为分组，分组作为一个整体，后接数量词
# re→ [...] 字符集，对应位置可以是是字符集中任意字符
# re→ {m,n}  匹配前一个字符m到n次，m和n可以省略
# re→   *    匹配前一个字符0次或无限次
# re→   +    匹配前一个字符1次或无限次
# re→   ？   匹配前一个字符0次或1次
# re→   ^    匹配字符串开头，多行中匹配每一行的开头；取反
# re→   $    匹配字符串末尾，多行中匹配每一行的末尾
# re→  \d    数字：[0-9]
# re→  \D    非数字：[^\d]
# re→  \s    空白字符[<空格>\t\r\n\f\v]
# re→  \S    非空白字符
# re→  \w    单词字符[]A-Za-z0-9]
# re→  \W    非单词字符
##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++##
print('start+++++++++')

##### 01 1,2,3
pa=re.compile( r'^([1-9]\d*)(,[1-9]\d*)*$' )
# ^([1-9]\d*) 表示开头数字必须是1-9中的任意一个数字，不能为0，可以是多位数
# (,[1-9]\d*)*$ 表示从第二位开始必须是以一个逗号和数字结合的模式 

ma=pa.match('1,2,3 2,,3 ') 

if ma:
    print('Ok!')
else:
    print('Not Ok!')
    
##### 02 1:2:10 1:10
pattern=re.compile( r'^([1-9]\d*)(:[1-9]\d*){1,2}$' )
match=pattern.match('1:3:10:19') 

if match:
    print('Ok!')
else:
    print('Not Ok!') 


##### 03 1-1-10 1-10
pattern=re.compile( r'^([1-9]\d*)(-[1-9]\d*){1,2}$' )
match=pattern.match('1-1-') 

if match:
    print('Ok!')
else:
    print('Not Ok!') 

print('end++++++++++')












