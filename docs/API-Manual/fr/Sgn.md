# Sgn

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: fr -->

Renvoie le signe.

## Syntaxe exacte

```text
Sgn(value:Any) -> Integer
```

## Paramètres

- `value` — Argument obligatoire : Integer/Decimal ou texte décimal avec point et exposant facultatif, par exemple "-1.25e2". Indépendant de la langue. Texte invalide/hexadécimal, Unit, Array et Object donnent 0 ; un littéral hexadécimal numérique est déjà Integer. NaN/Infinity sont possibles. -1 négatif, 0 nul, +1 positif. NaN provoque une erreur mathématique ; les infinis donnent leur signe.

## Retour

Integer — sign(value). -1 négatif, 0 nul, +1 positif. NaN provoque une erreur mathématique ; les infinis donnent leur signe. Nombre, pas un ID ni un indicateur de réussite. 1/0 ne signifient pas réussite/échec.

## Comportement

- Calcul local sur le fil du script, sans serveur, déplacement, curseur, attente ni modification des variables globales.
- Decimal est un Double binaire, pas .NET decimal. Comparer les valeurs finies approchées avec une tolérance. NaN/Infinity ne conviennent pas aux coordonnées ou quantités.
- -1 négatif, 0 nul, +1 positif. NaN provoque une erreur mathématique ; les infinis donnent leur signe.

### Fonctions internes : de l’appel au résultat

Étapes réelles de liaison/conversion. Les fonctions auxiliaires complètes montrent des formules de script, sans remplacer les mathématiques de la plateforme.

#### 1. Register

Register lie le nom BASIC à un calcul natif à un argument, puis System.Math après conversion. Aucun script caché ni traitement serveur.

Integer — sign(value). -1 négatif, 0 nul, +1 positif. NaN provoque une erreur mathématique ; les infinis donnent leur signe. Nombre, pas un ID ni un indicateur de réussite. 1/0 ne signifient pas réussite/échec.

Source du projet: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApi.cs`; fonction `Register`.

#### 2. BasicDouble

BasicDouble conserve Integer/Decimal, analyse le texte via NumberStyles.Float invariant, sinon renvoie 0. Abs traite directement un Integer ordinaire avant le repli Double.

Argument obligatoire : Integer/Decimal ou texte décimal avec point et exposant facultatif, par exemple "-1.25e2". Indépendant de la langue. Texte invalide/hexadécimal, Unit, Array et Object donnent 0 ; un littéral hexadécimal numérique est déjà Integer. NaN/Infinity sont possibles.

Source du projet: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApi.cs`; fonction `BasicDouble`.

#### 3. BasicSgn

-1 négatif, 0 nul, +1 positif. NaN provoque une erreur mathématique ; les infinis donnent leur signe.

Integer — sign(value). -1 négatif, 0 nul, +1 positif. NaN provoque une erreur mathématique ; les infinis donnent leur signe. Nombre, pas un ID ni un indicateur de réussite. 1/0 ne signifient pas réussite/échec.

Source du projet: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApi.cs`; fonction `BasicSgn`.

Calcul local sur le fil du script, sans serveur, déplacement, curseur, attente ni modification des variables globales.


## Exemples

### Calcul direct

```vb
# Calcul direct
#
# Renvoie le signe.
#
# Integer — sign(value). -1 négatif, 0 nul, +1 positif. NaN provoque une erreur mathématique ;
# les infinis donnent leur signe. Nombre, pas un ID ni un indicateur de réussite. 1/0 ne
# signifient pas réussite/échec.

SUB Main()
    # value = -8 ; résultat attendu -1 (~ : approximation). value conserve le résultat ; CStr le
    # formate pour Print.

    VAR value = Sgn(-8)
    UO.Print(CStr(value))
END SUB
```

**Explication des paramètres et du déroulement:**

- value = -8 ; résultat attendu -1 (~ : approximation). value conserve le résultat ; CStr le formate pour Print.

### Autre argument via une variable

```vb
# Autre argument via une variable
#
# Renvoie le signe.
#
# Integer — sign(value). -1 négatif, 0 nul, +1 positif. NaN provoque une erreur mathématique ;
# les infinis donnent leur signe. Nombre, pas un ID ni un indicateur de réussite. 1/0 ne
# signifient pas réussite/échec.

SUB Main()
    # value = 10-10 ; résultat attendu 0 (~ : approximation). value conserve le résultat ; CStr le
    # formate pour Print.

    VAR inputValue = 10-10
    VAR value = Sgn(inputValue)
    UO.Print(CStr(value))
END SUB
```

**Explication des paramètres et du déroulement:**

- value = 10-10 ; résultat attendu 0 (~ : approximation). value conserve le résultat ; CStr le formate pour Print.

### Fonction auxiliaire complète

```vb
# Fonction auxiliaire complète
#
# Renvoie le signe.
#
# Integer — sign(value). -1 négatif, 0 nul, +1 positif. NaN provoque une erreur mathématique ;
# les infinis donnent leur signe. Nombre, pas un ID ni un indicateur de réussite. 1/0 ne
# signifient pas réussite/échec.

# manual-check: scalar-math Sgn
SUB Main()
    # current/destination : positions sur un axe. StepToward donne -1/0/1, pas une direction à huit
    # voies ni un déplacement.

    VAR value = StepToward(12,10)
    UO.Print(CStr(value))
END SUB

SUB StepToward(current,destination)
    RETURN Sgn(CDbl(destination)-CDbl(current))
END SUB
```

**Explication des paramètres et du déroulement:**

- current/destination : positions sur un axe. StepToward donne -1/0/1, pas une direction à huit voies ni un déplacement.
