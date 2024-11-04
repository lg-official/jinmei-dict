import csv
import os

# 入力ファイル名と出力ファイル名を指定
input_file = f'{os.path.dirname(__file__)}/../data/addon/user_dict_seed.csv'
output_file = f'{os.path.dirname(__file__)}/../data/addon/user_dict_generated.csv'

# CSVファイルを読み込み、指定の形式に変換する関数


def convert_csv(input_file, output_file):
    with open(input_file, mode='r', encoding='utf-8') as infile, \
            open(output_file, mode='w', encoding='utf-8', newline='') as outfile:

        reader = csv.reader(infile, skipinitialspace=True)
        writer = csv.writer(outfile)

        for row in reader:
            type = row[0]
            if type == '姓' or type == '名':
                for yomi in row[2:]:
                    if len(yomi) > 0:
                        converted_row = [row[1], '*', '*', '*', '名詞',
                                         '固有名詞', '人名', type, '*', '*', '*', yomi, yomi]
                        writer.writerow(converted_row)
                    else:
                        raise Exception("余分な,があります。")


# 関数を実行
convert_csv(input_file, output_file)
