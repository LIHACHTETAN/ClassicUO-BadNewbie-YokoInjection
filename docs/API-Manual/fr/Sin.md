# Sin

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: fr -->

Calcule le sinus.

## Syntaxe exacte

```text
Sin(radians:Any) -> Decimal
```

## Paramètres

- `radians` — Argument obligatoire : Integer/Decimal ou texte décimal avec point et exposant facultatif, par exemple "-1.25e2". Indépendant de la langue. Texte invalide/hexadécimal, Unit, Array et Object donnent 0 ; un littéral hexadécimal numérique est déjà Integer. NaN/Infinity sont possibles. Radians, pas degrés ni direction du jeu. Résultat fini dans [-1,1] ; NaN/infini donnent NaN.

## Retour

Decimal — sin(radians). Radians, pas degrés ni direction du jeu. Résultat fini dans [-1,1] ; NaN/infini donnent NaN. Nombre, pas un ID ni un indicateur de réussite. 1/0 ne signifient pas réussite/échec.

## Comportement

- Calcul local sur le fil du script, sans serveur, déplacement, curseur, attente ni modification des variables globales.
- Decimal est un Double binaire, pas .NET decimal. Comparer les valeurs finies approchées avec une tolérance. NaN/Infinity ne conviennent pas aux coordonnées ou quantités.
- Radians, pas degrés ni direction du jeu. Résultat fini dans [-1,1] ; NaN/infini donnent NaN.

### Fonctions internes : de l’appel au résultat

Étapes réelles de liaison/conversion. Les fonctions auxiliaires complètes montrent des formules de script, sans remplacer les mathématiques de la plateforme.

#### 1. Register

Register lie le nom BASIC à un calcul natif à un argument, puis System.Math après conversion. Aucun script caché ni traitement serveur.

Decimal — sin(radians). Radians, pas degrés ni direction du jeu. Résultat fini dans [-1,1] ; NaN/infini donnent NaN. Nombre, pas un ID ni un indicateur de réussite. 1/0 ne signifient pas réussite/échec.

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
# Calcule le sinus.
#
# Decimal — sin(radians). Radians, pas degrés ni direction du jeu. Résultat fini dans [-1,1] ;
# NaN/infini donnent NaN. Nombre, pas un ID ni un indicateur de réussite. 1/0 ne signifient pas
# réussite/échec.

SUB Main()
    # radians = 0 ; résultat attendu 0 (~ : approximation). value conserve le résultat ; CStr le
    # formate pour Print.

    VAR value = Sin(0)
    UO.Print(CStr(value))
END SUB
```

**Explication des paramètres et du déroulement:**

- radians = 0 ; résultat attendu 0 (~ : approximation). value conserve le résultat ; CStr le formate pour Print.

### Autre argument via une variable

```vb
# Autre argument via une variable
#
# Calcule le sinus.
#
# Decimal — sin(radians). Radians, pas degrés ni direction du jeu. Résultat fini dans [-1,1] ;
# NaN/infini donnent NaN. Nombre, pas un ID ni un indicateur de réussite. 1/0 ne signifient pas
# réussite/échec.

SUB Main()
    # radians = 1.5707963267948966 ; résultat attendu ~1 (~ : approximation). value conserve le
    # résultat ; CStr le formate pour Print.

    VAR inputValue = 1.5707963267948966
    VAR value = Sin(inputValue)
    UO.Print(CStr(value))
END SUB
```

**Explication des paramètres et du déroulement:**

- radians = 1.5707963267948966 ; résultat attendu ~1 (~ : approximation). value conserve le résultat ; CStr le formate pour Print.

### Fonction auxiliaire complète

```vb
# Fonction auxiliaire complète
#
# Calcule le sinus.
#
# Decimal — sin(radians). Radians, pas degrés ni direction du jeu. Résultat fini dans [-1,1] ;
# NaN/infini donnent NaN. Nombre, pas un ID ni un indicateur de réussite. 1/0 ne signifient pas
# réussite/échec.

# manual-check: scalar-math Sin
SUB Main()
    # degrees est en degrés ; pi/180 convertit avant Sin. SineDegrees(30)≈0.5.

    VAR value = SineDegrees(30)
    UO.Print(CStr(value))
END SUB

SUB SineDegrees(degrees)
    RETURN Sin(degrees*3.141592653589793/180)
END SUB
```

**Explication des paramètres et du déroulement:**

- degrees est en degrés ; pi/180 convertit avant Sin. SineDegrees(30)≈0.5.
