# 나의 코드
num = int(input().strip())
alphabet = 'abcdefghijklmnopqrstuvwxyz'
if num:
    print(alphabet.upper())
else:
    print(alphabet)


# 앞으로 가야할 코드 방향
import string 

string.ascii_lowercase # 소문자 abcdefghijklmnopqrstuvwxyz
string.ascii_uppercase # 대문자 ABCDEFGHIJKLMNOPQRSTUVWXYZ
string.ascii_letters # 대소문자 모두 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
string.digits # 숫자 0123456789