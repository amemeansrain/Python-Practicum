n, m = (int(input()) for i in range(2))
n_set, m_set = (set() for i in range(2))
for i in range(n):
    n_set.add(s := input())
for i in range(m):
    m_set.add(s := input())
nm = n_set & m_set
print(len(nm)) if len(nm) > 0 else print("Таких нет")