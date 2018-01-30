yr=raw_input()
  if(yr%4==0 and yr%100!=0):
    print leap year
  elif(yr%100==0):
    print not leap year
  elif(yr%400==0):
    print leap year
  else:
    print not leap year
