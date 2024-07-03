broken,brand = map(int,input().split())
p_arr = []
o_arr = []

for _ in range(brand):
    package,one = map(int,input().split())
    p_arr.append(package)
    o_arr.append(one)

p_min = min(p_arr)
o_min = min(o_arr)

result = []
if broken>= 6:
    result.append(broken * o_min)
    i = broken // 6
    j = broken % 6
    result.append(p_min*i + o_min*j)
    result.append(p_min*(i+1))
else:
    result.append(broken*o_min)
    result.append(p_min)

print(min(result))

