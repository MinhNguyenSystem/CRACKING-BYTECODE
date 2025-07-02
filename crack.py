# Tool CRACKING bypass bytecode (PREMIUM)
# COPYRIGHT: MinhNguyen2412
from types import CodeType
from typing import Union, Callable
import requests, marshal, base64, dis, pprint, inspect
def clear_():__import__('os').system("cls" if __import__('os').name == "nt" else "clear")
clear_()
def debug_byte(obj: Union[CodeType, Callable]) -> None:
    if inspect.isfunction(obj) or inspect.ismethod(obj):
        code_obj = obj.__code__
        name = obj.__qualname__
    elif isinstance(obj, CodeType):
        code_obj = obj
        name = code_obj.co_name
    else:
        raise TypeError(f"Unsupported object type: {type(obj)}")
    print(f"\nDisassembly of {name!r} (at {hex(id(code_obj))}):")
    dis.dis(code_obj)
    for const in code_obj.co_consts:
        if isinstance(const, CodeType):
            debug_byte(const)
__doc__ = """
[X]~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~[X]
[X] 1: disassembly - (phân tách lấy data bytecode)[X]
[X]    2: change bytecode - (sửa đổi bytecode)    [X]
[X]      3: remove bytecode - (xóa bytecode)      [X]
[X]~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~[X]
"""
# =========== Ví dụ test ============== #
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
# ===================================== #

def VERSION(v):
    if v == '3.13': return 'https://minhnguyenpy313.pythonanywhere.com'
    elif v == '3.12': return 'https://nguyenminhpython312.pythonanywhere.com'
    elif v == '3.11': return 'https://minhnguyenpyt311.pythonanywhere.com'
    elif v == '3.10': return 'https://minhnguyenpy310.pythonanywhere.com'
    elif v == '3.9': return 'https://minhnguyenpython39.pythonanywhere.com'

# Cách 1
# convert file.pyc sang marshal bằng cách..
# ===================================== #
# Thay thế file của bạn muốn truyền vào
# -------------------------------------
# with open('file.pyc', 'rb') as f:
#     f.seek(16)
#     code = f.read()
# byte = code
# -------------------------------------
# print(marshal.dumps(byte)) # debug chuỗi byte (marshal) -> b'..'
# ===================================== #


# Cách 2
# ===================================== #
# byte = b'...' # dán chuỗi byte marshal trực tiếp
# ===================================== #

# debug byte and lưu byte
# ===================================== #
# debug_byte(byte) # debug phân tách để xem byte
# with open('file.txt', 'w', encoding='utf-8') as f: dis.dis(byte, file = f)
# ===================================== #

# ===================================== #
enc = base64.b64encode(marshal.dumps(byte)).decode('ascii')
# ===================================== #

# ===================================== #
url = VERSION('3.12') # thay thế phiên bản của định dạng phiên bản marshal
# ===================================== #


# (phân tách lấy data bytecode)
# ===================================== #
payload = {'bytes': enc }
resp = requests.post(
    f'{url}/disassembly',
    json=payload
)
# debug hoặc lưu
# --------------
pprint.pprint(resp.json())
# open('file.json', 'w', encoding='utf-8').write(f"{resp.json()})
# exit()

# # -------- kết quả vd ---------
# {'2': [{'6': 'Hello, world!'}],
#  '3': [{'18': '<code object main at 0x784203e576a0, file "<string>", line 3>'}],
#  '4': [{'4': 'MinhNguyen2412'}],
#  '5': [{'12': 'Key True'}],
#  '6': [{'14': 'Key False'}],
#  '7': [{'28': 'Nhập key: '}],
#  '9': [{'56': 2412}]}
# # -----------------------------

# (sửa đổi bytecode)
# -----------------------------
# data = {'2': [{'6': 'Hello, world - crack!'}],
#  '3': [{'18': '<code object main at 0x784203e576a0, file "<string>", line 3>'}], # (<code object...) tham số này cho biết phần này chứa byte định danh của 1 hàm
#  '4': [{'4': 'MinhNguyen2412 - crack'}],
#  '5': [{'12': 'Key True - crack'}],
#  '6': [{'14': 'Key False - crack'}],
#  '7': [{'28': 'Nhập key - crack: '}],
#  '9': [{'56': bool(2412)}]}
# -----------------------------

# ví dụ dựng hàm để change byte hàm (<code object...)
# -----------------------------
# def main(key):
#     if key == True:
#         return 'Key đã bị crack'
#     return 'Key đã bị crack'
# raw_main = marshal.dumps(main.__code__)
# b64_main = base64.b64encode(raw_main).decode('ascii')
# data = {
#     '3': [{'18': b64_main}],
# }
# -----------------------------

# payload = {'bytes': enc , 'data':data}
# resp = requests.post(
#     f'{url}/crack_byte',
#     json=payload
# )
# byte_new = marshal.loads(base64.b64decode(resp.json()['bytes'])) # or ['error]
# ===================================== #
# exit()

# (xóa bytecode)
# ===================================== #
# ví dụ 1 byte đã phân tách:
# -----------------------------
# 3           0 RESUME                   0

# 4           2 LOAD_FAST                0 (key)
#             4 LOAD_CONST               1 ('MinhNguyen2412')
#             6 COMPARE_OP              40 (==)
#            10 POP_JUMP_IF_FALSE        1 (to 14)

# 5          12 RETURN_CONST             2 ('Key True')

# 6     >>   14 RETURN_CONST             3 ('Key False')
# -----------------------------

# data = [
#     # ------ VD --------
#     # ----- cách 1 -----
#     [4, 4], # 2 là bắt đầu từ dòng thứ 2 và kết thúc là dòng 2
#     # ----- cách 2 -----
#     [4, 4, 2, 10], # 2 là bắt đầu từ dòng thứ 2 và kết thúc là dòng 2 | nhảy từ offset 2 đến 18
#     # ------------------
# ]
# payload = {'bytes': enc , 'data':data}
# resp = requests.post(
#     f'{url}/remove_byte',
#     json=payload
# )
# byte_new = marshal.loads(base64.b64decode(resp.json()['bytes'])) # or ['error]
# ===================================== #
# exit()

# ===================================== #
# chuyển marshal sang pyc
# def CONVERT_PYC(code):
#     def uint32(val):return __import__('struct').pack("<I", val)
#     if __import__('sys').version_info >= (3,4):from importlib.util import MAGIC_NUMBER
#     data = bytearray(MAGIC_NUMBER)
#     if __import__('sys').version_info >= (3,7):data.extend(uint32(0))
#     data.extend(uint32(int(0)))
#     if __import__('sys').version_info >= (3,2):data.extend(uint32(0))
#     data.extend(__import__('marshal').dumps(code))
#     return data
# open('output.pyc', 'wb').write(CONVERT_PYC(byte_new))
# ===================================== #

# ===================================== #
# lưu chuỗi byte marshal mới vào file
# open('output.py', 'w').write(f"exec(__import__('marshal').loads({base64.b64decode(resp.json()['bytes'])}))")
# debug_byte(byte_new) # debug phân tách byte mới để xem sự khác biệt
# exec(byte_new) # thực thi byte mới xem lỗi không
# ===================================== #
