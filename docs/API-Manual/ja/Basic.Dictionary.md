# Dictionary

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ja -->

Dictionary() はキーと値のコレクションを作ります。返されたオブジェクトのメソッドを使います。数値キーと文字列キー、また "ore" と "Ore" は異なります。

## 正確な構文

```text
Dictionary() -> Object:Dictionary
Dictionary(source:Dictionary) -> Object:Dictionary
values.Add(key:String/Number, value:Any) -> Unit
values.Item(key:String/Number) -> Any
values[key] = value
values.Set(key:String/Number, value:Any) -> Unit
values.Get(key:String/Number, fallback:Any) -> Any
values.Count() -> Integer
values.ContainsKey(key:String/Number) -> Integer:1/0
values.Remove(key:String/Number) -> Integer:1/0
values.Clear() -> Unit
values.Keys() -> Array
values.Values() -> Array
entry.Key() -> String/Number
entry.Value() -> Any
```

## パラメーター

- `source` — source：省略すると空になります。List は配列または List、Dictionary は Dictionary を受け取ります。外側の容器をコピーし、入れ子の参照は共有します。
- `index / key` — index / key：List の位置は 0 からの整数値です。Insert は Count() も許可します。Dictionary のキーは文字列または有限数です。数値 1 と 1.0 は同じキー、文字列 "1" は別です。
- `value` — value：初期化済み Basic 値です。配列やコレクションも含みます。Unit は保存できません。数値、大小文字を区別する文字列、配列／オブジェクトの参照同一性で比較します。
- `fallback` — fallback：キーがなければ Get はこの代替値を返し、挿入しません。fallback の式を含むすべての引数はメソッド呼び出し前に評価します。

## 戻り値

生成は Object:Dictionary を返します。Item／添字／Get は値、Count はキー数を返します。ContainsKey/Remove は 1=TRUE または 0=FALSE、Add/Set/Clear は Unit、Keys/Values は新しい Array を返します。For Each はエントリーを返し、Key() がキー、Value() が値を返します。

## 動作

- Add は既存キーを上書きせず拒否します。Set／添字代入は作成または置換、Item／添字読み取りには既存キーが必要で、Get は代替値を指定できます。Remove は不在なら 0、Clear は全削除です。
- NaN、無限大、配列、オブジェクト、Unit はキーに使えません。キーの順序は未規定です。各エントリーは自身のペアを保持し、次の反復へ進んでも変わりません。
- Keys/Values は浅いスナップショットです。削除や置換には Keys() を反復し、辞書を直接反復するとエントリーオブジェクトを得ます。
- 直接 For Each 中に Set を含む変更を行うと、次のステップで捕捉可能なエラーになります。Try/Finally は通常どおり終了処理します。失敗した変更は元のデータを保ちます。
- 別名と ByVal 引数はコレクションを共有します。コピーやスナップショットは外側だけを複製します。添字付き ByRef と複合代入は容器／キーを一度評価し、変数を置換しても書き戻し先は変わりません。
- ローカルのスクリプトデータです。メソッドはゲーム内アイテムを動かさず、ネットワークも使いません。一つの要素として格納したスタックは一つの位置を占めます。

## 使用例

### 1. キー型と代替値

```vb
# "ore" は 5 から 8 になります。数値キー 1 は 2、文字列キー "1" は 3 を格納。Get("wood",7) は挿入せず 7 を返します。Main は 8*100+2*10+3+7、Integer 830 を返します。
Option Explicit On
Sub Main()
    Var values = Dictionary()
    values.Add("ore", 5)
    values.Set("ore", 8)
    values[1] = 2
    values["1"] = 3
    Return values.Item("ore")*100 + values[1]*10 + values["1"] + values.Get("wood", 7)
End Sub
```

**パラメーターと実行の説明:**

"ore" は 5 から 8 になります。数値キー 1 は 2、文字列キー "1" は 3 を格納。Get("wood",7) は挿入せず 7 を返します。Main は 8*100+2*10+3+7、Integer 830 を返します。

### 2. エントリー、スナップショット、削除

```vb
# 二つの値の合計は 5。Keys() により反復中も削除できます。copied は ore=2、snapshot は二つの値を保持。Clear 後は Count()=0。Main は 5*100+2*10+2+0、Integer 522 を返します。
Option Explicit On
Sub Main()
    Var values = Dictionary()
    values.Add("ore", 2)
    values.Add("wood", 3)
    Var copied = Dictionary(values)
    Var snapshot = values.Values()
    Var total = 0
    For Each entry In values
        If values.ContainsKey(entry.Key()) Then
            total += entry.Value()
        End If
    Next
    For Each key In values.Keys()
        values.Remove(key)
    Next
    values.Clear()
    Return total*100 + copied["ore"]*10 + GetArrayLength(snapshot) + values.Count()
End Sub
```

**パラメーターと実行の説明:**

二つの値の合計は 5。Keys() により反復中も削除できます。copied は ore=2、snapshot は二つの値を保持。Clear 後は Count()=0。Main は 5*100+2*10+2+0、Integer 522 を返します。

### 3. 重複キーの処理

```vb
# 最初の Add が ore=4 を保存。二回目の値 7 はエラーとなり Catch が caught=1 にします。元の ore=4 は残ります。Main は 4*10+1、Integer 41 を返します。
Option Explicit On
Sub Main()
    Var values = Dictionary()
    values.Add("ore", 4)
    Var caught = 0
    Try
        values.Add("ore", 7)
    Catch problem
        caught = 1
    End Try
    Return values["ore"]*10 + caught
End Sub
```

**パラメーターと実行の説明:**

最初の Add が ore=4 を保存。二回目の値 7 はエラーとなり Catch が caught=1 にします。元の ore=4 は残ります。Main は 4*10+1、Integer 41 を返します。

<!-- implementation references (not callable script procedures):
Runtime/ObjectTypes/DictionaryObject.cs: registered methods
Runtime/ObjectTypes/IndexedCollectionObject.cs: CollectionArguments
Runtime/IndexedValueSlot.cs: Read / Write
Runtime/ForScope.cs: enumeration lifetime
https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.dictionary-2?view=net-8.0
-->
