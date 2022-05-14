from quickSort import *
from mergeSort import *
## 딕셔너리 안에 lpn 삽입
## 딕셔너리 안에 lpn 있으면 1출력, 없으면 1추가
## 딕셔너리 정렬 -> sorted는 말고! quick sort이용해서 ............
def do_sort(input_file):
    data_file = open(input_file)
    A = []
    for line in data_file.readlines():
        lpn = line.split()[0]
