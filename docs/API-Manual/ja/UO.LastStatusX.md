# UO.LastStatusX

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: ja -->

最後に状態を受理した物体の保存済み X 座標を返します。

## 正確な構文

```text
UO.LastStatusX() -> Integer
```

## パラメーター

引数はありません。

## 戻り値

Integer — 保存済みの X 座標。状態ウィンドウの画素や Boolean ではありません。初回受理前とワールド消去後は0ですが、実際の座標0も有効です。記録の有無は UO.LastStatus() で確認します。

## 動作

- 引数はありません。読み取りはパケット送信、ウィンドウ表示、応答待機を行いません。UO.GetStatus(id)、RequestStats、UpdateObject はデータ要求であり、送信時点では LastStatus を変更しません。
- 受理した0x11パケットは serial と既知の X/Y をスクリプト共通の World に保存します。不明・破棄済み物体や不完全な基本パケットは記録を置き換えません。後から別の物体の状態で置き換わる場合があります。
- X/Y は受理時の Entity の座標であり、現在位置ではありません。mobile ではワールドのマスですが、容器内のアイテムでは内容物の座標の場合があります。状態パケット自体に X/Y はありません。後の移動・削除では変わらず、World.Clear でリセットします。現存物体の現在位置には GetX/GetY を使います。
- 別々の呼び出しは不可分の取得ではなく、その間に更新が入ります。同じ serial でも自分の要求への新しい応答とは限りません。括弧なしの laststatus は動的な組み込み値ですが、同名の変数で隠せます。UO.LastStatus() は登録された関数です。

### 内部関数：呼び出しから結果まで

実際の C# 内部処理を示します。ReadSavedStatus は例に完全な定義を含む補助関数で、隠れた組み込み命令ではありません。

#### 1. CharacterStatus

CharacterStatus は基本パケットと Entity を World.Get で検証し、状態と serial/X/Y を保存します。位置は状態パケットではなく Entity から読みます。

Integer — 保存済みの X 座標。状態ウィンドウの画素や Boolean ではありません。初回受理前とワールド消去後は0ですが、実際の座標0も有効です。記録の有無は UO.LastStatus() で確認します。

プロジェクトのソース: `src/ClassicUO.Client/Network/PacketHandlers.cs`; 関数 `CharacterStatus`.

#### 2. LastStatusX

ExecuteStealthCompatibility は bridge の serial を Integer として返します。LastStatusX/LastStatusY は IStatusSnapshotBridge を使います。このインターフェースを持たない古い外部 bridge では GetX/GetY による取得を保ちます。

Integer — 保存済みの X 座標。状態ウィンドウの画素や Boolean ではありません。初回受理前とワールド消去後は0ですが、実際の座標0も有効です。記録の有無は UO.LastStatus() で確認します。

プロジェクトのソース: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; 関数 `LastStatusX`.

#### 3. Invoke

Invoke はキャンセルを確認しながらゲームスレッドで World を読みます。ネットワーク応答を待たず、状態を変更しません。

引数はありません。読み取りはパケット送信、ウィンドウ表示、応答待機を行いません。UO.GetStatus(id)、RequestStats、UpdateObject はデータ要求であり、送信時点では LastStatus を変更しません。

プロジェクトのソース: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; 関数 `Invoke`.

#### 4. Clear

Clear は serial と両座標を0にします。実行中スクリプトを保持する消去でも同様です。

X/Y は受理時の Entity の座標であり、現在位置ではありません。mobile ではワールドのマスですが、容器内のアイテムでは内容物の座標の場合があります。状態パケット自体に X/Y はありません。後の移動・削除では変わらず、World.Clear でリセットします。現存物体の現在位置には GetX/GetY を使います。

プロジェクトのソース: `src/ClassicUO.Client/Game/World.cs`; 関数 `Clear`.

別々の呼び出しは不可分の取得ではなく、その間に更新が入ります。同じ serial でも自分の要求への新しい応答とは限りません。括弧なしの laststatus は動的な組み込み値ですが、同名の変数で隠せます。UO.LastStatus() は登録された関数です。


## 使用例

### 最後の値を読む

```vb
# 最後の値を読む
#
# 最後に状態を受理した物体の保存済み X 座標を返します。
#
# Integer — 保存済みの X 座標。状態ウィンドウの画素や Boolean ではありません。初回受理前とワールド消去後は0ですが、実際の座標0も有効です。記録の有無は
# UO.LastStatus() で確認します。

SUB Main()
    # 一度だけ読みます。HEX は serial を16進数で、CStr は座標を数字で表示します。物体は選択しません。

    VAR value = UO.LastStatusX()
    UO.Print('Saved value: ' + CStr(value))
END SUB
```

**パラメーターと実行の説明:**

- 一度だけ読みます。HEX は serial を16進数で、CStr は座標を数字で表示します。物体は選択しません。

### 状態を要求して既知の情報を読む

```vb
# 状態を要求して既知の情報を読む
#
# 最後に状態を受理した物体の保存済み X 座標を返します。
#
# Integer — 保存済みの X 座標。状態ウィンドウの画素や Boolean ではありません。初回受理前とワールド消去後は0ですが、実際の座標0も有効です。記録の有無は
# UO.LastStatus() で確認します。

SUB Main()
    # subject は self の serial です。500 は例示の待機ミリ秒数であり、応答を保証しません。表示値は古い記録や別の物体の場合があります。

    VAR subject = UO.Self()
    IF subject <> 0 THEN
        UO.GetStatus(subject)
        WAIT(500)
        VAR value = UO.LastStatusX()
        UO.Print('Known value: ' + CStr(value))
    END IF
END SUB
```

**パラメーターと実行の説明:**

- subject は self の serial です。500 は例示の待機ミリ秒数であり、応答を保証しません。表示値は古い記録や別の物体の場合があります。

### 完全な ReadSavedStatus 補助関数

```vb
# 完全な ReadSavedStatus 補助関数
#
# 最後に状態を受理した物体の保存済み X 座標を返します。
#
# Integer — 保存済みの X 座標。状態ウィンドウの画素や Boolean ではありません。初回受理前とワールド消去後は0ですが、実際の座標0も有効です。記録の有無は
# UO.LastStatus() で確認します。

SUB Main()
    # expectedId は Main で保存した serial です。補助関数を下に完全定義しています。-1 は対象の記録が変わったことを示し、API
    # 自体の戻り値ではありません。前後の確認で物体の混在を減らせますが、同じ serial の更新では不可分性を保証できません。

    VAR expectedId = UO.LastStatus()
    IF expectedId <> 0 THEN
        VAR value = ReadSavedStatus(expectedId)
        UO.Print('Checked value: ' + CStr(value))
    END IF
END SUB

SUB ReadSavedStatus(expectedId)
    IF expectedId = 0 OR UO.LastStatus() <> expectedId THEN
        RETURN -1
    END IF
    VAR value = UO.LastStatusX()
    IF UO.LastStatus() <> expectedId THEN
        RETURN -1
    END IF
    RETURN value
END SUB
```

**パラメーターと実行の説明:**

- expectedId は Main で保存した serial です。補助関数を下に完全定義しています。-1 は対象の記録が変わったことを示し、API 自体の戻り値ではありません。前後の確認で物体の混在を減らせますが、同じ serial の更新では不可分性を保証できません。
