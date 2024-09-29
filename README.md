Jリーグの同一カテゴリー・節のハイライトをダウンロードし、1つの動画ファイルにまとめるプログラムです。

## 事前準備
以下のコマンドを実行してください。
```
git clone https://github.com/PoloLavapies/jLeague_highlights.git
cd jLeague_highlights
brew install ffmpeg
pip install selenium yt-dlp
```
なお、Pythonがインストールされていない場合は、インストールが必要です。

## ダウンロード方法
以下のコマンドを実行してください。
```
chmod u+x j_highlights.sh
j_highlights.sh {見たいカテゴリー}

# 例 J2のハイライトを見る場合
j_highlights.sh 2

# 例 J2の直近の節の第10節のハイライトを見る場合
j_highlights.sh 2 10
```