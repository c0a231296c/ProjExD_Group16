# こうかとんVSゾンビ

## 実行環境の必要条件
* python >= 3.10
* pygame >= 2.1

## ゲームの概要
* 様々なこうかとんを設置し、進行してくるゾンビを倒すゲーム
* 参考URL：[Plants vs. Zombies™ - Google Play のアプリ】](https://play.google.com/store/apps/details?id=com.ea.game.pvzfree_row&hl=ja)

## ゲームの遊び方
* こうかとんを選択し、配置する。
* ゾンビが10体以上陣地に侵入するとゲームオーバー

## ゲームの実装
### 共通基本機能
* 背景画像の描画と敵、味方の出現

### 分担追加機能
* 押したキーによって設置するこうかとんを選択する機能(小太郎)
* こうかとんが弾を発射するようにする機能：完了(廣木)
* 弾とゾンビの衝突によってダメージを与える機能(山本)
* 倒したゾンビに応じてスコアを増やす機能(山本)
* ゾンビの出現数やタイミングを調整する機能(池田)

### ToDo
- [ ] イラストをダウンロードする
- [ ] 変数名を決定する

### メモ
* 衝突判定には授業内で使ったものを用いる
* こうかとんとゾンビには様々な種類がいる
