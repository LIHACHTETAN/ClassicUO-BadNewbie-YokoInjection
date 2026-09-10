# For / To / Step / Next / Exit For

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ja -->

For は到達可能な終点を含む数値範囲でブロックを繰り返します。配列インデックスや既知回数の処理向けです。For Each は要素の値を列挙します。

## 正確な構文

```text
For [VAR] counter = start To limit [Step increment]
    statements
Next [counter]
Continue For
Exit For
Break
```

## パラメーター

- `counter / VAR` — 書き込み可能なスカラーのカウンター。VAR は手続き内に宣言し、省略時は既存変数を使います。Option Explicit On では事前宣言または For Var が必要です。型は事前に DIM counter AS Integer と宣言します。数値 For のヘッダー内の AS は未対応です。
- `start` — 開始数値式。一度評価して代入してから limit と increment を評価します。
- `limit` — 範囲に含める終点。開始時に一度評価します。正のステップは counter <= limit、負は counter >= limit で判定します。
- `increment` — 省略可能な数値ステップ。既定値 1、負数や小数も使用可能です。ゼロは捕捉可能なエラーです。カウンターの型とステップは実際に値が進むように選びます。
- `statements / Next / exit` — 本体と Next は別々の行に記述します。Next 後の名前は省略可能ですが、指定時は一致が必要です。Continue For は次のステップへ、Exit For は最も近い For/For Each の外へ進みます。Break は種類を問わず最も近いループを終了します。

## 戻り値

For、Next、Exit For に戻り値はありません。カウンターは数値であり、自動的なアイテム ID ではありません。本エンジンは正常終了時に範囲外の値ではなく最後に実行した値を保持します。本体を飛ばした場合は start、早期終了時は現在値が残ります。例は Main から Integer 12、28、395 を返します。

## 動作

- 開始時に start を代入し、終点とステップを保存、ゼロを拒否して最初の値を検査します。方向が合わなければ本体を飛ばし、start=limit なら一回実行します。
- Next は counter+step を検査し、次の反復が範囲内の場合だけ代入します。1 To 5 Step 3 は 1 と 4 を使います。終点・ステップの元変数を変更しても保存値は変わりません。カウンター自体の変更は次のステップに影響します。
- 構造と Next の名前は実行前に検査し、構造エラーは SC020 です。入れ子では異なるカウンターを使います。Try を出ると Finally を実行します。一時停止・停止は有効ですが、自動の待機やタイムアウトはありません。

## 使用例

### 1. 配列セルの合計

```vb
# values[2] はインデックス 0、1、2 に 2、4、6 を格納します。Sum は配列を ByVal で受け、index=0 から length-1=2 まで、既定のステップ 1 で三セルを訪問します。total=12 を Main に返します。
Option Explicit On
Function Sum(ByVal items)
    Var total = 0
    For Var index = 0 To GetArrayLength(items) - 1
        total += items[index]
    Next index
    Return total
End Function
Sub Main()
    Dim values[2]
    values[0] = 2
    values[1] = 4
    values[2] = 6
    Return Sum(values)
End Sub
```

**パラメーターと実行の説明:**

values[2] はインデックス 0、1、2 に 2、4、6 を格納します。Sum は配列を ByVal で受け、index=0 から length-1=2 まで、既定のステップ 1 で三セルを訪問します。total=12 を Main に返します。

### 2. 末尾から削除

```vb
# items は -1、3、-2、5 です。開始 Count()-1=3、終点 0、ステップ -1。負の要素を削除しても移動するのは訪問済みのインデックスであり、未処理要素を飛ばしません。残る 3 と 5 から Count()*10+3+5=28 を返します。
Option Explicit On
Sub Main()
    Var items = List()
    items.Add(-1)
    items.Add(3)
    items.Add(-2)
    items.Add(5)
    For Var index = items.Count() - 1 To 0 Step -1
        If items[index] < 0 Then
            items.RemoveAt(index)
        End If
    Next index
    Return items.Count() * 10 + items[0] + items[1]
End Sub
```

**パラメーターと実行の説明:**

items は -1、3、-2、5 です。開始 Count()-1=3、終点 0、ステップ -1。負の要素を削除しても移動するのは訪問済みのインデックスであり、未処理要素を飛ばしません。残る 3 と 5 から Count()*10+3+5=28 を返します。

### 3. 保存した境界と最終カウンター

```vb
# ReadLimit は calls を ByRef で増やし value を返します。開始 1、終点 5、ステップ 2 を一度ずつ評価し calls=3。本体の upper=99、stride=1 はこのループを変えません。1、3、5 を訪問して total=9、index は 5 のままです。Main は 395 を返します。
Option Explicit On
Function ReadLimit(ByRef calls, ByVal value)
    calls += 1
    Return value
End Function
Sub Main()
    Var calls = 0
    Var upper = 5
    Var stride = 2
    Var total = 0
    For Var index = ReadLimit(calls, 1) To ReadLimit(calls, upper) Step ReadLimit(calls, stride)
        total += index
        upper = 99
        stride = 1
    Next index
    Return calls * 100 + total * 10 + index
End Sub
```

**パラメーターと実行の説明:**

ReadLimit は calls を ByRef で増やし value を返します。開始 1、終点 5、ステップ 2 を一度ずつ評価し calls=3。本体の upper=99、stride=1 はこのループを変えません。1、3、5 を訪問して total=9、index は 5 のままです。Main は 395 を返します。

<!-- implementation references (not callable script procedures):
Parsing/injection.g4
Analysis/LoopStructureValidator.cs
Runtime/Interpreter.cs: InterpretFor / CallSubrutine
Runtime/ForScope.cs: ContainsCurrent / HasNext
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/for-next-statement
-->
