"2.เขียนโปรแกรมหา index ของตัวเลขที่มีค่ามากที่สุดใน Array ด้วยภาษา python เช่น [1,2,1,3,5,6,4] ลำดับที่มีค่ามากที่สุด คือ index = 5 โดยไม่ให้ใช้ฟังก์ชั่นที่มีอยู่แล้ว ให้ใช้แค่ลูปกับการเช็คเงื่อนไข"
from operator import index


def maxloop(number):
    x =number[0] #คือตำแหน่งที่3
    for n in number:
        if n > x:
            x = n
    return index(x)

if __name__=="__main__":
    number = [3,6,14,2]
    print(maxloop(number))