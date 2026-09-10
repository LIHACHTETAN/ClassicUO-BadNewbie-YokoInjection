# IF / ELSEIF / ELSE / END IF

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: fr -->

IF sélectionne au plus une branche : IF, puis les ELSEIF jusqu’au premier résultat vrai, sinon ELSE s’il existe. L’exécution continue normalement après END IF.

## Syntaxe exacte

```text
IF condition THEN
    statements
END IF
IF condition THEN
    statements
ELSEIF elseifCondition THEN
    statements
ELSE
    statements
END IF
```

## Paramètres

- `condition` — condition : expression testée une fois à l’entrée. Zéro numérique est faux, tout nombre non nul est vrai. Préférer comparaisons explicites ou résultats booléens API.
- `elseifCondition` — elseifCondition : condition supplémentaire facultative, évaluée seulement si toutes les précédentes sont fausses. Écrire ELSEIF en un mot.
- `statements / ELSE` — statements / ELSE : instructions aux lignes suivantes. ELSE est facultatif, sans condition, unique et final. THEN et END IF sont obligatoires ; utiliser un bloc multiligne.

## Retour

Aucune valeur (Unit). IF est une instruction, pas une fonction. Une condition ou un RETURN sélectionné peut produire une valeur. Comparer les booléens 1/0 à TRUE/FALSE est valide ; IF count accepte tout nombre non nul, IF count=TRUE uniquement 1.

## Comportement

- Le compilateur crée des sauts conditionnels et de sortie. Faux passe à la condition suivante ou ELSE ; une branche choisie saute les alternatives restantes. Chaque IF imbriqué possède son ELSE. RETURN quitte la procédure en exécutant les FINALLY englobants.
- Par compatibilité, IF compare à zéro numérique sans convertir chaque type avec CBool. Texte "0", texte vide, tableaux, objets et Unit prennent donc la branche vraie. Convertir le texte explicitement ou comparer la propriété voulue. AndAlso/OrElse exigent des nombres.
- Les déclarations d’une branche sautée ne créent pas de variables à l’exécution. Initialiser les résultats partagés avant IF. Option Explicit vérifie les noms, pas l’affectation sur chaque chemin. Plusieurs ELSE sont refusés avant exécution avec SC015, même sans Option Explicit.

## Exemples

### 1. Quatre cas

```vb
# Classify(value) teste <0, =0, <10 puis ELSE. -2, 0, 7, 20 donnent negative, zero, small, large. Main renvoie "negative:zero:small:large" ; chaque appel exécute un seul RETURN.
Option Explicit On
FUNCTION Classify(value)
    IF value < 0 THEN
        RETURN "negative"
    ELSEIF value = 0 THEN
        RETURN "zero"
    ELSEIF value < 10 THEN
        RETURN "small"
    ELSE
        RETURN "large"
    END IF
END FUNCTION
SUB Main()
    RETURN Classify(-2) + ":" + Classify(0) + ":" + Classify(7) + ":" + Classify(20)
END SUB
```

**Explication des paramètres et du déroulement:**

Classify(value) teste <0, =0, <10 puis ELSE. -2, 0, 7, 20 donnent negative, zero, small, large. Main renvoie "negative:zero:small:large" ; chaque appel exécute un seul RETURN.

### 2. Décisions imbriquées

```vb
# Action(enabled, amount) teste enabled, puis amount>0 pour choisir work ou idle. Le ELSE extérieur donne disabled. (TRUE,5), (TRUE,0), (FALSE,5) produisent "work:idle:disabled". Chaque END IF ferme son bloc.
Option Explicit On
FUNCTION Action(enabled, amount)
    IF enabled THEN
        IF amount > 0 THEN
            RETURN "work"
        ELSE
            RETURN "idle"
        END IF
    ELSE
        RETURN "disabled"
    END IF
END FUNCTION
SUB Main()
    RETURN Action(TRUE, 5) + ":" + Action(TRUE, 0) + ":" + Action(FALSE, 5)
END SUB
```

**Explication des paramètres et du déroulement:**

Action(enabled, amount) teste enabled, puis amount>0 pour choisir work ou idle. Le ELSE extérieur donne disabled. (TRUE,5), (TRUE,0), (FALSE,5) produisent "work:idle:disabled". Chaque END IF ferme son bloc.

### 3. Ordre des conditions

```vb
# Check(calls,value) incrémente calls ByRef et renvoie value. La première condition est fausse, la seconde vraie ; troisième et ELSE sont sautés. result=7, calls=2 ; Main renvoie calls*10+result=27. Tous les auxiliaires sont inclus.
Option Explicit On
FUNCTION Check(ByRef calls, ByVal value)
    calls += 1
    RETURN value
END FUNCTION
SUB Main()
    VAR calls = 0
    VAR result = 0
    IF Check(calls, FALSE) THEN
        result = 5
    ELSEIF Check(calls, TRUE) THEN
        result = 7
    ELSEIF Check(calls, TRUE) THEN
        result = 9
    ELSE
        result = 8
    END IF
    RETURN calls * 10 + result
END SUB
```

**Explication des paramètres et du déroulement:**

Check(calls,value) incrémente calls ByRef et renvoie value. La première condition est fausse, la seconde vraie ; troisième et ELSE sont sautés. result=7, calls=2 ; Main renvoie calls*10+result=27. Tous les auxiliaires sont inclus.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: if / elseif / else
Runtime/Instructions/Generator.cs: Generate(IfContext)
Runtime/Interpreter.cs: CallSubrutine / IfInstruction / CreateArgumentWriter
Analysis/MisplacedStatementsVisitor.cs: VisitIf
Runtime/InjectionRuntime.cs: BlockingLanguageError
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/if-then-else-statement
-->
