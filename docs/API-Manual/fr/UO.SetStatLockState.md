# UO.SetStatLockState

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: fr -->

Demande un changement de mode de progression de la caractéristique.

## Syntaxe exacte

```text
UO.SetStatLockState(statNum:Any, statState:Any) -> Unit
```

## Paramètres

- `statNum` — Numéro de caractéristique obligatoire : 0 — STR, 1 — DEX, 2 — INT. Ce n’est ni sa valeur actuelle ni son nom textuel.
- `statState` — Mode obligatoire : 0 — augmentation, 1 — diminution, 2 — verrouillage. Trois codes, pas un Boolean ; true/false ne décrivent pas tous les modes.

## Retour

Unit — aucune valeur renvoyée. Ne traitez pas le résultat comme un succès/échec et ne le comparez pas à true. Une lecture ultérieure montre le modèle local, pas un accusé de réception du serveur.

## Comportement

- Une demande valide envoie un paquet via GameActions et modifie immédiatement le mode local. Les règles du serveur restent applicables ; aucun gain n’est garanti. Compétence inconnue, indice/mode invalide ou personnage absent sont ignorés sans paquet.
- Numéro de caractéristique obligatoire : 0 — STR, 1 — DEX, 2 — INT. Ce n’est ni sa valeur actuelle ni son nom textuel.
- ExecuteStealthCompatibility choisit la branche. Text lit le sélecteur de compétence ; Arg lit les numéros et modes. Un argument non convertible peut provoquer une erreur de conversion.

### Fonctions internes : de l’appel au résultat

Voici les véritables étapes internes C#. ApplyMode est une fonction auxiliaire entièrement définie dans l’exemple, pas une commande intégrée cachée.

#### 1. ExecuteStealthCompatibility

ExecuteStealthCompatibility choisit la branche. Text lit le sélecteur de compétence ; Arg lit les numéros et modes. Un argument non convertible peut provoquer une erreur de conversion.

Unit — aucune valeur renvoyée. Ne traitez pas le résultat comme un succès/échec et ne le comparez pas à true. Une lecture ultérieure montre le modèle local, pas un accusé de réception du serveur.

Source du projet: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; fonction `ExecuteStealthCompatibility`.

#### 2. Invoke

Invoke lit dans le thread du jeu ; un thread de travail attend le traitement par le gestionnaire. L’annulation du script interrompt cette attente. Aucun délai ni appel réseau supplémentaire.

Une demande valide envoie un paquet via GameActions et modifie immédiatement le mode local. Les règles du serveur restent applicables ; aucun gain n’est garanti. Compétence inconnue, indice/mode invalide ou personnage absent sont ignorés sans paquet.

Source du projet: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; fonction `Invoke`.

#### 3. SetStatLockState

GetStatLockState/SetStatLockState choisissent StrLock, DexLock ou IntLock selon 0/1/2. Un numéro inconnu se lit −1 ; l’écriture vérifie les deux bornes avant l’envoi.

Unit — aucune valeur renvoyée. Ne traitez pas le résultat comme un succès/échec et ne le comparez pas à true. Une lecture ultérieure montre le modèle local, pas un accusé de réception du serveur.

Source du projet: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; fonction `SetStatLockState`.

#### 4. ChangeStatLock

Une demande valide envoie un paquet via GameActions et modifie immédiatement le mode local. Les règles du serveur restent applicables ; aucun gain n’est garanti. Compétence inconnue, indice/mode invalide ou personnage absent sont ignorés sans paquet.

Unit — aucune valeur renvoyée. Ne traitez pas le résultat comme un succès/échec et ne le comparez pas à true. Une lecture ultérieure montre le modèle local, pas un accusé de réception du serveur.

Source du projet: `src/ClassicUO.Client/Game/GameActions.cs`; fonction `ChangeStatLock`.

Une demande valide envoie un paquet via GameActions et modifie immédiatement le mode local. Les règles du serveur restent applicables ; aucun gain n’est garanti. Compétence inconnue, indice/mode invalide ou personnage absent sont ignorés sans paquet.


## Exemples

### Lire et afficher

```vb
# Lire et afficher
#
# Demande un changement de mode de progression de la caractéristique.
#
# Unit — aucune valeur renvoyée. Ne traitez pas le résultat comme un succès/échec et ne le
# comparez pas à true. Une lecture ultérieure montre le modèle local, pas un accusé de réception
# du serveur.

SUB Main()
    # L’exemple fixe selector et, pour une écriture, mode. La première ligne choisit la compétence
    # par nom ou la caractéristique par numéro. Print affiche seulement le résultat.

    VAR selector = 0
    VAR mode = 2
    UO.SetStatLockState(selector, mode)
    UO.Print(CStr(UO.GetStatLockState(selector)))
END SUB
```

**Explication des paramètres et du déroulement:**

- L’exemple fixe selector et, pour une écriture, mode. La première ligne choisit la compétence par nom ou la caractéristique par numéro. Print affiche seulement le résultat.

### Utiliser dans une condition ou comparaison

```vb
# Utiliser dans une condition ou comparaison
#
# Demande un changement de mode de progression de la caractéristique.
#
# Unit — aucune valeur renvoyée. Ne traitez pas le résultat comme un succès/échec et ne le
# comparez pas à true. Une lecture ultérieure montre le modèle local, pas un accusé de réception
# du serveur.

SUB Main()
    # Le seuil 95.1 et les modes 0/1/2 sont des réglages d’exemple. Vérifiez −1 avant de changer le
    # mode. Lire après l’écriture montre la copie locale sans attendre le serveur.

    VAR selector = 0
    VAR before = UO.GetStatLockState(selector)
    IF before >= 0 AND before <= 2 THEN
        UO.SetStatLockState(selector, 0)
        UO.Print(CStr(UO.GetStatLockState(selector)))
    END IF
END SUB
```

**Explication des paramètres et du déroulement:**

- Le seuil 95.1 et les modes 0/1/2 sont des réglages d’exemple. Vérifiez −1 avant de changer le mode. Lire après l’écriture montre la copie locale sans attendre le serveur.

### Fonction auxiliaire complète

```vb
# Fonction auxiliaire complète
#
# Demande un changement de mode de progression de la caractéristique.
#
# Unit — aucune valeur renvoyée. Ne traitez pas le résultat comme un succès/échec et ne le
# comparez pas à true. Une lecture ultérieure montre le modèle local, pas un accusé de réception
# du serveur.

SUB Main()
    # La fonction complète suit Main. selector choisit la compétence/caractéristique ; mode indique
    # le mode d’écriture. ReadValue/ReadMode renvoient le nombre initial ; ApplyMode vérifie les
    # arguments, agit et ne renvoie rien. WAIT(1000) sépare deux instantanés de lecture.

    ApplyMode(0, 2)
END SUB

SUB ApplyMode(selector, mode)
    IF mode < 0 OR mode > 2 THEN
        RETURN
    END IF
    IF UO.GetStatLockState(selector) < 0 THEN
        RETURN
    END IF
    UO.SetStatLockState(selector, mode)
END SUB
```

**Explication des paramètres et du déroulement:**

- La fonction complète suit Main. selector choisit la compétence/caractéristique ; mode indique le mode d’écriture. ReadValue/ReadMode renvoient le nombre initial ; ApplyMode vérifie les arguments, agit et ne renvoie rien. WAIT(1000) sépare deux instantanés de lecture.
