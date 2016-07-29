import random
HANDS = ('グー', 'チョキ', 'パー')


def select_hand():

    HANDS_choice = random.choice(HANDS)

    return HANDS_choice


def judgement(player, computer):


    if player == 1 and computer == 1:
        return 1

    if player == 1 and computer == 2:
        return -1

    if player == 2 and computer == 2:
        return 1

    if player == 2 and computer == 0:
        return -1

    if player == 3 and computer == 0:
        return 1

    if player == 3 and computer == 1:
        return -1


    else:
        return 0
    """
    じゃんけんの勝敗を判定する。
    :param player: HANDSの中のどれか
    :param computer: HANDSの中のどれか
    :return: プレイヤーが勝ちの場合は1,あいこは0,負けは-1を返す
    """

def save_score(result):
    pass

    """
    'score.txt'に戦績を保存。
    win:x lose:y draw:zのディクショナリデータを保存する。
    :param hresult:
    :return: None
    """
if __name__ == '__main__':
    player = int(input('グー(1)/チョキ(2)/パー(3)を選んでください(数字):'))
    computer = select_hand()
    result = judgement(player, computer)
    # コンピュータの手と勝敗の結果を表示
    save_score(result)

    print(result)
    print(player, computer)