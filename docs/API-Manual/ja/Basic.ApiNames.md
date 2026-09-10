# Basic / UO.

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ja -->

ゲームコマンドは UO. を使用し、Basic の構文・組み込み関数・自作関数は宣言された名前を使用します。

## 正確な構文

```text
UO.command(arguments)
BasicFunction(arguments)
UserFunction(arguments)
```

## パラメーター

- `UO.command` — UO.command(arguments)：ゲーム API に必須の接頭辞です。UO.GetType(id) は画像／身体番号を読み、Basic や CLR の型を返すものではありません。
- `BasicFunction` — BasicFunction(arguments)：Int(value)、Str(value)、CInt(value) などに UO. は付けません。
- `arguments` — self、backpack、ground、Rhand はオブジェクト・フィルター・レイヤー引数として有効です。引数名は省略形のコマンド呼び出しではありません。

## 戻り値

命名規則自体に戻り値はありません。Int は Integer、Str は String、3 種類の Api*Exists は TRUE/FALSE として扱える Integer 1/0 を返します。

## 動作

- 大文字と小文字は区別しません。InjectionApi は接頭辞なしの Basic、InjectionApiUO は UO. 付きのゲーム呼び出しを登録します。古い短縮呼び出しには SC005 と登録済み UO. 名の候補が表示され、自動実行はされません。属性値にも UO. が必要です。ApiNameExists、ApiSignatureExists、ApiParameterExists は前後の空白を除き、接頭辞を補わず正確な登録名を検査します。サーバー状態ではなくメタデータの検査です。VB.NET のリフレクション演算子 GetType(TypeName) は未実装です。

## 使用例

### 1. 1

```vb
# graphic は身体番号を読み、情報がなければ 0、whole は 2 です。registered は引数 1 個の UO.GetType を検査します。Main は画像に関係なく "2:1" を返し、移動や転送はしません。
Option Explicit On
Sub Main()
    Var graphic = UO.GetType('self')
    Var whole = Int(2.9)
    Var registered = UO.ApiSignatureExists('UO.GetType', 1)
    Return CStr(whole) + ":" + CStr(registered)
End Sub
```

**パラメーターと実行の説明:**

graphic は身体番号を読み、情報がなければ 0、whole は 2 です。registered は引数 1 個の UO.GetType を検査します。Main は画像に関係なく "2:1" を返し、移動や転送はしません。

### 2. 2

```vb
# 完全に定義した自作 Function GetType は CInt(6) の value=6 を受け取り 7 を返します。UO.GetType はゲームの画像番号を読み続け、互いの呼び出しを横取りしません。
Option Explicit On
Function GetType(value)
    Return value + 1
End Function
Sub Main()
    Var localResult = GetType(CInt(6))
    Var graphic = UO.GetType('self')
    Return localResult
End Sub
```

**パラメーターと実行の説明:**

完全に定義した自作 Function GetType は CInt(6) の value=6 を受け取り 7 を返します。UO.GetType はゲームの画像番号を読み続け、互いの呼び出しを横取りしません。

### 3. 3

```vb
# oldCall=0、gameCall=1、basicCall=1 は GetType、UO.GetType(id)、Int(value) を検査します。argumentName=1 は backpack が引数として有効であることを示します。Main は "0:1:1:1" を返します。自作プロシージャは検索しません。
Option Explicit On
Sub Main()
    Var oldCall = UO.ApiSignatureExists('GetType', 1)
    Var gameCall = UO.ApiSignatureExists('UO.GetType', 1)
    Var basicCall = UO.ApiSignatureExists('Int', 1)
    Var argumentName = UO.ApiParameterExists('backpack')
    Return CStr(oldCall) + ":" + CStr(gameCall) + ":" + CStr(basicCall) + ":" + CStr(argumentName)
End Sub
```

**パラメーターと実行の説明:**

oldCall=0、gameCall=1、basicCall=1 は GetType、UO.GetType(id)、Int(value) を検査します。argumentName=1 は backpack が引数として有効であることを示します。Main は "0:1:1:1" を返します。自作プロシージャは検索しません。

<!-- implementation references (not callable script procedures):
Runtime/InjectionApi.cs: Register
Runtime/InjectionApiUO.cs: Register / RegisterCharacterGetterAliases / ApiNameExists / ApiSignatureExists / ApiParameterExists
Analysis/InvalidSymbolVisitor.cs: VisitCall
Runtime/ScriptBindings.cs: Builder.CallName
-->
