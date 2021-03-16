from collections import defaultdict

a = '''0
103
131
121
151
118
12
7
2
90
74
160
58
15
83
153
140
166
1
148
33
165
39
100
135
68
77
25
9
54
94
101
55
141
22
97
35
57
117
102
64
109
114
56
51
125
82
154
142
155
45
75
158
120
5
19
61
34
128
106
88
84
137
96
136
27
6
21
89
69
162
112
127
119
161
38
42
134
20
81
48
73
87
26
95
146
113
76
32
70
8
18
67
124
80
93
29
126
147
28
152
145
159'''


def check_valid(listz):
    for i in range(1,len(listz)):
        if listz[i] - listz[i-1] > 3:
            return False
    return True

correct_answers = []
counter = 1

inputz = list(a.split('\n'))
for i in range(0,len(inputz)):
    inputz[i] = int(inputz[i])

inputz.sort()

def check_all(listz):
    global counter
    global correct_answers
    for i in range(1,len(listz)-1):
        new_list = listz.copy()
        del new_list[i]
        if new_list not in correct_answers:
            if check_valid(new_list):
                counter = counter + 1
                correct_answers.append(new_list)
                check_all(new_list)


def consecutives(listz):
    results = []
    counter = 1
    for i in range(1,len(listz)):
        if listz[i] - listz[i-1] == 1:
           counter += 1
        else:
            results.append(counter)
            counter = 1

        if i == (len(listz) - 1) and counter != 1:
            results.append(counter)
    return(results)


checker = [1,1,1,2,4,7]


answers = consecutives(inputz)
answers2 = []
total = 1

for i in answers:
    answers2.append(checker[i])

for i in answers2:
    total = total * i

print(inputz)
print(answers)
print(answers2)
print(total)

