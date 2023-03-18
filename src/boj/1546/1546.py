N = int(input())
total = 0

nums = list(map(int, input().split()))
max_val = max(nums)
new_list = []

for n in nums:
    new_list.append(n / max_val * 100)

new_total = sum(new_list)
new_avg = new_total / N

if new_avg == round(new_avg, 2):
    print(new_avg)
else:
    formatted_new_avg = "{:.9f}".format(new_avg)
    print(formatted_new_avg)
