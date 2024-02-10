import csv

def split_words_into_files(input_file):
    with open(input_file, encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file, quoting=csv.QUOTE_NONE)
        words = []  # 単語を保持するリスト

        for row in reader:
            if row:  # 空の行を無視
                words.append(row[0])  # 1番左の列の単語を追加

        # 50語ごとにカンマ区切りでファイルに保存
        for i in range(0, len(words), 50):
            part_number = i // 50 + 1  # ファイル名のためのパート番号
            output_file = f'Part{part_number}.txt'
            
            with open(output_file, 'w', encoding='utf-8') as f:
                # 現在のチャンクの単語をカンマ区切りでファイルに書き込む
                f.write(','.join(words[i:i+50]))

    print(f'処理が完了しました。ファイルは {input_file} と同じディレクトリに保存されています。')

# スクリプトを実行するための関数呼び出し
# 'example.csv' を実際のファイル名に置き換えてください。
split_words_into_files('TOEIC_Service_List.csv')
