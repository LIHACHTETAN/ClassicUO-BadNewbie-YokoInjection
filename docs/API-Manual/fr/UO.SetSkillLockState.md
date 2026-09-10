# UO.SetSkillLockState

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: fr -->

Demande un changement de mode de progression de la compétence.

## Syntaxe exacte

```text
UO.SetSkillLockState(SkillName:Any, skillState:Any) -> Unit
```

## Paramètres

- `SkillName` — Compétence obligatoire : nom des données client, comme "Mining" ou "Animal Lore", ou indice décimal 0..Skills.Length−1 sous forme de nombre ou chaîne. Ignore la casse, retire les espaces extérieurs et remplace _ par un espace. Ce n’est ni un ID d’objet ni un indice commençant à 1. Une chaîne numérique désigne toujours un indice.
- `skillState` — Mode obligatoire : 0 — augmentation, 1 — diminution, 2 — verrouillage. Trois codes, pas un Boolean ; true/false ne décrivent pas tous les modes.

## Retour

Unit — aucune valeur renvoyée. Ne traitez pas le résultat comme un succès/échec et ne le comparez pas à true. Une lecture ultérieure montre le modèle local, pas un accusé de réception du serveur.

## Comportement

- Une demande valide envoie un paquet via GameActions et modifie immédiatement le mode local. Les règles du serveur restent applicables ; aucun gain n’est garanti. Compétence inconnue, indice/mode invalide ou personnage absent sont ignorés sans paquet.
- Compétence obligatoire : nom des données client, comme "Mining" ou "Animal Lore", ou indice décimal 0..Skills.Length−1 sous forme de nombre ou chaîne. Ignore la casse, retire les espaces extérieurs et remplace _ par un espace. Ce n’est ni un ID d’objet ni un indice commençant à 1. Une chaîne numérique désigne toujours un indice.
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

#### 3. FindSkillUnsafe

FindSkillUnsafe vérifie d’abord l’indice décimal et ses bornes ; sinon normalise le nom et compare exactement Skill.Name sans tenir compte de la casse. Un nom inconnu produit null ; aucune cible ne s’ouvre.

Une compétence inconnue ou un personnage absent renvoie −1.

Source du projet: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; fonction `FindSkillUnsafe`.

#### 4. SetSkillLockState

Une demande valide envoie un paquet via GameActions et modifie immédiatement le mode local. Les règles du serveur restent applicables ; aucun gain n’est garanti. Compétence inconnue, indice/mode invalide ou personnage absent sont ignorés sans paquet.

Unit — aucune valeur renvoyée. Ne traitez pas le résultat comme un succès/échec et ne le comparez pas à true. Une lecture ultérieure montre le modèle local, pas un accusé de réception du serveur.

Source du projet: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; fonction `SetSkillLockState`.

#### 5. ChangeSkillLockStatus

Une demande valide envoie un paquet via GameActions et modifie immédiatement le mode local. Les règles du serveur restent applicables ; aucun gain n’est garanti. Compétence inconnue, indice/mode invalide ou personnage absent sont ignorés sans paquet.

Unit — aucune valeur renvoyée. Ne traitez pas le résultat comme un succès/échec et ne le comparez pas à true. Une lecture ultérieure montre le modèle local, pas un accusé de réception du serveur.

Source du projet: `src/ClassicUO.Client/Game/GameActions.cs`; fonction `ChangeSkillLockStatus`.

Une demande valide envoie un paquet via GameActions et modifie immédiatement le mode local. Les règles du serveur restent applicables ; aucun gain n’est garanti. Compétence inconnue, indice/mode invalide ou personnage absent sont ignorés sans paquet.


## Exemples

### Lire et afficher

```vb
# Lire et afficher
#
# Demande un changement de mode de progression de la compétence.
#
# Unit — aucune valeur renvoyée. Ne traitez pas le résultat comme un succès/échec et ne le
# comparez pas à true. Une lecture ultérieure montre le modèle local, pas un accusé de réception
# du serveur.

SUB Main()
    # L’exemple fixe selector et, pour une écriture, mode. La première ligne choisit la compétence
    # par nom ou la caractéristique par numéro. Print affiche seulement le résultat.

    VAR selector = 'Mining'
    VAR mode = 2
    UO.SetSkillLockState(selector, mode)
    UO.Print(CStr(UO.GetSkillLockState(selector)))
END SUB
```

**Explication des paramètres et du déroulement:**

- L’exemple fixe selector et, pour une écriture, mode. La première ligne choisit la compétence par nom ou la caractéristique par numéro. Print affiche seulement le résultat.

### Utiliser dans une condition ou comparaison

```vb
# Utiliser dans une condition ou comparaison
#
# Demande un changement de mode de progression de la compétence.
#
# Unit — aucune valeur renvoyée. Ne traitez pas le résultat comme un succès/échec et ne le
# comparez pas à true. Une lecture ultérieure montre le modèle local, pas un accusé de réception
# du serveur.

SUB Main()
    # Le seuil 95.1 et les modes 0/1/2 sont des réglages d’exemple. Vérifiez −1 avant de changer le
    # mode. Lire après l’écriture montre la copie locale sans attendre le serveur.

    VAR selector = 'Mining'
    VAR before = UO.GetSkillLockState(selector)
    IF before >= 0 AND before <= 2 THEN
        UO.SetSkillLockState(selector, 0)
        UO.Print(CStr(UO.GetSkillLockState(selector)))
    END IF
END SUB
```

**Explication des paramètres et du déroulement:**

- Le seuil 95.1 et les modes 0/1/2 sont des réglages d’exemple. Vérifiez −1 avant de changer le mode. Lire après l’écriture montre la copie locale sans attendre le serveur.

### Fonction auxiliaire complète

```vb
# Fonction auxiliaire complète
#
# Demande un changement de mode de progression de la compétence.
#
# Unit — aucune valeur renvoyée. Ne traitez pas le résultat comme un succès/échec et ne le
# comparez pas à true. Une lecture ultérieure montre le modèle local, pas un accusé de réception
# du serveur.

SUB Main()
    # La fonction complète suit Main. selector choisit la compétence/caractéristique ; mode indique
    # le mode d’écriture. ReadValue/ReadMode renvoient le nombre initial ; ApplyMode vérifie les
    # arguments, agit et ne renvoie rien. WAIT(1000) sépare deux instantanés de lecture.

    ApplyMode('Mining', 2)
END SUB

SUB ApplyMode(selector, mode)
    IF mode < 0 OR mode > 2 THEN
        RETURN
    END IF
    IF UO.GetSkillLockState(selector) < 0 THEN
        RETURN
    END IF
    UO.SetSkillLockState(selector, mode)
END SUB
```

**Explication des paramètres et du déroulement:**

- La fonction complète suit Main. selector choisit la compétence/caractéristique ; mode indique le mode d’écriture. ReadValue/ReadMode renvoient le nombre initial ; ApplyMode vérifie les arguments, agit et ne renvoie rien. WAIT(1000) sépare deux instantanés de lecture.
