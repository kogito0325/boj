s = input()
nums = list(map(int, s.replace('-', '+').split('+')))
seps = []
for c in s:
    if c in ('+', '-'):
        seps.append(c)

whole = 0
if '-' not in seps:
    print(sum(nums))
    exit()
std = seps.index('-')
whole += sum(nums[:std+1])
whole -= sum(nums[std+1:])
print(whole)