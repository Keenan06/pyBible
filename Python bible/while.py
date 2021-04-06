num = 1
while num <= 10:
    if num % 2 == 0:
        print(num)
    num = num + 1

List = []
while len(List) <3:
    new_name = input("add name:").strip().capitalize()
    List.append(new_name)

print("No more space available")
print(List)