Jリーグの試合の3分ハイライトを見るためのプログラムです。
同一カテゴリー・節のハイライトの連続視聴が可能です。

ブラウザで見る方法・ダウンロードして見る方法の2種類があります。

## (共通) 事前準備
以下のコマンドを実行してください。
```
git clone https://github.com/PoloLavapies/jLeague_highlights.git
cd jLeague_highlights
brew install ffmpeg
pip install selenium yt-dlp
```
なお、Pythonがインストールされていない場合は、インストールが必要です。

## ダウンロードして見る場合
以下のコマンドを実行してください。
```
chmod u+x j_highlights.sh
j_highlights.sh {見たいカテゴリー}

# 例 J2のハイライトを見る場合
j_highlights.sh 2

# 例 J2の直近の節の第10節のハイライトを見る場合
j_highlights.sh 2 10
```

## ブラウザで見る場合
以下のコマンドを実行してください。
```
python j_highlights_browser.py {見たいカテゴリー}

# 例 J2の直近の節のハイライトを見る場合
python j_highlights_browser.py 2

# 例 J2の第10節のハイライトを見る場合
python j_highlights_browser.py 2 10
```
注意点として、ハイライトの再生から次のハイライトの再生の間隔は190秒です。
広告が再生されると途中で次の動画が始まる可能性があるので、広告ブロックツールを利用してください。
