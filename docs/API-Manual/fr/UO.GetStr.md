# UO.GetStr

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: fr -->

Lit la Force actuelle (Strength, STR).

## Syntaxe exacte

```text
UO.GetStr() -> Integer
UO.GetStr(ObjID:Any) -> Integer
```

## Paramètres

- `ObjID` — ObjID, seulement dans la forme à un argument : serial entier, chaîne décimale/hexadécimale 0x, "self", "lasttarget" ou nom AddObject. Identifie le personnage, pas son graphic/type. Sans argument : personnage actuel.

## Retour

Integer — points actuels, 0..65535 dans le modèle, pas pourcentage, ID, compétence, verrouillage ni Boolean. 0 peut aussi indiquer un personnage absent/détruit ou un sujet indisponible. Comparer à un seuil numérique, pas = TRUE. Ce n’est ni le plafond ni nécessairement la valeur de base sans bonus.

## Comportement

- Formes acceptées : () pour self, (ObjID) pour un sujet explicite. Aucun autre argument facultatif.
- Lit Player.Strength si Player existe et n’est pas détruit, sinon 0. Un personnage mort encore présent n’est pas un objet détruit. Aucune déduction à partir des HP, du mana ou de l’endurance.
- GetStr/GetInt/GetDex acceptent ObjID, mais ces attributs sont stockés uniquement dans PlayerMobile : tout autre serial donne 0, même pour un mobile chargé. Limitation par rapport à la description générale Stealth ; aucune statistique distante n’est inventée.
- Invoke lit sur le fil du jeu ; l’attente respecte l’annulation du script. Aucun paquet, demande de status, ciblage, modification ni délai intégré.
- Chaque appel relit les données locales. Une variable conserve un instantané ; plusieurs lectures peuvent voir différentes mises à jour. Un résultat non nul ne prouve pas la connexion ; zéro peut être une valeur ou une absence de données.
- Noms équivalents avec ou sans UO., insensibles à la casse : `Str Strength GetStr GetStrength`.
- Int(value) sans UO. arrondit un nombre BASIC vers le bas ; Str(value) le formate en texte. Ces opérations diffèrent de UO.Int()/UO.Str(), lectures d’attributs. GetInt(ObjID) n’est pas un arrondi.
- ExecuteStealthCompatibility.Arg résout le nom d’objet avant conversion numérique. Un texte inconnu non numérique produit une erreur, pas un curseur. Decimal est converti en Integer ; Array/Unit en 0. Fournir un serial valide.

### Fonctions internes : de l’appel au résultat

Étapes natives de lecture. AttributeAtLeast est une fonction BASIC utilisateur entièrement définie ci-dessous, pas une API cachée ni une modification d’attribut.

#### 1. RegisterCharacterGetterAliases

RegisterCharacterGetterAliases ajoute les fonctions sans argument et intrinsèques manquantes. Les branches de compatibilité existantes choisissent leur getter ; les deux chemins renvoient Integer. Un intrinsèque est relu sauf si une variable le masque.

Noms équivalents avec ou sans UO., insensibles à la casse : `Str Strength GetStr GetStrength`.

Source du projet: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; fonction `RegisterCharacterGetterAliases`.

#### 2. ExecuteStealthCompatibility

ObjID, seulement dans la forme à un argument : serial entier, chaîne décimale/hexadécimale 0x, "self", "lasttarget" ou nom AddObject. Identifie le personnage, pas son graphic/type. Sans argument : personnage actuel.

ExecuteStealthCompatibility.Arg résout le nom d’objet avant conversion numérique. Un texte inconnu non numérique produit une erreur, pas un curseur. Decimal est converti en Integer ; Array/Unit en 0. Fournir un serial valide.

Source du projet: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; fonction `ExecuteStealthCompatibility`.

#### 3. GetStrength

GetStr/GetInt/GetDex acceptent ObjID, mais ces attributs sont stockés uniquement dans PlayerMobile : tout autre serial donne 0, même pour un mobile chargé. Limitation par rapport à la description générale Stealth ; aucune statistique distante n’est inventée.

Lit Player.Strength si Player existe et n’est pas détruit, sinon 0. Un personnage mort encore présent n’est pas un objet détruit. Aucune déduction à partir des HP, du mana ou de l’endurance.

Source du projet: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; fonction `GetStrength`.

#### 4. Invoke

Lit Player.Strength si Player existe et n’est pas détruit, sinon 0. Un personnage mort encore présent n’est pas un objet détruit. Aucune déduction à partir des HP, du mana ou de l’endurance. Invoke lit sur le fil du jeu ; l’attente respecte l’annulation du script. Aucun paquet, demande de status, ciblage, modification ni délai intégré.

Integer — points actuels, 0..65535 dans le modèle, pas pourcentage, ID, compétence, verrouillage ni Boolean. 0 peut aussi indiquer un personnage absent/détruit ou un sujet indisponible. Comparer à un seuil numérique, pas = TRUE. Ce n’est ni le plafond ni nécessairement la valeur de base sans bonus. Chaque appel relit les données locales. Une variable conserve un instantané ; plusieurs lectures peuvent voir différentes mises à jour. Un résultat non nul ne prouve pas la connexion ; zéro peut être une valeur ou une absence de données.

