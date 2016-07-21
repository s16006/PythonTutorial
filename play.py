
HANDS = ('グー', 'チョキ', 'パー')

def select_hand():
    import random
    random.choice(-1, 1)

def judgment(player, computer):

    if player == computer:
        return(0)
        print('あいこ')

    if computer > player:
        return(-1)
        print('負け')

    else:
        return (1)
        print('勝ち')
"""
def save_score(result):
"""
if __name__ == '__main__':
    player = int(input('グー(1)/チョキ(2)/パー(3)を選んでください(数字): '))
    computer = select_hand()
    result = judgement(player, computer)