# UO.GetStaticTilesArray

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: ja -->

矩形内の Static/Multi/Item レコードを graphic/type で検索します。

## 正確な構文

```text
UO.GetStaticTilesArray(Xmin:Any, Ymin:Any, Xmax:Any, Ymax:Any, WorldNum:Any, TileType:Any) -> Any
```

## パラメーター

- `Xmin` — 両端を含む二つの角のワールド座標、0..65535。角が逆順でも正規化されます。最大 1,000,000 セル。不正な範囲は地図を読む前にスクリプトエラーになります。
- `Ymin` — 両端を含む二つの角のワールド座標、0..65535。角が逆順でも正規化されます。最大 1,000,000 セル。不正な範囲は地図を読む前にスクリプトエラーになります。
- `Xmax` — 両端を含む二つの角のワールド座標、0..65535。角が逆順でも正規化されます。最大 1,000,000 セル。不正な範囲は地図を読む前にスクリプトエラーになります。
- `Ymax` — 両端を含む二つの角のワールド座標、0..65535。角が逆順でも正規化されます。最大 1,000,000 セル。不正な範囲は地図を読む前にスクリプトエラーになります。
- `WorldNum` — 地図／ファセット番号 0..255。UO.WorldNum() を使用します。別の地図なら空の Array。分割処理の途中で地図が変わると部分結果を破棄します。
- `TileType` — タイルの graphic/type を一つ指定します。通常 0..65535 で、serial ではありません。0 は graphic 0 だけに一致し、-1 はワイルドカードではありません。一致しなければ空の結果です。

## 戻り値

各行が [graphic, X, Y, Z, hue] の Array。全フィールドは Integer。Z は基部の高さ、hue は色。同一セルの複数レコードは別々に残ります。一致なしは空の Array。 件数は GetArrayLength(result) で取得します。添字は 0 始まりです。Boolean、serial、Pascal record ではなく、七番目の出力引数もありません。

## 動作

- ローカルデータを読み、FindItem/FindCount を変更せず、移動、target、サーバーコマンド送信も行いません。
- X の昇順、各 X の中で Y の昇順です。同じセル内は bridge の順序を維持し、距離や高さ順には並べません。
- 一回の処理は最大 32 セル、時間の目安は約 1 ms です。処理の間でキャンセルを確認します。複雑なセルや未読データの読み込みは目安を超える場合があります。広い領域は分割してください。読み取り中に世界が変化することがあります。
- 現在の static 処理には Static、Multi、Item と読み込み済み地面アイテムが含まれ、Land と Mobile は含まれません。ファイル上の静的タイルだけより広い範囲です。

### 内部関数：呼び出しから結果まで

実際の C# 処理であり、追加の UO コマンドではありません。例には補助プロシージャをすべて定義しています。

#### 1. ExecuteStealthCompatibility

六つの引数を受け取り、通常形は一つの型、Ex は Array または単一値を型リストに変換します。

land/static モードで FindPortableTiles を呼び出し、レコードの Array を直接返します。

プロジェクトのソース: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; 関数 `ExecuteStealthCompatibility`.

#### 2. FindPortableTiles

座標、地図、面積を 64 ビット演算で確認し、角を正規化して型の HashSet を作ります。

X/Y カーソルを保持し、ExecutePathQuerySlice で ScanSlice を実行します。処理間の Wait(0) がキャンセルを確認し、地図変更なら空の Array になります。

プロジェクトのソース: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; 関数 `FindPortableTiles`.

#### 3. ScanSlice

ゲームスレッドで最大 32 セルを処理し、各セルの後でカーソルを保存します。

GetLandscapeTile は graphic/Z/flags、GetStaticTiles は graphic/Z/hue の三つ組を返します。一致する行を追加し、分割処理の間で制御を戻します。

プロジェクトのソース: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; 関数 `ScanSlice`.

#### 4. GetChunk2

ブロック座標と読み込みフラグを受け取り、線形添字にする前に両軸を確認します。

Chunk または null を返します。地図外の Y を隣の列として扱いません。読み込み済みブロックを再利用し、必要なものだけ読みます。

プロジェクトのソース: `src/ClassicUO.Client/Game/Map/Map.cs`; 関数 `GetChunk2`.

ローカルデータを読み、FindItem/FindCount を変更せず、移動、target、サーバーコマンド送信も行いません。


## 使用例

### キャラクターの近くを検索

