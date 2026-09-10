# UO.GetPhysicalResist

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: fr -->

Lit le champ de résistance du joueur actuel : armure/résistance physique.

## Syntaxe exacte

```text
UO.GetPhysicalResist() -> Integer
```

## Paramètres

Aucun paramètre.

## Retour

Integer — valeur signée du status, -32768..32767 dans le modèle. Les valeurs négatives sont conservées. 0 peut être réel, inconnu ou dû à Player absent/détruit ; GetResist renvoie aussi 0 pour un sélecteur inconnu. Ni Boolean, ID, compétence ni plafond. 1 signifie un point, pas un succès.

## Comportement

- Aucun argument. Respecter les signatures affichées.
- Lit Player.PhysicalResistance sur le fil du jeu si Player existe sans être détruit ; sinon 0. Aucun parcours de l’équipement, calcul de bonus, requête status ou attente. Un fantôme présent n’est pas un Player détruit.
- PhysicalResistance est le champ armure/status du serveur : indice d’armure selon les règles classiques, résistance physique selon les règles à résistances. Aucune conversion entre règles ni calcul du pourcentage de dégâts évités. Armor et les alias physiques lisent ce même champ.
- CharacterStatus valide le corps fixe avant toute modification, puis convertit les mots de résistance en Int16 signé. Un corps tronqué conserve les données. La fin optionnelle du type 6 garde son comportement existant ; ces getters ne lisent pas ses plafonds de résistance.
- Chaque appel relit les données locales. Une variable conserve un instantané ; plusieurs lectures peuvent voir différentes mises à jour. Un résultat non nul ne prouve pas la connexion ; zéro peut être une valeur ou une absence de données.
- RegisterCharacterGetterAliases ajoute les fonctions sans argument et intrinsèques manquants ; les branches existantes lisent le même champ. Noms insensibles à la casse ; intrinsèque sans parenthèses relu sauf si une variable le masque.

### Fonctions internes : de l’appel au résultat

Étapes natives de lecture locale. ResistanceAtLeast ci-dessous est une fonction BASIC utilisateur complète, pas une API cachée ni une commande d’équipement.

#### 1. RegisterCharacterGetterAliases

RegisterCharacterGetterAliases ajoute les fonctions sans argument et intrinsèques manquants ; les branches existantes lisent le même champ. Noms insensibles à la casse ; intrinsèque sans parenthèses relu sauf si une variable le masque.

`Armor PhysicalResist ResistPhysical GetArmor GetPhysicalResist GetResistPhysical`.

Source du projet: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; fonction `RegisterCharacterGetterAliases`.

#### 2. Invoke

Lit Player.PhysicalResistance sur le fil du jeu si Player existe sans être détruit ; sinon 0. Aucun parcours de l’équipement, calcul de bonus, requête status ou attente. Un fantôme présent n’est pas un Player détruit.

Invoke lit sur le fil du jeu ; l’attente respecte l’annulation du script. Aucun paquet, demande de status, ciblage, modification ni délai intégré.

Source du projet: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; fonction `Invoke`.

#### 3. CharacterStatus

CharacterStatus valide le corps fixe avant toute modification, puis convertit les mots de résistance en Int16 signé. Un corps tronqué conserve les données. La fin optionnelle du type 6 garde son comportement existant ; ces getters ne lisent pas ses plafonds de résistance.

PhysicalResistance est le champ armure/status du serveur : indice d’armure selon les règles classiques, résistance physique selon les règles à résistances. Aucune conversion entre règles ni calcul du pourcentage de dégâts évités. Armor et les alias physiques lisent ce même champ.

Source du projet: `src/ClassicUO.Client/Network/PacketHandlers.cs`; fonction `CharacterStatus`.

#### 4. Clear

World.Clear retire Player. Les lectures donnent ensuite 0 jusqu’au retour du personnage et de ses données. Une valeur sauvegardée ne prouve pas qu’un seuil est atteint après reconnexion.

Integer — valeur signée du status, -32768..32767 dans le modèle. Les valeurs négatives sont conservées. 0 peut être réel, inconnu ou dû à Player absent/détruit ; GetResist renvoie aussi 0 pour un sélecteur inconnu. Ni Boolean, ID, compétence ni plafond. 1 signifie un point, pas un succès.

