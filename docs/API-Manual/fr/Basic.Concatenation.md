# String + / &

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: fr -->

Assembler du texte avec + ou la notation Basic compatible &. Convertir explicitement les nombres avec CStr avant de les ajouter à des libellés, quantités ou coordonnées.

## Syntaxe exacte

```text
leftText + rightText
leftText & rightText
"label" & CStr(number)
```

## Paramètres

- `leftText` — Texte gauche : littéral, variable String ou résultat de fonction converti en texte.
- `rightText` — Texte droit. CStr(number) convertit un nombre ; CStr(Unit) donne un texte vide. Fournir soi-même espaces, deux-points et autres séparateurs.

## Retour

String si les deux opérandes sont String, sans indicateur de réussite. Ici & est normalisé en + et en hérite les règles : deux nombres s’additionnent, donc 2 & 3 donne Integer 5. Mélanger String et nombre provoque une erreur. Cela diffère de la conversion implicite de VB.

## Comportement

- Les deux côtés sont évalués et assemblés dans l’ordre ; les chaînes d’opérations vont de gauche à droite. Calculer une expression numérique entre parenthèses puis convertir son résultat avant de la joindre.
- Aucun séparateur, espace, guillemet ou saut de ligne n’est ajouté automatiquement. & dans un littéral reste une esperluette. Le jeton logique && reste AND, sans concaténation.
- CStr formate les nombres indépendamment de la langue du client, avec un point décimal. Convertir et concaténer n’imprime et n’envoie rien : passer ensuite la String à une API si nécessaire.
- Les chaînes sont immuables : la jointure crée une nouvelle valeur sans modifier les sources. Agrandir continuellement une grande chaîne recopie son contenu ; produire uniquement la sortie utile au lieu de reconstruire tout un rapport à chaque tour.

## Exemples

### 1. Quantité et libellé

```vb
# amount=50 est Integer. CStr(amount) donne "50". "Items: " contient un deux-points et un espace final. Main renvoie "Items: 50", sans impression automatique.
Option Explicit On
SUB Main()
    VAR amount = 50
    RETURN "Items: " & CStr(amount)
END SUB
```

**Explication des paramètres et du déroulement:**

amount=50 est Integer. CStr(amount) donne "50". "Items: " contient un deux-points et un espace final. Main renvoie "Items: 50", sans impression automatique.

### 2. Fonction de formatage complète

```vb
# Label reçoit name="ore", amount=3. Elle joint le nom, un deux-points explicite et CStr(amount). Cette fonction complète renvoie "ore:3" à Main et accepte d’autres noms et quantités.
Option Explicit On
FUNCTION Label(name, amount)
    RETURN name + ":" + CStr(amount)
END FUNCTION
SUB Main()
    RETURN Label("ore", 3)
END SUB
```

**Explication des paramètres et du déroulement:**

Label reçoit name="ore", amount=3. Elle joint le nom, un deux-points explicite et CStr(amount). Cette fonction complète renvoie "ore:3" à Main et accepte d’autres noms et quantités.

### 3. Calculer puis assembler

```vb
# CStr(2+3) calcule 5 puis le convertit en "5". Le second littéral conserve point-virgule, espaces et A&B. Main renvoie "Total: 5; literal: A&B".
Option Explicit On
SUB Main()
    RETURN "Total: " & CStr(2 + 3) & "; literal: A&B"
END SUB
```

**Explication des paramètres et du déroulement:**

CStr(2+3) calcule 5 puis le convertit en "5". Le second littéral conserve point-virgule, espaces et A&B. Main renvoie "Total: 5; literal: A&B".

<!-- implementation references (not callable script procedures):
Runtime/BasicSyntaxPreprocessor.cs: ProtectLiteralText / ReplaceConcatenationOutsideLiterals
Runtime/InjectionValue.cs: operator + / explicit operator string
Runtime/InjectionApi.cs: CStr
-->
