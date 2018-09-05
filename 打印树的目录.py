"题目"
"输入"
"a\b\c"
"a\d\e"
"b\cst"
"d\"

"输出"
"a"
"b"
"c"
"d"
"e"
"b"
"cst"
"d"

import sys
line_1 = input().split()
n = int(line_1[0])

work_re = []
while n:
    ss=sys.stdin.readline()
    if ss.strip():
        line = ss.strip().split()
        work_re.append([x for x in line])
        n=n-1

print(work_re)
print(len(work_re))

ans=[]
maps={}
for i in range(len(work_re)):
    strs=work_re[i][0]
    s=strs.split("\\")
    for j in range(len(s)):
        if s[j] in maps:
            if maps[s[j]]!=j:
                ans.append(s[j])
        else:
            maps[s[j]]=j
            ans.append(s[j])
        # if s[j] not in ans:
        #     ans.append(s[j])
for i in range(len(ans)):
    print(ans[i])

"只A了30%...有待思考"