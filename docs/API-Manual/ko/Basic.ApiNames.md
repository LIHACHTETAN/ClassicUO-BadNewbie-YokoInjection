# Basic / UO.

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: ko -->

게임 명령은 UO.를 사용하고 Basic 구문, 내장 함수와 사용자 함수는 선언된 이름을 사용합니다.

## 정확한 구문

```text
UO.command(arguments)
BasicFunction(arguments)
UserFunction(arguments)
```

## 매개변수

- `UO.command` — UO.command(arguments): 게임 API에 필수인 접두사입니다. UO.GetType(id)는 그래픽/몸체 번호를 읽으며 Basic 또는 CLR 형식이 아닙니다.
- `BasicFunction` — BasicFunction(arguments): Int(value), Str(value), CInt(value) 등에는 UO.를 붙이지 않습니다.
- `arguments` — self, backpack, ground, Rhand는 객체, 필터, 레이어 인수로 계속 유효합니다. 인수 이름은 접두사를 생략한 게임 호출이 아닙니다.

## 반환값

명명 규칙 자체는 값을 반환하지 않습니다. Int는 Integer, Str는 String, 세 Api*Exists는 TRUE/FALSE로 사용할 수 있는 Integer 1/0을 반환합니다.

## 동작

- 대소문자를 구분하지 않습니다. InjectionApi는 접두사 없는 Basic을, InjectionApiUO는 UO.가 있는 게임 호출을 등록합니다. 이전 짧은 호출에는 SC005와 등록된 UO. 대안이 표시되며 자동 실행하지 않습니다. 캐릭터 속성 값도 UO.가 필요합니다. ApiNameExists, ApiSignatureExists, ApiParameterExists는 양끝 공백을 제거하고 접두사를 추가하지 않은 정확한 등록 이름을 검사합니다. 서버 상태가 아닌 메타데이터 검사입니다. VB.NET 리플렉션 연산자 GetType(TypeName)은 구현되지 않았습니다.

## 예제

### 1. 1

```vb
# graphic은 몸체 번호를 읽고 정보가 없으면 0이며 whole=2입니다. registered는 인수 하나인 UO.GetType을 검사합니다. Main은 그래픽과 관계없이 "2:1"을 반환하며 이동하거나 아이템을 옮기지 않습니다.
Option Explicit On
Sub Main()
    Var graphic = UO.GetType('self')
    Var whole = Int(2.9)
    Var registered = UO.ApiSignatureExists('UO.GetType', 1)
    Return CStr(whole) + ":" + CStr(registered)
End Sub
```

**매개변수 및 실행 설명:**

graphic은 몸체 번호를 읽고 정보가 없으면 0이며 whole=2입니다. registered는 인수 하나인 UO.GetType을 검사합니다. Main은 그래픽과 관계없이 "2:1"을 반환하며 이동하거나 아이템을 옮기지 않습니다.

### 2. 2

```vb
# 전체 정의된 사용자 Function GetType은 CInt(6)에서 value=6을 받아 7을 반환합니다. UO.GetType은 게임 그래픽을 계속 읽으며 두 호출은 서로 가로채지 않습니다.
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

**매개변수 및 실행 설명:**

전체 정의된 사용자 Function GetType은 CInt(6)에서 value=6을 받아 7을 반환합니다. UO.GetType은 게임 그래픽을 계속 읽으며 두 호출은 서로 가로채지 않습니다.

### 3. 3

```vb
# oldCall=0, gameCall=1, basicCall=1은 GetType, UO.GetType(id), Int(value)를 검사합니다. argumentName=1은 backpack 인수가 유효함을 확인합니다. Main은 "0:1:1:1"을 반환합니다. 사용자 프로시저는 검색하지 않습니다.
Option Explicit On
Sub Main()
    Var oldCall = UO.ApiSignatureExists('GetType', 1)
    Var gameCall = UO.ApiSignatureExists('UO.GetType', 1)
    Var basicCall = UO.ApiSignatureExists('Int', 1)
    Var argumentName = UO.ApiParameterExists('backpack')
    Return CStr(oldCall) + ":" + CStr(gameCall) + ":" + CStr(basicCall) + ":" + CStr(argumentName)
End Sub
```

**매개변수 및 실행 설명:**

oldCall=0, gameCall=1, basicCall=1은 GetType, UO.GetType(id), Int(value)를 검사합니다. argumentName=1은 backpack 인수가 유효함을 확인합니다. Main은 "0:1:1:1"을 반환합니다. 사용자 프로시저는 검색하지 않습니다.

<!-- implementation references (not callable script procedures):
Runtime/InjectionApi.cs: Register
Runtime/InjectionApiUO.cs: Register / RegisterCharacterGetterAliases / ApiNameExists / ApiSignatureExists / ApiParameterExists
Analysis/InvalidSymbolVisitor.cs: VisitCall
Runtime/ScriptBindings.cs: Builder.CallName
-->
