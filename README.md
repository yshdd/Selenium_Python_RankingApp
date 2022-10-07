# Selenium_Python_RankingApp

Seleniumとpythonを用いたwebアプリの開発。
検索クエリと調べたいURLを入力すると、google検索ページで上位何番目に掲載されているかを調べてブラウザに表示してくれる。

### アプリの画面
最初の画面。検索クエリと調べたいURLを入力して青いボタンをクリックする。
画像では例として、検索クエリを『python　公式ページ』, 検索URLを https://www.python.org　とした。

![スクリーンショット 2022-10-07 22 51 54](https://user-images.githubusercontent.com/70735561/194575634-5e224de9-7e83-42d4-89f9-875a7bb8987a.png)

以下は調査結果の画面。

![スクリーンショット 2022-10-07 22 52 19](https://user-images.githubusercontent.com/70735561/194576094-5a8496ea-a6f2-48da-982e-f2bdacc937cf.png)

最大2ページまで見て、ない場合は以下のページを表示する。青い戻るボタンをクリックすると最初の画面に戻る。
<img width="597" alt="スクリーンショット 2022-10-07 23 06 20" src="https://user-images.githubusercontent.com/70735561/194576269-6cfb287d-6499-4440-93e3-1a9999b3c064.png">

### 注意点
ページ内に同じURLが複数あった場合、上位のものだけ取り出す仕様になっている。
