# UO.LastTargetY

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: ja -->

最後のターゲット選択時に保存した Y を読みます。

## 正確な構文

```text
UO.LastTargetY() -> Integer
```

## パラメーター

引数はありません。

## 戻り値

Integer — 保存済み Y 座標。画素や Boolean ではありません。選択前/Clear 後や不明な物体では0ですが、実際の座標0も有効です。LastTarget()=0 でも地面/静的物体の座標を取得できます。

## 動作

- 引数なし。カーソル表示、選択、攻撃、送信はしません。LastAttack や LastStatus とは異なります。通常の self 選択では置き換えず、明示的な ClientMarkChar では変更できます。
- SetEntity は既知の Entity.X/Y を保存し、容器内部の座標の場合もあります。SetLand/SetStatic はワールドのマスを保存します。後の移動/削除では変わりません。現在位置は GetX/GetY(serial) で取得します。
- Clear と World.Clear はスクリプトを保持してもリセットします。不明な serial を明示設定すると X/Y=0 になり、古い座標を引き継ぎません。サーバー上の存在は保証しません。
- 別々の読み取りは不可分ではありません。物体ターゲットの LastTile は通信上の X/Y=65535 を保ちます。地面/静的物体では LastTile(1)/(2) が X/Y です。括弧なしの lasttarget は動的ですが同名の変数で隠せます。
- World.Clear は ClearWorldState を呼び、現在のカーソル/callback、保存済みターゲット、再送用パケットを消去します。通常の Reset は履歴を保持します。ネイティブ TargetLast はサーバーカーソルが有効な場合だけ保存パケットを送信します。履歴なしやローカル callback では何も送らずカーソルを残します。 有効なクライアント callback にはキャンセルとして null が一度だけ渡り、ClientTargetResponsePresent は空の応答で 1 になります。完了済みの選択には再通知しません。

### 内部関数：呼び出しから結果まで

実際の C# 内部処理を示します。ReadTargetValue は例に完全な定義を含む補助関数で、隠れた組み込み命令ではありません。

#### 1. SetEntity

SetEntity は World.Get から serial と X/Y を保存します。不在/破棄済み Entity なら X/Y=0。通信の特殊値は保ちます。

SetEntity は既知の Entity.X/Y を保存し、容器内部の座標の場合もあります。SetLand/SetStatic はワールドのマスを保存します。後の移動/削除では変わりません。現在位置は GetX/GetY(serial) で取得します。

プロジェクトのソース: `src/ClassicUO.Client/Game/Managers/TargetManager.cs`; 関数 `SetEntity`.

#### 2. SetLand

SetLand/SetStatic は serial 0 と X/Y/Z を保存します。SavedX/SavedY は送信フィールドとは別です。

Integer — 保存済み Y 座標。画素や Boolean ではありません。選択前/Clear 後や不明な物体では0ですが、実際の座標0も有効です。LastTarget()=0 でも地面/静的物体の座標を取得できます。

プロジェクトのソース: `src/ClassicUO.Client/Game/Managers/TargetManager.cs`; 関数 `SetLand`.

#### 3. SetStatic

SetLand/SetStatic は serial 0 と X/Y/Z を保存します。SavedX/SavedY は送信フィールドとは別です。

Integer — 保存済み Y 座標。画素や Boolean ではありません。選択前/Clear 後や不明な物体では0ですが、実際の座標0も有効です。LastTarget()=0 でも地面/静的物体の座標を取得できます。

プロジェクトのソース: `src/ClassicUO.Client/Game/Managers/TargetManager.cs`; 関数 `SetStatic`.

#### 4. LastTargetY

LastTargetX/LastTargetY は ITargetSnapshotBridge を読み、古い外部 bridge では GetX/GetY を保ちます。Invoke はキャンセルに対応してゲームスレッドで読みます。

Integer — 保存済み Y 座標。画素や Boolean ではありません。選択前/Clear 後や不明な物体では0ですが、実際の座標0も有効です。LastTarget()=0 でも地面/静的物体の座標を取得できます。

プロジェクトのソース: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; 関数 `LastTargetY`.

#### 5. Invoke

LastTargetX/LastTargetY は ITargetSnapshotBridge を読み、古い外部 bridge では GetX/GetY を保ちます。Invoke はキャンセルに対応してゲームスレッドで読みます。

引数なし。カーソル表示、選択、攻撃、送信はしません。LastAttack や LastStatus とは異なります。通常の self 選択では置き換えず、明示的な ClientMarkChar では変更できます。

プロジェクトのソース: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; 関数 `Invoke`.

#### 6. Clear

Clear は serial と保存座標を消し、World.Clear が清掃時に呼び出します。

Clear と World.Clear はスクリプトを保持してもリセットします。不明な serial を明示設定すると X/Y=0 になり、古い座標を引き継ぎません。サーバー上の存在は保証しません。

プロジェクトのソース: `src/ClassicUO.Client/Game/Managers/TargetManager.cs`; 関数 `Clear`.

#### 7. ClearWorldState

World.Clear は ClearWorldState を呼び、現在のカーソル/callback、保存済みターゲット、再送用パケットを消去します。通常の Reset は履歴を保持します。ネイティブ TargetLast はサーバーカーソルが有効な場合だけ保存パケットを送信します。履歴なしやローカル callback では何も送らずカーソルを残します。 有効なクライアント callback にはキャンセルとして null が一度だけ渡り、ClientTargetResponsePresent は空の応答で 1 になります。完了済みの選択には再通知しません。

