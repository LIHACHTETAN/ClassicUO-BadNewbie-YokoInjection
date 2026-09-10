# UO.GetMaxWeight

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: fr -->

Lit le compteur de status du joueur actuel : poids maximal en stones.

## Syntaxe exacte

```text
UO.GetMaxWeight() -> Integer
```

## Paramètres

Aucun paramètre.

## Retour

Integer — poids maximal en stones, 0..65535 dans le modèle. 0 peut être réel, inconnu ou dû à Player absent/détruit. Quantité, pas Boolean, ID ou type : 1 signifie une unité, pas un succès. Aucun parcours d’objets ni tableau retourné.

## Comportement

- Aucun argument. Respecter les signatures affichées.
- Lit Player.WeightMax sur le fil du jeu si Player existe sans être détruit ; sinon 0. Aucun parcours de l’équipement, calcul de bonus, requête status ou attente. Un fantôme présent n’est pas un Player détruit.
- MaxWeight lit WeightMax en cache. Le status propre de type >= 5 fournit la limite UInt16 du serveur, même 0. Un ancien status étendu la calcule à sa réception : protocole UO >= 5.0.0a, 7 * floor(STR / 2) + 40 ; sinon STR * 4 + 25. Stockage UInt16, donc bouclage modulo 65536 aux extrêmes. STR=101 donne 390 ou 429. Le getter ne recalcule pas si STR change séparément.
- CharacterStatus valide son corps fixe avant modification. Weight vient du status propre étendu, les emplacements du type 3, Luck du type 4 et WeightMax serveur du type 5. Un paquet compact/ancien sans compteur optionnel conserve le cache. Un nouveau Player commence à zéro ; la query ne prouve pas un status récent.
- RegisterCharacterGetterAliases ajoute les fonctions sans argument et intrinsèques manquants ; les branches existantes lisent le même champ. Noms insensibles à la casse ; intrinsèque sans parenthèses relu sauf si une variable le masque.
- Chaque appel relit les données locales. Une variable conserve un instantané ; plusieurs lectures peuvent voir différentes mises à jour. Un résultat non nul ne prouve pas la connexion ; zéro peut être une valeur ou une absence de données.

### Fonctions internes : de l’appel au résultat

Étapes natives de lecture du cache. CanCarry, LuckAtLeast ou CanAddFollower est une fonction BASIC utilisateur complète dans l’exemple, pas une action native cachée. Aucun inventaire ou familier modifié.

#### 1. RegisterCharacterGetterAliases

RegisterCharacterGetterAliases ajoute les fonctions sans argument et intrinsèques manquants ; les branches existantes lisent le même champ. Noms insensibles à la casse ; intrinsèque sans parenthèses relu sauf si une variable le masque.

`MaxWeight GetMaxWeight`.

Source du projet: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; fonction `RegisterCharacterGetterAliases`.

#### 2. Invoke

Lit Player.WeightMax sur le fil du jeu si Player existe sans être détruit ; sinon 0. Aucun parcours de l’équipement, calcul de bonus, requête status ou attente. Un fantôme présent n’est pas un Player détruit.

Invoke lit sur le fil du jeu ; l’attente respecte l’annulation du script. Aucun paquet, demande de status, ciblage, modification ni délai intégré.

Source du projet: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; fonction `Invoke`.

#### 3. CharacterStatus

CharacterStatus valide son corps fixe avant modification. Weight vient du status propre étendu, les emplacements du type 3, Luck du type 4 et WeightMax serveur du type 5. Un paquet compact/ancien sans compteur optionnel conserve le cache. Un nouveau Player commence à zéro ; la query ne prouve pas un status récent.

MaxWeight lit WeightMax en cache. Le status propre de type >= 5 fournit la limite UInt16 du serveur, même 0. Un ancien status étendu la calcule à sa réception : protocole UO >= 5.0.0a, 7 * floor(STR / 2) + 40 ; sinon STR * 4 + 25. Stockage UInt16, donc bouclage modulo 65536 aux extrêmes. STR=101 donne 390 ou 429. Le getter ne recalcule pas si STR change séparément.

Source du projet: `src/ClassicUO.Client/Network/PacketHandlers.cs`; fonction `CharacterStatus`.

#### 4. Clear

World.Clear retire Player. Les lectures donnent ensuite 0 jusqu’au retour du personnage et de ses données. Une valeur sauvegardée ne prouve pas qu’un seuil est atteint après reconnexion.

