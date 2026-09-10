# Log

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: fr -->

Calcule le logarithme naturel.

## Syntaxe exacte

```text
Log(number:Any) -> Decimal
```

## Paramètres

- `number` — Argument obligatoire : Integer/Decimal ou texte décimal avec point et exposant facultatif, par exemple "-1.25e2". Indépendant de la langue. Texte invalide/hexadécimal, Unit, Array et Object donnent 0 ; un littéral hexadécimal numérique est déjà Integer. NaN/Infinity sont possibles. Base e, pas 10. Log(1)=0 ; Log(0)=-Infinity ; négatif : NaN ; +Infinity : Infinity.

## Retour

Decimal — ln(number). Base e, pas 10. Log(1)=0 ; Log(0)=-Infinity ; négatif : NaN ; +Infinity : Infinity. Nombre, pas un ID ni un indicateur de réussite. 1/0 ne signifient pas réussite/échec.

## Comportement

- Calcul local sur le fil du script, sans serveur, déplacement, curseur, attente ni modification des variables globales.
- Decimal est un Double binaire, pas .NET decimal. Comparer les valeurs finies approchées avec une tolérance. NaN/Infinity ne conviennent pas aux coordonnées ou quantités.
- Base e, pas 10. Log(1)=0 ; Log(0)=-Infinity ; négatif : NaN ; +Infinity : Infinity.

### Fonctions internes : de l’appel au résultat

Étapes réelles de liaison/conversion. Les fonctions auxiliaires complètes montrent des formules de script, sans remplacer les mathématiques de la plateforme.

#### 1. Register

Register lie le nom BASIC à un calcul natif à un argument, puis System.Math après conversion. Aucun script caché ni traitement serveur.

Decimal — ln(number). Base e, pas 10. Log(1)=0 ; Log(0)=-Infinity ; négatif : NaN ; +Infinity : Infinity. Nombre, pas un ID ni un indicateur de réussite. 1/0 ne signifient pas réussite/échec.

Source du projet: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApi.cs`; fonction `Register`.

#### 2. BasicDouble

BasicDouble conserve Integer/Decimal, analyse le texte via NumberStyles.Float invariant, sinon renvoie 0. Abs traite directement un Integer ordinaire avant le repli Double.

Argument obligatoire : Integer/Decimal ou texte décimal avec point et exposant facultatif, par exemple "-1.25e2". Indépendant de la langue. Texte invalide/hexadécimal, Unit, Array et Object donnent 0 ; un littéral hexadécimal numérique est déjà Integer. NaN/Infinity sont possibles.

Source du projet: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApi.cs`; fonction `BasicDouble`.

Calcul local sur le fil du script, sans serveur, déplacement, curseur, attente ni modification des variables globales.


## Exemples

### Calcul direct

```vb
# Calcul direct
#
# Calcule le logarithme naturel.
#
# Decimal — ln(number). Base e, pas 10. Log(1)=0 ; Log(0)=-Infinity ; négatif : NaN ; +Infinity
# : Infinity. Nombre, pas un ID ni un indicateur de réussite. 1/0 ne signifient pas
# réussite/échec.

SUB Main()
    # number = 1 ; résultat attendu 0 (~ : approximation). value conserve le résultat ; CStr le
    # formate pour Print.

    VAR value = Log(1)
    UO.Print(CStr(value))
END SUB
```

**Explication des paramètres et du déroulement:**

- number = 1 ; résultat attendu 0 (~ : approximation). value conserve le résultat ; CStr le formate pour Print.

### Autre argument via une variable

```vb
# Autre argument via une variable
#
# Calcule le logarithme naturel.
#
# Decimal — ln(number). Base e, pas 10. Log(1)=0 ; Log(0)=-Infinity ; négatif : NaN ; +Infinity
# : Infinity. Nombre, pas un ID ni un indicateur de réussite. 1/0 ne signifient pas
# réussite/échec.

SUB Main()
    # number = 2.718281828459045 ; résultat attendu ~1 (~ : approximation). value conserve le
    # résultat ; CStr le formate pour Print.

    VAR inputValue = 2.718281828459045
    VAR value = Log(inputValue)
    UO.Print(CStr(value))
END SUB
```

**Explication des paramètres et du déroulement:**

- number = 2.718281828459045 ; résultat attendu ~1 (~ : approximation). value conserve le résultat ; CStr le formate pour Print.

### Fonction auxiliaire complète

```vb
# Fonction auxiliaire complète
#
# Calcule le logarithme naturel.
#
# Decimal — ln(number). Base e, pas 10. Log(1)=0 ; Log(0)=-Infinity ; négatif : NaN ; +Infinity
# : Infinity. Nombre, pas un ID ni un indicateur de réussite. 1/0 ne signifient pas
# réussite/échec.

# manual-check: scalar-math Log
SUB Main()
    # value>0, baseValue>0 et <>1. Log(value)/Log(baseValue) ; LogBase(100,10)≈2. Entrées invalides
    # : repli 0, aussi possible comme résultat valide.

    VAR value = LogBase(100,10)
    UO.Print(CStr(value))
END SUB

SUB LogBase(value,baseValue)
    IF value <= 0 OR baseValue <= 0 OR baseValue = 1 THEN
        RETURN 0
    END IF
    RETURN Log(value)/Log(baseValue)
END SUB
```

**Explication des paramètres et du déroulement:**

- value>0, baseValue>0 et <>1. Log(value)/Log(baseValue) ; LogBase(100,10)≈2. Entrées invalides : repli 0, aussi possible comme résultat valide.
