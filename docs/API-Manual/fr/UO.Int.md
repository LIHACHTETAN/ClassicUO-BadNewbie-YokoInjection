# UO.Int

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: fr -->

Lit l’Intelligence actuelle (INT).

## Syntaxe exacte

```text
UO.Int() -> Integer
```

## Paramètres

Aucun paramètre.

## Retour

Integer — points actuels, 0..65535 dans le modèle, pas pourcentage, ID, compétence, verrouillage ni Boolean. 0 peut aussi indiquer un personnage absent/détruit ou un sujet indisponible. Comparer à un seuil numérique, pas = TRUE. Ce n’est ni le plafond ni nécessairement la valeur de base sans bonus.

## Comportement

- Aucun argument. Respecter les signatures affichées.
- Lit Player.Intelligence si Player existe et n’est pas détruit, sinon 0. Un personnage mort encore présent n’est pas un objet détruit. Aucune déduction à partir des HP, du mana ou de l’endurance.
- GetStr/GetInt/GetDex acceptent ObjID, mais ces attributs sont stockés uniquement dans PlayerMobile : tout autre serial donne 0, même pour un mobile chargé. Limitation par rapport à la description générale Stealth ; aucune statistique distante n’est inventée.
- Invoke lit sur le fil du jeu ; l’attente respecte l’annulation du script. Aucun paquet, demande de status, ciblage, modification ni délai intégré.
- Chaque appel relit les données locales. Une variable conserve un instantané ; plusieurs lectures peuvent voir différentes mises à jour. Un résultat non nul ne prouve pas la connexion ; zéro peut être une valeur ou une absence de données.
- Noms équivalents avec ou sans UO., insensibles à la casse : `Int Intelligence GetInt GetIntelligence`.
- Int(value) sans UO. arrondit un nombre BASIC vers le bas ; Str(value) le formate en texte. Ces opérations diffèrent de UO.Int()/UO.Str(), lectures d’attributs. GetInt(ObjID) n’est pas un arrondi.

### Fonctions internes : de l’appel au résultat

Étapes natives de lecture. AttributeAtLeast est une fonction BASIC utilisateur entièrement définie ci-dessous, pas une API cachée ni une modification d’attribut.

#### 1. RegisterCharacterGetterAliases

RegisterCharacterGetterAliases ajoute les fonctions sans argument et intrinsèques manquantes. Les branches de compatibilité existantes choisissent leur getter ; les deux chemins renvoient Integer. Un intrinsèque est relu sauf si une variable le masque.

Noms équivalents avec ou sans UO., insensibles à la casse : `Int Intelligence GetInt GetIntelligence`.

Source du projet: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; fonction `RegisterCharacterGetterAliases`.

#### 2. Invoke

Lit Player.Intelligence si Player existe et n’est pas détruit, sinon 0. Un personnage mort encore présent n’est pas un objet détruit. Aucune déduction à partir des HP, du mana ou de l’endurance. Invoke lit sur le fil du jeu ; l’attente respecte l’annulation du script. Aucun paquet, demande de status, ciblage, modification ni délai intégré.

Integer — points actuels, 0..65535 dans le modèle, pas pourcentage, ID, compétence, verrouillage ni Boolean. 0 peut aussi indiquer un personnage absent/détruit ou un sujet indisponible. Comparer à un seuil numérique, pas = TRUE. Ce n’est ni le plafond ni nécessairement la valeur de base sans bonus. Chaque appel relit les données locales. Une variable conserve un instantané ; plusieurs lectures peuvent voir différentes mises à jour. Un résultat non nul ne prouve pas la connexion ; zéro peut être une valeur ou une absence de données.

Source du projet: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; fonction `Invoke`.

#### 3. CharacterStatus

CharacterStatus affecte le champ STR/DEX/INT reçu à Player.Intelligence pour un paquet de status personnel applicable. La commande lit ce cache sans attendre un nouveau paquet.

Invoke lit sur le fil du jeu ; l’attente respecte l’annulation du script. Aucun paquet, demande de status, ciblage, modification ni délai intégré.

Source du projet: `src/ClassicUO.Client/Network/PacketHandlers.cs`; fonction `CharacterStatus`.

#### 4. Clear

