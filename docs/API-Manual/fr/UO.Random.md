# UO.Random

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: fr -->

Choisit un entier pseudo-aléatoire. Random(min,max) inclut les deux bornes ; l’ancienne forme Random(max) exclut la borne supérieure.

## Syntaxe exacte

```text
UO.Random(max:Integer) -> Integer
UO.Random(min:Integer, max:Integer) -> Integer
```

## Paramètres

- `min` — Borne inférieure, uniquement avec deux arguments. Entier signé sur 32 bits, de -2147483648 à 2147483647 ; doit être <= max.
- `max` — Deux arguments : borne supérieure incluse, tout Integer signé. Un argument : borne supérieure exclue, 0..2147483647. Random(0) renvoie 0.

## Retour

Integer — un nombre choisi, pas un booléen ni un serial. Deux arguments : min <= résultat <= max. Un argument positif : 0 <= résultat < max. Les répétitions sont possibles.

## Comportement

- Aucune forme sans argument. Des bornes égales donnent cette valeur. Des bornes inversées ou un argument unique négatif provoquent une erreur de script ; elles ne sont pas permutées.
- Toute la plage signée sur 32 bits est prise en charge sans débordement de max+1. Pour des fractions discrètes, divisez des entiers : Random(0,100)/100.0.
- Le générateur appartient au runtime du script ; les appels simultanés sont synchronisés. Aucun paramètre seed ; cette fonction diffère de BASIC Rnd. Mémorisez le résultat pour le réutiliser.
- L’appel est local : aucune attente, aucun déplacement ni paquet réseau. Vérifiez les coordonnées tirées au sort ; Random(0)=0 ne fournit pas d’indice valide à un tableau vide.

## Exemples

### Lancer un dé

```vb
# Lancer un dé
#
# Choisit un entier pseudo-aléatoire. Random(min,max) inclut les deux bornes ; l’ancienne forme
# Random(max) exclut la borne supérieure.
#
# Integer — un nombre choisi, pas un booléen ni un serial. Deux arguments : min <= résultat <=
# max. Un argument positif : 0 <= résultat < max. Les répétitions sont possibles.

SUB Main()
    # min=1 et max=6 incluent les six valeurs. roll conserve un tirage ; STR le convertit en texte.
    # Un autre appel peut donner la même valeur.

    VAR roll = UO.Random(1, 6)
    UO.Print(STR(roll))
END SUB
```

**Explication des paramètres et du déroulement:**

- min=1 et max=6 incluent les six valeurs. roll conserve un tirage ; STR le convertit en texte. Un autre appel peut donner la même valeur.

### Attendre un délai aléatoire

```vb
# Attendre un délai aléatoire
#
# Choisit un entier pseudo-aléatoire. Random(min,max) inclut les deux bornes ; l’ancienne forme
# Random(max) exclut la borne supérieure.
#
# Integer — un nombre choisi, pas un booléen ni un serial. Deux arguments : min <= résultat <=
# max. Un argument positif : 0 <= résultat < max. Les répétitions sont possibles.

SUB Main()
    # min=350 et max=700 sont des millisecondes inclusives. Random calcule delay ; UO.Wait(delay)
    # attend. Respectez le délai minimal requis par le serveur.

    VAR delay = UO.Random(350, 700)
    UO.Print(STR(delay))
    UO.Wait(delay)
END SUB
```

**Explication des paramètres et du déroulement:**

- min=350 et max=700 sont des millisecondes inclusives. Random calcule delay ; UO.Wait(delay) attend. Respectez le délai minimal requis par le serveur.

### Indices historiques et bornes égales

```vb
# Indices historiques et bornes égales
#
# Choisit un entier pseudo-aléatoire. Random(min,max) inclut les deux bornes ; l’ancienne forme
# Random(max) exclut la borne supérieure.
#
# Integer — un nombre choisi, pas un booléen ni un serial. Deux arguments : min <= résultat <=
# max. Un argument positif : 0 <= résultat < max. Les répétitions sont possibles.

SUB Main()
    # Random(10) donne 0..9, jamais 10. Random(7,7) donne toujours 7. Random(-2,2) peut donner
    # -2,-1,0,1,2. Chaque expression effectue un tirage distinct.

    VAR index = UO.Random(10)
    VAR fixedValue = UO.Random(7, 7)
    VAR offset = UO.Random(-2, 2)
    UO.Print(STR(index) + ', ' + STR(fixedValue) + ', ' + STR(offset))
END SUB
```

**Explication des paramètres et du déroulement:**

- Random(10) donne 0..9, jamais 10. Random(7,7) donne toujours 7. Random(-2,2) peut donner -2,-1,0,1,2. Chaque expression effectue un tirage distinct.