World.Clear は ClearWorldState を呼び、現在のカーソル/callback、保存済みターゲット、再送用パケットを消去します。通常の Reset は履歴を保持します。ネイティブ TargetLast はサーバーカーソルが有効な場合だけ保存パケットを送信します。履歴なしやローカル callback では何も送らずカーソルを残します。 有効なクライアント callback にはキャンセルとして null が一度だけ渡り、ClientTargetResponsePresent は空の応答で 1 になります。完了済みの選択には再通知しません。

プロジェクトのソース: `src/ClassicUO.Client/Game/Managers/TargetManager.cs`; 関数 `ClearWorldState`.

#### 8. TargetLast

World.Clear は ClearWorldState を呼び、現在のカーソル/callback、保存済みターゲット、再送用パケットを消去します。通常の Reset は履歴を保持します。ネイティブ TargetLast はサーバーカーソルが有効な場合だけ保存パケットを送信します。履歴なしやローカル callback では何も送らずカーソルを残します。 有効なクライアント callback にはキャンセルとして null が一度だけ渡り、ClientTargetResponsePresent は空の応答で 1 になります。完了済みの選択には再通知しません。

World.Clear は ClearWorldState を呼び、現在のカーソル/callback、保存済みターゲット、再送用パケットを消去します。通常の Reset は履歴を保持します。ネイティブ TargetLast はサーバーカーソルが有効な場合だけ保存パケットを送信します。履歴なしやローカル callback では何も送らずカーソルを残します。 有効なクライアント callback にはキャンセルとして null が一度だけ渡り、ClientTargetResponsePresent は空の応答で 1 になります。完了済みの選択には再通知しません。

プロジェクトのソース: `src/ClassicUO.Client/Game/Managers/TargetManager.cs`; 関数 `TargetLast`.

別々の読み取りは不可分ではありません。物体ターゲットの LastTile は通信上の X/Y=65535 を保ちます。地面/静的物体では LastTile(1)/(2) が X/Y です。括弧なしの lasttarget は動的ですが同名の変数で隠せます。


## 使用例

### 保存値を読む

```vb
# 保存値を読む
#
# 最後のターゲット選択時に保存した Y を読みます。
#
# Integer — 保存済み Y 座標。画素や Boolean ではありません。選択前/Clear 後や不明な物体では0ですが、実際の座標0も有効です。LastTarget()=0
# でも地面/静的物体の座標を取得できます。

SUB Main()
    # value が結果です。HEX は ID、CStr は座標を表示します。選択は行いません。

    VAR value = UO.LastTargetY()
    UO.Print('Saved value: ' + CStr(value))
END SUB
```

**パラメーターと実行の説明:**

- value が結果です。HEX は ID、CStr は座標を表示します。選択は行いません。

### 保存位置と現在位置を比較する

```vb
# 保存位置と現在位置を比較する
#
# 最後のターゲット選択時に保存した Y を読みます。
#
# Integer — 保存済み Y 座標。画素や Boolean ではありません。選択前/Clear 後や不明な物体では0ですが、実際の座標0も有効です。LastTarget()=0
# でも地面/静的物体の座標を取得できます。

SUB Main()
    # id は保存された serial です。GetX/GetY の前に Exists で確認します。位置は異なる場合があり、ID=0 は点の選択を証明しません。

    VAR id = UO.LastTarget()
    VAR x = UO.LastTargetX()
    VAR y = UO.LastTargetY()
    UO.Print('Saved XY: ' + CStr(x) + ',' + CStr(y))
    IF id <> 0 AND UO.Exists(id) THEN
        UO.Print('Live XY: ' + CStr(UO.GetX(id)) + ',' + CStr(UO.GetY(id)))
    END IF
END SUB
```

**パラメーターと実行の説明:**

- id は保存された serial です。GetX/GetY の前に Exists で確認します。位置は異なる場合があり、ID=0 は点の選択を証明しません。

### 完全な ReadTargetValue 補助関数

```vb
# 完全な ReadTargetValue 補助関数
#
# 最後のターゲット選択時に保存した Y を読みます。
#
# Integer — 保存済み Y 座標。画素や Boolean ではありません。選択前/Clear 後や不明な物体では0ですが、実際の座標0も有効です。LastTarget()=0
# でも地面/静的物体の座標を取得できます。

SUB Main()
    # minimum/maximum は補助関数の範囲設定で API の引数ではありません。-1 は補助関数独自の範囲外通知です。ID 版は最上位ビットを含む非ゼロ serial を保持します。

    VAR value = ReadTargetValue(0,65535)
    UO.Print('Checked value: ' + CStr(value))
END SUB

SUB ReadTargetValue(minimum,maximum)
    VAR value = UO.LastTargetY()
    IF value < minimum OR value > maximum THEN
        RETURN -1
    END IF
    RETURN value
END SUB
```

**パラメーターと実行の説明:**

- minimum/maximum は補助関数の範囲設定で API の引数ではありません。-1 は補助関数独自の範囲外通知です。ID 版は最上位ビットを含む非ゼロ serial を保持します。
