# UO.Backpack

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: fr -->

Renvoie l’ID du sac à dos actuellement équipé.

## Syntaxe exacte

```text
UO.Backpack() -> Integer
```

## Paramètres

Aucun paramètre.

## Retour

Integer — serial/ID, pas graphic/type, couche, quantité ni Boolean. 0 : aucun objet actuel. Les 32 bits sont conservés ; tester <> 0, pas = TRUE ou > 0. Une valeur enregistrée ne se met pas à jour seule. Cherche un objet non détruit sur la couche Backpack de Player. Player absent/détruit ou sac absent/détruit donne 0. Identifie le conteneur, pas son contenu ; ne crée aucun sac.

## Comportement

- Aucun argument. Lecture locale via Invoke sur le fil du jeu ; l’annulation peut interrompre l’attente de ce fil. Aucun paquet, ouverture de conteneur, ciblage ou déplacement d’objet.
- Les intrinsèques self/backpack sans parenthèses sont relus sauf si une variable les masque. Les alias entre guillemets dépendent de la commande destinataire. Pour un transfert, "self" désigne le sac, mais UO.Self() renvoie le personnage. Employer UO.Backpack() pour un ID de conteneur.
- World.Clear retire Player : les lectures suivantes donnent 0. Connexion ou remplacement du sac peut changer l’ID. Plusieurs lectures ne sont pas atomiques. Un ID non nul ne prouve ni connexion, ni autorisation serveur, ni contenu chargé.

### Fonctions internes : de l’appel au résultat

Étapes réelles de lecture de l’objet client. IsOwnSerial est la fonction complète de l’exemple, pas une API intégrée supplémentaire.

#### 1. ExecuteStealthCompatibility

ExecuteStealthCompatibility choisit la branche sans argument et enveloppe l’entier du bridge dans InjectionValue. Aucun paramètre de sortie Pascal ni argument facultatif supplémentaire.

Integer — serial/ID, pas graphic/type, couche, quantité ni Boolean. 0 : aucun objet actuel. Les 32 bits sont conservés ; tester <> 0, pas = TRUE ou > 0. Une valeur enregistrée ne se met pas à jour seule.

Source du projet: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; fonction `ExecuteStealthCompatibility`.

#### 2. Invoke

Cherche un objet non détruit sur la couche Backpack de Player. Player absent/détruit ou sac absent/détruit donne 0. Identifie le conteneur, pas son contenu ; ne crée aucun sac. Invoke lit dans le thread du jeu ; un thread de travail attend le traitement par le gestionnaire. L’annulation du script interrompt cette attente. Aucun délai ni appel réseau supplémentaire.

Integer — serial/ID, pas graphic/type, couche, quantité ni Boolean. 0 : aucun objet actuel. Les 32 bits sont conservés ; tester <> 0, pas = TRUE ou > 0. Une valeur enregistrée ne se met pas à jour seule. Aucun argument. Lecture locale via Invoke sur le fil du jeu ; l’annulation peut interrompre l’attente de ce fil. Aucun paquet, ouverture de conteneur, ciblage ou déplacement d’objet.

Source du projet: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; fonction `Invoke`.

#### 3. FindItemByLayer

Cherche un objet non détruit sur la couche Backpack de Player. Player absent/détruit ou sac absent/détruit donne 0. Identifie le conteneur, pas son contenu ; ne crée aucun sac.

Integer — serial/ID, pas graphic/type, couche, quantité ni Boolean. 0 : aucun objet actuel. Les 32 bits sont conservés ; tester <> 0, pas = TRUE ou > 0. Une valeur enregistrée ne se met pas à jour seule.

Source du projet: `src/ClassicUO.Client/Game/GameObjects/Entity.cs`; fonction `FindItemByLayer`.

#### 4. Clear

World.Clear retire Player : les lectures suivantes donnent 0. Connexion ou remplacement du sac peut changer l’ID. Plusieurs lectures ne sont pas atomiques. Un ID non nul ne prouve ni connexion, ni autorisation serveur, ni contenu chargé.

World.Clear retire Player : les lectures suivantes donnent 0. Connexion ou remplacement du sac peut changer l’ID. Plusieurs lectures ne sont pas atomiques. Un ID non nul ne prouve ni connexion, ni autorisation serveur, ni contenu chargé.

