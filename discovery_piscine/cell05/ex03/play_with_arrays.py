num = [2, 8, 9, 48, 8, 22, -12, 2]
new_num = []
for i in range(len(num)):
    if num[i] > 5:
        new_num.append(num[i]+2)
print(f"{num}\n{set(new_num)}")