World.Clear retire Player. Les lectures donnent ensuite 0 jusqu’au retour du personnage et de ses données. Une valeur sauvegardée ne prouve pas qu’un seuil est atteint après reconnexion.

Integer — points actuels, 0..65535 dans le modèle, pas pourcentage, ID, compétence, verrouillage ni Boolean. 0 peut aussi indiquer un personnage absent/détruit ou un sujet indisponible. Comparer à un seuil numérique, pas = TRUE. Ce n’est ni le plafond ni nécessairement la valeur de base sans bonus.

Source du projet: `src/ClassicUO.Client/Game/World.cs`; fonction `Clear`.

World.Clear retire Player. Les lectures donnent ensuite 0 jusqu’au retour du personnage et de ses données. Une valeur sauvegardée ne prouve pas qu’un seuil est atteint après reconnexion.


## Exemples

### Afficher les points

```vb
# Afficher les points
#
# Lit l’Intelligence actuelle (INT).
#
# Integer — points actuels, 0..65535 dans le modèle, pas pourcentage, ID, compétence,
# verrouillage ni Boolean. 0 peut aussi indiquer un personnage absent/détruit ou un sujet
# indisponible. Comparer à un seuil numérique, pas = TRUE. Ce n’est ni le plafond ni
# nécessairement la valeur de base sans bonus.

SUB Main()
    # value contient le nombre ; CStr le formate pour le journal. Aucun argument ni action du
    # personnage.

    VAR value = UO.Int()
    UO.Print('Intelligence: ' + CStr(value))
END SUB
```

**Explication des paramètres et du déroulement:**

- value contient le nombre ; CStr le formate pour le journal. Aucun argument ni action du personnage.

### Comparer deux observations

```vb
# Comparer deux observations
#
# Lit l’Intelligence actuelle (INT).
#
# Integer — points actuels, 0..65535 dans le modèle, pas pourcentage, ID, compétence,
# verrouillage ni Boolean. 0 peut aussi indiquer un personnage absent/détruit ou un sujet
# indisponible. Comparer à un seuil numérique, pas = TRUE. Ce n’est ni le plafond ni
# nécessairement la valeur de base sans bonus.

SUB Main()
    # before/after sont séparés de 1000 ms ; WAIT appartient à l’exemple. change=after-before peut
    # être positif, nul ou négatif, sans distinguer toutes les mises à jour intermédiaires ou une
    # déconnexion.

    VAR before = UO.Int()
    WAIT(1000)
    VAR after = UO.Int()
    VAR change = after - before
    UO.Print('Change: ' + CStr(change))
END SUB
```

**Explication des paramètres et du déroulement:**

- before/after sont séparés de 1000 ms ; WAIT appartient à l’exemple. change=after-before peut être positif, nul ou négatif, sans distinguer toutes les mises à jour intermédiaires ou une déconnexion.

### Fonction complète de vérification

```vb
# Fonction complète de vérification
#
# Lit l’Intelligence actuelle (INT).
#
# Integer — points actuels, 0..65535 dans le modèle, pas pourcentage, ID, compétence,
# verrouillage ni Boolean. 0 peut aussi indiquer un personnage absent/détruit ou un sujet
# indisponible. Comparer à un seuil numérique, pas = TRUE. Ce n’est ni le plafond ni
# nécessairement la valeur de base sans bonus.

SUB Main()
    # minimum=80 est un seuil d’exemple. AttributeAtLeast(minimum) rejette un personnage absent, lit
    # une fois puis renvoie Integer Boolean 1=TRUE ou 0=FALSE selon >= minimum. C’est la comparaison
    # qui est logique, pas l’attribut.

    IF AttributeAtLeast(80) = TRUE THEN
        UO.Print('Requirement met')
    ELSE
        UO.Print('Requirement not met or no player')
    END IF
END SUB

SUB AttributeAtLeast(minimum)
    IF UO.Self() = 0 THEN
        RETURN FALSE
    END IF
    VAR value = UO.Int()
    RETURN value >= minimum
END SUB
```

**Explication des paramètres et du déroulement:**

- minimum=80 est un seuil d’exemple. AttributeAtLeast(minimum) rejette un personnage absent, lit une fois puis renvoie Integer Boolean 1=TRUE ou 0=FALSE selon >= minimum. C’est la comparaison qui est logique, pas l’attribut.
