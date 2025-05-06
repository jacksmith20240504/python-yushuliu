import random

# 平假名字典
hiragana = {
    'あ': 'a', 'い': 'i', 'う': 'u', 'え': 'e', 'お': 'o',
    'か': 'ka', 'き': 'ki', 'く': 'ku', 'け': 'ke', 'こ': 'ko',
    'さ': 'sa', 'し': 'shi', 'す': 'su', 'せ': 'se', 'そ': 'so',
    'た': 'ta', 'ち': 'chi', 'つ': 'tsu', 'て': 'te', 'と': 'to',
    'な': 'na', 'に': 'ni', 'ぬ': 'nu', 'ね': 'ne', 'の': 'no',
    'は': 'ha', 'ひ': 'hi', 'ふ': 'fu', 'へ': 'he', 'ほ': 'ho',
    'ま': 'ma', 'み': 'mi', 'む': 'mu', 'め': 'me', 'も': 'mo',
    'や': 'ya', 'ゆ': 'yu', 'よ': 'yo',
    'ら': 'ra', 'り': 'ri', 'る': 'ru', 'れ': 're', 'ろ': 'ro',
    'わ': 'wa', 'を': 'wo', 'ん': 'n'
}

# 片假名字典
katakana = {
    'ア': 'a', 'イ': 'i', 'ウ': 'u', 'エ': 'e', 'オ': 'o',
    'カ': 'ka', 'キ': 'ki', 'ク': 'ku', 'ケ': 'ke', 'コ': 'ko',
    'サ': 'sa', 'シ': 'shi', 'ス': 'su', 'セ': 'se', 'ソ': 'so',
    'タ': 'ta', 'チ': 'chi', 'ツ': 'tsu', 'テ': 'te', 'ト': 'to',
    'ナ': 'na', 'ニ': 'ni', 'ヌ': 'nu', 'ネ': 'ne', 'ノ': 'no',
    'ハ': 'ha', 'ヒ': 'hi', 'フ': 'fu', 'ヘ': 'he', 'ホ': 'ho',
    'マ': 'ma', 'ミ': 'mi', 'ム': 'mu', 'メ': 'me', 'モ': 'mo',
    'ヤ': 'ya', 'ユ': 'yu', 'ヨ': 'yo',
    'ラ': 'ra', 'リ': 'ri', 'ル': 'ru', 'レ': 're', 'ロ': 'ro',
    'ワ': 'wa', 'ヲ': 'wo', 'ン': 'n'
}

def practice_kana(kana_type):
    """练习平假名或片假名"""
    kana_dict = hiragana if kana_type == "hiragana" else katakana
    total = 0
    correct = 0
    
    while True:
        # 随机选择一个假名
        kana = random.choice(list(kana_dict.keys()))
        answer = input(f"\n请输入这个{kana_type} '{kana}' 的罗马音 (输入'q'退出): ")
        
        if answer.lower() == 'q':
            break
            
        total += 1
        if answer.lower() == kana_dict[kana]:
            print("正确!")
            correct += 1
        else:
            print(f"错误. 正确答案是: {kana_dict[kana]}")
            
    if total > 0:
        accuracy = (correct / total) * 100
        print(f"\n练习结束! 总题数: {total}, 正确: {correct}, 正确率: {accuracy:.2f}%")

def main():
    while True:
        print("\n日语假名练习程序")
        print("1. 练习平假名")
        print("2. 练习片假名")
        print("3. 退出")
        
        choice = input("请选择 (1-3): ")
        
        if choice == '1':
            practice_kana("hiragana")
        elif choice == '2':
            practice_kana("katakana")
        elif choice == '3':
            print("谢谢使用!")
            break
        else:
            print("无效选择，请重试")

if __name__ == "__main__":
    main()

# 这个程序总共有89行代码
