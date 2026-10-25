a = {"x":1,"y":2}
b =dict(x=1, y=2)
c =dict([("x",1),("y",2)])
results = {
    "张三": {"数学": 87, "物理": 92},
    "李四": {"数学": 65},
}
print(results["张三"])
print(results["张三"]["数学"])
scores = {"张三": 87}
print(scores.get("赵六",0))
print(scores.setdefault("赵六",0))
scores = {"张三": 87, "李四": 92}
scores["王五"]=65
scores["张三"]=90
del scores["李四"]
scores = {"张三": 87, "李四": 92, "王五": 65}
to_delete = [name for name,s in scores.items() if s < 90]
for name in to_delete:
    del scores[name]
print(scores)
passed = {name:s for name,s in scores.items() if s>= 90}
d = {"x": 1, "y": 2}
print(d.popitem())
print(d)
print(dict.fromkeys(["a","b","a"]))
print(dict.fromkeys(["a","b"],0))
a = {"scores": [87, 92]}
b = a.copy()
b["scores"].append(65)
print(a)
print(b)
a = {"x": 1, "y": 2}
b = {"y": 20, "z": 30}
print({**a,**b})
print(a|b)
c = a.copy()
print(c.update(b))
print(c)
line = "张三,87,数学"
parts = line.split(",")
print(parts)
print("-".join(parts))
print("".join(parts))
print(line.split())
text = "  the quick   brown fox  "
print(text.split())
print(text.split(" "))
s = "  hello  \n"
print(repr(s.strip()))
print(repr(s.lstrip()))
print(repr(s.rstrip()))
for s in ["123","12.3","abc","abc123"," ",""]:
    print(f"{s!r:10} isdigit={s.isdigit()!s:<6} isalpha={s.isalpha()!s:<6})