# str

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: fr -->

Str(value) formate une valeur scalaire Basic en texte.

## Syntaxe exacte

```text
str(value:Decimal) -> String
str(value:Integer) -> String
str(value:String) -> String
```

## Paramètres

- `value` — Un Integer, Decimal ou String obligatoire. La surcharge dépend du type réel. Array, Object et Unit n’ont aucune surcharge Str correspondante.

## Retour

String: texte numérique invariant ou String d’origine inchangée. Aucun espace initial pour les nombres positifs. Aucun paramètre de précision.

## Comportement

- Calcul local sans requête au jeu. Omettre l’argument est une erreur. Les attributs utilisent UO.Int()/UO.Str(), pas Int()/Str(). Int appelle BasicDouble puis Math.Floor; Str choisit InternalSubrutines.Str selon le type et formate sans dépendre de la langue.

## Exemples

### Str — 1

```vb
# Str — 1
#
# Str(value) formate une valeur scalaire Basic en texte.
#
# String: texte numérique invariant ou String d’origine inchangée. Aucun espace initial pour les
# nombres positifs. Aucun paramètre de précision.

SUB Main()
    # value=42 est Integer. Str produit "42" sans espace initial; Main renvoie cette String.

    RETURN Str(42)
END SUB
```

**Explication des paramètres et du déroulement:**

- value=42 est Integer. Str produit "42" sans espace initial; Main renvoie cette String.

### Str — 2

```vb
# Str — 2
#
# Str(value) formate une valeur scalaire Basic en texte.
#
# String: texte numérique invariant ou String d’origine inchangée. Aucun espace initial pour les
# nombres positifs. Aucun paramètre de précision.

SUB Main()
    # amount=-12.5 est Decimal. Str mémorise "-12.5" dans text avec un point dans toutes les
    # langues. Main renvoie text; amount reste numérique.

    VAR amount = -12.5
    VAR text = Str(amount)
    RETURN text
END SUB
```

**Explication des paramètres et du déroulement:**

- amount=-12.5 est Decimal. Str mémorise "-12.5" dans text avec un point dans toutes les langues. Main renvoie text; amount reste numérique.

### Str — 3

```vb
# Str — 3
#
# Str(value) formate une valeur scalaire Basic en texte.
#
# String: texte numérique invariant ou String d’origine inchangée. Aucun espace initial pour les
# nombres positifs. Aucun paramètre de précision.

SUB Main()
    # ItemLabel reçoit name="ore", count=3. Str(name) conserve le nom et Str(count) produit "3". Le
    # helper joint les textes avec " x"; Main renvoie "ore x3".

    RETURN ItemLabel("ore",3)
END SUB

SUB ItemLabel(name,count)
    RETURN Str(name) + " x" + Str(count)
END SUB
```

**Explication des paramètres et du déroulement:**

- ItemLabel reçoit name="ore", count=3. Str(name) conserve le nom et Str(count) produit "3". Le helper joint les textes avec " x"; Main renvoie "ore x3".