Integer — poids maximal en stones, 0..65535 dans le modèle. 0 peut être réel, inconnu ou dû à Player absent/détruit. Quantité, pas Boolean, ID ou type : 1 signifie une unité, pas un succès. Aucun parcours d’objets ni tableau retourné.

Source du projet: `src/ClassicUO.Client/Game/World.cs`; fonction `Clear`.

Chaque appel relit les données locales. Une variable conserve un instantané ; plusieurs lectures peuvent voir différentes mises à jour. Un résultat non nul ne prouve pas la connexion ; zéro peut être une valeur ou une absence de données.


## Exemples

### Afficher le compteur en cache

```vb
# Afficher le compteur en cache
#
# Lit le compteur de status du joueur actuel : poids maximal en stones.
#
# Integer — poids maximal en stones, 0..65535 dans le modèle. 0 peut être réel, inconnu ou dû à
# Player absent/détruit. Quantité, pas Boolean, ID ou type : 1 signifie une unité, pas un
# succès. Aucun parcours d’objets ni tableau retourné.

SUB Main()
    # value conserve une lecture sans argument du joueur ; CStr la formate pour le journal sans
    # changer son sens.

    VAR value = UO.GetMaxWeight()
    UO.Print('WeightMax: ' + CStr(value))
END SUB
```

**Explication des paramètres et du déroulement:**

- value conserve une lecture sans argument du joueur ; CStr la formate pour le journal sans changer son sens.

### Observer une variation

```vb
# Observer une variation
#
# Lit le compteur de status du joueur actuel : poids maximal en stones.
#
# Integer — poids maximal en stones, 0..65535 dans le modèle. 0 peut être réel, inconnu ou dû à
# Player absent/détruit. Quantité, pas Boolean, ID ou type : 1 signifie une unité, pas un
# succès. Aucun parcours d’objets ni tableau retourné.

SUB Main()
    # WAIT(500) sépare before et after de 500 ms. difference peut être positive, nulle ou négative ;
    # des mises à jour ou changements de personnage peuvent échapper. L’attente appartient à
    # l’exemple.

    VAR before = UO.GetMaxWeight()
    WAIT(500)
    VAR after = UO.GetMaxWeight()
    VAR difference = after - before
    UO.Print('Counter change: ' + CStr(difference))
END SUB
```

**Explication des paramètres et du déroulement:**

- WAIT(500) sépare before et after de 500 ms. difference peut être positive, nulle ou négative ; des mises à jour ou changements de personnage peuvent échapper. L’attente appartient à l’exemple.

### Fonction de décision complète

```vb
# Fonction de décision complète
#
# Lit le compteur de status du joueur actuel : poids maximal en stones.
#
# Integer — poids maximal en stones, 0..65535 dans le modèle. 0 peut être réel, inconnu ou dû à
# Player absent/détruit. Quantité, pas Boolean, ID ou type : 1 signifie une unité, pas un
# succès. Aucun parcours d’objets ni tableau retourné.

SUB Main()
    # CanCarry(extra) reçoit un poids ajouté en stones ; 10 est un exemple, pas un nombre de piles.
    # Rejette extra négatif, Player absent ou maximum <= 0, lit actuel/maximum puis renvoie Integer
    # Boolean 1=TRUE ou 0=FALSE selon extra <= maximum - current. La soustraction évite le
    # débordement de current + extra. Surcharge : false même pour extra=0. Estimation locale, pas
    # autorisation serveur ; lectures non atomiques et poids nul parfois inconnu.

    IF CanCarry(10) = TRUE THEN
        UO.Print('Local check passed')
    ELSE
        UO.Print('Local check failed or data unavailable')
    END IF
END SUB

SUB CanCarry(extra)
    IF extra < 0 OR UO.Self() = 0 THEN
        RETURN FALSE
    END IF
    VAR current = UO.Weight()
    VAR maximum = UO.GetMaxWeight()
    IF maximum <= 0 THEN
        RETURN FALSE
    END IF
    RETURN extra <= maximum - current
END SUB
```

**Explication des paramètres et du déroulement:**

- CanCarry(extra) reçoit un poids ajouté en stones ; 10 est un exemple, pas un nombre de piles. Rejette extra négatif, Player absent ou maximum <= 0, lit actuel/maximum puis renvoie Integer Boolean 1=TRUE ou 0=FALSE selon extra <= maximum - current. La soustraction évite le débordement de current + extra. Surcharge : false même pour extra=0. Estimation locale, pas autorisation serveur ; lectures non atomiques et poids nul parfois inconnu.
