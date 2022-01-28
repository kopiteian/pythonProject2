import math, random

print('Rounded Up 9.5:', math.ceil(9.5))
print('Rounded Down 9.5:', math.floor(9.5))
num = 4
print(num, 'Squared:', math.pow(num, 2))
print(num, 'Square Root:', math.sqrt(num))
nums = random.sample( range(1, 59),7 )
print('Lotto Numbers Are:', nums)
nums1 = random.sample(range(1, 50), 5)
print('Euromollions Number Are:',nums1)
nums2 = random.sample(range(1, 12),2)
print('Lucky Stars Are;', nums2)