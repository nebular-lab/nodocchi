# nodocchi
[天鳳のポイントのスクレイピングと推移グラフの描画アプリ](https://8kn42foqob.execute-api.ap-northeast-1.amazonaws.com/prod)

以下のような通信で実現されるアプリを開発しました。

現状はフォームを送信してからグラフが描画されるまでに30秒近くかかり、しかも50個のデータしか取得出来ません。
これを、30秒から3秒以内、50個から5000個、とアップグレードさせたいと思っています。
そのために、その都度スクレイピングをするのではなく、データベースを作成してそこからデータを取得する構造に変えようと思っています。
![nodocchi](https://user-images.githubusercontent.com/78769350/172051391-4eeab1e8-71e9-4245-a409-31aad8855e4b.jpeg)

https://user-images.githubusercontent.com/78769350/172049656-de476878-f9ab-46e3-9d5c-6cf6e7596335.mov

