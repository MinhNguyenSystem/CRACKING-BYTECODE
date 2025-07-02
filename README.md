# ~~CRACKING BYTECODE - (bẻ khóa mã byte)~~
---
> ## [X] Cách sử dụng [X]
---

> #Ví dụ code đã compile
```python
code = """
print("Hello, world!")
def main(key):
    if key == 'MinhNguyen2412':
        return 'Key True'
    else:return 'Key False'
key = input('Nhập key: ')
main(key)
xxxx = 2412
print(xxxx)
""". encode()
byte = compile(code, '<string>', 'exec')
```

### I. disassembly - (phân tách lấy data bytecode)


```python
payload = {'bytes': enc }
resp = requests.post(
    f'{url}/disassembly',
    json=payload
)
pprint.pprint(resp.json())
```
- Kết quả sẽ cho ra là:
```
{'2': [{'6': 'Hello, world!'}],
 '3': [{'18': '<code object main at 0x784203e576a0, file "<string>", line 3>'}],
 '4': [{'4': 'MinhNguyen2412'}],
 '5': [{'12': 'Key True'}],
 '6': [{'14': 'Key False'}],
 '7': [{'28': 'Nhập key: '}],
 '9': [{'56': 2412}]}
 ```
### II. change bytecode - (sửa đổi bytecode)


```python
data = {'2': [{'6': 'Hello, world - crack!'}],
#  '3': [{'18': '<code object main at 0x784203e576a0, file "<string>", line 3>'}], # (<code object...) tham số này cho biết phần này chứa byte định danh của 1 hàm
 '4': [{'4': 'MinhNguyen2412 - crack'}],
 '5': [{'12': 'Key True - crack'}],
 '6': [{'14': 'Key False - crack'}],
 '7': [{'28': 'Nhập key - crack: '}],
 '9': [{'56': bool(2412)}]}
payload = {'bytes': enc , 'data':data}
resp = requests.post(
    f'{url}/crack_byte',
    json=payload
)
byte_new = marshal.loads(base64.b64decode(resp.json()['bytes'])) # or ['error]
exec(byte_new)
```
- Kết quả demo output:
```
print("Hello, world - crack!")
def main(key):
    if key == 'MinhNguyen2412 - crack':
        return 'Key True - crack'
    else:return 'Key False - crack'
key = input('Nhập key - crack: ')
main(key)
xxxx = True
print(xxxx)
 ```
- ví dụ dựng hàm để change byte hàm (<code object...)
```python
def main(key):
    if key == True:
        return 'Key đã bị crack'
    return 'Key đã bị crack'
raw_main = marshal.dumps(main.__code__)
b64_main = base64.b64encode(raw_main).decode('ascii')
data = {
    '3': [{'18': b64_main}],
}
 ```
 - Kết quả demo output:
```
def main(key):
    if key == True:
        return 'Key đã bị crack'
    return 'Key đã bị crack'
 ```
### III. remove bytecode - (xóa bytecode)
 - ví dụ byte đã phân tách của if check key:
```
3           0 RESUME                   0

4           2 LOAD_FAST                0 (key)
            4 LOAD_CONST               1 ('MinhNguyen2412')
            6 COMPARE_OP              40 (==)
           10 POP_JUMP_IF_FALSE        1 (to 14)

5          12 RETURN_CONST             2 ('Key True')

6     >>   14 RETURN_CONST             3 ('Key False')
```
 - xóa nó bằng cách:
 ```python
data = [
    # ------ VD --------
    # ----- cách 1 -----
    [4, 4], # 2 là bắt đầu từ dòng thứ 2 và kết thúc là dòng 2
    # ----- cách 2 -----
    [4, 4, 2, 10], # 2 là bắt đầu từ dòng thứ 2 và kết thúc là dòng 2 | nhảy từ offset 2 đến 18
    # ------------------
]
payload = {'bytes': enc , 'data':data}
resp = requests.post(
    f'{url}/remove_byte',
    json=payload
)
byte_new = marshal.loads(base64.b64decode(resp.json()['bytes'])) # or ['error]
exec(byte_new)
```
 - Kết quả demo output:
 ```
 def main(key):
    return 'Key True'
 ```
---
[x] API SẼ CẬP NHẬT LIÊN TỤC NÊN AE SỬ DỤNG CÓ LỖI GÌ HÃY LIÊN HỆ (TELE_ADMIN: @Minh_Nguyen_2412) !!
