# NOT / AND / OR / XOR

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: fr -->

NOT inverse une condition. AND exige les deux, OR au moins une, XOR exactement une. && est un alias de AND, || de OR. La casse des mots-clés est indifférente.

## Syntaxe exacte

```text
NOT (condition)
left AND right
left && right
left OR right
left || right
left XOR right
```

## Paramètres

- `left` — Condition gauche binaire. AND/OR exigent Integer ou Decimal : zéro est faux, tout nombre non nul est vrai.
- `right` — Condition droite, également numérique pour AND/OR. Les deux opérandes sont évalués : un AND gauche faux ou un OR gauche vrai ne saute pas cette expression.
- `NOT / grouping` — Avec NOT, mettre toute la condition à inverser entre parenthèses. Pour combiner AND, OR et XOR, expliciter le groupement par des parenthèses.

## Retour

Integer 1 (TRUE) ou Integer 0 (FALSE). Ce sont des opérations logiques, non bit à bit : 2 AND 4 renvoie 1, pas un masque. Le drapeau retourné se teste avec =TRUE ou =1, =FALSE ou =0.

## Comportement

- AND, OR et XOR ont la même priorité et vont de gauche à droite dans ce moteur : TRUE OR FALSE AND FALSE vaut 0, TRUE OR (FALSE AND FALSE) vaut 1. Tenir compte de cette règle historique en adaptant du VB.
- NOT(condition) évalue puis inverse la condition. En tête de comparaison, NOT 1=2 signifie NOT(1=2). Écrire (NOT value) si la valeur inversée doit elle-même être un opérande de comparaison.
- AND/OR refusent String, Array, Object et Unit. Les NOT et XOR historiques testent plutôt l’égalité au zéro numérique : "0", texte vide, tableaux, objets et Unit sont tous non nuls. Définir des prédicats numériques explicites pour ces valeurs ; CBool possède ses propres conversions.
- Toutes les expressions droites s’exécutent, y compris les appels, attentes et erreurs. Les parenthèses changent le groupement, pas cette évaluation systématique. Utiliser des IF imbriqués si une expression ne doit s’exécuter qu’après une condition réussie.

## Exemples

### 1. Combiner des drapeaux nommés

```vb
# ready=TRUE, blocked=FALSE. NOT(blocked) donne 1, donc canRun vaut 1. ready XOR blocked est vrai car un seul drapeau est vrai. Main renvoie canRun*10+exclusive=11.
Option Explicit On
SUB Main()
    VAR ready = TRUE
    VAR blocked = FALSE
    VAR canRun = ready AND (NOT blocked)
    VAR exclusive = ready XOR blocked
    RETURN canRun * 10 + exclusive
END SUB
```

**Explication des paramètres et du déroulement:**

ready=TRUE, blocked=FALSE. NOT(blocked) donne 1, donc canRun vaut 1. ready XOR blocked est vrai car un seul drapeau est vrai. Main renvoie canRun*10+exclusive=11.

### 2. Observer les deux appels

```vb
# Mark incrémente counter reçu ByRef puis renvoie TRUE. Main démarre avec counter=0. FALSE AND Mark(counter) appelle quand même Mark ; TRUE OR Mark(counter) l’appelle encore. Les conditions valent 0 et 1, mais Main renvoie counter=2. Mark est entièrement définie.
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

**Explication des paramètres et du déroulement:**

Mark incrémente counter reçu ByRef puis renvoie TRUE. Main démarre avec counter=0. FALSE AND Mark(counter) appelle quand même Mark ; TRUE OR Mark(counter) l’appelle encore. Les conditions valent 0 et 1, mais Main renvoie counter=2. Mark est entièrement définie.

### 3. Expliciter le groupement

```vb
# legacy évalue TRUE OR FALSE puis AND FALSE et vaut 0. grouped évalue d’abord FALSE AND FALSE entre parenthèses puis OR avec TRUE et vaut 1. Main renvoie legacy*10+grouped=1.
Option Explicit On
SUB Main()
    VAR legacy = TRUE OR FALSE AND FALSE
    VAR grouped = TRUE OR (FALSE AND FALSE)
    RETURN legacy * 10 + grouped
END SUB
```

**Explication des paramètres et du déroulement:**

legacy évalue TRUE OR FALSE puis AND FALSE et vaut 0. grouped évalue d’abord FALSE AND FALSE entre parenthèses puis OR avec TRUE et vaut 1. Main renvoie legacy*10+grouped=1.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: expression / logicalOperand / signedOperand
Runtime/Interpreter.cs: VisitExpression / VisitLogicalOperand / VisitSignedOperand
Runtime/InjectionValue.cs: operator & / operator | / Equals
-->
