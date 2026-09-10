# Atn

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: fr -->

Calcule l’arc tangente.

## Syntaxe exacte

```text
Atn(number:Any) -> Decimal
```

## Paramètres

- `number` — Argument obligatoire : Integer/Decimal ou texte décimal avec point et exposant facultatif, par exemple "-1.25e2". Indépendant de la langue. Texte invalide/hexadécimal, Unit, Array et Object donnent 0 ; un littéral hexadécimal numérique est déjà Integer. NaN/Infinity sont possibles. Pente en entrée, radians dans [-pi/2,pi/2] en sortie. Les infinis donnent les limites ; NaN reste NaN. Ce n’est pas atan2.

## Retour

Decimal — atan(number). Pente en entrée, radians dans [-pi/2,pi/2] en sortie. Les infinis donnent les limites ; NaN reste NaN. Ce n’est pas atan2. Nombre, pas un ID ni un indicateur de réussite. 1/0 ne signifient pas réussite/échec.

## Comportement

- Calcul local sur le fil du script, sans serveur, déplacement, curseur, attente ni modification des variables globales.
- Decimal est un Double binaire, pas .NET decimal. Comparer les valeurs finies approchées avec une tolérance. NaN/Infinity ne conviennent pas aux coordonnées ou quantités.
- Pente en entrée, radians dans [-pi/2,pi/2] en sortie. Les infinis donnent les limites ; NaN reste NaN. Ce n’est pas atan2.

### Fonctions internes : de l’appel au résultat

Étapes réelles de liaison/conversion. Les fonctions auxiliaires complètes montrent des formules de script, sans remplacer les mathématiques de la plateforme.

#### 1. Register

Register lie le nom BASIC à un calcul natif à un argument, puis System.Math après conversion. Aucun script caché ni traitement serveur.

Decimal — atan(number). Pente en entrée, radians dans [-pi/2,pi/2] en sortie. Les infinis donnent les limites ; NaN reste NaN. Ce n’est pas atan2. Nombre, pas un ID ni un indicateur de réussite. 1/0 ne signifient pas réussite/échec.

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
# Calcule l’arc tangente.
#
# Decimal — atan(number). Pente en entrée, radians dans [-pi/2,pi/2] en sortie. Les infinis
# donnent les limites ; NaN reste NaN. Ce n’est pas atan2. Nombre, pas un ID ni un indicateur de
# réussite. 1/0 ne signifient pas réussite/échec.

SUB Main()
    # number = 0 ; résultat attendu 0 (~ : approximation). value conserve le résultat ; CStr le
    # formate pour Print.

    VAR value = Atn(0)
    UO.Print(CStr(value))
END SUB
```

**Explication des paramètres et du déroulement:**

- number = 0 ; résultat attendu 0 (~ : approximation). value conserve le résultat ; CStr le formate pour Print.

### Autre argument via une variable

```vb
# Autre argument via une variable
#
# Calcule l’arc tangente.
#
# Decimal — atan(number). Pente en entrée, radians dans [-pi/2,pi/2] en sortie. Les infinis
# donnent les limites ; NaN reste NaN. Ce n’est pas atan2. Nombre, pas un ID ni un indicateur de
# réussite. 1/0 ne signifient pas réussite/échec.

SUB Main()
    # number = 1 ; résultat attendu ~0.7853981633974483 (~ : approximation). value conserve le
    # résultat ; CStr le formate pour Print.

    VAR inputValue = 1
    VAR value = Atn(inputValue)
    UO.Print(CStr(value))
END SUB
```

**Explication des paramètres et du déroulement:**

- number = 1 ; résultat attendu ~0.7853981633974483 (~ : approximation). value conserve le résultat ; CStr le formate pour Print.

### Fonction auxiliaire complète

```vb
# Fonction auxiliaire complète
#
# Calcule l’arc tangente.
#
# Decimal — atan(number). Pente en entrée, radians dans [-pi/2,pi/2] en sortie. Les infinis
# donnent les limites ; NaN reste NaN. Ce n’est pas atan2. Nombre, pas un ID ni un indicateur de
# réussite. 1/0 ne signifient pas réussite/échec.

# manual-check: scalar-math Atn
SUB Main()
    # rise/run : pente ; run=0 donne le repli 0, pas un angle vertical. SlopeDegrees(1,1)≈45 ; ne
    # distingue pas tous les quadrants.

    VAR value = SlopeDegrees(1,1)
    UO.Print(CStr(value))
END SUB

SUB SlopeDegrees(rise,run)
    IF run = 0 THEN
        RETURN 0
    END IF
    RETURN Atn(CDbl(rise)/CDbl(run))*180/3.141592653589793
END SUB
```

**Explication des paramètres et du déroulement:**

- rise/run : pente ; run=0 donne le repli 0, pas un angle vertical. SlopeDegrees(1,1)≈45 ; ne distingue pas tous les quadrants.
