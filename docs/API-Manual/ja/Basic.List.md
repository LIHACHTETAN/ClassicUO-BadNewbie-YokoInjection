# List

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ja -->

List() は順序を持つ可変長コレクションを作ります。結果を変数に保存してください。items.Add はオブジェクトのメソッドであり、グローバルな List.Add 命令はありません。

## 正確な構文

```text
List() -> Object:List
List(source:Array/List) -> Object:List
items.Add(value:Any) -> Unit
items.Insert(index:Number, value:Any) -> Unit
items.Item(index:Number) -> Any
items[index] = value
items.Set(index:Number, value:Any) -> Unit
items.Count() -> Integer
items.Contains(value:Any) -> Integer:1/0
items.IndexOf(value:Any) -> Integer:index/-1
items.Remove(value:Any) -> Integer:1/0
items.RemoveAt(index:Number) -> Unit
items.Clear() -> Unit
items.ToArray() -> Array
```

## パラメーター

- `source` — source：省略すると空になります。List は配列または List、Dictionary は Dictionary を受け取ります。外側の容器をコピーし、入れ子の参照は共有します。
- `index / key` — index / key：List の位置は 0 からの整数値です。Insert は Count() も許可します。Dictionary のキーは文字列または有限数です。数値 1 と 1.0 は同じキー、文字列 "1" は別です。
- `value` — value：初期化済み Basic 値です。配列やコレクションも含みます。Unit は保存できません。数値、大小文字を区別する文字列、配列／オブジェクトの参照同一性で比較します。
- `fallback` — fallback：キーがなければ Get はこの代替値を返し、挿入しません。fallback の式を含むすべての引数はメソッド呼び出し前に評価します。

## 戻り値

生成は Object:List を返します。Item／添字は格納値、Count は要素数、IndexOf は 0 からの位置または -1 を返します。Contains/Remove は 1=TRUE または 0=FALSE、Add/Insert/Set/RemoveAt/Clear は Unit、ToArray は新しい Array を返します。

## 動作

- Add は末尾に追加、Insert は位置の前に挿入、Set／添字代入は既存要素を置換します。Item／添字は読み取りです。Remove は最初の等しい値、RemoveAt は指定位置、Clear は全要素を削除します。
- Contains は存在確認、IndexOf は最初の一致位置を検索します。負数、小数、文字列、範囲外の添字は捕捉可能なエラーとなり、リストは変わりません。
- For Each は順序を保ちます。ToArray は浅いスナップショットです。元のリストを変更しながら処理する場合はこちらを反復してください。
- 直接 For Each 中に Set を含む変更を行うと、次のステップで捕捉可能なエラーになります。Try/Finally は通常どおり終了処理します。失敗した変更は元のデータを保ちます。
- 別名と ByVal 引数はコレクションを共有します。コピーやスナップショットは外側だけを複製します。添字付き ByRef と複合代入は容器／キーを一度評価し、変数を置換しても書き戻し先は変わりません。
- ローカルのスクリプトデータです。メソッドはゲーム内アイテムを動かさず、ネットワークも使いません。一つの要素として格納したスタックは一つの位置を占めます。

## 使用例

### 1. リストの作成と合計

```vb
# Add で [3,7]、Insert(1,5) で [3,5,7]、Set(0,2) で [2,5,7] になります。For Each が三つの値を合計します。Main は Integer 14 を返します。
Option Explicit On
Sub Main()
    Var items = List()
    items.Add(3)
    items.Add(7)
    items.Insert(1, 5)
    items.Set(0, 2)
    Var total = 0
    For Each item In items
        total += item
    Next
    Return total
End Sub
```

**パラメーターと実行の説明:**

Add で [3,7]、Insert(1,5) で [3,5,7]、Set(0,2) で [2,5,7] になります。For Each が三つの値を合計します。Main は Integer 14 を返します。

### 2. 独立したコピーとスナップショット

```vb
# seed=[4,6]。copied と snapshot は値を保持します。元は [9,6] になり、Remove(6) は TRUE=1、RemoveAt(0) で空、Clear でも空です。Main は 4*100+6*10+1+0、Integer 461 を返します。
Option Explicit On
Sub Main()
    Dim seed[1]
    seed[0] = 4
    seed[1] = 6
    Var items = List(seed)
    Var copied = List(items)
    Var snapshot = items.ToArray()
    items[0] = 9
    Var removed = items.Remove(6)
    items.RemoveAt(0)
    items.Clear()
    Return snapshot[0]*100 + copied[1]*10 + removed + items.Count()
End Sub
```

**パラメーターと実行の説明:**

seed=[4,6]。copied と snapshot は値を保持します。元は [9,6] になり、Remove(6) は TRUE=1、RemoveAt(0) で空、Clear でも空です。Main は 4*100+6*10+1+0、Integer 461 を返します。

### 3. 検索と ByRef による変更

```vb
# NextIndex は一度だけ実行され、calls=1、添字は 0。Bump が 5 を 6 にします。Contains(6)=TRUE、IndexOf(6)=0、Item(0) は 6。Main は Integer 601 を返します。
Option Explicit On
Function NextIndex(ByRef calls)
    calls += 1
    Return 0
End Function
Sub Bump(ByRef value)
    value += 1
End Sub
Sub Main()
    Var items = List()
    items.Add(5)
    Var calls = 0
    Bump(items[NextIndex(calls)])
    If items.Contains(6) AndAlso items.IndexOf(6) = 0 Then
        Return items.Item(0)*100 + calls
    End If
    Return -1
End Sub
```

**パラメーターと実行の説明:**

NextIndex は一度だけ実行され、calls=1、添字は 0。Bump が 5 を 6 にします。Contains(6)=TRUE、IndexOf(6)=0、Item(0) は 6。Main は Integer 601 を返します。

<!-- implementation references (not callable script procedures):
Runtime/ObjectTypes/ListObject.cs: registered methods
Runtime/ObjectTypes/IndexedCollectionObject.cs: CollectionArguments
Runtime/IndexedValueSlot.cs: Read / Write
Runtime/ForScope.cs: enumeration lifetime
https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.list-1?view=net-8.0
-->