```vb
# キャラクターの近くを検索
#
# 矩形内の Static/Multi/Item レコードを graphic/type で検索します。
#
# 各行が [graphic, X, Y, Z, hue] の Array。全フィールドは Integer。Z は基部の高さ、hue
# は色。同一セルの複数レコードは別々に残ります。一致なしは空の Array。 件数は GetArrayLength(result) で取得します。添字は 0
# 始まりです。Boolean、serial、Pascal record ではなく、七番目の出力引数もありません。

SUB Main()
    # x/y は self の座標、map は現在の地図です。3×3 の範囲は端を含みます。Ex は二つ、通常形は一つの例示型を使います。リソースに合わせて graphic を変更し、物体 ID
    # と混同しないでください。

    VAR x = UO.GetX()
    VAR y = UO.GetY()
    VAR map = UO.WorldNum()
    VAR rows = UO.GetStaticTilesArray(x, y, x + 2, y + 2, map, 0x0CCA)
    UO.Print("Records: " + CStr(GetArrayLength(rows)))
END SUB
```

**パラメーターと実行の説明:**

- x/y は self の座標、map は現在の地図です。3×3 の範囲は端を含みます。Ex は二つ、通常形は一つの例示型を使います。リソースに合わせて graphic を変更し、物体 ID と混同しないでください。

### 逆順の角と全フィールドの表示

```vb
# 逆順の角と全フィールドの表示
#
# 矩形内の Static/Multi/Item レコードを graphic/type で検索します。
#
# 各行が [graphic, X, Y, Z, hue] の Array。全フィールドは Integer。Z は基部の高さ、hue
# は色。同一セルの複数レコードは別々に残ります。一致なしは空の Array。 件数は GetArrayLength(result) で取得します。添字は 0
# 始まりです。Boolean、serial、Pascal record ではなく、七番目の出力引数もありません。

SUB Main()
    # 2×2 の範囲は大きい角から小さい角へ指定していますが正規化されます。row は一行です。PrintTile は完全な定義を含み、数値を表示するだけです。地形の hue=0
    # は補助引数の仮値で、地形レコードに hue はありません。

    VAR x = UO.GetX()
    VAR y = UO.GetY()
    VAR map = UO.WorldNum()
    VAR rows = UO.GetStaticTilesArray(x + 1, y + 1, x, y, map, 0x0CCA)
    VAR i = 0
    WHILE i < GetArrayLength(rows)
        VAR row = rows[i]
        PrintTile(row[0], row[1], row[2], row[3], row[4])
        i = i + 1
    WEND
END SUB

SUB PrintTile(graphic, x, y, z, hue)
    UO.Print("Type=" + CStr(graphic) + " X=" + CStr(x) + " Y=" + CStr(y))
    UO.Print("Z=" + CStr(z) + " hue=" + CStr(hue))
END SUB
```

**パラメーターと実行の説明:**

- 2×2 の範囲は大きい角から小さい角へ指定していますが正規化されます。row は一行です。PrintTile は完全な定義を含み、数値を表示するだけです。地形の hue=0 は補助引数の仮値で、地形レコードに hue はありません。

### 回数を制限した再検索

```vb
# 回数を制限した再検索
#
# 矩形内の Static/Multi/Item レコードを graphic/type で検索します。
#
# 各行が [graphic, X, Y, Z, hue] の Array。全フィールドは Integer。Z は基部の高さ、hue
# は色。同一セルの複数レコードは別々に残ります。一致なしは空の Array。 件数は GetArrayLength(result) で取得します。添字は 0
# 始まりです。Boolean、serial、Pascal record ではなく、七番目の出力引数もありません。

SUB Main()
    # 同じセルを最大三回検索し、間に WAIT(250) を置きます。各呼び出しは新しい結果です。長さ 0 は現在一致なしという意味で、サーバー上の永続的な不存在ではありません。

    VAR x = UO.GetX()
    VAR y = UO.GetY()
    VAR map = UO.WorldNum()
    VAR attempt = 0
    WHILE attempt < 3
        VAR rows = UO.GetStaticTilesArray(x, y, x, y, map, 0x0CCA)
        UO.Print("Records: " + CStr(GetArrayLength(rows)))
        attempt = attempt + 1
        WAIT(250)
    WEND
END SUB
```

**パラメーターと実行の説明:**

- 同じセルを最大三回検索し、間に WAIT(250) を置きます。各呼び出しは新しい結果です。長さ 0 は現在一致なしという意味で、サーバー上の永続的な不存在ではありません。
