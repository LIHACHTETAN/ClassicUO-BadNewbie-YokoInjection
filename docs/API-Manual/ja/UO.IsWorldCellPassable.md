# UO.IsWorldCellPassable

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: ja -->

隣接するワールドセルへの一歩を調べ、通行可否と高さを返します。

## 正確な構文

```text
UO.IsWorldCellPassable(CurrX:Any, CurrY:Any, CurrZ:Any, DestX:Any, DestY:Any, DestZ:Any, WorldNum:Any) -> Array
```

## パラメーター

- `CurrX` — 必須の開始セルのワールド座標 X：読み込み済みマップ内の整数 0..65535。gump 座標ではありません。
- `CurrY` — 必須の開始セルのワールド座標 Y：読み込み済みマップ内の整数 0..65535。gump 座標ではありません。
- `CurrZ` — 必須の開始高度 −128..127。階数ではありません。不正な高度は制限値に丸めず拒否します。
- `DestX` — 必須の目的セルのワールド座標 X：読み込み済みマップ内の整数 0..65535。gump 座標ではありません。
- `DestY` — 必須の目的セルのワールド座標 Y：読み込み済みマップ内の整数 0..65535。gump 座標ではありません。
- `DestZ` — 必須の予備入力 Z。通常は CurrZ。var ではなく、変数を変更せず階も指定しません。計算高度は result[1] から読みます。この bridge は常に自身の高さを返し、この引数は Pascal 形式を維持します。
- `WorldNum` — 必須のマップ番号：UO.WorldNum()。寸法が既知の現在マップのみ検査し、他のマップは読み込みません。

## 戻り値

二つの Integer を持つ Array：[0] — 通行可否、1 = TRUE、0 = FALSE；[1] — 計算した Z。論理値は先頭要素だけで、配列自体を TRUE と比較しません。0 や負の高さも有効で、[0]=0 の高さは到達可能性を示しません。引数拒否時は [0, CurrZ]。

## 動作

- 移動、開扉、ターゲット、ネットワーク送信をしません。既存のローカル幾何を読み、後の歩行はサーバーに拒否される場合があります。各照会は別スナップショットです。
- 隣接セルの X/Y 差はそれぞれ 1 以下です。遠い目的地、マップ範囲外、キャラクター/マップ不在、IsDestroyed は衝突計算前に拒否します。全経路には GetPathArray または NewMoveXY を使用します。
- 同じ有効 X/Y は一歩不要なので衝突検査なしに [1, CurrZ]。そのセルから出られるかの検査ではありません。キャラクター状態と現在の Pathfinder 規則が隣接歩行に影響し、幾何が未読み込みなら拒否される場合があります。

### 内部関数：呼び出しから結果まで

実際の C# 内部処理を示します。IsCellOpen は例に完全な定義を含む補助関数で、隠れた組み込み命令ではありません。

#### 1. ExecuteStealthCompatibility

七つの Integer 引数を読みます。別の bridge が高さを返さない場合だけ DestZ を使います。引数を書き換えず配列を返します。

二つの Integer を持つ Array：[0] — 通行可否、1 = TRUE、0 = FALSE；[1] — 計算した Z。論理値は先頭要素だけで、配列自体を TRUE と比較しません。0 や負の高さも有効で、[0]=0 の高さは到達可能性を示しません。引数拒否時は [0, CurrZ]。

プロジェクトのソース: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; 関数 `ExecuteStealthCompatibility`.

#### 2. CheckWorldStep

Invoke は座標の減算前にキャラクター、マップ、寸法、座標、高度、隣接性を検証し、方向を選びます。CanWalkForQuery 後の X/Y も目的と完全一致する必要があります。

二つの Integer を持つ Array：[0] — 通行可否、1 = TRUE、0 = FALSE；[1] — 計算した Z。論理値は先頭要素だけで、配列自体を TRUE と比較しません。0 や負の高さも有効で、[0]=0 の高さは到達可能性を示しません。引数拒否時は [0, CurrZ]。

プロジェクトのソース: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; 関数 `CheckWorldStep`.

#### 3. CanWalkForQuery

別経路の禁止セル判定を一時的に除き finally で戻します。経路を開始せず CanWalk を呼びます。

移動、開扉、ターゲット、ネットワーク送信をしません。既存のローカル幾何を読み、後の歩行はサーバーに拒否される場合があります。各照会は別スナップショットです。

プロジェクトのソース: `src/ClassicUO.Client/Game/Pathfinder.cs`; 関数 `CanWalkForQuery`.

#### 4. CanWalk

主歩行と斜めの側セルを検査します。bool を返し、受理した歩行のみ ref 座標を更新します。

衝突関数は読み込み済み幾何とキャラクター状態を参照します。斜めから横セルへの代替歩行は、要求セルへの到達ではありません。

プロジェクトのソース: `src/ClassicUO.Client/Game/Pathfinder.cs`; 関数 `CanWalk`.

#### 5. CalculateNewZ

目的 X/Y、ref 開始 Z、方向を受け、キャラクター状態から表面と空間を選択します。bool は通行可否、z は高度です。

衝突関数は読み込み済み幾何とキャラクター状態を参照します。斜めから横セルへの代替歩行は、要求セルへの到達ではありません。

プロジェクトのソース: `src/ClassicUO.Client/Game/Pathfinder.cs`; 関数 `CalculateNewZ`.

