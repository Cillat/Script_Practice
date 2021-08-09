#


#for i in range(3):
 #  for j  in range(i + 1, a.length):
  #%      if  a[j] < a[i]:
    #        tmp = a[i]
            #a[i] = a[j]
            #a[j] = tmp
        #b.append(a[i])


#print(type(input_value))

#','.join(map(str, input_value))


input_value_str = input()
input_value = input_value_str.split() 

input_value.sort(reverse=True)

value1 = input_value.pop(0)
value2 = input_value.pop(0)

sum = int(value1) + int(value2)

print(sum)