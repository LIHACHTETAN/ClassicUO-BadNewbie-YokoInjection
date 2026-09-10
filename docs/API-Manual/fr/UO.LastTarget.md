# UO.LastTarget

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: fr -->

Lit le serial de la dernière cible objet mémorisée.

## Syntaxe exacte

```text
UO.LastTarget() -> Integer
```

## Paramètres

Aucun paramètre.

## Retour

Integer — serial/ID, pas un type ni un booléen. 0 : aucune cible objet, y compris une cible terrain/statique dont les coordonnées peuvent être mémorisées. Les 32 bits sont conservés. Tester <> 0, pas > 0 ni = TRUE.

## Comportement

- Sans paramètres, curseur, attaque, sélection ni transmission. LastTarget diffère de LastAttack et LastStatus. Cibler normalement self ne remplace pas la cible ; ClientMarkChar peut la modifier explicitement.
- SetEntity conserve Entity.X/Y connus, éventuellement les coordonnées internes d’un conteneur. SetLand/SetStatic conservent les cases du monde. Déplacement/suppression ultérieurs ne changent pas ces valeurs. GetX/GetY(serial) donnent la position actuelle.
- Clear et World.Clear réinitialisent même si les scripts restent actifs. Un serial inconnu affecté explicitement reçoit X/Y=0, jamais les coordonnées précédentes. L’existence côté serveur n’est pas garantie.
- Les lectures séparées ne sont pas atomiques. Pour une cible objet, LastTile garde les coordonnées de protocole 65535 ; terrain/statique : LastTile(1)/(2) lisent X/Y. lasttarget sans parenthèses est dynamique sauf masquage par une variable.
- World.Clear appelle ClearWorldState : efface curseur/callback actif, cible et paquet de répétition. Reset ordinaire conserve l’historique. TargetLast natif n’envoie un paquet mémorisé que pour un curseur serveur actif ; sans historique ou pour un callback local, il conserve le curseur sans rien envoyer. Le callback client actif reçoit null une seule fois pour annulation : ClientTargetResponsePresent vaut 1 avec une réponse vide. Une sélection terminée ne reçoit pas un second résultat.

### Fonctions internes : de l’appel au résultat

Voici les véritables étapes internes C#. ReadTargetValue est une fonction auxiliaire entièrement définie dans l’exemple, pas une commande intégrée cachée.

#### 1. SetEntity

SetEntity mémorise serial et X/Y via World.Get. Une Entity absente/détruite donne X/Y=0 ; les sentinelles du protocole restent intactes.

SetEntity conserve Entity.X/Y connus, éventuellement les coordonnées internes d’un conteneur. SetLand/SetStatic conservent les cases du monde. Déplacement/suppression ultérieurs ne changent pas ces valeurs. GetX/GetY(serial) donnent la position actuelle.

Source du projet: `src/ClassicUO.Client/Game/Managers/TargetManager.cs`; fonction `SetEntity`.

#### 2. SetLand

SetLand/SetStatic mémorisent X/Y/Z avec serial 0. SavedX/SavedY sont séparés des champs transmis.

Integer — serial/ID, pas un type ni un booléen. 0 : aucune cible objet, y compris une cible terrain/statique dont les coordonnées peuvent être mémorisées. Les 32 bits sont conservés. Tester <> 0, pas > 0 ni = TRUE.

Source du projet: `src/ClassicUO.Client/Game/Managers/TargetManager.cs`; fonction `SetLand`.

#### 3. SetStatic

SetLand/SetStatic mémorisent X/Y/Z avec serial 0. SavedX/SavedY sont séparés des champs transmis.

Integer — serial/ID, pas un type ni un booléen. 0 : aucune cible objet, y compris une cible terrain/statique dont les coordonnées peuvent être mémorisées. Les 32 bits sont conservés. Tester <> 0, pas > 0 ni = TRUE.

Source du projet: `src/ClassicUO.Client/Game/Managers/TargetManager.cs`; fonction `SetStatic`.

#### 4. ExecuteStealthCompatibility

LastTargetX/LastTargetY lisent ITargetSnapshotBridge ; un ancien bridge externe garde GetX/GetY. Invoke lit sur le fil du jeu avec annulation.

Integer — serial/ID, pas un type ni un booléen. 0 : aucune cible objet, y compris une cible terrain/statique dont les coordonnées peuvent être mémorisées. Les 32 bits sont conservés. Tester <> 0, pas > 0 ni = TRUE.

Source du projet: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; fonction `ExecuteStealthCompatibility`.

#### 5. Invoke

LastTargetX/LastTargetY lisent ITargetSnapshotBridge ; un ancien bridge externe garde GetX/GetY. Invoke lit sur le fil du jeu avec annulation.

Sans paramètres, curseur, attaque, sélection ni transmission. LastTarget diffère de LastAttack et LastStatus. Cibler normalement self ne remplace pas la cible ; ClientMarkChar peut la modifier explicitement.

Source du projet: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; fonction `Invoke`.

#### 6. Clear

Clear efface serial et coordonnées mémorisées ; World.Clear l’appelle au nettoyage.

Clear et World.Clear réinitialisent même si les scripts restent actifs. Un serial inconnu affecté explicitement reçoit X/Y=0, jamais les coordonnées précédentes. L’existence côté serveur n’est pas garantie.

Source du projet: `src/ClassicUO.Client/Game/Managers/TargetManager.cs`; fonction `Clear`.

#### 7. ClearWorldState

