# +, -, *, /, MOD

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: fr -->

Une expression arithmétique calcule une valeur : + additionne, - soustrait ou change le signe, * multiplie, / divise, MOD donne le reste entier. Affectez le résultat à une variable ou renvoyez-le avec RETURN.

## Syntaxe exacte

```text
left + right
left - right
-right
left * right
left / right
left MOD right
(expression)
```

## Paramètres

- `left` — Opérande numérique gauche : littéral, variable déclarée, expression entre parenthèses ou résultat de fonction. Le moins unaire ne possède pas cet opérande.
- `right` — Opérande numérique droit. Pour /, il est le diviseur. Pour MOD, sa conversion en Integer doit rester non nulle : 0.5 devient 0 et provoque une erreur.
- `operator / precedence` — Priorité : moins unaire, puis * / MOD au même niveau de gauche à droite, puis + - binaires de gauche à droite. Les parenthèses modifient cet ordre. Le plus unaire, la puissance ^ et la division entière par barre oblique inverse ne sont pas pris en charge.

## Retour

Integer pour +, -, * et le moins unaire sur des entiers ; Decimal si un opérande numérique est Decimal. / renvoie toujours Decimal : 5/2=2.5. MOD renvoie Integer. Ce nombre ne représente une réussite ou un nombre d’objets que si le script lui donne ce sens.

## Comportement

- MOD convertit les opérandes en entiers signés sur 32 bits, en tronquant les fractions représentables vers zéro. Le reste conserve le signe du dividende : -17 MOD 5=-2 ; -2147483648 MOD -1=0. La casse, même mOd, ne change rien.
- MOD par zéro déclenche une erreur interceptable par TRY/CATCH. / utilise la division flottante : un numérateur non nul divisé par zéro donne Infinity avec son signe, et 0/0 donne NaN. Vérifiez le diviseur si un résultat fini est nécessaire.
- Les opérations entières +, -, * et la négation débordent sur 32 bits sans élargissement automatique. Convertissez un opérande en Decimal avant un grand calcul si une approximation convient ; les calculs flottants comportent des arrondis binaires.
- Les opérateurs numériques ordinaires ne convertissent pas automatiquement le texte. String+String concatène, String+Integer échoue. Convertissez explicitement, par exemple avec CDbl. MOD infixe analyse le texte entier plus strictement que la fonction BasicMod.
- L’évaluateur calcule les opérandes dans l’ordre de l’expression, sélectionne le jeton opérateur et crée une InjectionValue. Une expression entre parenthèses se termine d’abord. Aucun déplacement, délai ou appel réseau n’a lieu sauf si un opérande appelle une API correspondante.

## Exemples

### 1. Priorité et parenthèses

```vb
# plain=2+3*4 effectue d’abord la multiplication et vaut 14. grouped=(2+3)*4 vaut 20. Main renvoie plain*100+grouped=1420 pour vérifier les deux résultats.
Option Explicit On
SUB Main()
    VAR plain = 2 + 3 * 4
    VAR grouped = (2 + 3) * 4
    RETURN plain * 100 + grouped
END SUB
```

**Explication des paramètres et du déroulement:**

plain=2+3*4 effectue d’abord la multiplication et vaut 14. grouped=(2+3)*4 vaut 20. Main renvoie plain*100+grouped=1420 pour vérifier les deux résultats.

### 2. Lots complets et objets restants

```vb
# DescribeBatches reçoit total=27 et size=5. La garde rejette une taille nulle ou négative. Fix(total/size) transforme 5.4 en 5 lots ; total mOd size donne 2 objets restants. CStr permet de renvoyer le texte "5:2". La fonction auxiliaire est entièrement définie.
Option Explicit On
FUNCTION DescribeBatches(total, size)
    IF size <= 0 THEN
        RETURN "invalid"
    END IF
    VAR whole = Fix(total / size)
    VAR remaining = total mOd size
    RETURN CStr(whole) + ":" + CStr(remaining)
END FUNCTION
SUB Main()
    RETURN DescribeBatches(27, 5)
END SUB
```

**Explication des paramètres et du déroulement:**

DescribeBatches reçoit total=27 et size=5. La garde rejette une taille nulle ou négative. Fix(total/size) transforme 5.4 en 5 lots ; total mOd size donne 2 objets restants. CStr permet de renvoyer le texte "5:2". La fonction auxiliaire est entièrement définie.

### 3. Intercepter un diviseur invalide

```vb
# 10 MOD 0 déclenche une erreur avant d’affecter unusedResult. CATCH la stocke dans problem et définit caught=TRUE. Main renvoie 1 : indicateur de traitement d’erreur de l’exemple, pas résultat du MOD échoué.
Option Explicit On
SUB Main()
    VAR caught = FALSE
    TRY
        VAR unusedResult = 10 MOD 0
    CATCH problem
        caught = TRUE
    END TRY
    RETURN caught
END SUB
```

**Explication des paramètres et du déroulement:**

10 MOD 0 déclenche une erreur avant d’affecter unusedResult. CATCH la stocke dans problem et définit caught=TRUE. Main renvoie 1 : indicateur de traitement d’erreur de l’exemple, pas résultat du MOD échoué.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: signedOperand / additiveOperand / comparativeOperand
Runtime/Interpreter.cs: VisitSignedOperand / VisitAdditiveOperand / VisitComparativeOperand
Runtime/InjectionValue.cs: arithmetic operators
Runtime/NumberConversions.cs: ToInt
-->
