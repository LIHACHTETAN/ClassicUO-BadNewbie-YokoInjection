# UO.GetStatLockState

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: fr -->

Lit le mode local de progression de la caractéristique.

## Syntaxe exacte

```text
UO.GetStatLockState(statNum:Any) -> Integer
```

## Paramètres

- `statNum` — Numéro de caractéristique obligatoire : 0 — STR, 1 — DEX, 2 — INT. Ce n’est ni sa valeur actuelle ni son nom textuel.

## Retour

Integer : 0 — augmentation, 1 — diminution, 2 — verrouillage. Code de mode, pas true/false. Un numéro hors de 0..2 renvoie −1. Sans personnage, un numéro valide donne 0 par défaut ; cela ne confirme pas l’état du serveur.

## Comportement

- Invoke lit les données existantes sur le fil du jeu, sans paquet réseau. La compétence n’est ni utilisée ni entraînée. Deux lectures sont des instantanés distincts.
- Numéro de caractéristique obligatoire : 0 — STR, 1 — DEX, 2 — INT. Ce n’est ni sa valeur actuelle ni son nom textuel.
- ExecuteStealthCompatibility choisit la branche. Text lit le sélecteur de compétence ; Arg lit les numéros et modes. Un argument non convertible peut provoquer une erreur de conversion.

### Fonctions internes : de l’appel au résultat

Voici les véritables étapes internes C#. ReadMode est une fonction auxiliaire entièrement définie dans l’exemple, pas une commande intégrée cachée.

#### 1. ExecuteStealthCompatibility

ExecuteStealthCompatibility choisit la branche. Text lit le sélecteur de compétence ; Arg lit les numéros et modes. Un argument non convertible peut provoquer une erreur de conversion.

Integer : 0 — augmentation, 1 — diminution, 2 — verrouillage. Code de mode, pas true/false. Un numéro hors de 0..2 renvoie −1. Sans personnage, un numéro valide donne 0 par défaut ; cela ne confirme pas l’état du serveur.

Source du projet: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; fonction `ExecuteStealthCompatibility`.

#### 2. Invoke

Invoke lit dans le thread du jeu ; un thread de travail attend le traitement par le gestionnaire. L’annulation du script interrompt cette attente. Aucun délai ni appel réseau supplémentaire.

Invoke lit les données existantes sur le fil du jeu, sans paquet réseau. La compétence n’est ni utilisée ni entraînée. Deux lectures sont des instantanés distincts.

Source du projet: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; fonction `Invoke`.

#### 3. GetStatLockState

GetStatLockState/SetStatLockState choisissent StrLock, DexLock ou IntLock selon 0/1/2. Un numéro inconnu se lit −1 ; l’écriture vérifie les deux bornes avant l’envoi.

Integer : 0 — augmentation, 1 — diminution, 2 — verrouillage. Code de mode, pas true/false. Un numéro hors de 0..2 renvoie −1. Sans personnage, un numéro valide donne 0 par défaut ; cela ne confirme pas l’état du serveur.

Source du projet: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; fonction `GetStatLockState`.

Invoke lit les données existantes sur le fil du jeu, sans paquet réseau. La compétence n’est ni utilisée ni entraînée. Deux lectures sont des instantanés distincts.


## Exemples

### Lire et afficher

```vb
# Lire et afficher
#
# Lit le mode local de progression de la caractéristique.
#
# Integer : 0 — augmentation, 1 — diminution, 2 — verrouillage. Code de mode, pas true/false. Un
# numéro hors de 0..2 renvoie −1. Sans personnage, un numéro valide donne 0 par défaut ; cela ne
# confirme pas l’état du serveur.

SUB Main()
    # L’exemple fixe selector et, pour une écriture, mode. La première ligne choisit la compétence
    # par nom ou la caractéristique par numéro. Print affiche seulement le résultat.

    VAR selector = 0
    VAR mode = UO.GetStatLockState(selector)
    UO.Print(CStr(mode))
END SUB
```

**Explication des paramètres et du déroulement:**

- L’exemple fixe selector et, pour une écriture, mode. La première ligne choisit la compétence par nom ou la caractéristique par numéro. Print affiche seulement le résultat.

### Utiliser dans une condition ou comparaison

```vb
# Utiliser dans une condition ou comparaison
#
# Lit le mode local de progression de la caractéristique.
#
# Integer : 0 — augmentation, 1 — diminution, 2 — verrouillage. Code de mode, pas true/false. Un
# numéro hors de 0..2 renvoie −1. Sans personnage, un numéro valide donne 0 par défaut ; cela ne
# confirme pas l’état du serveur.

SUB Main()
    # Le seuil 95.1 et les modes 0/1/2 sont des réglages d’exemple. Vérifiez −1 avant de changer le
    # mode. Lire après l’écriture montre la copie locale sans attendre le serveur.

    VAR mode = UO.GetStatLockState(0)
    IF mode = 2 THEN
        UO.Print("Locked")
    ELSE
        IF mode = -1 THEN
            UO.Print("Unknown selector")
        ELSE
            UO.Print("Mode: " + CStr(mode))
        END IF
    END IF
END SUB
```

**Explication des paramètres et du déroulement:**

- Le seuil 95.1 et les modes 0/1/2 sont des réglages d’exemple. Vérifiez −1 avant de changer le mode. Lire après l’écriture montre la copie locale sans attendre le serveur.

### Fonction auxiliaire complète

```vb
# Fonction auxiliaire complète
#
# Lit le mode local de progression de la caractéristique.
#
# Integer : 0 — augmentation, 1 — diminution, 2 — verrouillage. Code de mode, pas true/false. Un
# numéro hors de 0..2 renvoie −1. Sans personnage, un numéro valide donne 0 par défaut ; cela ne
# confirme pas l’état du serveur.

SUB Main()
    # La fonction complète suit Main. selector choisit la compétence/caractéristique ; mode indique
    # le mode d’écriture. ReadValue/ReadMode renvoient le nombre initial ; ApplyMode vérifie les
    # arguments, agit et ne renvoie rien. WAIT(1000) sépare deux instantanés de lecture.

    VAR before = ReadMode(0)
    WAIT(1000)
    VAR after = ReadMode(0)
    UO.Print(CStr(before) + " -> " + CStr(after))
END SUB

SUB ReadMode(selector)
    RETURN UO.GetStatLockState(selector)
END SUB
```

**Explication des paramètres et du déroulement:**

- La fonction complète suit Main. selector choisit la compétence/caractéristique ; mode indique le mode d’écriture. ReadValue/ReadMode renvoient le nombre initial ; ApplyMode vérifie les arguments, agit et ne renvoie rien. WAIT(1000) sépare deux instantanés de lecture.
