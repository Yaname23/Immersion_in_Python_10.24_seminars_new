#сделайте вручную кортеж, содержащий элементы пазных типов
#получите из него словать списков, где:
# ключ-тип элемента
# значение =список элементов данного типа
""" print('--------вариант 1---------')
from collections import defaultdict

def empty():
    return []
def main():
    out = defaultdict(empty)
    _input = (1,2,3,4,5,False,False,True,1.2,1.4,1.6)
    for i in _input:
        out[type(i)].append(i)
    print(out)

if __name__ == '__main__':
    main()"""
print('--------вариант 2---------')
from pprint import pp
_typle = (1,2,3,'1','2','3',True,False,None,[1])
out = dict()

for i in _typle:
    if type(i) not in out:
        out[type(i)] = []
    out[type(i)].append(i)
pp(out)
print('--------вариант 3---------')
_typle = (1,2,3,'1','2','3',True,False,None,[1])
out = dict()
for i in _typle:
    out.setdefault(type(i),[])
    out[type(i)].append(i)
pp(out)
print('--------вариант 4---------')
_typle = (1,2,3,'1','2','3',True,False,None,[1])
result = {}
for item in _typle:
     if type(item) in result:
         result[type(item)].append(item)
     else:
         result[type(item)] = [item]

pp(result)