World.Clear appelle ClearWorldState : efface curseur/callback actif, cible et paquet de répétition. Reset ordinaire conserve l’historique. TargetLast natif n’envoie un paquet mémorisé que pour un curseur serveur actif ; sans historique ou pour un callback local, il conserve le curseur sans rien envoyer. Le callback client actif reçoit null une seule fois pour annulation : ClientTargetResponsePresent vaut 1 avec une réponse vide. Une sélection terminée ne reçoit pas un second résultat.

World.Clear appelle ClearWorldState : efface curseur/callback actif, cible et paquet de répétition. Reset ordinaire conserve l’historique. TargetLast natif n’envoie un paquet mémorisé que pour un curseur serveur actif ; sans historique ou pour un callback local, il conserve le curseur sans rien envoyer. Le callback client actif reçoit null une seule fois pour annulation : ClientTargetResponsePresent vaut 1 avec une réponse vide. Une sélection terminée ne reçoit pas un second résultat.

Source du projet: `src/ClassicUO.Client/Game/Managers/TargetManager.cs`; fonction `ClearWorldState`.

#### 8. TargetLast

World.Clear appelle ClearWorldState : efface curseur/callback actif, cible et paquet de répétition. Reset ordinaire conserve l’historique. TargetLast natif n’envoie un paquet mémorisé que pour un curseur serveur actif ; sans historique ou pour un callback local, il conserve le curseur sans rien envoyer. Le callback client actif reçoit null une seule fois pour annulation : ClientTargetResponsePresent vaut 1 avec une réponse vide. Une sélection terminée ne reçoit pas un second résultat.

World.Clear appelle ClearWorldState : efface curseur/callback actif, cible et paquet de répétition. Reset ordinaire conserve l’historique. TargetLast natif n’envoie un paquet mémorisé que pour un curseur serveur actif ; sans historique ou pour un callback local, il conserve le curseur sans rien envoyer. Le callback client actif reçoit null une seule fois pour annulation : ClientTargetResponsePresent vaut 1 avec une réponse vide. Une sélection terminée ne reçoit pas un second résultat.

Source du projet: `src/ClassicUO.Client/Game/Managers/TargetManager.cs`; fonction `TargetLast`.

Les lectures séparées ne sont pas atomiques. Pour une cible objet, LastTile garde les coordonnées de protocole 65535 ; terrain/statique : LastTile(1)/(2) lisent X/Y. lasttarget sans parenthèses est dynamique sauf masquage par une variable.


## Exemples

### Lire la valeur mémorisée

```vb
# Lire la valeur mémorisée
#
# Lit le serial de la dernière cible objet mémorisée.
#
# Integer — serial/ID, pas un type ni un booléen. 0 : aucune cible objet, y compris une cible
# terrain/statique dont les coordonnées peuvent être mémorisées. Les 32 bits sont conservés.
# Tester <> 0, pas > 0 ni = TRUE.

SUB Main()
    # value contient le résultat ; HEX affiche l’ID, CStr la coordonnée. Aucune sélection.

    VAR value = UO.LastTarget()
    UO.Print('Saved value: ' + HEX(value))
END SUB
```

**Explication des paramètres et du déroulement:**

- value contient le résultat ; HEX affiche l’ID, CStr la coordonnée. Aucune sélection.

### Comparer position mémorisée et actuelle

```vb
# Comparer position mémorisée et actuelle
#
# Lit le serial de la dernière cible objet mémorisée.
#
# Integer — serial/ID, pas un type ni un booléen. 0 : aucune cible objet, y compris une cible
# terrain/statique dont les coordonnées peuvent être mémorisées. Les 32 bits sont conservés.
# Tester <> 0, pas > 0 ni = TRUE.

SUB Main()
    # id est le serial mémorisé. Exists précède GetX/GetY ; les deux positions peuvent différer. Un
    # ID nul ne prouve pas qu’un point a été sélectionné.

    VAR id = UO.LastTarget()
    VAR x = UO.LastTargetX()
    VAR y = UO.LastTargetY()
    UO.Print('Saved XY: ' + CStr(x) + ',' + CStr(y))
    IF id <> 0 AND UO.Exists(id) THEN
        UO.Print('Live XY: ' + CStr(UO.GetX(id)) + ',' + CStr(UO.GetY(id)))
    END IF
END SUB
```

**Explication des paramètres et du déroulement:**

- id est le serial mémorisé. Exists précède GetX/GetY ; les deux positions peuvent différer. Un ID nul ne prouve pas qu’un point a été sélectionné.

### Fonction ReadTargetValue complète

```vb
# Fonction ReadTargetValue complète
#
# Lit le serial de la dernière cible objet mémorisée.
#
# Integer — serial/ID, pas un type ni un booléen. 0 : aucune cible objet, y compris une cible
# terrain/statique dont les coordonnées peuvent être mémorisées. Les 32 bits sont conservés.
# Tester <> 0, pas > 0 ni = TRUE.

SUB Main()
    # minimum/maximum règlent le filtre de la fonction auxiliaire, pas l’API. -1 est son propre
    # signal hors plage. Pour un ID, la variante conserve tout serial non nul et son bit supérieur.

    VAR value = ReadTargetValue()
    UO.Print('Checked value: ' + CStr(value))
END SUB

SUB ReadTargetValue()
    VAR value = UO.LastTarget()
    IF value = 0 THEN
        RETURN -1
    END IF
    RETURN value
END SUB
```

**Explication des paramètres et du déroulement:**

- minimum/maximum règlent le filtre de la fonction auxiliaire, pas l’API. -1 est son propre signal hors plage. Pour un ID, la variante conserve tout serial non nul et son bit supérieur.
