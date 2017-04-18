def stringMult(num1,num2):
  if len(num1) > len(num2):
    bigger = num1
    shorter = num2
  elif len(num2) > len(num1):
    bigger = num2
    shorter = num1
  else:
    bigger = num1
    shorter = num2

  totalProd = 0
  intermediates = []
  outerInter = []
  power = 0
  
  for x in range(len(shorter),0,-1):
    result = ""
    dig = 0
    # print "power is",power
    count = 10**power
    for y in range(len(bigger),0,-1):
      # print "!!!!!count is",count
      dig+=1
      # print dig
      digit1 = int(shorter[x-1])
      digit2 = int(bigger[y-1])
      print "multiplying",digit1,"*",digit2

      product = digit1*digit2
      place = product % 10
      carry = product / 10
      intermediates.insert(dig,carry)
      # print "place",place
      if dig <= 1:
        #print "appending",place,"carry is",carry
        result+=str(place)
      else:  
        print place,"+",intermediates[dig-2]
        place = (place+intermediates[dig-2])
        # print "appending",place,"carry is",carry
        result+=str(place)
    endRes = int(str(carry)+result[::-1])*count
    outerInter.append(endRes)
    print "at the end",outerInter[power]
    power+=1
  # print result[::-1]
  for x in outerInter:
    totalProd += x
  print totalProd
  return totalProd

stringMult('384','124138')