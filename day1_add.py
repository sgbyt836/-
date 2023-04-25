def add(a, b):
  if (a<-99)|(b<-99):
    return "参数小于99"
  elif (a>99)|(b>99):
    return "参数大于99"
  else:
    return a+b

result1 = add(23, 99)
print(result1)
result2 = add(-101, 23)
print(result2)
result3 = add(120, 23)
print(result3)
