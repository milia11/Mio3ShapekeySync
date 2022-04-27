# Mio3 ShapeKey

キャラクターモデリングに特化したシェイプキー補助ツールです。
複数のオブエジェクトのシェイプキーを同期して操作できるようにします。

## 入手方法

安定版はリリースページからダウンロードしてください。

最新版は [Code > Download ZIP](https://github.com/mio3io/Mio3ShapekeySync/archive/master.zip) または Dev ブランチから ZIP ファイルをダウンロードしてください。

## 機能

![](https://github.com/mio3io/resources/raw/Mio3ShapekeySync/Mio3ShapekeySync2022-04-20%20221900.png)

### 同期コレクション

選択したコレクションに含まれるすべてのオブジェクトのシェイプキーの数値を同期します。顔やアイライン、眉や瞳などを分けて制作する際に役立ちます。

#### コレクションで同期する操作

- 値の状態
- ミュート状態
- 選択しているキー（存在しない場合は Basis）
- シェイプキー固定（選択キー同期のオプションと一緒に使用するとよい）

これ以外の操作は同期コレクションを設定していても影響しません

### 登録シェイプキー数の表示

オブジェクト自身のシェイプキーの数、同期しているコレクションのすべてのシェイプキーの数（名前の重複は 1 カウント）を表示する機能も付いています。統合後のシェイプキーの数を調整するのに役立ちます。

### よく使うシェイプキーの自動追加

- VRChat リップシンク
- MMD モーフ
- パーフェクトシンク
- その他 CSV ファイルの読み込み

### その他の機能

- シェイプキーの形状をリセット
- シェイプキーの名前でソート
- 単体・複数のシェイプキーの移動を補助
- X ミラー編集の自動選択・解除

## 導入方法

Blender の `Edit > Preferences > Addons > Install` を開き、ダウンロードしたアドオンの ZIP ファイルを選択してインストールボタンを押します。
インストール後、該当するアドオンの左側についているチェックボックスを ON にします。

## 使い方

シェイプキーを使用できるオブジェクトを選択するとサイドバーの Item に「Mio3 ShapeKey」とい項目が表示されます。
選択中のオブジェクトのシェイプキーと同期させたいコレクションを設定してください。
コレクションに含まれるオブジェクトのシェイプキーが同期します。
コレクションに自分自身が含まれてても問題ありません。
