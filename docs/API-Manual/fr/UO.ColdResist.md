# UO.ColdResist

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: fr -->

Lit le champ de résistance du joueur actuel : froid.

## Syntaxe exacte

```text
UO.ColdResist() -> Integer
```

## Paramètres

Aucun paramètre.

## Retour

Integer — valeur signée du status, -32768..32767 dans le modèle. Les valeurs négatives sont conservées. 0 peut être réel, inconnu ou dû à Player absent/détruit ; GetResist renvoie aussi 0 pour un sélecteur inconnu. Ni Boolean, ID, compétence ni plafond. 1 signifie un point, pas un succès.

## Comportement

- Aucun argument. Respecter les signatures affichées.
- Lit Player.ColdResistance sur le fil du jeu si Player existe sans être détruit ; sinon 0. Aucun parcours de l’équipement, calcul de bonus, requête status ou attente. Un fantôme présent n’est pas un Player détruit.
- Les champs élémentaires arrivent par CharacterStatus (0x11), type >= 4. Le getter ne vérifie pas l’ère du serveur. Un status compact/ancien sans ces champs garde le cache antérieur ; un nouveau Player commence à 0. Résistance au poison ≠ Poisoned ; aucune de ces valeurs n’est la compétence Resisting Spells.
- CharacterStatus valide le corps fixe avant toute modification, puis convertit les mots de résistance en Int16 signé. Un corps tronqué conserve les données. La fin optionnelle du type 6 garde son comportement existant ; ces getters ne lisent pas ses plafonds de résistance.
- Chaque appel relit les données locales. Une variable conserve un instantané ; plusieurs lectures peuvent voir différentes mises à jour. Un résultat non nul ne prouve pas la connexion ; zéro peut être une valeur ou une absence de données.
- RegisterCharacterGetterAliases ajoute les fonctions sans argument et intrinsèques manquants ; les branches existantes lisent le même champ. Noms insensibles à la casse ; intrinsèque sans parenthèses relu sauf si une variable le masque.

### Fonctions internes : de l’appel au résultat

Étapes natives de lecture locale. ResistanceAtLeast ci-dessous est une fonction BASIC utilisateur complète, pas une API cachée ni une commande d’équipement.

#### 1. RegisterCharacterGetterAliases

RegisterCharacterGetterAliases ajoute les fonctions sans argument et intrinsèques manquants ; les branches existantes lisent le même champ. Noms insensibles à la casse ; intrinsèque sans parenthèses relu sauf si une variable le masque.

`ColdResist ResistCold GetColdResist GetResistCold`.

Source du projet: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; fonction `RegisterCharacterGetterAliases`.

#### 2. Invoke

Lit Player.ColdResistance sur le fil du jeu si Player existe sans être détruit ; sinon 0. Aucun parcours de l’équipement, calcul de bonus, requête status ou attente. Un fantôme présent n’est pas un Player détruit.

Invoke lit sur le fil du jeu ; l’attente respecte l’annulation du script. Aucun paquet, demande de status, ciblage, modification ni délai intégré.

Source du projet: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; fonction `Invoke`.

#### 3. CharacterStatus

CharacterStatus valide le corps fixe avant toute modification, puis convertit les mots de résistance en Int16 signé. Un corps tronqué conserve les données. La fin optionnelle du type 6 garde son comportement existant ; ces getters ne lisent pas ses plafonds de résistance.

Les champs élémentaires arrivent par CharacterStatus (0x11), type >= 4. Le getter ne vérifie pas l’ère du serveur. Un status compact/ancien sans ces champs garde le cache antérieur ; un nouveau Player commence à 0. Résistance au poison ≠ Poisoned ; aucune de ces valeurs n’est la compétence Resisting Spells.

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
# Lit le champ de résistance du joueur actuel : froid.
#
# Integer — valeur signée du status, -32768..32767 dans le modèle. Les valeurs négatives sont
# conservées. 0 peut être réel, inconnu ou dû à Player absent/détruit ; GetResist renvoie aussi
# 0 pour un sélecteur inconnu. Ni Boolean, ID, compétence ni plafond. 1 signifie un point, pas
# un succès.

SUB Main()
    # value conserve une lecture sans argument du joueur ; CStr la formate pour le journal.

    VAR value = UO.ColdResist()
    UO.Print('ColdResistance: ' + CStr(value))
END SUB
```

**Explication des paramètres et du déroulement:**

- value conserve une lecture sans argument du joueur ; CStr la formate pour le journal.

### Comparer deux observations

```vb
# Comparer deux observations
#
# Lit le champ de résistance du joueur actuel : froid.
#
# Integer — valeur signée du status, -32768..32767 dans le modèle. Les valeurs négatives sont
# conservées. 0 peut être réel, inconnu ou dû à Player absent/détruit ; GetResist renvoie aussi
# 0 pour un sélecteur inconnu. Ni Boolean, ID, compétence ni plafond. 1 signifie un point, pas
# un succès.

SUB Main()
    # WAIT(500) sépare before et after de 500 ms ; difference peut être négative. Des mises à jour
    # intermédiaires peuvent échapper. Cette attente appartient à l’exemple.

    VAR before = UO.ColdResist()
    WAIT(500)
    VAR after = UO.ColdResist()
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
# Lit le champ de résistance du joueur actuel : froid.
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
    VAR value = UO.ColdResist()
    RETURN value >= minimum
END SUB
```

**Explication des paramètres et du déroulement:**

- minimum=50 est un exemple, pas un plafond. ResistanceAtLeast rejette Player absent, lit une valeur et renvoie Integer Boolean 1=TRUE ou 0=FALSE selon value >= minimum. La résistance elle-même n’est pas Boolean. Fonction définie entièrement ci-dessous.
