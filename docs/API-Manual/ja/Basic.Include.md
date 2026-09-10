# Include

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ja -->

Include は解析と実行の前に別のソースファイルを読み込みます。関数や変数を主スクリプトで利用できますが、手続きやスレッドは自動的に起動しません。

## 正確な構文

```text
Include "fileName"
```

## パラメーター

- `fileName` — fileName：一重または二重引用符で囲む空でないファイル名。相対・絶対パスを使用できます。変数や式ではなくリテラルのパスです。拡張子は任意ですが、内容はこのエンジンの対応言語で記述します。

## 戻り値

戻り値はありません。ソース準備用の指示であり、Include(...) の代入や ID、TRUE/FALSE、1/0 の取得はできません。読み込んだ関数は RETURN で独自の値を返します。

## 動作

- SUB/FUNCTION の外で Include を独立した行に記述します。読み込み元と同じフォルダー、その Include 子フォルダーの順に検索します。入れ子のパスは現在のライブラリーが基準です。相対パス使用前に主ファイルを保存します。
- 同じ完全パスは準備ごとに一度読み込みます。A → B → A の循環は SC016 です。パス・アクセス・構文エラーはグローバル初期化前に実行を止めます。診断とデバッガーは元ファイルと行番号を保持します。
- 文字列リテラルと SUB/FUNCTION は開始したファイル内で閉じてください。グローバル変数や定数の重複宣言は実行前に SC017 となります。
- 次回起動時にライブラリーの変更を読み込みます。準備済み・実行中のスクリプトはコードのスナップショットを保持します。プロファイルのコピーや別スクリプトの起動はしません。
- 各ファイルは自分の宣言前に Option Explicit を指定できます。省略時は主ファイルの設定を継承します。宣言は名前空間を共有し、モジュールは自動生成しません。
- UTF-8 で読み、BOM を認識します。上限は主ファイル込みで 128 ファイル、入れ子 32 階層、ソース文字数 16,777,216 です。コメントや文字列内の Include は読み込みません。
- 各例は別フォルダーです。Main.bas と表示されたすべてのファイルを指定名・子フォルダーで保存します。完成例は API Manual/Examples/Basic.Include/1、/2、/3 にあります。全内容を結合せず Main.bas を実行してください。

## 使用例

### 1. 共通関数

```vb
# Main.bas は Common.bas を読み Add(4, 7) を呼びます。left と right は値渡しで、Add は和、Main は Integer 11 を返します。Common.bas は単独で起動しません。
Option Explicit On
Include "Common.bas"
SUB Main()
    RETURN Add(4, 7)
END SUB
```

**パラメーターと実行の説明:**

Main.bas は Common.bas を読み Add(4, 7) を呼びます。left と right は値渡しで、Add は和、Main は Integer 11 を返します。Common.bas は単独で起動しません。

**Common.bas**

```vbnet
Option Explicit On
FUNCTION Add(ByVal left, ByVal right)
    RETURN left + right
END FUNCTION
```

### 2. 入れ子のライブラリー

```vb
# Main.bas は lib/Route.bas を読み、後者は自分の lib フォルダーから Math.bas を読みます。Distance(-3, 5) は dx=-3、dy=5 を Manhattan に渡します。Abs が符号を除き合計は Integer 8 です。キャラクターの移動は行いません。
Option Explicit On
Include "lib/Route.bas"
SUB Main()
    RETURN Distance(-3, 5)
END SUB
```

**パラメーターと実行の説明:**

Main.bas は lib/Route.bas を読み、後者は自分の lib フォルダーから Math.bas を読みます。Distance(-3, 5) は dx=-3、dy=5 を Manhattan に渡します。Abs が符号を除き合計は Integer 8 です。キャラクターの移動は行いません。

**lib/Route.bas**

```vbnet
Option Explicit On
Include "Math.bas"
FUNCTION Distance(ByVal dx, ByVal dy)
    RETURN Manhattan(dx, dy)
END FUNCTION
```

**lib/Math.bas**

```vbnet
Option Explicit On
FUNCTION Manhattan(ByVal dx, ByVal dy)
    RETURN Abs(dx) + Abs(dy)
END FUNCTION
```

### 3. 重複読み込み

```vb
# Common.bas と ./Common.bas は同一ファイルなので CONST と関数は一度だけ宣言されます。SharedValue=7、GetShared() は 7 を返し、Main は 2 倍の Integer 14 を返します。両ファイルで Option Explicit On を使用します。
Option Explicit On
Include "Common.bas"
Include "./Common.bas"
SUB Main()
    RETURN GetShared() * 2
END SUB
```

**パラメーターと実行の説明:**

Common.bas と ./Common.bas は同一ファイルなので CONST と関数は一度だけ宣言されます。SharedValue=7、GetShared() は 7 を返し、Main は 2 倍の Integer 14 を返します。両ファイルで Option Explicit On を使用します。

**Common.bas**

```vbnet
Option Explicit On
CONST SharedValue = 7
FUNCTION GetShared()
    RETURN SharedValue
END FUNCTION
```

<!-- implementation references (not callable script procedures):
Parsing/ScriptSourceGraph.cs: Load / Builder.AddInclude / ResolveLine
Runtime/InjectionRuntime.cs: Prepare / Load
Runtime/Interpreter.cs: Location / EvaluateInitializer / CallObserved
Analysis/SanityAnalyzer.cs: Analyze
ClassicUO.Client/Game/Managers/YokoInjectionManager.cs: PrepareScriptForExecution
InjectionScript.Lsp/Workspace.cs: UpdateDiagnostic
-->
