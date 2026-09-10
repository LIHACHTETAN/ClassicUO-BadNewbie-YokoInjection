# Sqr

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: fr -->

Calcule la racine carrée.

## Syntaxe exacte

```text
Sqr(number:Any) -> Decimal
```

## Paramètres

- `number` — Argument obligatoire : Integer/Decimal ou texte décimal avec point et exposant facultatif, par exemple "-1.25e2". Indépendant de la langue. Texte invalide/hexadécimal, Unit, Array et Object donnent 0 ; un littéral hexadécimal numérique est déjà Integer. NaN/Infinity sont possibles. Entrée >=0 : racine non négative. Négatif : NaN ; +Infinity : Infinity ; NaN inchangé.

## Retour

Decimal — sqrt(number). Entrée >=0 : racine non négative. Négatif : NaN ; +Infinity : Infinity ; NaN inchangé. Nombre, pas un ID ni un indicateur de réussite. 1/0 ne signifient pas réussite/échec.

## Comportement

- Calcul local sur le fil du script, sans serveur, déplacement, curseur, attente ni modification des variables globales.
- Decimal est un Double binaire, pas .NET decimal. Comparer les valeurs finies approchées avec une tolérance. NaN/Infinity ne conviennent pas aux coordonnées ou quantités.
- Entrée >=0 : racine non négative. Négatif : NaN ; +Infinity : Infinity ; NaN inchangé.

### Fonctions internes : de l’appel au résultat

Étapes réelles de liaison/conversion. Les fonctions auxiliaires complètes montrent des formules de script, sans remplacer les mathématiques de la plateforme.

#### 1. Register

Register lie le nom BASIC à un calcul natif à un argument, puis System.Math après conversion. Aucun script caché ni traitement serveur.

Decimal — sqrt(number). Entrée >=0 : racine non négative. Négatif : NaN ; +Infinity : Infinity ; NaN inchangé. Nombre, pas un ID ni un indicateur de réussite. 1/0 ne signifient pas réussite/échec.

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
# Calcule la racine carrée.
#
# Decimal — sqrt(number). Entrée >=0 : racine non négative. Négatif : NaN ; +Infinity : Infinity
# ; NaN inchangé. Nombre, pas un ID ni un indicateur de réussite. 1/0 ne signifient pas
# réussite/échec.

SUB Main()
    # number = 25 ; résultat attendu 5 (~ : approximation). value conserve le résultat ; CStr le
    # formate pour Print.

    VAR value = Sqr(25)
    UO.Print(CStr(value))
END SUB
```

**Explication des paramètres et du déroulement:**

- number = 25 ; résultat attendu 5 (~ : approximation). value conserve le résultat ; CStr le formate pour Print.

### Autre argument via une variable

```vb
# Autre argument via une variable
#
# Calcule la racine carrée.
#
# Decimal — sqrt(number). Entrée >=0 : racine non négative. Négatif : NaN ; +Infinity : Infinity
# ; NaN inchangé. Nombre, pas un ID ni un indicateur de réussite. 1/0 ne signifient pas
# réussite/échec.

SUB Main()
    # number = 2 ; résultat attendu ~1.4142135623730951 (~ : approximation). value conserve le
    # résultat ; CStr le formate pour Print.

    VAR inputValue = 2
    VAR value = Sqr(inputValue)
    UO.Print(CStr(value))
END SUB
```

**Explication des paramètres et du déroulement:**

- number = 2 ; résultat attendu ~1.4142135623730951 (~ : approximation). value conserve le résultat ; CStr le formate pour Print.

### Fonction auxiliaire complète

```vb
# Fonction auxiliaire complète
#
# Calcule la racine carrée.
#
# Decimal — sqrt(number). Entrée >=0 : racine non négative. Négatif : NaN ; +Infinity : Infinity
# ; NaN inchangé. Nombre, pas un ID ni un indicateur de réussite. 1/0 ne signifient pas
# réussite/échec.

# manual-check: scalar-math Sqr
SUB Main()
    # dx/dy : écarts de coordonnées. CDbl évite le débordement entier avant sqrt(dx²+dy²).
    # SegmentLength(3,4)=5 ; distance euclidienne, pas un trajet ni une collision.

    VAR value = SegmentLength(3,4)
    UO.Print(CStr(value))
END SUB

SUB SegmentLength(dx,dy)
    VAR x = CDbl(dx)
    VAR y = CDbl(dy)
    RETURN Sqr(x*x+y*y)
END SUB
```

**Explication des paramètres et du déroulement:**

- dx/dy : écarts de coordonnées. CDbl évite le débordement entier avant sqrt(dx²+dy²). SegmentLength(3,4)=5 ; distance euclidienne, pas un trajet ni une collision.
