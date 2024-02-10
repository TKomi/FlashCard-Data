import json
import os

def convert_to_json(folder_path):
    # フォルダ内のすべてのテキストファイルを処理
    for i in range(1, 26):  # Part1.txt から Part25.txt まで
        input_file_name = f'Part{i}.txt'
        output_file_name = f'Part{i}.json'
        
        # ファイルのフルパスを生成
        input_file_path = os.path.join(folder_path, input_file_name)
        output_file_path = os.path.join(folder_path, output_file_name)
        
        # 入力ファイルを開いて処理
        with open(input_file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            data_list = []  # JSONに変換されるデータのリスト
            
            for line in lines:
                # 入力ファイルの各行の書式: word, answer, option1, option2, option3
                w, j, d1, d2, d3 = line.strip().split(', ')
                data_list.append({
                    "word": w,
                    "quiz": {
                        "answer": j,
                        "options": [d1, d2, d3]
                    }
                })
        
        # JSON形式で出力ファイルに保存
        with open(output_file_path, 'w', encoding='utf-8') as json_file:
            json.dump(data_list, json_file, ensure_ascii=False, indent=2)
        
        print(f'{input_file_name} が {output_file_name} に変換されました。')

# スクリプトを実行する
# 'folder_path' には、対象のテキストファイルが含まれるフォルダのパスを指定してください。
# 例: convert_to_json('/path/to/your/folder')
convert_to_json('./problems')
