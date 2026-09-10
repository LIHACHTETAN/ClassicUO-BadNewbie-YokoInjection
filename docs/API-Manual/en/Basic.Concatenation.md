# String + / &

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: en -->

Join text with + or the Basic compatibility spelling &. Convert numeric values explicitly with CStr before adding labels, quantities or coordinates to a message.

## Exact syntax

```text
leftText + rightText
leftText & rightText
"label" & CStr(number)
```

## Parameters

- `leftText` — Left text. It may be a literal, String variable or function result converted to text.
- `rightText` — Right text. CStr(number) converts a number; CStr(Unit) gives empty text. Supply separators such as spaces or colons yourself.

## Returns

String when both operands are String. No success flag is returned. In this engine & is normalized to + and inherits its rules: two numeric operands add numerically, so 2 & 3 gives Integer 5. Mixed String/number operands raise an error. This differs from implicit VB text conversion.

## Behavior

- Both sides are evaluated and joined in order. Chained joins associate left to right. Use parentheses around a numeric calculation and convert its result before concatenating it.
- No separators, spaces, quotation marks or newline characters are inserted automatically. & inside a quoted literal stays a literal ampersand. The logical token && remains AND and is not concatenation.
- CStr uses invariant numeric formatting, including a decimal point, regardless of the client language. The conversion and joins do not print or send anything; use the resulting String in a later API call if required.
- Strings are immutable: joining creates a new value and does not modify either source variable. Repeatedly growing a large string copies its content; build only the output needed rather than regenerating an entire report on every loop iteration.

## Examples

### 1. Add a quantity to a label

```vb
# amount=50 is Integer. CStr(amount) produces "50". The literal "Items: " includes a colon and a trailing space. Main returns "Items: 50"; nothing is printed automatically.
Option Explicit On
SUB Main()
    VAR amount = 50
    RETURN "Items: " & CStr(amount)
END SUB
```

**Parameter and execution notes:**

amount=50 is Integer. CStr(amount) produces "50". The literal "Items: " includes a colon and a trailing space. Main returns "Items: 50"; nothing is printed automatically.

### 2. Reusable complete formatter

```vb
# Label receives name="ore" and amount=3. It joins the name, an explicit colon and CStr(amount). The full helper returns "ore:3" to Main; it can be reused with other names and quantities.
Option Explicit On
FUNCTION Label(name, amount)
    RETURN name + ":" + CStr(amount)
END FUNCTION
SUB Main()
    RETURN Label("ore", 3)
END SUB
```

**Parameter and execution notes:**

Label receives name="ore" and amount=3. It joins the name, an explicit colon and CStr(amount). The full helper returns "ore:3" to Main; it can be reused with other names and quantities.

### 3. Calculate before joining

```vb
# CStr(2+3) calculates 5 first and converts it to "5". The second literal contains a semicolon, spaces and A&B; these characters are kept. Main returns "Total: 5; literal: A&B".
Option Explicit On
SUB Main()
    RETURN "Total: " & CStr(2 + 3) & "; literal: A&B"
END SUB
```

**Parameter and execution notes:**

CStr(2+3) calculates 5 first and converts it to "5". The second literal contains a semicolon, spaces and A&B; these characters are kept. Main returns "Total: 5; literal: A&B".

<!-- implementation references (not callable script procedures):
Runtime/BasicSyntaxPreprocessor.cs: ProtectLiteralText / ReplaceConcatenationOutsideLiterals
Runtime/InjectionValue.cs: operator + / explicit operator string
Runtime/InjectionApi.cs: CStr
-->