#### 6. CalculateMinMaxZ

新セル、現在 Z、方向、モードを受けます。CreateItemList の開始幾何から ref minZ/maxZ を計算します。

衝突関数は読み込み済み幾何とキャラクター状態を参照します。斜めから横セルへの代替歩行は、要求セルへの到達ではありません。

プロジェクトのソース: `src/ClassicUO.Client/Game/Pathfinder.cs`; 関数 `CalculateMinMaxZ`.

#### 7. CreateItemList

リスト、X/Y、モードを受け、読み込み済み物体と衝突規則を集めます。bool は幾何の存在を示します。Map.GetTile は load=false で新ブロックを読みません。

衝突関数は読み込み済み幾何とキャラクター状態を参照します。斜めから横セルへの代替歩行は、要求セルへの到達ではありません。

プロジェクトのソース: `src/ClassicUO.Client/Game/Pathfinder.cs`; 関数 `CreateItemList`.

移動、開扉、ターゲット、ネットワーク送信をしません。既存のローカル幾何を読み、後の歩行はサーバーに拒否される場合があります。各照会は別スナップショットです。


## 使用例

### 東のセルを調べる

```vb
# 東のセルを調べる
#
# 隣接するワールドセルへの一歩を調べ、通行可否と高さを返します。
#
# 二つの Integer を持つ Array：[0] — 通行可否、1 = TRUE、0 = FALSE；[1] — 計算した Z。論理値は先頭要素だけで、配列自体を TRUE
# と比較しません。0 や負の高さも有効で、[0]=0 の高さは到達可能性を示しません。引数拒否時は [0, CurrZ]。

SUB Main()
    # x/y/z は開始位置、x+1/y は隣接セル、第六引数は予備 Z、最後は現在マップです。result[1] より前に result[0] を調べます。

    VAR x = UO.GetX()
    VAR y = UO.GetY()
    VAR z = UO.GetZ()
    VAR result = UO.IsWorldCellPassable(x,y,z,x+1,y,z,UO.WorldNum())
    IF result[0] = TRUE THEN
        UO.Print('Passable, Z=' + CStr(result[1]))
    ELSE
        UO.Print('Blocked')
    END IF
END SUB
```

**パラメーターと実行の説明:**

- x/y/z は開始位置、x+1/y は隣接セル、第六引数は予備 Z、最後は現在マップです。result[1] より前に result[0] を調べます。

### 引数を変えず Z を読む

```vb
# 引数を変えず Z を読む
#
# 隣接するワールドセルへの一歩を調べ、通行可否と高さを返します。
#
# 二つの Integer を持つ Array：[0] — 通行可否、1 = TRUE、0 = FALSE；[1] — 計算した Z。論理値は先頭要素だけで、配列自体を TRUE
# と比較しません。0 や負の高さも有効で、[0]=0 の高さは到達可能性を示しません。引数拒否時は [0, CurrZ]。

SUB Main()
    # proposedZ は 0 のままです。targetZ は引数ではなく result[1] から読みます。拒否時に高さを推測しません。

    VAR x = UO.GetX()
    VAR y = UO.GetY()
    VAR z = UO.GetZ()
    VAR proposedZ = 0
    VAR result = UO.IsWorldCellPassable(x,y,z,x,y+1,proposedZ,UO.WorldNum())
    IF result[0] = 1 THEN
        VAR targetZ = result[1]
        UO.Print('Input=' + CStr(proposedZ) + '; result=' + CStr(targetZ))
    END IF
END SUB
```

**パラメーターと実行の説明:**

- proposedZ は 0 のままです。targetZ は引数ではなく result[1] から読みます。拒否時に高さを推測しません。

### 完全な IsCellOpen 関数

```vb
# 完全な IsCellOpen 関数
#
# 隣接するワールドセルへの一歩を調べ、通行可否と高さを返します。
#
# 二つの Integer を持つ Array：[0] — 通行可否、1 = TRUE、0 = FALSE；[1] — 計算した Z。論理値は先頭要素だけで、配列自体を TRUE
# と比較しません。0 や負の高さも有効で、[0]=0 の高さは到達可能性を示しません。引数拒否時は [0, CurrZ]。

SUB Main()
    # Main 後の完全な関数は開始 X/Y/Z、目的 X/Y、マップを受け、第六引数を補います。配列ではなく Integer 1/0 のみを返すため IsCellOpen は TRUE
    # と比較できます。キャラクターは移動しません。

    VAR x = UO.GetX()
    VAR y = UO.GetY()
    VAR openCell = IsCellOpen(x,y,UO.GetZ(),x+1,y+1,UO.WorldNum())
    IF openCell = TRUE THEN
        UO.Print('Diagonal cell is locally passable')
    END IF
END SUB

SUB IsCellOpen(x,y,z,toX,toY,map)
    VAR cellResult = UO.IsWorldCellPassable(x,y,z,toX,toY,z,map)
    IF GetArrayLength(cellResult) <> 2 THEN
        RETURN 0
    END IF
    RETURN cellResult[0]
END SUB
```

**パラメーターと実行の説明:**

- Main 後の完全な関数は開始 X/Y/Z、目的 X/Y、マップを受け、第六引数を補います。配列ではなく Integer 1/0 のみを返すため IsCellOpen は TRUE と比較できます。キャラクターは移動しません。
