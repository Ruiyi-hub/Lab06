def invert(d:dict[str,int]):
    new_d={}
    for alpha,num in d.items():
        new_d[num]=alpha
    return new_d
def unique_ordered(items:list[int]):
    seen=set()
    result=[]
    for i in items:
        if i not in seen:
            seen.add(i)
            result.append(i)
    return result
def common(a: list[str],b:list[str]):
    seen=set()
    seen2=set()
    result=[]
    for i in a:
        if i not in seen:
            seen.add (i)
    for x in b:
        if x in seen and x not in seen2 :
            seen2.add(x)
            result.append(x)
    result = sorted(result)
    return result
def group_by_first(word:list[str]):
    cha = set()
    group = {}
    for i in word:
        if i[0] not in cha:
            cha.add(i[0])
            group[i[0]] = [i]
        elif i[0] in cha:
            group[i[0]].append(i)
    return group
def parse(line:list[str]):
    result = {}
    names = set()
    for i in line:
        name, subject, raw_mark = i.split(",")
        name = name.strip()
        subject = subject.strip()
        mark = int(raw_mark.strip())
        if name not in names:
            names.add(name)
            result[name] = {subject:mark}
        else:
            result[name][subject] = mark
    return result
def count_of(pair:tuple[str, int]):
    return (-pair[1], pair[0])
def top_words(text:str, n: int):
    counts: dict[str, int] = {}
    for i in text.split():
        i = i.strip(".,!?;:")
        i = i.lower()
        if i == "":
            continue
        counts[i] = counts.get(i,0)+1
    rank = sorted(counts.items(),key=count_of)
    if n <= 0:
        return []
    else:
        return rank[:n]
def contains_counted(items: list[int], target: int) -> tuple[bool, int]:
    checks = 0
    for x in items:
        checks += 1
        if x == target:
            return True, checks
    return False, checks
import time
for n in[1000,2000,4000]:
    items = list(range(n))
    for i in [0, n//2, n-1, n]:
        result, checks=contains_counted(items,i)
start = time.perf_counter()
for n in [1000,2000]:
    items = list(range(n))
    members = set(items)
    for t in[0, n//2, n-1, n]:
        res = t in members
build_seconds = time.perf_counter() - start
print("构造集合耗时：", build_seconds)
#test git test12345