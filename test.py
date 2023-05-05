import json
import chardet

with open('D:/01_work/480/lastic_company_address.json', 'rb') as f:
    result = chardet.detect(f.read())
    encoding = result['encoding']

with open('D:/01_work/480/lastic_company_address.json', encoding=encoding) as f:
    data_lastic = json.load(f)

with open('D:/01_work/480/pg_company_address.json', 'rb') as f:
    result = chardet.detect(f.read())
    encoding = result['encoding']

with open('D:/01_work/480/pg_company_address.json', encoding=encoding) as f:
    data_postgrel = json.load(f)

if all(data_lastic.get(key) == data_postgrel.get(key) for key in data_lastic):
    print('Ok')
else:
    print('Not ok')
    for key_cicl in data_lastic:
        if data_lastic.get(key_cicl) != data_postgrel.get(key_cicl):
            print(f'В ластике "{key_cicl}": "{data_lastic.get(key_cicl)}"\n'
                  f'В постргесс "{key_cicl}": "{data_postgrel.get(key_cicl)}"')
            print()

if sorted(data_lastic.items()) == sorted(data_postgrel.items()):
    print('Ok 2')
else:
    print('Not ok 2')