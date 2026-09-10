# Int

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: fr -->

Int(value) arrondit un nombre Basic vers moins l’infini.

## Syntaxe exacte

```text
Int(value:Any) -> Integer
```

## Paramètres

- `value` — Un Integer/Decimal ou texte numérique obligatoire. Le séparateur est le point quelle que soit la langue. Texte invalide, Array, Object et Unit deviennent 0; contrôlez les saisies avec IsNumeric.

## Retour

Integer: floor(value), par exemple 2.9 -> 2 et -2.9 -> -3. Le résultat doit tenir dans Int32 signé; évitez valeurs non finies et dépassements.

## Comportement

- Calcul local sans requête au jeu. Omettre l’argument est une erreur. Les attributs utilisent UO.Int()/UO.Str(), pas Int()/Str(). Int appelle BasicDouble puis Math.Floor; Str choisit InternalSubrutines.Str selon le type et formate sans dépendre de la langue.

## Exemples

### Int — 1

```vb
# Int — 1
#
# Int(value) arrondit un nombre Basic vers moins l’infini.
#
# Integer: floor(value), par exemple 2.9 -> 2 et -2.9 -> -3. Le résultat doit tenir dans Int32
# signé; évitez valeurs non finies et dépassements.

SUB Main()
    # value=2.9. L’arrondi inférieur donne Integer 2, renvoyé par Main.

    RETURN Int(2.9)
END SUB
```

**Explication des paramètres et du déroulement:**

- value=2.9. L’arrondi inférieur donne Integer 2, renvoyé par Main.

### Int — 2

```vb
# Int — 2
#
# Int(value) arrondit un nombre Basic vers moins l’infini.
#
# Integer: floor(value), par exemple 2.9 -> 2 et -2.9 -> -3. Le résultat doit tenir dans Int32
# signé; évitez valeurs non finies et dépassements.

SUB Main()
    # value=-2.9. L’arrondi inférieur donne -3, contrairement à la troncature vers zéro qui
    # donnerait -2. Main renvoie Integer -3.

    VAR value = -2.9
    RETURN Int(value)
END SUB
```

**Explication des paramètres et du déroulement:**

- value=-2.9. L’arrondi inférieur donne -3, contrairement à la troncature vers zéro qui donnerait -2. Main renvoie Integer -3.

### Int — 3

```vb
# Int — 3
#
# Int(value) arrondit un nombre Basic vers moins l’infini.
#
# Integer: floor(value), par exemple 2.9 -> 2 et -2.9 -> -3. Le résultat doit tenir dans Int32
# signé; évitez valeurs non finies et dépassements.

SUB Main()
    # WholeUnits reçoit total=27 et size=5. Si size<=0, résultat 0; sinon Int(total/size) arrondit
    # 5.4 vers le bas. Main renvoie 5 unités complètes. La fonction et ses deux paramètres sont
    # entièrement définis.

    RETURN WholeUnits(27,5)
END SUB

SUB WholeUnits(total,size)
    IF size <= 0 THEN
        RETURN 0
    END IF
    RETURN Int(total/size)
END SUB
```

**Explication des paramètres et du déroulement:**

- WholeUnits reçoit total=27 et size=5. Si size<=0, résultat 0; sinon Int(total/size) arrondit 5.4 vers le bas. Main renvoie 5 unités complètes. La fonction et ses deux paramètres sont entièrement définis.
