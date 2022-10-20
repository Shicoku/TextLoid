# TextLoid
[ボイスロイド](https://www.ah-soft.com/voiceroid/) の支援ツールです
<br>本ソフトはボイスロイドの音声をテキストファイルから一行づつ呼び出し、生成するツールです

## インストール
[Releases](https://github.com/texture08/voiceroid_tool/releases) から最新のzipをダウンロードして展開してください

## アンインストール
展開したフォルダを削除してください

## 使い方
[Releases](https://github.com/texture08/voiceroid_tool/releases) からzipファイルをダウンロードします
好きな場所に解凍したらインストールは完了です
<br>任意のフォルダにexeファイル、script.txt、その他のファイルやフォルダができます
<br>script.txtには生成したいテキストを行ごとに書きます
<br>次にexeファイルを起動します
<br>テキストボックスにボイスロイドの名前を入れて、下の保存ボタンを押します
<br>東北きりたんなら、VOICEROID＋ 東北きりたんEX* と書きます
<br>VOICEROID＋の＋は全角なので気を付けてください
<br>次にボイスロイドを起動して、ボイスロイドのテキスト欄に文字を書いてください
<br>なんでもいいので書いたら消してください
<br>これは必要なことなので、めんどくさいですがやってください
<br>最後に、ボイスロイド支援ツールの合成を押したら生成が開始されます
<br>[ニコニコ動画](https://nico.ms/sm39961372) と [YouTube](https://youtu.be/wTHKdOxWHso) にも使い方を載せています
<br>※初期リリースとインストールの仕方が変わっているので注意してください

## 注意
ファイル生成中はマウスを動かさないでください
<br>変に動かしてしますとできなくなってしまいます
<br><br>本ソフトによる損害、不利益などは製作者は一切責任を取りません
<br><br>VOICEVOX、棒読みちゃん等での使用はできません
<br>今後の課題にしていこうと思います

## config.jsonについて
config.jsonには本ソフトの設定項目があります
### window
ボイスロイドのウィンドウ一覧です。自分の使いたいボイスロイドがない場合は各自で追加してください
### start_win
初期選択されるウィンドウを指定します。基本いじらなくて結構です
### end_window
生成完了後に確認ダイアログを表示するかどうかを指定します
<br>true で表示、false で非表示です
### save_text
音声生成時に参照するテキストの中身です
<br>ファイルは必ず、本ソフトのsetフォルダ内に入れてください

## 利用規約
二次配布、自作発言は禁止です
<br>営利利用、商用利用等は [こちらのライセンス](https://www.ah-soft.com/licensee/voice_individual.html) をご覧ください
<br>クレジット表記は不要です

## 使用したパッケージ、ライブラリ等
opencv
<br>tkinter
<br>win32gui
<br>json
<br>pyautogui
<br>pyperclip

<br><br>バグ、お問い合わせは [Twitter@H2DH8K](https://twitter.com/H2DH8K) までお願いします

## リリース
### v1.0.0
- 初回リリース
- 諸事情により非公開
### v.2.0.0
- インストール方法の変更
- 生成完了後、確認ダイアログを表示
### v.2.1.0
- 一行目が無視されるバグの改善
- 生成完了後、確認ダイアログを表示するかどうかを設定で変更可能に
- コンフィグにて、参照するファイルを変更可能に

### v.2.2.0
- ソフトの名称を変更
- config.jsonを編集
- ボイスロイドの選択をコンボボックスに変更
