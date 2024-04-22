test_str1 = 'int integral = 0;'
 
print("The original string 1 is : " + str(test_str1))
range = [(0, 4)]
res = ""
 
for idx, chr in enumerate(test_str1):
  for strt_idx, end_idx in range:
    if strt_idx <= idx + 1 <= end_idx: 
      break
    else:
        res += chr
 
# printing result 
print("The reconstructed string : " + str(res)) 