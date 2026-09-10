# UO.GetSkillValue

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: fr -->

Lit la valeur de base de la compétence sans modificateurs.

## Syntaxe exacte

```text
UO.GetSkillValue(SkillName:Any) -> Decimal
```

## Paramètres

- `SkillName` — Compétence obligatoire : nom des données client, comme "Mining" ou "Animal Lore", ou indice décimal 0..Skills.Length−1 sous forme de nombre ou chaîne. Ignore la casse, retire les espaces extérieurs et remplace _ par un espace. Ce n’est ni un ID d’objet ni un indice commençant à 1. Une chaîne numérique désigne toujours un indice.

## Retour

Decimal (Double) — points de compétence par dixièmes, par exemple 95,1 et non 951. Le champ BaseFixed est divisé directement par 10 en Double. Zéro signifie une compétence à zéro ou un personnage/une compétence absent. Pas un Boolean. Les anciennes SkillVal/BaseVal utilisent une autre échelle ; ne mélangez pas ces familles.

## Comportement

- Invoke lit les données existantes sur le fil du jeu, sans paquet réseau. La compétence n’est ni utilisée ni entraînée. Deux lectures sont des instantanés distincts.
- Compétence obligatoire : nom des données client, comme "Mining" ou "Animal Lore", ou indice décimal 0..Skills.Length−1 sous forme de nombre ou chaîne. Ignore la casse, retire les espaces extérieurs et remplace _ par un espace. Ce n’est ni un ID d’objet ni un indice commençant à 1. Une chaîne numérique désigne toujours un indice.
- ExecuteStealthCompatibility choisit la branche. Text lit le sélecteur de compétence ; Arg lit les numéros et modes. Un argument non convertible peut provoquer une erreur de conversion.

### Fonctions internes : de l’appel au résultat

Voici les véritables étapes internes C#. ReadValue est une fonction auxiliaire entièrement définie dans l’exemple, pas une commande intégrée cachée.

#### 1. ExecuteStealthCompatibility

ExecuteStealthCompatibility choisit la branche. Text lit le sélecteur de compétence ; Arg lit les numéros et modes. Un argument non convertible peut provoquer une erreur de conversion.

Decimal (Double) — points de compétence par dixièmes, par exemple 95,1 et non 951. Le champ BaseFixed est divisé directement par 10 en Double. Zéro signifie une compétence à zéro ou un personnage/une compétence absent. Pas un Boolean. Les anciennes SkillVal/BaseVal utilisent une autre échelle ; ne mélangez pas ces familles.

Source du projet: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; fonction `ExecuteStealthCompatibility`.

#### 2. Invoke

Invoke lit dans le thread du jeu ; un thread de travail attend le traitement par le gestionnaire. L’annulation du script interrompt cette attente. Aucun délai ni appel réseau supplémentaire.

Invoke lit les données existantes sur le fil du jeu, sans paquet réseau. La compétence n’est ni utilisée ni entraînée. Deux lectures sont des instantanés distincts.

Source du projet: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; fonction `Invoke`.

#### 3. FindSkillUnsafe

FindSkillUnsafe vérifie d’abord l’indice décimal et ses bornes ; sinon normalise le nom et compare exactement Skill.Name sans tenir compte de la casse. Un nom inconnu produit null ; aucune cible ne s’ouvre.

Une compétence inconnue ou un personnage absent renvoie −1.

Source du projet: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; fonction `FindSkillUnsafe`.

#### 4. GetSkillValue

GetSkillValue choisit BaseFixed, ValueFixed ou CapFixed et divise les dixièmes entiers par 10d, sans arrondi intermédiaire en Single.

Decimal (Double) — points de compétence par dixièmes, par exemple 95,1 et non 951. Le champ BaseFixed est divisé directement par 10 en Double. Zéro signifie une compétence à zéro ou un personnage/une compétence absent. Pas un Boolean. Les anciennes SkillVal/BaseVal utilisent une autre échelle ; ne mélangez pas ces familles.

Source du projet: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; fonction `GetSkillValue`.

Invoke lit les données existantes sur le fil du jeu, sans paquet réseau. La compétence n’est ni utilisée ni entraînée. Deux lectures sont des instantanés distincts.


## Exemples

### Lire et afficher

```vb
# Lire et afficher
#
# Lit la valeur de base de la compétence sans modificateurs.
#
# Decimal (Double) — points de compétence par dixièmes, par exemple 95,1 et non 951. Le champ
# BaseFixed est divisé directement par 10 en Double. Zéro signifie une compétence à zéro ou un
# personnage/une compétence absent. Pas un Boolean. Les anciennes SkillVal/BaseVal utilisent une
# autre échelle ; ne mélangez pas ces familles.

SUB Main()
    # L’exemple fixe selector et, pour une écriture, mode. La première ligne choisit la compétence
    # par nom ou la caractéristique par numéro. Print affiche seulement le résultat.

    VAR selector = 'Mining'
    VAR value = UO.GetSkillValue(selector)
    UO.Print(CStr(value))
END SUB
```

**Explication des paramètres et du déroulement:**

- L’exemple fixe selector et, pour une écriture, mode. La première ligne choisit la compétence par nom ou la caractéristique par numéro. Print affiche seulement le résultat.

### Utiliser dans une condition ou comparaison

```vb
# Utiliser dans une condition ou comparaison
#
# Lit la valeur de base de la compétence sans modificateurs.
#
# Decimal (Double) — points de compétence par dixièmes, par exemple 95,1 et non 951. Le champ
# BaseFixed est divisé directement par 10 en Double. Zéro signifie une compétence à zéro ou un
# personnage/une compétence absent. Pas un Boolean. Les anciennes SkillVal/BaseVal utilisent une
# autre échelle ; ne mélangez pas ces familles.

SUB Main()
    # Le seuil 95.1 et les modes 0/1/2 sont des réglages d’exemple. Vérifiez −1 avant de changer le
    # mode. Lire après l’écriture montre la copie locale sans attendre le serveur.

    IF UO.GetSkillLockState('Mining') >= 0 THEN
        VAR value = UO.GetSkillValue('Mining')
        IF value >= 95.1 THEN
            UO.Print('Value >= 95.1: ' + CStr(value))
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
# Lit la valeur de base de la compétence sans modificateurs.
#
# Decimal (Double) — points de compétence par dixièmes, par exemple 95,1 et non 951. Le champ
# BaseFixed est divisé directement par 10 en Double. Zéro signifie une compétence à zéro ou un
# personnage/une compétence absent. Pas un Boolean. Les anciennes SkillVal/BaseVal utilisent une
# autre échelle ; ne mélangez pas ces familles.

SUB Main()
    # La fonction complète suit Main. selector choisit la compétence/caractéristique ; mode indique
    # le mode d’écriture. ReadValue/ReadMode renvoient le nombre initial ; ApplyMode vérifie les
    # arguments, agit et ne renvoie rien. WAIT(1000) sépare deux instantanés de lecture.

    VAR before = ReadValue('Animal_Lore')
    WAIT(1000)
    VAR after = ReadValue('Animal Lore')
    UO.Print(CStr(after - before))
END SUB

SUB ReadValue(selector)
    RETURN UO.GetSkillValue(selector)
END SUB
```

**Explication des paramètres et du déroulement:**

- La fonction complète suit Main. selector choisit la compétence/caractéristique ; mode indique le mode d’écriture. ReadValue/ReadMode renvoient le nombre initial ; ApplyMode vérifie les arguments, agit et ne renvoie rien. WAIT(1000) sépare deux instantanés de lecture.
