list1 = [10, 20, 30, 40, 50]
for i in list1:
    print(i)

list2 = ["가", "나", "다", "라", "마"]
for i in list2:
    print(i)

list3 = ["python", "java", "c", ["javascript", "typescript"]]
for i in list3:
    print(i)

# 한줄로 표현할때
for i in list3:
    #print(i, end=" ")
    print(i, end="\t")
    