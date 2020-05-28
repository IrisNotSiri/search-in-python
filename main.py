def linear_search(num_list,target):
  for x in range(len(num_list)):
    if target == num_list[x]:
      return x
  return -1



num_list = [11,23,5,63,43,21,1,3,5]
target = 5
result = linear_search(num_list,target)
if result == -1:
  print ('Number is not in list')
else:
  print ("Number's index is: ",result)