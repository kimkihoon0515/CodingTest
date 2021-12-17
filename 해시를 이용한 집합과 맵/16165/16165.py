N, M = map(int, input().split())
group = {}
for i in range(N):
    g_name = input()
    member = int(input())
    for j in range(member):
        m_name = input()
        group[g_name] = group.get(g_name, []) + [m_name]

for i in range(M):
    name, num = input(), int(input())
    if num == 0:
        for n in sorted(group[name]):
            print(n)
    else:
        for g in group:
            if name in group[g]:
                print(g)