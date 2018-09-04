"题目"
"对于一个字符串，请设计一个算法，只在字符串的单词间做逆序调整，也就是说，字符串由一些由空格分隔的部分组成，你需要将这些部分逆序。"
"给定一个原字符串A和他的长度，请返回逆序后的字符串。"

"测试样例"
"dog loves pig" "返回pig loves dog"

def reverse(s):
    a=s.split(" ")
    return ' '.join(a[::-1])

s="dog loves pig"
result=reverse(s)
print(result)