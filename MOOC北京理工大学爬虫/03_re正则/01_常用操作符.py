# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/24

# 38/65

.   表示任何单个字符
[]  字符集，对单个字符给出取值范围，[a-z]，[abc]
[^] 非字符集，对单个字符给出排除范围，[^abc]，没有abc
*   前一个字符0次或无限次扩展，abc*表示ab,abc,abcc,abcccc等
+   前要给字符1次或无限次扩展，abc+表示abc，abcc，abccc等
?   前一个字符0次或1次扩展，abc?表示ab、abc
|   左右表达式任意一个，abc|def表示abc、def
{m} 扩展前一个字符m次，ab{2}c表示abbc
{m,n}   扩展前一个字符m至n次（含n），ab{1,2}c表示abc、abbc
^   匹配字符串开头
$   匹配字符串结尾
()  分组标记，内部只能使用|操作符，(abc)表示abc
\d  数字，等价于[0-9]
\w  单词字符，等价于[A-Za-z0-9_]

经典实例
^[A-Za-z]+$ 由26个字母组成的字符串
^[A-Za-z0-9]+$ 由26个字母和数字组成的字符串
^-?\d+$ 整数形式的字符串
^[0-9]*[1-9][0-9]*$ 正整数形式的字符串
[1-9]\d{5}  中国境内邮政编码，6位，但是发现有0开头的
[\u4e00-\u9fa5] 中文字符的正则表达式
国内电话号码(0511-4405222、021-87888822)：\d{3}-\d{8}|\d{4}-\d{7}
IP地址 [0-2][0-9]{2}.[0-2][0-9]{2}.[0-2][0-9]{2}.[0-2][0-9]{2}
     老师最后写了一个更精确的表示

