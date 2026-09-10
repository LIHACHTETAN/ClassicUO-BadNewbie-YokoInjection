# 123 / 0x0EED / "text" / TRUE

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: en -->

A literal writes a value directly in source code. Numbers and quoted text do not require declarations. TRUE and FALSE are predefined logical values. A quoted number remains text until an explicit or declared conversion changes it.

## Exact syntax

```text
123
-2147483648
0x0EED
0xFFFFFFFF
2.5
"text"
'text'
TRUE
FALSE
```

## Parameters

- `integer / hexadecimal` — Decimal Integer from -2147483648 to 2147483647, or 0x followed by hexadecimal digits 0–9/A–F. Use the lowercase x prefix. A hexadecimal literal represents 32 bits: 0xFFFFFFFF is Integer -1, not a positive 64-bit number.
- `floating` — Floating number with digits before and after a dot, for example 2.5 or -0.25. Use 0.5 rather than .5. A comma, exponent notation such as 1e3, and suffixes on numeric literals are not supported by this source grammar.
- `text` — Text enclosed in matching single or double quotes. Use the other quote style to include a quote, or Chr(34)/Chr(39) when building text. Backslash escape sequences and doubled-quote escaping are not interpreted. Keep an example string on one physical line.
- `TRUE / FALSE` — TRUE is Integer 1 and FALSE is Integer 0. Do not redeclare these predefined names. They are values, not calls: use TRUE, not TRUE().

## Returns

Evaluating an integer/hexadecimal literal gives Integer; a dotted number gives Decimal (binary floating point); quoted text gives String. TRUE/FALSE give Integer 1/0. Evaluating a value does not perform a game action or declare a variable.

## Behavior

- The sign in -5 is a unary operation. The engine handles -2147483648 as the minimum signed Integer without first requiring its positive magnitude to fit. Out-of-range integer literals fail; use an appropriate floating value when a calculation genuinely needs a larger approximate number.
- Text preserves its characters and case. "350" is not the number 350 and "false" is not FALSE. # and ; inside quotes are text; outside quotes they begin comments. AS and conversion functions have their own rules, described in AS and their command cards.
- The lexer recognizes the literal token. Number evaluation parses decimal/hexadecimal integers or floating text with invariant culture; string evaluation removes the surrounding quotes. Changing the IDE language does not change the decimal separator in source code.
- Game APIs may distinguish a serial, a graphic type and a coordinate even when all are represented numerically. The literal alone supplies no such meaning: the called command’s parameter contract decides what it represents.

## Examples

### 1. Hexadecimal type and integer boundary

```vb
# itemType=0x0EED equals decimal 3821. lowest=-2147483648 equals the signed bit pattern 0x80000000. The comparison succeeds and Main returns itemType=3821. This only checks values; it does not search for an item.
Option Explicit On
SUB Main()
    VAR itemType = 0x0EED
    VAR lowest = -2147483648
    IF lowest = 0x80000000 THEN
        RETURN itemType
    END IF
    RETURN 0
END SUB
```

**Parameter and execution notes:**

itemType=0x0EED equals decimal 3821. lowest=-2147483648 equals the signed bit pattern 0x80000000. The comparison succeeds and Main returns itemType=3821. This only checks values; it does not search for an item.

### 2. Both quote styles

```vb
# owner="O'Brien" contains an apostrophe. instruction uses single quotes around text containing double quotes. Joining owner, " | " and instruction returns O'Brien | say "go". No escape backslashes are needed in this script.
Option Explicit On
SUB Main()
    VAR owner = "O'Brien"
    VAR instruction = 'say "go"'
    RETURN owner + " | " + instruction
END SUB
```

**Parameter and execution notes:**

owner="O'Brien" contains an apostrophe. instruction uses single quotes around text containing double quotes. Joining owner, " | " and instruction returns O'Brien | say "go". No escape backslashes are needed in this script.

### 3. Logical values are numeric

```vb
# enabled=TRUE stores 1 and stopped=FALSE stores 0. Multiplication and addition produce 1*10+0=10. Main returns that number; 10 itself is a count/calculation result, not the canonical Boolean TRUE.
Option Explicit On
SUB Main()
    VAR enabled = TRUE
    VAR stopped = FALSE
    RETURN enabled * 10 + stopped
END SUB
```

**Parameter and execution notes:**

enabled=TRUE stores 1 and stopped=FALSE stores 0. Multiplication and addition produce 1*10+0=10. Main returns that number; 10 itself is a count/calculation result, not the canonical Boolean TRUE.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: number / literal / HEX_NUMBER / DEC_NUMBER
Runtime/Interpreter.cs: VisitNumber / VisitLiteral / VisitSignedOperand
Runtime/InjectionApiUO.cs: TRUE / FALSE intrinsic values
-->
