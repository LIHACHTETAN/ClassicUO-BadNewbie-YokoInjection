# UO.Alive

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: fr -->

Vérifie la présence d’un objet sans état de mort.

## Syntaxe exacte

```text
UO.Alive() -> Integer
UO.Alive(value:Any) -> Integer
```

## Paramètres

- `value` — Objet facultatif dans les formes affichées : serial numérique ou chaîne hexadécimale, self, lasttarget ou nom AddObject enregistré. Ce n’est pas un type. Sans argument, lit self. Un texte inconnu provoque une erreur de conversion dans certaines formes ; vérifiez le nom.

## Retour

Integer Boolean : 1 = TRUE, 0 = FALSE. Comparez avec des nombres ou des constantes logiques sans guillemets. 1 si un serial positif existe sans être marqué mort. Un objet présent renvoie aussi 1 : ce n’est pas un filtre de mobiles. Un objet mort ou absent renvoie 0.

Résultat logique : 1 = TRUE, 0 = FALSE. Après VAR result = commande(...), utilisez IF result = TRUE THEN ou IF result = 1 THEN ; sinon IF result = FALSE THEN ou IF result = 0 THEN. TRUE/FALSE sans guillemets. Appelez une seule fois et conservez le résultat : un nouvel appel peut répéter l’action ou lire un état modifié.

## Comportement

- Lit le modèle local : aucun target, aucune demande de status, aucune modification d’indicateur ni émission de paquet. Un objet détruit est absent avant même le retrait de son entrée du dictionnaire.
- Chaque résultat est une lecture distincte. Le monde peut changer entre Exists et l’appel suivant ; plusieurs lectures ne forment pas un instantané atomique.

### Fonctions internes : de l’appel au résultat

Voici les véritables étapes internes C#. ReadState est une fonction auxiliaire entièrement définie dans l’exemple, pas une commande intégrée cachée.

#### 1. RegisterCharacterGetterAliases

À la création du runtime, RegisterCharacterGetterAliases enregistre les noms et les formes. Sans argument, utilise bridge.Self ; avec un argument, son serial. Les enregistrements existants sont conservés.

1 si un serial positif existe sans être marqué mort. Un objet présent renvoie aussi 1 : ce n’est pas un filtre de mobiles. Un objet mort ou absent renvoie 0.

Source du projet: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; fonction `RegisterCharacterGetterAliases`.

#### 2. TryGetObject

TryGetObject résout les nombres, les chaînes hexadécimales et les noms enregistrés. Le nom AddObject est résolu à chaque appel ; aucune recherche graphic/type ni sélection interactive.

Objet facultatif dans les formes affichées : serial numérique ou chaîne hexadécimale, self, lasttarget ou nom AddObject enregistré. Ce n’est pas un type. Sans argument, lit self. Un texte inconnu provoque une erreur de conversion dans certaines formes ; vérifiez le nom.

Source du projet: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; fonction `TryGetObject`.

#### 3. Invoke

Invoke lit dans le thread du jeu ; un thread de travail attend le traitement par le gestionnaire. L’annulation du script interrompt cette attente. Aucun délai ni appel réseau supplémentaire.

Chaque résultat est une lecture distincte. Le monde peut changer entre Exists et l’appel suivant ; plusieurs lectures ne forment pas un instantané atomique.

Source du projet: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; fonction `Invoke`.

#### 4. Get

World.Get résout le serial et renvoie null pour IsDestroyed, puis lit l’indicateur Mobile. Alive vérifie Exists et l’absence de IsDead ; les objets sont admis. Dead sur self lit Player.IsDead.

1 si un serial positif existe sans être marqué mort. Un objet présent renvoie aussi 1 : ce n’est pas un filtre de mobiles. Un objet mort ou absent renvoie 0.

Source du projet: `src/ClassicUO.Client/Game/World.cs`; fonction `Get`.

Lit le modèle local : aucun target, aucune demande de status, aucune modification d’indicateur ni émission de paquet. Un objet détruit est absent avant même le retrait de son entrée du dictionnaire.


## Exemples

### Vérifier son propre état

