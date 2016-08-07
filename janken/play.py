HANDS = ('グー', 'チョキ', 'パー')
import random

def select_hand():
    HANDS_choice = random.choice(HANDS)
    return HANDS_choice


    # コンピュータの手をランダムに決める
    # :return: HANDSの中のいずれか。



def judgement(player,  computer):
    if player == 'グー' and computer == 'チョキ':
        return '勝ち'
    if player == 'チョキ'  and computer == 'パー':
        return '勝ち'
    if  player == 'パー' and computer == 'グー':
        return '勝ち'

    elif player == computer:
        return 'あいこ'
    else:
        return '負け'



def save_score(result):
    i = {'win':'勝ち', 'lose':'負け', 'draw':'あいこ'}
    if result == '勝ち':
        return 'win'
    if result == '負け':
        return 'lose'
    if result == 'あいこ':
        return 'draw'

    f = open('Tutorial/janken/score.txt', 'w')
    f.write(save_score(result))
    f.close

    # 'score.txt'に戦績を保存。
    # win:x lose:y draw:zのディクショナリデータを保存する。
    # :param result:
    # :return: None



if __name__ == '__main__':
    player = HANDS[int(input('グー(0)/チョキ(1/パー(2)を選んでください(数字): '))]
    computer = select_hand()
    result = judgement(player, computer)
    # コンピュータの手と勝敗の結果を表示

    save_score(result)
    print(result)
    print(player, computer)
