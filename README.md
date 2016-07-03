# yourtype Finder

Who is your type? By using Deep Learning, algorithm will suggest the best matched person based on your type

## requirements
required libraries are described on `requirements.txt`
* Python 3.4


## Processing
* collecting actress name and image from this web site
 - http://gensun.org
 - `wget -r htt@://gensun.org`
 - scraping name and image from this html

--------------------------------
## 第一段階の手続き
* 画像を大量に取得してくる
 - facebookを用いる
   - facebookが無理であることがわかった
 - こんなのあった
   - http://gensun.org/list_ja_female.html
* dlibで顔画像を切り取って96×96の大きさにリサイズする。
 - 顔写真が取れているので、この必要もなくなった
* 好みかどうかを付け加えるweb appをかく
* 一人につき100枚以上になるようにdata augmentation
* chainerで顔画像を学習させる
* 学習モデルから任意の画像を予測する

## 第二段階
* 実際にあった人のbig fiveを手で書く
* 上のものを正解データとして、テキスト内容からbigfiveを推定する
* big fiveを推定した後に、顔の好みから推定する

### 画像の収集
* bing api