Source du projet: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; fonction `Invoke`.

#### 5. CharacterStatus

CharacterStatus affecte le champ STR/DEX/INT reçu à Player.Strength pour un paquet de status personnel applicable. La commande lit ce cache sans attendre un nouveau paquet.

Invoke lit sur le fil du jeu ; l’attente respecte l’annulation du script. Aucun paquet, demande de status, ciblage, modification ni délai intégré.

Source du projet: `src/ClassicUO.Client/Network/PacketHandlers.cs`; fonction `CharacterStatus`.

#### 6. Clear

World.Clear retire Player. Les lectures donnent ensuite 0 jusqu’au retour du personnage et de ses données. Une valeur sauvegardée ne prouve pas qu’un seuil est atteint après reconnexion.

Integer — points actuels, 0..65535 dans le modèle, pas pourcentage, ID, compétence, verrouillage ni Boolean. 0 peut aussi indiquer un personnage absent/détruit ou un sujet indisponible. Comparer à un seuil numérique, pas = TRUE. Ce n’est ni le plafond ni nécessairement la valeur de base sans bonus.

Source du projet: `src/ClassicUO.Client/Game/World.cs`; fonction `Clear`.

World.Clear retire Player. Les lectures donnent ensuite 0 jusqu’au retour du personnage et de ses données. Une valeur sauvegardée ne prouve pas qu’un seuil est atteint après reconnexion.


## Exemples

### Afficher les points

```vb
# Afficher les points
#
# Lit la Force actuelle (Strength, STR).
#
# Integer — points actuels, 0..65535 dans le modèle, pas pourcentage, ID, compétence,
# verrouillage ni Boolean. 0 peut aussi indiquer un personnage absent/détruit ou un sujet
# indisponible. Comparer à un seuil numérique, pas = TRUE. Ce n’est ni le plafond ni
# nécessairement la valeur de base sans bonus.

SUB Main()
    # value contient le nombre ; CStr le formate pour le journal. Aucun argument ni action du
    # personnage.

    VAR value = UO.GetStr()
    UO.Print('Strength: ' + CStr(value))
END SUB
```

**Explication des paramètres et du déroulement:**

- value contient le nombre ; CStr le formate pour le journal. Aucun argument ni action du personnage.

### Comparer deux observations

```vb
# Comparer deux observations
#
# Lit la Force actuelle (Strength, STR).
#
# Integer — points actuels, 0..65535 dans le modèle, pas pourcentage, ID, compétence,
# verrouillage ni Boolean. 0 peut aussi indiquer un personnage absent/détruit ou un sujet
# indisponible. Comparer à un seuil numérique, pas = TRUE. Ce n’est ni le plafond ni
# nécessairement la valeur de base sans bonus.

SUB Main()
    # before/after sont séparés de 1000 ms ; WAIT appartient à l’exemple. change=after-before peut
    # être positif, nul ou négatif, sans distinguer toutes les mises à jour intermédiaires ou une
    # déconnexion.

    VAR before = UO.GetStr()
    WAIT(1000)
    VAR after = UO.GetStr()
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
# Lit la Force actuelle (Strength, STR).
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
    VAR value = UO.GetStr()
    RETURN value >= minimum
END SUB
```

**Explication des paramètres et du déroulement:**

- minimum=80 est un seuil d’exemple. AttributeAtLeast(minimum) rejette un personnage absent, lit une fois puis renvoie Integer Boolean 1=TRUE ou 0=FALSE selon >= minimum. C’est la comparaison qui est logique, pas l’attribut.

### Choisir le personnage par serial et nom

```vb
# Choisir le personnage par serial et nom
#
# Lit la Force actuelle (Strength, STR).
#
# Integer — points actuels, 0..65535 dans le modèle, pas pourcentage, ID, compétence,
# verrouillage ni Boolean. 0 peut aussi indiquer un personnage absent/détruit ou un sujet
# indisponible. Comparer à un seuil numérique, pas = TRUE. Ce n’est ni le plafond ni
# nécessairement la valeur de base sans bonus.

SUB Main()
    # id vient de UO.Self(), pas d’un type. AddObject enregistre statSubject sans curseur car le
    # second argument est fourni. Les deux appels désignent le même sujet, mais les lectures ne sont
    # pas atomiques.

    VAR id = UO.Self()
    IF id <> 0 THEN
        UO.AddObject('statSubject', id)
        VAR direct = UO.GetStr(id)
        VAR byName = UO.GetStr('statSubject')
        UO.Print('Direct: ' + CStr(direct) + '; alias: ' + CStr(byName))
    END IF
END SUB
```

**Explication des paramètres et du déroulement:**

- id vient de UO.Self(), pas d’un type. AddObject enregistre statSubject sans curseur car le second argument est fourni. Les deux appels désignent le même sujet, mais les lectures ne sont pas atomiques.
