import random

my_hand = input('グー(0)チョキ(1)パー(2)>')
r_hand = random.randint(0,2)

try:
  my_hand = int(my_hand)
  if (my_hand >= 0 and my_hand <= 2):
    if r_hand == 0:
      if r_hand == my_hand:
        print('あいこ')
      elif r_hand == (my_hand -1):
        print('負け')
      elif r_hand == my_hand -2 :
        print('勝ち')

    elif r_hand == 1:
      if r_hand == my_hand+1:
        print('かち')
      elif r_hand == my_hand:
        print('あいこ')
      elif r_hand == my_hand -1 :
        print('負け')

    elif r_hand == 2:
      if r_hand == my_hand+2:
        print('負け')
      elif r_hand == my_hand+1:
        print('かち')
      elif r_hand == my_hand:
        print('あいこ')
  else:
    print('正しく入力してください')
except:
  print('正しく入力してください')
