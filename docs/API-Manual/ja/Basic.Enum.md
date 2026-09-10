# Enum / End Enum

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ja -->

Enum はスクリプトの状態やモードを表す名前付き Integer 定数をまとめます。ファイルまたは Module レベルに宣言し、Sub/Function 内には置けません。VB.NET 列挙の一部を実装したもので、.NET Enum オブジェクトは生成しません。

## 正確な構文

```text
[Public | Private] Enum name [As Integer]
    member [= constantExpression]
    ...
End Enum
Dim state As name = name.member
ModuleName.name.member
```

## パラメーター

- `Public / Private` — 既定は Public で、Module 内も同じです。Private は Module 内だけで使用でき、型とメンバーを他のモジュールやファイルのスコープから隠します。
- `name` — Mode のようなドットを含まない単純な名前を使います。大文字小文字は区別しません。UO と組み込み型名は予約済みで、完全名を Enum、Module、グローバル変数と重複させることはできません。
- `As Integer` — 省略可能。基底型は符号付き 32 ビット Integer、-2147483648..2147483647 のみです。他の型は拒否されます。変数・引数・Function 戻り値の As Mode は通常の Integer 保存と変換を使い、列挙された値だけに制限しません。未初期化の場合は 0 です。
- `member` — 1 行に単純なメンバー名を 1 つ、最低 1 メンバー必要です。同名、True、False は不可。式を省略した最初の値は 0、以後は直前の値に 1 を加えます。異なる名前が同じ値を持つことは可能です。
- `constantExpression` — 省略可能な定数式：10 進/0x 整数、括弧、単項マイナス、+ - * / Mod、先行メンバー、宣言済みの数値 Const。最終値は範囲内の整数である必要があり、中間の除算には小数を使用できます。参照 Const も Integer を算出し、型なしまたは As Integer/Long/Short/Byte に限ります。関数呼び出し、変数、文字列、比較、配列参照は不可。前方参照、依存関係の循環、128 階層を超える依存は拒否されます。
- `name.member` — Mode.Ready で読み、モジュール外では Tools.Mode.Ready を使います。Tools 内なら Mode.Ready、With Mode 内なら .Ready が使えます。代入、+=、ByRef の書き戻しで定数は変更できません。Enum 型は関数として呼び出せません。

## 戻り値

宣言自体に戻り値も呼び出し括弧もありません。メンバー参照は Integer（例：Mode.Working = 3）を返します。状態値であり、自動的な成功フラグではありません。state = Mode.Finished の Boolean 比較は 1/True または 0/False を返し、両表記が利用できます。状態 0 は失敗ではなく Idle の場合があります。

## 動作

- 準備時に EnumCatalog はスクリプト/API を実行せず、先行定数を計算して連番を付け、名前・アクセス・範囲を検査します。SC026 は Option Explicit がなくても起動を止めます。構文エラーも実行を止め、編集途中の宣言は診断を返します。
- DefinitionCollector はグローバル初期化と Optional 既定値より前に不変メンバーを登録するため、そこではファイル後方の Enum を参照できます。Enum 内の定数式では引き続き先行定数のみが使えます。準備済みスクリプトは固定カタログを保持し、別スクリプトの読み込みで置き換えます。
- ScriptBindings はモジュール相対名と Private を一度だけ解決します。実行時は普通の定数読み取りで、ループでの再計算やリフレクションはありません。As Mode は Integer に正規化され、デバッガーにも Integer と表示される場合があります。Include から宣言を読み込めます。Flags 属性、System.Enum メソッド、暗黙のメンバーインポート、自動メンバー一覧はありません。

## 使用例

### 1. 状態に名前を付ける

```vb
# Idle=0、Queued=1 は自動です。Working=10 が連番を変えるので Finished=11。state As TaskState は 10 を受け取ります。Main は CStr で数値を文字列にし、String "0:1:10:11" を返します。名前は自分の状態名に変えられます。宣言だけでは処理は始まりません。
Option Explicit On
Enum TaskState As Integer
    Idle
    Queued
    Working = 10
    Finished
End Enum

Sub Main()
    Dim state As TaskState = TaskState.Working
    Return CStr(TaskState.Idle) & ":" & CStr(TaskState.Queued) & ":" & CStr(state) & ":" & CStr(TaskState.Finished)
End Sub
```

