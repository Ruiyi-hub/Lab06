def format_row(name,score):
    return f"{name:<10}{score:>6.1f}"
print(format_row('jessica',99.5))
def parse(record):
    record=record.split(',')
    name=record[0]
    score=float(record[1])
    return name, score
print(parse("张三,87.5"))
print(parse("欧阳修远,92"))
print(format_row(*parse("张三,87.5")))
print(format_row(*parse("欧阳修远,92")))
print(format_row(*parse("李四,65.25")))