HANDS = ('グー', 'チョキ', 'パー')
import random

def select_hand():
    HANDS_choice = random.choice(HANDS)
    return HANDS_choice

    """
    コンピュータの手をランダムに決める
    :return: HANDSの中のいずれか。
    """


def judgement(player,  computer):
    if player == 'グー' and computer == 'チョキ':
        return 1
    if player == 'チョキ'  and computer == 'パー':
        return 1
    if  player == 'パー' and computer == 'グー':
        return 1

    elif player == computer:
        return 0
    else:
        return -1



def save_score(result):
    b = [{'win':'x', 'lose':'y', 'draw':'z'}]
    f = open("score.py","w")
    ff = b[result]
    f.write(ff)
    f.close

"""
    'score.txt'に戦績を保存。
    win:x lose:y draw:zのディクショナリデータを保存する。
    :param result:
    :return: Non
"""


if __name__ == '__main__':
    player = HANDS[int(input('グー(0)/チョキ(1/パー(2)を選んでください(数字): '))]
    computer = select_hand()
    result = judgement(player, computer)
    # コンピュータの手と勝敗の結果を表示


    print(result)
    print(player, computer)