**パラメーターと実行の説明:**

Idle=0、Queued=1 は自動です。Working=10 が連番を変えるので Finished=11。state As TaskState は 10 を受け取ります。Main は CStr で数値を文字列にし、String "0:1:10:11" を返します。名前は自分の状態名に変えられます。宣言だけでは処理は始まりません。

### 2. モジュールの状態を隠す

```vb
# Controller.Mode は Controller 内専用です。NextMode の distance は ByVal As Integer で、呼び出し元の引数を変更しません。distance<=1 なら Arrived=5、それ以外は Walking=4。state の初期値は 0。Main は 3 と 1 を渡し、4 と 5 を得て Integer 45 を返します。キャラクターは移動せず、distance は例の入力です。外部から Controller.NextMode は使えますが Controller.Mode.Arrived は読めません。
Option Explicit On
Module Controller
    Private Enum Mode
        Idle
        Walking = 4
        Arrived
    End Enum

    Public Function NextMode(ByVal distance As Integer) As Integer
        Dim state As Mode
        If distance <= 1 Then
            state = Mode.Arrived
        Else
            state = Mode.Walking
        End If
        Return state
    End Function
End Module

Sub Main()
    Dim farState = Controller.NextMode(3)
    Dim nearState = Controller.NextMode(1)
    Return farState * 10 + nearState
End Sub
```

**パラメーターと実行の説明:**

Controller.Mode は Controller 内専用です。NextMode の distance は ByVal As Integer で、呼び出し元の引数を変更しません。distance<=1 なら Arrived=5、それ以外は Walking=4。state の初期値は 0。Main は 3 と 1 を渡し、4 と 5 を得て Integer 45 を返します。キャラクターは移動せず、distance は例の入力です。外部から Controller.NextMode は使えますが Controller.Mode.Arrived は読めません。

### 3. 状態を進めて Boolean を返す

```vb
# 先行 Integer Const の FirstState=2 により Idle=2、Working=3、Finished=4。Advance は state を ByRef で受け取り Main の変数を変更します。With Mode で名前を短縮し、Select Case で遷移を選びます。2 回で 2→3→4。IsFinal は ByVal のコピーを Finished と比較するので Main は 1/True を返します。1 回だけなら 0/False。さらに Advance を呼ぶと "No next state" エラーになり、Mode 定数は変わりません。
Option Explicit On
Const FirstState As Integer = 2
Enum Mode
    Idle = FirstState
    Working = Idle + 1
    Finished
End Enum

Sub Advance(ByRef state As Mode)
    With Mode
        Select Case state
            Case .Idle
                state = .Working
            Case .Working
                state = .Finished
            Case Else
                Throw "No next state"
        End Select
    End With
End Sub

Function IsFinal(ByVal state As Mode) As Boolean
    Return state = Mode.Finished
End Function

Sub Main()
    Dim state As Mode = Mode.Idle
    Advance(state)
    Advance(state)
    Return IsFinal(state)
End Sub
```

**パラメーターと実行の説明:**

先行 Integer Const の FirstState=2 により Idle=2、Working=3、Finished=4。Advance は state を ByRef で受け取り Main の変数を変更します。With Mode で名前を短縮し、Select Case で遷移を選びます。2 回で 2→3→4。IsFinal は ByVal のコピーを Finished と比較するので Main は 1/True を返します。1 回だけなら 0/False。さらに Advance を呼ぶと "No next state" エラーになり、Mode 定数は変わりません。

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: enumDeclaration / enumMember
Runtime/EnumCatalog.cs: Build / Observe / Reference / Evaluate
Runtime/DefinitionCollector.cs: VisitFile / VisitEnumDeclaration
Runtime/ScriptBindings.cs: Variable / VisitTypeClause / VisitWithStatement
Runtime/SemanticScope.cs: DefineGlobalVariables / SetVar
Runtime/Metadata.cs: NormalizeType
-->
