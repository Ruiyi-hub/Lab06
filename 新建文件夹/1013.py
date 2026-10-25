score=[87,92,45,78,55,95]
print("人数",len(score))
print("平均分",round(sum(score)/len(score),2))
print("最高",max(score))
print("最低",min(score))
passed=[s for s in score if s>=60]
print("及格率",round(len(passed)/len(score)*100,2),"%")
def my_max(nums:list[int]):
    if len(nums)==0:
        return None
    max_num=nums[0]
    for i in nums:
        if i>max_num:
            max_num=i
    return max_num
print(my_max([]))
def dedup(nums:list[int]):
    result=[]
    for s in nums:
        repeat=False
        for y in result:
            if s==y:
                repeat=True
                break
        if not repeat:
            result.append(s)
    return result
print(dedup([1,2,3,4,3,2,5]))
def transpose(matrix:list[list[int]]):
    if matrix==[]:
        return []
    result=[]
    for i in range(0,len(matrix[0])):
        for s in range(0,len(matrix)):
            result.append(matrix[s][i])
    new_list=[]
    for i in range(0,len(result),len(matrix)):
        new_list.append(result[i:i+len(matrix)])
    return new_list
print(transpose([[1, 2, 3], [4, 5, 6],[7,8,9]]))
def double(lst):
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            lst.insert(i, lst[i] * 2)
            lst.remove(lst[i+1])
    return lst
print(double([1, 2, 3, 4, 5, 6]))
a=[[1,2,3],[5,6]]
b=a
print("a=",id(a))
print("b=",id(b))
b=a[:]
print("a=",id(a))
print("b=",id(b))
print("b[0]=",id(b[0]))
print("a[0]=",id(a[0]))
RAW = [
    "2026001 zhangsan 91 57 59",
    "2026002 lisi 70 81 55",
    "2026003 wangwu 43 65 66",
    "2026004 zhaoliu - 78 90",
    "2026005 qianqi 90 90 61",
    "2026006 sunba 73 91 73",
    "2026007 zhoujiu 60 53 75",
    "2026008 wushi 105 60 70",
    "2026008 wushi 60 70 80",
    "2026009 zhengyi 60 61 69",
    "2026010 chener 57 48 70",
    "2026011 chusan 59 99 46",
    "2026002 lisi 10 10 10",
    "2026012 weisi 43 59 89",
    "2026013 jiangwu 95 96 48",
    "2026014 shenliu 53 73 62",
    "2026015 hanqi 64 73 96",
    "2026016 yangba 59 71 85",
    "2026017 zhujiu 64 41",
    "2026018 qinshi 59 81 93",
    "2026011 chusan 88 88 88",
    "2026019 youyi 97 73 62",
    "   2026020   xuer   70 80 90  ",
    "2026021 hesan 82 90 80",
    "2026022 lvsi 61 55 60",
    "2026023 shiwu 58 x 88",
    "2026024 zhangliu 63 93 95",
    "2026019 youyi 40 40 40",
    "2026025 kongqi 41 100 67",
    "2026026 caoba 99 50 48",]
def parse_roster(lines:list[str]):
    result=[]
    for i in lines:
        parts=i.split()
        nums=parts[0]
        name=parts[1]
        scores=[]
        if len(parts)==5:
            for i in range(2,5):
                if parts[i].isdigit()==True:
                    scores.append(int(parts[i]))
                else:
                    scores.append(parts[i])
        else:
            for i in range(2,4):
                if parts[i].isdigit()==True:
                    scores.append(int(parts[i]))
                else:
                    scores.append(parts[i])
        record=[nums,name,scores]
        result.append(record)
    return result
def rank(records:list[list]):
    new_record=[]
    for i in records:
        nums=i[0]
        names=i[1]
        scores=i[2]
        for s in scores:
            if str(s).isdigit()==False:
                is_valid=False
                break
            else:
                is_valid=True
        if not is_valid:
            continue
        record=[-sum(scores),names,nums]
        new_record.append(record)
    new_record2=sorted(new_record)
    for y,item in enumerate(new_record2):
        item.insert(0,-item[0])
        item.remove(item[1])
        item.reverse()
        item.insert(0,y+1)
    return new_record2
def rank(records:list[list]):
    a=[]
    for rec in records:
        sid,name=rec[0],rec[1]
        scores=rec[2]
        total=0
        for x in scores:
            if type(x)==int:
                total+=x
        a.append([-total,sid,name,total])
    a.sort()
    i=1
    ranked=[]
    for x in a:
        ranked.append([i,x[1],x[2],x[3]])
        i=i+1
    return ranked
def clean(lines:list[str]):
    records=[]
    seen_id=[]
    for i in lines:
        parts=i.split()
        nums=parts[0]
        name=parts[1]
        scores=[]
        if len(parts)!=5:
            continue
        score_valid=True
        for s in range(2,5):
            if parts[s]=='-':
                scores.append(0)
            elif not parts[s].isdigit():
                score_valid=False
                break
            elif int(parts[s])>100 or int(parts[s])<0:
                score_valid=False
                break
            else:
                scores.append(int(parts[s]))
        if not score_valid:
            continue
        if nums not in seen_id:
            seen_id.append(nums)
            record=[nums,name,scores]
            records.append(record)
        else:
            continue
    return records
print(clean(RAW))
