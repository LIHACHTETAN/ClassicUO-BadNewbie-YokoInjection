# NOT / AND / OR / XOR

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ja -->

NOT は条件を反転します。AND は両方、OR は少なくとも一方、XOR は一方だけが成立するか調べます。&& は AND、|| は OR の別名です。キーワードの大文字小文字は区別しません。

## 正確な構文

```text
NOT (condition)
left AND right
left && right
left OR right
left || right
left XOR right
```

## パラメーター

- `left` — 二項演算の左条件。AND/OR は Integer または Decimal を要求し、ゼロは偽、非ゼロは真です。
- `right` — 右条件。AND/OR ではこちらも数値です。両オペランドを評価し、AND の左が偽、OR の左が真でも右を省略しません。
- `NOT / grouping` — NOT では反転する条件全体を括弧で囲みます。AND、OR、XOR の組み合わせは括弧で明確にグループ化します。

## 戻り値

Integer 1（TRUE）または Integer 0（FALSE）。ビット演算ではなく論理演算です。2 AND 4 はビットマスクではなく1です。結果フラグは =TRUE または =1、=FALSE または =0 で確認できます。

## 動作

- このエンジンでは AND、OR、XOR は同順位で左から評価します。TRUE OR FALSE AND FALSE は0、TRUE OR (FALSE AND FALSE) は1です。VB コードの移植時はこの互換規則に注意してください。
- NOT(condition) は条件を評価して真偽を反転します。比較の先頭にある NOT 1=2 は NOT(1=2) です。反転した値自体を比較オペランドにする場合は (NOT value) と書きます。
- AND/OR は String、Array、Object、Unit を受け付けません。従来の NOT と XOR は数値ゼロとの等値を調べるため、文字列 "0"、空文字列、配列、オブジェクト、Unit は非ゼロ扱いです。これらには明示的な数値条件を定義してください。CBool の変換規則は別です。
- 右の式は必ず実行され、関数、待機、エラーも発生します。括弧はグループだけを変え、評価を省略しません。前の条件が成立した場合だけ次を実行するには、入れ子の IF を使います。

## 使用例

### 1. 名前付きフラグの結合

```vb
# ready=TRUE、blocked=FALSE。NOT(blocked) は1なので canRun は1です。ready XOR blocked は片方だけ真なので真です。Main は canRun*10+exclusive=11 を返します。
Option Explicit On
SUB Main()
    VAR ready = TRUE
    VAR blocked = FALSE
    VAR canRun = ready AND (NOT blocked)
    VAR exclusive = ready XOR blocked
    RETURN canRun * 10 + exclusive
END SUB
```

**パラメーターと実行の説明:**

ready=TRUE、blocked=FALSE。NOT(blocked) は1なので canRun は1です。ready XOR blocked は片方だけ真なので真です。Main は canRun*10+exclusive=11 を返します。

### 2. 両方の呼び出しを観察

```vb
# Mark は ByRef 引数 counter を増やし TRUE を返します。Main は counter=0 で開始。FALSE AND Mark(counter) でも Mark を呼び、TRUE OR Mark(counter) でも再び呼びます。条件結果は0と1ですが Main は counter=2 を返します。Mark を全文掲載しています。
Option Explicit On
FUNCTION Mark(ByRef counter)
    counter = counter + 1
    RETURN TRUE
END FUNCTION
SUB Main()
    VAR counter = 0
    VAR first = FALSE AND Mark(counter)
    VAR second = TRUE OR Mark(counter)
    RETURN counter
END SUB
```

**パラメーターと実行の説明:**

Mark は ByRef 引数 counter を増やし TRUE を返します。Main は counter=0 で開始。FALSE AND Mark(counter) でも Mark を呼び、TRUE OR Mark(counter) でも再び呼びます。条件結果は0と1ですが Main は counter=2 を返します。Mark を全文掲載しています。

### 3. 明確なグループ化

```vb
# legacy は TRUE OR FALSE の後 AND FALSE を計算して0です。grouped は括弧内の FALSE AND FALSE の後 TRUE と OR を計算して1です。Main は legacy*10+grouped=1 を返します。
Option Explicit On
SUB Main()
    VAR legacy = TRUE OR FALSE AND FALSE
    VAR grouped = TRUE OR (FALSE AND FALSE)
    RETURN legacy * 10 + grouped
END SUB
```

**パラメーターと実行の説明:**

legacy は TRUE OR FALSE の後 AND FALSE を計算して0です。grouped は括弧内の FALSE AND FALSE の後 TRUE と OR を計算して1です。Main は legacy*10+grouped=1 を返します。

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: expression / logicalOperand / signedOperand
Runtime/Interpreter.cs: VisitExpression / VisitLogicalOperand / VisitSignedOperand
Runtime/InjectionValue.cs: operator & / operator | / Equals
-->