Source du projet: `src/ClassicUO.Client/Game/World.cs`; fonction `Clear`.

Chaque appel relit les données locales. Une variable conserve un instantané ; plusieurs lectures peuvent voir différentes mises à jour. Un résultat non nul ne prouve pas la connexion ; zéro peut être une valeur ou une absence de données.


## Exemples

### Afficher la valeur en cache

```vb
# Afficher la valeur en cache
#
# Lit le champ de résistance du joueur actuel : armure/résistance physique.
#
# Integer — valeur signée du status, -32768..32767 dans le modèle. Les valeurs négatives sont
# conservées. 0 peut être réel, inconnu ou dû à Player absent/détruit ; GetResist renvoie aussi
# 0 pour un sélecteur inconnu. Ni Boolean, ID, compétence ni plafond. 1 signifie un point, pas
# un succès.

SUB Main()
    # value conserve une lecture sans argument du joueur ; CStr la formate pour le journal.

    VAR value = UO.GetPhysicalResist()
    UO.Print('PhysicalResistance: ' + CStr(value))
END SUB
```

**Explication des paramètres et du déroulement:**

- value conserve une lecture sans argument du joueur ; CStr la formate pour le journal.

### Comparer deux observations

```vb
# Comparer deux observations
#
# Lit le champ de résistance du joueur actuel : armure/résistance physique.
#
# Integer — valeur signée du status, -32768..32767 dans le modèle. Les valeurs négatives sont
# conservées. 0 peut être réel, inconnu ou dû à Player absent/détruit ; GetResist renvoie aussi
# 0 pour un sélecteur inconnu. Ni Boolean, ID, compétence ni plafond. 1 signifie un point, pas
# un succès.

SUB Main()
    # WAIT(500) sépare before et after de 500 ms ; difference peut être négative. Des mises à jour
    # intermédiaires peuvent échapper. Cette attente appartient à l’exemple.

    VAR before = UO.GetPhysicalResist()
    WAIT(500)
    VAR after = UO.GetPhysicalResist()
    VAR difference = after - before
    UO.Print('Resistance change: ' + CStr(difference))
END SUB
```

**Explication des paramètres et du déroulement:**

- WAIT(500) sépare before et after de 500 ms ; difference peut être négative. Des mises à jour intermédiaires peuvent échapper. Cette attente appartient à l’exemple.

### Fonction complète de résistance minimale

```vb
# Fonction complète de résistance minimale
#
# Lit le champ de résistance du joueur actuel : armure/résistance physique.
#
# Integer — valeur signée du status, -32768..32767 dans le modèle. Les valeurs négatives sont
# conservées. 0 peut être réel, inconnu ou dû à Player absent/détruit ; GetResist renvoie aussi
# 0 pour un sélecteur inconnu. Ni Boolean, ID, compétence ni plafond. 1 signifie un point, pas
# un succès.

SUB Main()
    # minimum=50 est un exemple, pas un plafond. ResistanceAtLeast rejette Player absent, lit une
    # valeur et renvoie Integer Boolean 1=TRUE ou 0=FALSE selon value >= minimum. La résistance
    # elle-même n’est pas Boolean. Fonction définie entièrement ci-dessous.

    IF ResistanceAtLeast(50) = TRUE THEN
        UO.Print('Local resistance requirement met')
    ELSE
        UO.Print('Requirement not met or no player')
    END IF
END SUB

SUB ResistanceAtLeast(minimum)
    IF UO.Self() = 0 THEN
        RETURN FALSE
    END IF
    VAR value = UO.GetPhysicalResist()
    RETURN value >= minimum
END SUB
```

**Explication des paramètres et du déroulement:**

- minimum=50 est un exemple, pas un plafond. ResistanceAtLeast rejette Player absent, lit une valeur et renvoie Integer Boolean 1=TRUE ou 0=FALSE selon value >= minimum. La résistance elle-même n’est pas Boolean. Fonction définie entièrement ci-dessous.
