a = '''103
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

increments = [1,0,1]

inputz = list(a.split('\n'))
for i in range(0,len(inputz)):
    inputz[i] = int(inputz[i])

inputz.sort()

for i in range(1,len(inputz)):
    difference = inputz[i] - inputz[i-1]
    increments[difference - 1] += 1

print(increments)
print(increments[0] * increments[2])