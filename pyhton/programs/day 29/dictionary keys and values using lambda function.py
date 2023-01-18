## Dictionary keys and values using lambda function

company = [{"department":"finance","salary":50000},{"department":"programming","salary":25000},{"department":"HR","salary":25000}]

key_list = list(map(lambda x:x["department"],company))
value_list = list(map(lambda x:x["salary"],company))
print(key_list)
print(value_list)

#or
key = list(map(lambda x:x.keys(),company))
print(key)
value = list(map(lambda x:x.values(),company))
print(value)

## for getting from a specific department (filtration)
finance_det = list(filter(lambda x:x["department"]=="finance",company))
print(finance_det)

## print salary of person working in finance
s = list(filter(lambda x:x["department"]=="finance",company))
print(s)

sa = list(map(lambda x:x["salary"] if x["department"]=="finance" else "nil",company))
print(sa)

