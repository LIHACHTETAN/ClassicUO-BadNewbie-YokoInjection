# UO.ApiNameExists

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: fr -->

Vérifie un nom natif appelable.

## Syntaxe exacte

```text
UO.ApiNameExists(name:String) -> Integer
```

## Paramètres

- `name` — String obligatoire: nom enregistré exact, pas une expression d’appel. Casse et espaces extérieurs ignorés; aucun ajout de UO. Nom vide/inconnu: 0. Procédures utilisateur exclues.

## Retour

Integer 1 si enregistré, sinon 0; comparaisons avec TRUE/FALSE ou 1/0 possibles. Aucune confirmation d’objet, d’action ou d’autorisation serveur.

## Comportement

- La casse est ignorée. InjectionApi enregistre Basic sans préfixe, InjectionApiUO le jeu avec UO. Un ancien appel abrégé produit SC005 avec suggestion UO.; aucune exécution implicite. Les valeurs de caractéristiques exigent aussi UO. ApiNameExists, ApiSignatureExists et ApiParameterExists retirent les espaces extérieurs puis vérifient le nom exact sans ajouter de préfixe. Ils lisent les métadonnées, pas le serveur. GetType(TypeName), opérateur de réflexion VB.NET, est absent.

## Exemples

### UO.ApiNameExists — 1

```vb
# UO.ApiNameExists — 1
#
# Vérifie un nom natif appelable.
#
# Integer 1 si enregistré, sinon 0; comparaisons avec TRUE/FALSE ou 1/0 possibles. Aucune
# confirmation d’objet, d’action ou d’autorisation serveur.

SUB Main()
    # Le premier exemple vérifie un nom de jeu UO. explicite et renvoie 1. Nom exact et nombre
    # d’arguments éventuel figurent dans l’appel.

    RETURN UO.ApiNameExists('UO.GetType')
END SUB
```

**Explication des paramètres et du déroulement:**

- Le premier exemple vérifie un nom de jeu UO. explicite et renvoie 1. Nom exact et nombre d’arguments éventuel figurent dans l’appel.

### UO.ApiNameExists — 2

```vb
# UO.ApiNameExists — 2
#
# Vérifie un nom natif appelable.
#
# Integer 1 si enregistré, sinon 0; comparaisons avec TRUE/FALSE ou 1/0 possibles. Aucune
# confirmation d’objet, d’action ou d’autorisation serveur.

SUB Main()
    # Le deuxième vérifie Basic ou un sélecteur: Int(value) existe, Int() non; backpack est un
    # sélecteur. Résultat 1 ou "1:0" selon les appels.

    VAR name = 'CInt'
    RETURN UO.ApiNameExists(name)
END SUB
```

**Explication des paramètres et du déroulement:**

- Le deuxième vérifie Basic ou un sélecteur: Int(value) existe, Int() non; backpack est un sélecteur. Résultat 1 ou "1:0" selon les appels.

### UO.ApiNameExists — 3

```vb
# UO.ApiNameExists — 3
#
# Vérifie un nom natif appelable.
#
# Integer 1 si enregistré, sinon 0; comparaisons avec TRUE/FALSE ou 1/0 possibles. Aucune
# confirmation d’objet, d’action ou d’autorisation serveur.

SUB Main()
    # Le troisième définit tout le helper et compare une forme courte supprimée ou une arité absente
    # à une forme valide. name, first, second, count transmettent noms/nombre sans modification.
    # Résultat 0 pour les appels, "0:1" pour les valeurs.

    RETURN HasBoth('GetType','UO.GetType')
END SUB

FUNCTION HasBoth(first,second)
    RETURN UO.ApiNameExists(first) AndAlso UO.ApiNameExists(second)
END FUNCTION
```

**Explication des paramètres et du déroulement:**

- Le troisième définit tout le helper et compare une forme courte supprimée ou une arité absente à une forme valide. name, first, second, count transmettent noms/nombre sans modification. Résultat 0 pour les appels, "0:1" pour les valeurs.
