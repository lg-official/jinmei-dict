import csv
import wanakana

def conver_tss(file_in, file_out, label):
    # CSVファイルを読み込む
    with open(file_in, 'r', encoding='cp932') as file:
        reader = csv.reader(file)
        data = list(reader)

    # MeCabの辞書形式に変換する
    output = []
    for row in data:
        kanji = row[1]
        kana = wanakana.to_katakana(row[2])
        entry = f"{kanji},*,*,*,名詞,固有名詞,人名,{label},*,*,*,{kana},{kana}"
        output.append(entry)

    # 結果を出力する
    with open(file_out, 'w', encoding='cp932') as file:
        file.write('\n'.join(output))

conver_tss('../data/tss/【株式会社レガシー様向け】姓情報ファイル（TMC-7211）.csv', '../data/addon/tss_sei.csv', '姓')
conver_tss('../data/tss/【株式会社レガシー様向け】名情報ファイル（TMC-7212）.csv', '../data/addon/tss_mei.csv', '名')