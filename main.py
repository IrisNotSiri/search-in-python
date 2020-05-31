def linear_search(num_list,target):
  for x in range(len(num_list)):
    if target == num_list[x]:
      return x
  return -1


def binary_search(num_list,l,r,target):
    if r >= l:
      mid = l + (r -l)//2
      if num_list[mid] == target:
        return mid
      elif num_list[mid] > target:
        return binary_search (num_list,l, mid-1,target)
      else:
        return binary_search(num_list,mid+1,r,target)
    return -1

def binary_search2(num_list,l,r,target):
    while l <= r:
      # value l and r will be changed due to the position search position change, so shouldn't ues len to find mid position
      mid = l + (r-l)//2
      if target == num_list[mid]:
        return mid
      elif target < num_list[mid]:
        r = mid - 1
      else:
        l = mid + 1
    return -1
   


def merge_sort(nums): 
    if nums is None:
      return None
    if len(nums)>1:
      mid = len(nums)//2
      left = nums[:mid]
      right = nums[mid:]
      merge_sort(left)
      merge_sort(right)
      i = j = k = 0
      while i < len(left) and j < len(right):
        if left[i] < right[j]:
          nums[k] = left[i]
          i += 1
        else:
          nums[k] = right[j]
          j += 1
        k += 1
      while i < len(left):
        nums[k] = left[i]
        i += 1
        k += 1
      while j < len(right):
        nums[k] = right[j]
        j += 1
        k += 1


num_list = [11,23,6,63,43,21,1,3,5]
target = 12
# list for binart search should be sorted

merge_sort(num_list)
print ("Sorted num_list",num_list)

result = binary_search2(num_list,0,len(num_list)-1,target)



if result == -1:
  print ('Number is not in list')
else:
  print ("Number's index is: ",result)

