import random

choice = input('グー(0)チョキ(1)パー(2)>')
my_hands = ['グー','チョキ','パー']
judge = [
  ['あいこ','負け','かち'],
  ['かち','あいこ','負け'],
  ['負け','かち','あいこ']
]
result = ''

try:
  choice = int(choice)
  if (choice >= 0 and choice <= 2):
    print(my_hands[choice])

    while result == 'あいこ' or result == '':
      r_hand = random.randint(0,2)
      # 勝敗判定
      if r_hand == 0:
        if r_hand == choice:
          result = judge[0][0]
        elif r_hand == choice - 1:
          result = judge[0][1]
        elif r_hand == choice - 2 :
          result = judge[0][2]

      elif r_hand == 1:
        if r_hand == choice + 1:
          result = judge[1][0]
        elif r_hand == choice:
          result = judge[1][1]
        elif r_hand == choice - 1 :
          result = judge[1][2]

      elif r_hand == 2:
        if r_hand == choice + 2:
          result = judge[2][0]
        elif r_hand == choice + 1:
          result = judge[2][1]
        elif r_hand == choice:
          result = judge[2][2]
      print(result)
  else:
    print('正しく入力してください')
except:
  print('正しく入力してください')
