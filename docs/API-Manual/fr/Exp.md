# Exp

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: fr -->

Élève e à une puissance.

## Syntaxe exacte

```text
Exp(power:Any) -> Decimal
```

## Paramètres

- `power` — Argument obligatoire : Integer/Decimal ou texte décimal avec point et exposant facultatif, par exemple "-1.25e2". Indépendant de la langue. Texte invalide/hexadécimal, Unit, Array et Object donnent 0 ; un littéral hexadécimal numérique est déjà Integer. NaN/Infinity sont possibles. Exp(0)=1. Très positif : Infinity ; très négatif : 0 par sous-dépassement. NaN inchangé.

## Retour

Decimal — e^power. Exp(0)=1. Très positif : Infinity ; très négatif : 0 par sous-dépassement. NaN inchangé. Nombre, pas un ID ni un indicateur de réussite. 1/0 ne signifient pas réussite/échec.

## Comportement

- Calcul local sur le fil du script, sans serveur, déplacement, curseur, attente ni modification des variables globales.
- Decimal est un Double binaire, pas .NET decimal. Comparer les valeurs finies approchées avec une tolérance. NaN/Infinity ne conviennent pas aux coordonnées ou quantités.
- Exp(0)=1. Très positif : Infinity ; très négatif : 0 par sous-dépassement. NaN inchangé.

### Fonctions internes : de l’appel au résultat

Étapes réelles de liaison/conversion. Les fonctions auxiliaires complètes montrent des formules de script, sans remplacer les mathématiques de la plateforme.

#### 1. Register

Register lie le nom BASIC à un calcul natif à un argument, puis System.Math après conversion. Aucun script caché ni traitement serveur.

Decimal — e^power. Exp(0)=1. Très positif : Infinity ; très négatif : 0 par sous-dépassement. NaN inchangé. Nombre, pas un ID ni un indicateur de réussite. 1/0 ne signifient pas réussite/échec.

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
# Élève e à une puissance.
#
# Decimal — e^power. Exp(0)=1. Très positif : Infinity ; très négatif : 0 par sous-dépassement.
# NaN inchangé. Nombre, pas un ID ni un indicateur de réussite. 1/0 ne signifient pas
# réussite/échec.

SUB Main()
    # power = 0 ; résultat attendu 1 (~ : approximation). value conserve le résultat ; CStr le
    # formate pour Print.

    VAR value = Exp(0)
    UO.Print(CStr(value))
END SUB
```

**Explication des paramètres et du déroulement:**

- power = 0 ; résultat attendu 1 (~ : approximation). value conserve le résultat ; CStr le formate pour Print.

### Autre argument via une variable

```vb
# Autre argument via une variable
#
# Élève e à une puissance.
#
# Decimal — e^power. Exp(0)=1. Très positif : Infinity ; très négatif : 0 par sous-dépassement.
# NaN inchangé. Nombre, pas un ID ni un indicateur de réussite. 1/0 ne signifient pas
# réussite/échec.

SUB Main()
    # power = 1 ; résultat attendu ~2.718281828459045 (~ : approximation). value conserve le
    # résultat ; CStr le formate pour Print.

    VAR inputValue = 1
    VAR value = Exp(inputValue)
    UO.Print(CStr(value))
END SUB
```

**Explication des paramètres et du déroulement:**

- power = 1 ; résultat attendu ~2.718281828459045 (~ : approximation). value conserve le résultat ; CStr le formate pour Print.

### Fonction auxiliaire complète

```vb
# Fonction auxiliaire complète
#
# Élève e à une puissance.
#
# Decimal — e^power. Exp(0)=1. Très positif : Infinity ; très négatif : 0 par sous-dépassement.
# NaN inchangé. Nombre, pas un ID ni un indicateur de réussite. 1/0 ne signifient pas
# réussite/échec.

# manual-check: scalar-math Exp
SUB Main()
    # value : valeur initiale ; rate : croissance continue par unité ; period : durée dans cette
    # unité. Growth(100,0.05,2)≈110.517 ; exemple numérique.

    VAR value = Growth(100,0.05,2)
    UO.Print(CStr(value))
END SUB

SUB Growth(value,rate,period)
    RETURN value*Exp(rate*period)
END SUB
```

**Explication des paramètres et du déroulement:**

- value : valeur initiale ; rate : croissance continue par unité ; period : durée dans cette unité. Growth(100,0.05,2)≈110.517 ; exemple numérique.