Source du projet: `src/ClassicUO.Client/Game/World.cs`; fonction `Clear`.

World.Clear retire Player : les lectures suivantes donnent 0. Connexion ou remplacement du sac peut changer l’ID. Plusieurs lectures ne sont pas atomiques. Un ID non nul ne prouve ni connexion, ni autorisation serveur, ni contenu chargé.


## Exemples

### Lire et afficher l’ID

```vb
# Lire et afficher l’ID
#
# Renvoie l’ID du sac à dos actuellement équipé.
#
# Integer — serial/ID, pas graphic/type, couche, quantité ni Boolean. 0 : aucun objet actuel.
# Les 32 bits sont conservés ; tester <> 0, pas = TRUE ou > 0. Une valeur enregistrée ne se met
# pas à jour seule. Cherche un objet non détruit sur la couche Backpack de Player. Player
# absent/détruit ou sac absent/détruit donne 0. Identifie le conteneur, pas son contenu ; ne
# crée aucun sac.

SUB Main()
    # id conserve un résultat ; HEX formate le serial pour le journal. Aucun objet n’est sélectionné
    # ni utilisé.

    VAR id = UO.Backpack()
    UO.Print('ID: ' + HEX(id))
END SUB
```

**Explication des paramètres et du déroulement:**

- id conserve un résultat ; HEX formate le serial pour le journal. Aucun objet n’est sélectionné ni utilisé.

### Détecter un changement d’ID

```vb
# Détecter un changement d’ID
#
# Renvoie l’ID du sac à dos actuellement équipé.
#
# Integer — serial/ID, pas graphic/type, couche, quantité ni Boolean. 0 : aucun objet actuel.
# Les 32 bits sont conservés ; tester <> 0, pas = TRUE ou > 0. Une valeur enregistrée ne se met
# pas à jour seule. Cherche un objet non détruit sur la couche Backpack de Player. Player
# absent/détruit ou sac absent/détruit donne 0. Identifie le conteneur, pas son contenu ; ne
# crée aucun sac.

SUB Main()
    # before/after sont séparés de 250 ms. WAIT appartient à l’exemple. Des ID égaux aux extrémités
    # ne révèlent pas tous les changements intermédiaires.

    VAR before = UO.Backpack()
    WAIT(250)
    VAR after = UO.Backpack()
    IF before <> after THEN
        UO.Print('ID changed: ' + HEX(after))
    END IF
END SUB
```

**Explication des paramètres et du déroulement:**

- before/after sont séparés de 250 ms. WAIT appartient à l’exemple. Des ID égaux aux extrémités ne révèlent pas tous les changements intermédiaires.

### Fonction IsOwnSerial complète

```vb
# Fonction IsOwnSerial complète
#
# Renvoie l’ID du sac à dos actuellement équipé.
#
# Integer — serial/ID, pas graphic/type, couche, quantité ni Boolean. 0 : aucun objet actuel.
# Les 32 bits sont conservés ; tester <> 0, pas = TRUE ou > 0. Une valeur enregistrée ne se met
# pas à jour seule. Cherche un objet non détruit sur la couche Backpack de Player. Player
# absent/détruit ou sac absent/détruit donne 0. Identifie le conteneur, pas son contenu ; ne
# crée aucun sac.

SUB Main()
    # candidate est l’ID LastTarget sauvegardé. IsOwnSerial(candidate) prend un serial et renvoie
    # Integer Boolean : 1=TRUE pour l’ID propre actuel non nul, sinon 0=FALSE. Définition complète,
    # sans modifier la cible.

    VAR candidate = UO.LastTarget()
    IF IsOwnSerial(candidate) = TRUE THEN
        UO.Print('Own object selected')
    ELSE
        UO.Print('Different object or no own object')
    END IF
END SUB

SUB IsOwnSerial(candidate)
    VAR current = UO.Backpack()
    RETURN current <> 0 AND current = candidate
END SUB
```

**Explication des paramètres et du déroulement:**

- candidate est l’ID LastTarget sauvegardé. IsOwnSerial(candidate) prend un serial et renvoie Integer Boolean : 1=TRUE pour l’ID propre actuel non nul, sinon 0=FALSE. Définition complète, sans modifier la cible.
