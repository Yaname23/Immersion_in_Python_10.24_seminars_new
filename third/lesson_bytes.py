text_en = 'Hello world!'
res = text_en.encode('utf-8')
print(res, type(res))
print('------------------------')
text_ru = 'Привет мир!'
res = text_ru.encode('utf-8')
print(res, type(res))
print('------------------------')
x = bytes(b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82 \xd0\xbc\xd0\xb8\xd1\x80!')
y = bytearray(b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82 \xd0\xbc\xd0\xb8\xd1\x80!')
print(f'{x = }\n{y = }')