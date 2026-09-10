# Abs

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: fr -->

Renvoie la valeur absolue.

## Syntaxe exacte

```text
Abs(value:Any) -> Any
```

## Paramètres

- `value` — Argument obligatoire : Integer/Decimal ou texte décimal avec point et exposant facultatif, par exemple "-1.25e2". Indépendant de la langue. Texte invalide/hexadécimal, Unit, Array et Object donnent 0 ; un littéral hexadécimal numérique est déjà Integer. NaN/Infinity sont possibles. Integer conserve son type, sauf -2147483648 qui donne Decimal 2147483648. Decimal/texte donnent Decimal. NaN reste NaN ; les deux infinis donnent +Infinity.

## Retour

Integer/Decimal — abs(value). Integer conserve son type, sauf -2147483648 qui donne Decimal 2147483648. Decimal/texte donnent Decimal. NaN reste NaN ; les deux infinis donnent +Infinity. Nombre, pas un ID ni un indicateur de réussite. 1/0 ne signifient pas réussite/échec.

## Comportement

- Calcul local sur le fil du script, sans serveur, déplacement, curseur, attente ni modification des variables globales.
- Decimal est un Double binaire, pas .NET decimal. Comparer les valeurs finies approchées avec une tolérance. NaN/Infinity ne conviennent pas aux coordonnées ou quantités.
- Integer conserve son type, sauf -2147483648 qui donne Decimal 2147483648. Decimal/texte donnent Decimal. NaN reste NaN ; les deux infinis donnent +Infinity.

### Fonctions internes : de l’appel au résultat

Étapes réelles de liaison/conversion. Les fonctions auxiliaires complètes montrent des formules de script, sans remplacer les mathématiques de la plateforme.

#### 1. Register

Register lie le nom BASIC à un calcul natif à un argument, puis System.Math après conversion. Aucun script caché ni traitement serveur.

Integer/Decimal — abs(value). Integer conserve son type, sauf -2147483648 qui donne Decimal 2147483648. Decimal/texte donnent Decimal. NaN reste NaN ; les deux infinis donnent +Infinity. Nombre, pas un ID ni un indicateur de réussite. 1/0 ne signifient pas réussite/échec.

Source du projet: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApi.cs`; fonction `Register`.

#### 2. BasicDouble

BasicDouble conserve Integer/Decimal, analyse le texte via NumberStyles.Float invariant, sinon renvoie 0. Abs traite directement un Integer ordinaire avant le repli Double.

Argument obligatoire : Integer/Decimal ou texte décimal avec point et exposant facultatif, par exemple "-1.25e2". Indépendant de la langue. Texte invalide/hexadécimal, Unit, Array et Object donnent 0 ; un littéral hexadécimal numérique est déjà Integer. NaN/Infinity sont possibles.

Source du projet: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApi.cs`; fonction `BasicDouble`.

#### 3. BasicAbs

Integer conserve son type, sauf -2147483648 qui donne Decimal 2147483648. Decimal/texte donnent Decimal. NaN reste NaN ; les deux infinis donnent +Infinity.

Integer/Decimal — abs(value). Integer conserve son type, sauf -2147483648 qui donne Decimal 2147483648. Decimal/texte donnent Decimal. NaN reste NaN ; les deux infinis donnent +Infinity. Nombre, pas un ID ni un indicateur de réussite. 1/0 ne signifient pas réussite/échec.

Source du projet: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApi.cs`; fonction `BasicAbs`.

Calcul local sur le fil du script, sans serveur, déplacement, curseur, attente ni modification des variables globales.


## Exemples

### Calcul direct

```vb
# Calcul direct
#
# Renvoie la valeur absolue.
#
# Integer/Decimal — abs(value). Integer conserve son type, sauf -2147483648 qui donne Decimal
# 2147483648. Decimal/texte donnent Decimal. NaN reste NaN ; les deux infinis donnent +Infinity.
# Nombre, pas un ID ni un indicateur de réussite. 1/0 ne signifient pas réussite/échec.

SUB Main()
    # value = -12 ; résultat attendu 12 (~ : approximation). value conserve le résultat ; CStr le
    # formate pour Print.

    VAR value = Abs(-12)
    UO.Print(CStr(value))
END SUB
```

**Explication des paramètres et du déroulement:**

- value = -12 ; résultat attendu 12 (~ : approximation). value conserve le résultat ; CStr le formate pour Print.

### Autre argument via une variable

```vb
# Autre argument via une variable
#
# Renvoie la valeur absolue.
#
# Integer/Decimal — abs(value). Integer conserve son type, sauf -2147483648 qui donne Decimal
# 2147483648. Decimal/texte donnent Decimal. NaN reste NaN ; les deux infinis donnent +Infinity.
# Nombre, pas un ID ni un indicateur de réussite. 1/0 ne signifient pas réussite/échec.

SUB Main()
    # value = '-2.5' ; résultat attendu 2.5 (~ : approximation). value conserve le résultat ; CStr
    # le formate pour Print.

    VAR inputValue = '-2.5'
    VAR value = Abs(inputValue)
    UO.Print(CStr(value))
END SUB
```

**Explication des paramètres et du déroulement:**

- value = '-2.5' ; résultat attendu 2.5 (~ : approximation). value conserve le résultat ; CStr le formate pour Print.

### Fonction auxiliaire complète

```vb
# Fonction auxiliaire complète
#
# Renvoie la valeur absolue.
#
# Integer/Decimal — abs(value). Integer conserve son type, sauf -2147483648 qui donne Decimal
# 2147483648. Decimal/texte donnent Decimal. NaN reste NaN ; les deux infinis donnent +Infinity.
# Nombre, pas un ID ni un indicateur de réussite. 1/0 ne signifient pas réussite/échec.

# manual-check: scalar-math Abs
SUB Main()
    # value/target : nombres ; tolerance : écart admis >=0. IsWithin renvoie un booléen 1/0 ;
    # tolérance négative : 0.

    VAR value = IsWithin(12,10,2)
    UO.Print(CStr(value))
END SUB

SUB IsWithin(value,target,tolerance)
    IF tolerance < 0 THEN
        RETURN 0
    END IF
    RETURN Abs(CDbl(value)-CDbl(target)) <= tolerance
END SUB
```

**Explication des paramètres et du déroulement:**

- value/target : nombres ; tolerance : écart admis >=0. IsWithin renvoie un booléen 1/0 ; tolérance négative : 0.
