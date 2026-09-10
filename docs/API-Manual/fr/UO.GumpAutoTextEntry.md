# UO.GumpAutoTextEntry

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: fr -->

Affecte une valeur une seule fois au premier contrôle correspondant dans un gump serveur ; conserve une action en attente si le contrôle est absent.

## Syntaxe exacte

```text
UO.GumpAutoTextEntry(TextEntryID:Any, Value:Any) -> Unit
```

## Paramètres

- `TextEntryID` — Integer — ID exact du type de contrôle concerné. Ce n’est ni un indice, ni un GumpID, ni le serial de la fenêtre. 0 est un ID ordinaire, jamais le premier contrôle par défaut.
- `Value` — String — texte du champ ; une chaîne vide l’efface. Les restrictions de longueur et de caractères du champ restent applicables.

## Retour

Unit — aucune valeur renvoyée : ni succès, ni nouvelle valeur, ni confirmation du serveur.

## Comportement

- Parcourt les fenêtres existantes dans l’ordre actuel de l’interface, puis les dispositions serveur reçues ou reconstruites. Le premier contrôle du bon type et du bon ID consomme l’action. Utilisez NumGump* avec un indice pour une fenêtre précise.
- Les champs en attente sont remplis avant les réponses automatiques. Répéter le même type et ID dans le même script remplace une valeur encore en attente. Le client accepte 1024 champs en attente ; tout dépassement produit une erreur de script.
- La fin normale d’une procédure conserve ses actions en attente. L’annulation du propriétaire ou Terminate avec son nom les retire ; TerminateAll retire toutes les actions, même celles de procédures terminées. Un changement de monde vide la file. Rien n’est enregistré dans le profil.
- Un champ peut tronquer ou refuser le texte ; le contrôle trouvé consomme quand même l’action. La commande n’envoie aucune réponse de bouton et n’attend pas le serveur. Vérifiez le texte avec GetGumpInfo/NumGumpTextEntry.

## Exemples

### Remplir un contrôle ouvert

```vb
# Remplir un contrôle ouvert
#
# Affecte une valeur une seule fois au premier contrôle correspondant dans un gump serveur ;
# conserve une action en attente si le contrôle est absent.
#
# Unit — aucune valeur renvoyée : ni succès, ni nouvelle valeur, ni confirmation du serveur.

SUB Main()
    # 33 est un exemple d’ID de contrôle : remplacez-le par l’ID réel donné par InfoGump. Le
    # deuxième argument est la valeur. Si le contrôle est absent, l’action reste en attente.

    UO.GumpAutoTextEntry(33, '500')
END SUB
```

**Explication des paramètres et du déroulement:**

- 33 est un exemple d’ID de contrôle : remplacez-le par l’ID réel donné par InfoGump. Le deuxième argument est la valeur. Si le contrôle est absent, l’action reste en attente.

### Remplir avant l’ouverture

```vb
# Remplir avant l’ouverture
#
# Affecte une valeur une seule fois au premier contrôle correspondant dans un gump serveur ;
# conserve une action en attente si le contrôle est absent.
#
# Unit — aucune valeur renvoyée : ni succès, ni nouvelle valeur, ni confirmation du serveur.

SUB Main()
    # 33 est l’ID du contrôle, 100 un exemple de ButtonID de confirmation, 0x40001234 le serial de
    # l’objet ouvrant le formulaire. Remplacez les trois. Le champ est rempli avant la réponse, même
    # si la fenêtre arrive plus tard.

    UO.GumpAutoTextEntry(33, '500')
    UO.WaitGump(100)
    UO.UseObject('0x40001234')
END SUB
```

**Explication des paramètres et du déroulement:**

- 33 est l’ID du contrôle, 100 un exemple de ButtonID de confirmation, 0x40001234 le serial de l’objet ouvrant le formulaire. Remplacez les trois. Le champ est rempli avant la réponse, même si la fenêtre arrive plus tard.

### Remplacer une valeur en attente

```vb
# Remplacer une valeur en attente
#
# Affecte une valeur une seule fois au premier contrôle correspondant dans un gump serveur ;
# conserve une action en attente si le contrôle est absent.
#
# Unit — aucune valeur renvoyée : ni succès, ni nouvelle valeur, ni confirmation du serveur.

SUB Main()
    # Les deux appels utilisent l’ID 33. Si le contrôle n’est pas encore arrivé, seule la dernière
    # valeur reste. Sinon, les deux changements ont lieu immédiatement dans l’ordre des appels.

    UO.GumpAutoTextEntry(33, '500')
    UO.GumpAutoTextEntry(33, '')
END SUB
```

**Explication des paramètres et du déroulement:**

- Les deux appels utilisent l’ID 33. Si le contrôle n’est pas encore arrivé, seule la dernière valeur reste. Sinon, les deux changements ont lieu immédiatement dans l’ordre des appels.