```vb
# Vérifier son propre état
#
# Vérifie la présence d’un objet sans état de mort.
#
# Integer Boolean : 1 = TRUE, 0 = FALSE. Comparez avec des nombres ou des constantes logiques
# sans guillemets. 1 si un serial positif existe sans être marqué mort. Un objet présent renvoie
# aussi 1 : ce n’est pas un filtre de mobiles. Un objet mort ou absent renvoie 0.
#
# Résultat logique : 1 = TRUE, 0 = FALSE. Après VAR result = commande(...), utilisez IF result =
# TRUE THEN ou IF result = 1 THEN ; sinon IF result = FALSE THEN ou IF result = 0 THEN.
# TRUE/FALSE sans guillemets. Appelez une seule fois et conservez le résultat : un nouvel appel
# peut répéter l’action ou lire un état modifié.

SUB Main()
    # Les parenthèses vides lisent self. active conserve un résultat ; TRUE et FALSE choisissent les
    # deux branches. Print affiche seulement un exemple de message.

    VAR active = UO.Alive()
    IF active = TRUE THEN
        UO.Print('State is active')
    ELSE
        UO.Print('State is inactive or unavailable')
    END IF
END SUB
```

**Explication des paramètres et du déroulement:**

- Les parenthèses vides lisent self. active conserve un résultat ; TRUE et FALSE choisissent les deux branches. Print affiche seulement un exemple de message.

### Objet sélectionné et fonction ReadState complète

```vb
# Objet sélectionné et fonction ReadState complète
#
# Vérifie la présence d’un objet sans état de mort.
#
# Integer Boolean : 1 = TRUE, 0 = FALSE. Comparez avec des nombres ou des constantes logiques
# sans guillemets. 1 si un serial positif existe sans être marqué mort. Un objet présent renvoie
# aussi 1 : ce n’est pas un filtre de mobiles. Un objet mort ou absent renvoie 0.
#
# Résultat logique : 1 = TRUE, 0 = FALSE. Après VAR result = commande(...), utilisez IF result =
# TRUE THEN ou IF result = 1 THEN ; sinon IF result = FALSE THEN ou IF result = 0 THEN.
# TRUE/FALSE sans guillemets. Appelez une seule fois et conservez le résultat : un nouvel appel
# peut répéter l’action ou lire un état modifié.

SUB Main()
    # lasttarget est l’objet précédemment sélectionné. Exists vérifie sa présence. obj est l’unique
    # paramètre de ReadState ; la fonction renvoie le résultat inchangé. Sa définition complète est
    # incluse dans le code copié.

    IF UO.Exists('lasttarget') THEN
        VAR observed = ReadState('lasttarget')
        UO.Print('State 1/0: ' + CStr(observed))
    END IF
END SUB

SUB ReadState(obj)
    RETURN UO.Alive(obj)
END SUB
```

**Explication des paramètres et du déroulement:**

- lasttarget est l’objet précédemment sélectionné. Exists vérifie sa présence. obj est l’unique paramètre de ReadState ; la fonction renvoie le résultat inchangé. Sa définition complète est incluse dans le code copié.

### Détecter un changement en une demi-seconde

```vb
# Détecter un changement en une demi-seconde
#
# Vérifie la présence d’un objet sans état de mort.
#
# Integer Boolean : 1 = TRUE, 0 = FALSE. Comparez avec des nombres ou des constantes logiques
# sans guillemets. 1 si un serial positif existe sans être marqué mort. Un objet présent renvoie
# aussi 1 : ce n’est pas un filtre de mobiles. Un objet mort ou absent renvoie 0.
#
# Résultat logique : 1 = TRUE, 0 = FALSE. Après VAR result = commande(...), utilisez IF result =
# TRUE THEN ou IF result = 1 THEN ; sinon IF result = FALSE THEN ou IF result = 0 THEN.
# TRUE/FALSE sans guillemets. Appelez une seule fois et conservez le résultat : un nouvel appel
# peut répéter l’action ou lire un état modifié.

SUB Main()
    # Les deux appels sans argument lisent self ; WAIT(500) signifie 500 millisecondes. Deux
    # instantanés sont comparés : des transitions intermédiaires peuvent échapper à la lecture.
    # Aucune attente infinie.

    VAR before = UO.Alive()
    WAIT(500)
    VAR after = UO.Alive()
    IF before <> after THEN
        UO.Print('State changed: ' + CStr(before) + ' -> ' + CStr(after))
    END IF
END SUB
```

**Explication des paramètres et du déroulement:**

- Les deux appels sans argument lisent self ; WAIT(500) signifie 500 millisecondes. Deux instantanés sont comparés : des transitions intermédiaires peuvent échapper à la lecture. Aucune attente infinie.
