# UO.GetResist

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: fr -->

Lit une résistance du joueur actuel selon un sélecteur numérique ou textuel.

## Syntaxe exacte

```text
UO.GetResist(resistance:Any) -> Integer
```

## Paramètres

- `resistance` — resistance obligatoire : nombres 0=physical, 1=fire, 2=cold, 3=poison, 4=energy ; textes physical/phys/armor, fire, cold, poison, energy. Casse et espaces extérieurs ignorés. Aucun serial, type, hue, curseur ou deuxième argument.

## Retour

Integer — valeur signée du status, -32768..32767 dans le modèle. Les valeurs négatives sont conservées. 0 peut être réel, inconnu ou dû à Player absent/détruit ; GetResist renvoie aussi 0 pour un sélecteur inconnu. Ni Boolean, ID, compétence ni plafond. 1 signifie un point, pas un succès.

## Comportement

- Le type est examiné avant conversion : "1" et "0" sont des noms inconnus et donnent 0. Un Decimal non textuel est tronqué vers zéro : 1.9 -> fire, -0.9 -> physical. TRUE=1 choisit fire, FALSE=0 choisit physical ; Array/Unit deviennent aussi 0. Employer un entier ou un nom prévu. Aucun alias AddObject résolu.
- GetResistance choisit un seul getter du bridge ; nombre/nom inconnu donne Integer 0 sans lecture. Aucun relevé atomique des cinq champs ni modification des résistances.
- PhysicalResistance est le champ armure/status du serveur : indice d’armure selon les règles classiques, résistance physique selon les règles à résistances. Aucune conversion entre règles ni calcul du pourcentage de dégâts évités. Armor et les alias physiques lisent ce même champ.
- Les champs élémentaires arrivent par CharacterStatus (0x11), type >= 4. Le getter ne vérifie pas l’ère du serveur. Un status compact/ancien sans ces champs garde le cache antérieur ; un nouveau Player commence à 0. Résistance au poison ≠ Poisoned ; aucune de ces valeurs n’est la compétence Resisting Spells.
- CharacterStatus valide le corps fixe avant toute modification, puis convertit les mots de résistance en Int16 signé. Un corps tronqué conserve les données. La fin optionnelle du type 6 garde son comportement existant ; ces getters ne lisent pas ses plafonds de résistance.
- Invoke lit sur le fil du jeu ; l’attente respecte l’annulation du script. Aucun paquet, demande de status, ciblage, modification ni délai intégré.
- Chaque appel relit les données locales. Une variable conserve un instantané ; plusieurs lectures peuvent voir différentes mises à jour. Un résultat non nul ne prouve pas la connexion ; zéro peut être une valeur ou une absence de données.

### Fonctions internes : de l’appel au résultat

Étapes natives de lecture locale. ResistanceAtLeast ci-dessous est une fonction BASIC utilisateur complète, pas une API cachée ni une commande d’équipement.

#### 1. RegisterCharacterGetterAliases

Enregistre GetResist(resistance) et UO.GetResist(resistance), fonctions à un argument liées à GetResistance. Aucun intrinsèque sans argument pour ce sélecteur.

resistance obligatoire : nombres 0=physical, 1=fire, 2=cold, 3=poison, 4=energy ; textes physical/phys/armor, fire, cold, poison, energy. Casse et espaces extérieurs ignorés. Aucun serial, type, hue, curseur ou deuxième argument.

Source du projet: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; fonction `RegisterCharacterGetterAliases`.

#### 2. GetResistance

Le type est examiné avant conversion : "1" et "0" sont des noms inconnus et donnent 0. Un Decimal non textuel est tronqué vers zéro : 1.9 -> fire, -0.9 -> physical. TRUE=1 choisit fire, FALSE=0 choisit physical ; Array/Unit deviennent aussi 0. Employer un entier ou un nom prévu. Aucun alias AddObject résolu.

`0: PhysicalResistance; 1: FireResistance; 2: ColdResistance; 3: PoisonResistance; 4: EnergyResistance`. GetResistance choisit un seul getter du bridge ; nombre/nom inconnu donne Integer 0 sans lecture. Aucun relevé atomique des cinq champs ni modification des résistances.

Source du projet: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; fonction `GetResistance`.

#### 3. ToInt

ToInt reçoit ici uniquement un sélecteur non textuel. Integer inchangé, Decimal tronqué vers zéro, Array/Unit donnent 0. Le résultat est un indice, pas une résistance. GetResistance traite les noms textuels.

`0: PhysicalResistance; 1: FireResistance; 2: ColdResistance; 3: PoisonResistance; 4: EnergyResistance`.

Source du projet: `external/InjectionScript/src/InjectionScript/Runtime/NumberConversions.cs`; fonction `ToInt`.

#### 4. Invoke

Invoke lit le champ Player sélectionné dans la table ci-dessus en conservant le signe. Player absent/détruit donne 0. Aucune demande status ni attente de nouvelles données.

Invoke lit sur le fil du jeu ; l’attente respecte l’annulation du script. Aucun paquet, demande de status, ciblage, modification ni délai intégré.

Source du projet: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; fonction `Invoke`.

#### 5. CharacterStatus

CharacterStatus valide le corps fixe avant toute modification, puis convertit les mots de résistance en Int16 signé. Un corps tronqué conserve les données. La fin optionnelle du type 6 garde son comportement existant ; ces getters ne lisent pas ses plafonds de résistance.

