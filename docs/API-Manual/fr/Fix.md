# Fix

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: fr -->

Supprime la partie fractionnaire vers zéro.

## Syntaxe exacte

```text
Fix(value:Any) -> Integer
```

## Paramètres

- `value` — Argument obligatoire : Integer/Decimal ou texte décimal avec point et exposant facultatif, par exemple "-1.25e2". Indépendant de la langue. Texte invalide/hexadécimal, Unit, Array et Object donnent 0 ; un littéral hexadécimal numérique est déjà Integer. NaN/Infinity sont possibles. Entrée finie, résultat tronqué dans -2147483648..2147483647. -2.9 donne -2, contrairement au plancher -3. Hors plage/NaN/Infinity ne sont pas valides.

## Retour

Integer — truncate(value). Entrée finie, résultat tronqué dans -2147483648..2147483647. -2.9 donne -2, contrairement au plancher -3. Hors plage/NaN/Infinity ne sont pas valides. Nombre, pas un ID ni un indicateur de réussite. 1/0 ne signifient pas réussite/échec.

## Comportement

- Calcul local sur le fil du script, sans serveur, déplacement, curseur, attente ni modification des variables globales.
- Decimal est un Double binaire, pas .NET decimal. Comparer les valeurs finies approchées avec une tolérance. NaN/Infinity ne conviennent pas aux coordonnées ou quantités.
- Entrée finie, résultat tronqué dans -2147483648..2147483647. -2.9 donne -2, contrairement au plancher -3. Hors plage/NaN/Infinity ne sont pas valides.

### Fonctions internes : de l’appel au résultat

Étapes réelles de liaison/conversion. Les fonctions auxiliaires complètes montrent des formules de script, sans remplacer les mathématiques de la plateforme.

#### 1. Register

Register lie le nom BASIC à un calcul natif à un argument, puis System.Math après conversion. Aucun script caché ni traitement serveur.

Integer — truncate(value). Entrée finie, résultat tronqué dans -2147483648..2147483647. -2.9 donne -2, contrairement au plancher -3. Hors plage/NaN/Infinity ne sont pas valides. Nombre, pas un ID ni un indicateur de réussite. 1/0 ne signifient pas réussite/échec.

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
# Supprime la partie fractionnaire vers zéro.
#
# Integer — truncate(value). Entrée finie, résultat tronqué dans -2147483648..2147483647. -2.9
# donne -2, contrairement au plancher -3. Hors plage/NaN/Infinity ne sont pas valides. Nombre,
# pas un ID ni un indicateur de réussite. 1/0 ne signifient pas réussite/échec.

SUB Main()
    # value = 2.9 ; résultat attendu 2 (~ : approximation). value conserve le résultat ; CStr le
    # formate pour Print.

    VAR value = Fix(2.9)
    UO.Print(CStr(value))
END SUB
```

**Explication des paramètres et du déroulement:**

- value = 2.9 ; résultat attendu 2 (~ : approximation). value conserve le résultat ; CStr le formate pour Print.

### Autre argument via une variable

```vb
# Autre argument via une variable
#
# Supprime la partie fractionnaire vers zéro.
#
# Integer — truncate(value). Entrée finie, résultat tronqué dans -2147483648..2147483647. -2.9
# donne -2, contrairement au plancher -3. Hors plage/NaN/Infinity ne sont pas valides. Nombre,
# pas un ID ni un indicateur de réussite. 1/0 ne signifient pas réussite/échec.

SUB Main()
    # value = -2.9 ; résultat attendu -2 (~ : approximation). value conserve le résultat ; CStr le
    # formate pour Print.

    VAR inputValue = -2.9
    VAR value = Fix(inputValue)
    UO.Print(CStr(value))
END SUB
```

**Explication des paramètres et du déroulement:**

- value = -2.9 ; résultat attendu -2 (~ : approximation). value conserve le résultat ; CStr le formate pour Print.

### Fonction auxiliaire complète

```vb
# Fonction auxiliaire complète
#
# Supprime la partie fractionnaire vers zéro.
#
# Integer — truncate(value). Entrée finie, résultat tronqué dans -2147483648..2147483647. -2.9
# donne -2, contrairement au plancher -3. Hors plage/NaN/Infinity ne sont pas valides. Nombre,
# pas un ID ni un indicateur de réussite. 1/0 ne signifient pas réussite/échec.

# manual-check: scalar-math Fix
SUB Main()
    # total>=0, size>0 : lots complets ; 27/5 donne 5. Entrée invalide : repli 0, également possible
    # sans lot complet. Quotient dans Integer.

    VAR value = WholeBatches(27,5)
    UO.Print(CStr(value))
END SUB

SUB WholeBatches(total,size)
    IF total < 0 OR size <= 0 THEN
        RETURN 0
    END IF
    RETURN Fix(CDbl(total)/CDbl(size))
END SUB
```

**Explication des paramètres et du déroulement:**

- total>=0, size>0 : lots complets ; 27/5 donne 5. Entrée invalide : repli 0, également possible sans lot complet. Quotient dans Integer.
