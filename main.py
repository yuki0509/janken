import random

my_hand = int(input('グー(0)チョキ(1)パー(2)>'))
rhand = random.randint(0,2)

if (my_hand == 0 or my_hand == 1 or my_hand == 2):
  if rhand == 0:
    if rhand == my_hand:
      print('あいこ')
    elif rhand == (my_hand -1):
      print('負け')
    elif rhand == my_hand -2 :
      print('勝ち')

  elif rhand == 1:
    if rhand == my_hand+1:
      print('かち')
    elif rhand == my_hand:
      print('あいこ')
    elif rhand == my_hand -1 :
      print('負け')

  elif rhand == 2:
    if rhand == my_hand+2:
      print('負け')
    elif rhand == my_hand+1:
      print('かち')
    elif rhand == my_hand:
      print('あいこ')

else:
  print('正しく入力してください')
