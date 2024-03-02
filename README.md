# Flash Card Data

## 概要

* [FlashCard](https://github.com/TKomi/FlashCard)で使う単語帳データです
* FlashCardリポジトリのサブモジュールとして動作します
  * `public/data`に配置する
* 収録データは[New General Service List Project](https://www.newgeneralservicelist.com)(以下NGSLP)のものを使用し、ChatGPTによる加工を施したものです

## ファイル構成について

```
.
├── README.md  このファイルです。
├── index.json  リポジトリで管理する単語リストの目録です。
├── index.schema.json  index.jsonファイルのJSONスキーマです。
├── tsl  TOEIC Service List の単語データです。
└── wordSet.schema.json  単語データファイルのJSONスキーマです。
```

## 収録データについて

* TOEIC Service List(TSL): NGSLPにより、TOEICのコーパスから作成された重要語句1200語のリストです。NGSL(New General Service List)と併せることで、TOEICで使われる語句の98.5%をカバーできるとされています。
  * 位置: `/tsl`
  * 収録語彙数: 1200語
  * 本リポジトリのデータは、TSLの「頻度順」に50語ずつ区切ってPart1からPart24までに分かれています。

## ライセンスについて

* NGSLPによる収録データのオリジナルデータはCC-BY-SA 4.0でライセンスされています。
* したがってCC-BY-SAライセンスに則り、本リポジトリのデータもまたCC-BY-SA 4.0ライセンスで公開しています。

## 単語データの誤りに関するご報告のお願い

「英単語のスペルミスがある」「正解や誤答の選択肢が不適切」など、単語データの不備を見つけた際には、
お手数ですがIssueからその旨をご報告いただけると大変助かります。