PhysicalResistance est le champ armure/status du serveur : indice d’armure selon les règles classiques, résistance physique selon les règles à résistances. Aucune conversion entre règles ni calcul du pourcentage de dégâts évités. Armor et les alias physiques lisent ce même champ. Les champs élémentaires arrivent par CharacterStatus (0x11), type >= 4. Le getter ne vérifie pas l’ère du serveur. Un status compact/ancien sans ces champs garde le cache antérieur ; un nouveau Player commence à 0. Résistance au poison ≠ Poisoned ; aucune de ces valeurs n’est la compétence Resisting Spells.

Source du projet: `src/ClassicUO.Client/Network/PacketHandlers.cs`; fonction `CharacterStatus`.

#### 6. Clear

World.Clear retire Player. Les lectures donnent ensuite 0 jusqu’au retour du personnage et de ses données. Une valeur sauvegardée ne prouve pas qu’un seuil est atteint après reconnexion.

Integer — valeur signée du status, -32768..32767 dans le modèle. Les valeurs négatives sont conservées. 0 peut être réel, inconnu ou dû à Player absent/détruit ; GetResist renvoie aussi 0 pour un sélecteur inconnu. Ni Boolean, ID, compétence ni plafond. 1 signifie un point, pas un succès.

Source du projet: `src/ClassicUO.Client/Game/World.cs`; fonction `Clear`.

Chaque appel relit les données locales. Une variable conserve un instantané ; plusieurs lectures peuvent voir différentes mises à jour. Un résultat non nul ne prouve pas la connexion ; zéro peut être une valeur ou une absence de données.


## Exemples

### Choisir un nom avec casse mixte

```vb
# Choisir un nom avec casse mixte
#
# Lit une résistance du joueur actuel selon un sélecteur numérique ou textuel.
#
# Integer — valeur signée du status, -32768..32767 dans le modèle. Les valeurs négatives sont
# conservées. 0 peut être réel, inconnu ou dû à Player absent/détruit ; GetResist renvoie aussi
# 0 pour un sélecteur inconnu. Ni Boolean, ID, compétence ni plafond. 1 signifie un point, pas
# un succès.

SUB Main()
    # resistance=" FiRe " choisit le feu sans tenir compte de la casse ni des espaces extérieurs.
    # value reste signé ; aucun curseur.

    VAR value = UO.GetResist(' FiRe ')
    UO.Print('Fire resistance: ' + CStr(value))
END SUB
```

**Explication des paramètres et du déroulement:**

- resistance=" FiRe " choisit le feu sans tenir compte de la casse ni des espaces extérieurs. value reste signé ; aucun curseur.

### Comparer sélecteurs numérique et textuel

```vb
# Comparer sélecteurs numérique et textuel
#
# Lit une résistance du joueur actuel selon un sélecteur numérique ou textuel.
#
# Integer — valeur signée du status, -32768..32767 dans le modèle. Les valeurs négatives sont
# conservées. 0 peut être réel, inconnu ou dû à Player absent/détruit ; GetResist renvoie aussi
# 0 pour un sélecteur inconnu. Ni Boolean, ID, compétence ni plafond. 1 signifie un point, pas
# un succès.

SUB Main()
    # 2 choisit le froid, "poison" le poison. Ce ne sont pas des serials. La comparaison de deux
    # observations donne Boolean ; une résistance au poison ne signifie pas un empoisonnement.

    VAR cold = UO.GetResist(2)
    VAR poison = UO.GetResist('poison')
    IF cold < poison THEN
        UO.Print('Cold resistance is lower')
    ELSE
        UO.Print('Cold resistance is equal or higher')
    END IF
END SUB
```

**Explication des paramètres et du déroulement:**

- 2 choisit le froid, "poison" le poison. Ce ne sont pas des serials. La comparaison de deux observations donne Boolean ; une résistance au poison ne signifie pas un empoisonnement.

### Fonction complète de résistance minimale

```vb
# Fonction complète de résistance minimale
#
# Lit une résistance du joueur actuel selon un sélecteur numérique ou textuel.
#
# Integer — valeur signée du status, -32768..32767 dans le modèle. Les valeurs négatives sont
# conservées. 0 peut être réel, inconnu ou dû à Player absent/détruit ; GetResist renvoie aussi
# 0 pour un sélecteur inconnu. Ni Boolean, ID, compétence ni plafond. 1 signifie un point, pas
# un succès.

SUB Main()
    # minimum=50 est un exemple, pas un plafond. ResistanceAtLeast rejette Player absent, lit une
    # valeur et renvoie Integer Boolean 1=TRUE ou 0=FALSE selon value >= minimum. La résistance
    # elle-même n’est pas Boolean. Fonction définie entièrement ci-dessous.
    # selector est transmis tel quel à GetResist ; l’exemple utilise "fire". La fonction vérifie
    # Player, mais ni un sélecteur arbitraire ni la fraîcheur du status. Utiliser la liste
    # ci-dessus.

    IF ResistanceAtLeast('fire', 50) = TRUE THEN
        UO.Print('Local fire resistance requirement met')
    ELSE
        UO.Print('Requirement not met or no player')
    END IF
END SUB

SUB ResistanceAtLeast(selector, minimum)
    IF UO.Self() = 0 THEN
        RETURN FALSE
    END IF
    VAR value = UO.GetResist(selector)
    RETURN value >= minimum
END SUB
```

**Explication des paramètres et du déroulement:**

- minimum=50 est un exemple, pas un plafond. ResistanceAtLeast rejette Player absent, lit une valeur et renvoie Integer Boolean 1=TRUE ou 0=FALSE selon value >= minimum. La résistance elle-même n’est pas Boolean. Fonction définie entièrement ci-dessous.
- selector est transmis tel quel à GetResist ; l’exemple utilise "fire". La fonction vérifie Player, mais ni un sélecteur arbitraire ni la fraîcheur du status. Utiliser la liste ci-dessus.
