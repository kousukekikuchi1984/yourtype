# yourtype Finder

Who is your type? By using Deep Learning, algorithm will suggest the best matched person based on your type

## requirements
required libraries are described on `requirements.txt`
* Python 3.4
* PostgreSQL 9.5


## Processing
* collecting actress name and image from this web site
 - http://gensun.org/list_ja_female_\d.html
 - scraping name and image and insert into db
 - adding web application which can mark your type
* data augmentation

## Implementaion
- [ ] inserting data
- [ ] adding web app framework
- [ ] labeling each actress
- [ ] constructing a CNN model

--------------------------------
## 第一段階の手続き
* 画像を大量に取得してくる
 - http://gensun.org/list_ja_female.html
 - insert actress data into db
* 好みかどうかを付け加えるweb appをかく
* 一人につき100枚以上になるようにdata augmentation
* chainerで顔画像を学習させる
* 学習モデルから任意の画像を予測する

## 第二段階
* 実際にあった人のbig fiveを手で書く
* 上のものを正解データとして、テキスト内容からbigfiveを推定する
* big fiveを推定した後に、顔の好みから推定する

