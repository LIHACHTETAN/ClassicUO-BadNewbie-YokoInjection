# UO.WaitGump

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: fr -->

Enregistre une suite ordonnée de réponses uniques aux boutons. Le script continue immédiatement ; une fenêtre absente ne le bloque pas pendant 30 secondes.

## Syntaxe exacte

```text
UO.WaitGump(Value:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any, trigger8:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any, trigger8:Any, trigger9:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any, trigger8:Any, trigger9:Any, trigger10:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any, trigger8:Any, trigger9:Any, trigger10:Any, trigger11:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any, trigger8:Any, trigger9:Any, trigger10:Any, trigger11:Any, trigger12:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any, trigger8:Any, trigger9:Any, trigger10:Any, trigger11:Any, trigger12:Any, trigger13:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any, trigger8:Any, trigger9:Any, trigger10:Any, trigger11:Any, trigger12:Any, trigger13:Any, trigger14:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any, trigger8:Any, trigger9:Any, trigger10:Any, trigger11:Any, trigger12:Any, trigger13:Any, trigger14:Any, trigger15:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any, trigger8:Any, trigger9:Any, trigger10:Any, trigger11:Any, trigger12:Any, trigger13:Any, trigger14:Any, trigger15:Any, trigger16:Any) -> Unit
UO.WaitGump(triggerId:Integer) -> Unit
UO.WaitGump(triggerId:String) -> Unit
```

## Paramètres

- `triggerId` — Integer ButtonID ou String numérique. Une chaîne peut contenir une suite séparée par | ou des virgules. Les formes à 2..16 arguments acceptent aussi des tableaux et suites imbriquées. Tous les ID sont analysés avant l’enregistrement. Une suite vide, plus de 256 boutons en attente dans le client ou plus de 32 niveaux d’imbrication provoquent une erreur sans enregistrement partiel.
- `Value` — Élément de suite : Integer ButtonID, String numérique, chaîne séparée par |/virgules ou Array de ces éléments. Traitement de gauche à droite selon les limites de triggerId. Value désigne l’unique paramètre Any, qui accepte aussi un tableau.
- `trigger1` — Élément de suite : Integer ButtonID, String numérique, chaîne séparée par |/virgules ou Array de ces éléments. Traitement de gauche à droite selon les limites de triggerId. Value désigne l’unique paramètre Any, qui accepte aussi un tableau.
- `trigger2` — Élément de suite : Integer ButtonID, String numérique, chaîne séparée par |/virgules ou Array de ces éléments. Traitement de gauche à droite selon les limites de triggerId. Value désigne l’unique paramètre Any, qui accepte aussi un tableau.
- `trigger3` — Élément de suite : Integer ButtonID, String numérique, chaîne séparée par |/virgules ou Array de ces éléments. Traitement de gauche à droite selon les limites de triggerId. Value désigne l’unique paramètre Any, qui accepte aussi un tableau.
- `trigger4` — Élément de suite : Integer ButtonID, String numérique, chaîne séparée par |/virgules ou Array de ces éléments. Traitement de gauche à droite selon les limites de triggerId. Value désigne l’unique paramètre Any, qui accepte aussi un tableau.
- `trigger5` — Élément de suite : Integer ButtonID, String numérique, chaîne séparée par |/virgules ou Array de ces éléments. Traitement de gauche à droite selon les limites de triggerId. Value désigne l’unique paramètre Any, qui accepte aussi un tableau.
- `trigger6` — Élément de suite : Integer ButtonID, String numérique, chaîne séparée par |/virgules ou Array de ces éléments. Traitement de gauche à droite selon les limites de triggerId. Value désigne l’unique paramètre Any, qui accepte aussi un tableau.
- `trigger7` — Élément de suite : Integer ButtonID, String numérique, chaîne séparée par |/virgules ou Array de ces éléments. Traitement de gauche à droite selon les limites de triggerId. Value désigne l’unique paramètre Any, qui accepte aussi un tableau.
- `trigger8` — Élément de suite : Integer ButtonID, String numérique, chaîne séparée par |/virgules ou Array de ces éléments. Traitement de gauche à droite selon les limites de triggerId. Value désigne l’unique paramètre Any, qui accepte aussi un tableau.
- `trigger9` — Élément de suite : Integer ButtonID, String numérique, chaîne séparée par |/virgules ou Array de ces éléments. Traitement de gauche à droite selon les limites de triggerId. Value désigne l’unique paramètre Any, qui accepte aussi un tableau.
- `trigger10` — Élément de suite : Integer ButtonID, String numérique, chaîne séparée par |/virgules ou Array de ces éléments. Traitement de gauche à droite selon les limites de triggerId. Value désigne l’unique paramètre Any, qui accepte aussi un tableau.
- `trigger11` — Élément de suite : Integer ButtonID, String numérique, chaîne séparée par |/virgules ou Array de ces éléments. Traitement de gauche à droite selon les limites de triggerId. Value désigne l’unique paramètre Any, qui accepte aussi un tableau.
- `trigger12` — Élément de suite : Integer ButtonID, String numérique, chaîne séparée par |/virgules ou Array de ces éléments. Traitement de gauche à droite selon les limites de triggerId. Value désigne l’unique paramètre Any, qui accepte aussi un tableau.
- `trigger13` — Élément de suite : Integer ButtonID, String numérique, chaîne séparée par |/virgules ou Array de ces éléments. Traitement de gauche à droite selon les limites de triggerId. Value désigne l’unique paramètre Any, qui accepte aussi un tableau.
- `trigger14` — Élément de suite : Integer ButtonID, String numérique, chaîne séparée par |/virgules ou Array de ces éléments. Traitement de gauche à droite selon les limites de triggerId. Value désigne l’unique paramètre Any, qui accepte aussi un tableau.
- `trigger15` — Élément de suite : Integer ButtonID, String numérique, chaîne séparée par |/virgules ou Array de ces éléments. Traitement de gauche à droite selon les limites de triggerId. Value désigne l’unique paramètre Any, qui accepte aussi un tableau.
- `trigger16` — Élément de suite : Integer ButtonID, String numérique, chaîne séparée par |/virgules ou Array de ces éléments. Traitement de gauche à droite selon les limites de triggerId. Value désigne l’unique paramètre Any, qui accepte aussi un tableau.

## Retour

Unit — aucune valeur renvoyée : ni succès, ni nouvelle valeur, ni confirmation du serveur.

## Comportement

- Exige un vrai bouton Activate portant ce ButtonID ; ignore les changements de page et fenêtres sans correspondance. Les ID suivants ne dépassent pas le premier en attente. Une seule réponse par fenêtre et par réception de disposition. Une disposition reconstruite peut réutiliser le même objet fenêtre.
- Un autre WaitGump du même script prolonge sa suite en attente. Aucun filtre GumpID : utilisez NumGumpButton ou SendGumpSelect pour cibler précisément. ButtonID=0 exige un bouton Activate réel d’ID 0 ; ce n’est pas une fermeture universelle.
- La fin normale d’une procédure conserve ses actions en attente. L’annulation du propriétaire ou Terminate avec son nom les retire ; TerminateAll retire toutes les actions, même celles de procédures terminées. Un changement de monde vide la file. Rien n’est enregistré dans le profil.

## Exemples

### Une réponse

```vb
# Une réponse
#
# Enregistre une suite ordonnée de réponses uniques aux boutons. Le script continue
# immédiatement ; une fenêtre absente ne le bloque pas pendant 30 secondes.
#
# Unit — aucune valeur renvoyée : ni succès, ni nouvelle valeur, ni confirmation du serveur.

SUB Main()
    # 100 est le ButtonID de réponse. WaitGump l’enregistre avant UseObject ; la poursuite du script
    # ne prouve pas que le serveur a confirmé la réponse.

    UO.WaitGump(100)
    UO.UseObject('0x40001234')
END SUB
```

**Explication des paramètres et du déroulement:**

- 100 est le ButtonID de réponse. WaitGump l’enregistre avant UseObject ; la poursuite du script ne prouve pas que le serveur a confirmé la réponse.

### Plusieurs étapes

```vb
# Plusieurs étapes
#
# Enregistre une suite ordonnée de réponses uniques aux boutons. Le script continue
# immédiatement ; une fenêtre absente ne le bloque pas pendant 30 secondes.
#
# Unit — aucune valeur renvoyée : ni succès, ni nouvelle valeur, ni confirmation du serveur.

SUB Main()
    # 7, 22 et 1 sont les ButtonID de formulaires successifs, vérifiés dans cet ordre. Le nombre
    # d’arguments n’est pas un délai ; l’appel enregistre toute la suite.

    UO.WaitGump(7,22,1)
    UO.UseObject('0x40001234')
END SUB
```

**Explication des paramètres et du déroulement:**

- 7, 22 et 1 sont les ButtonID de formulaires successifs, vérifiés dans cet ordre. Le nombre d’arguments n’est pas un délai ; l’appel enregistre toute la suite.

### Annuler les attentes

```vb
# Annuler les attentes
#
# Enregistre une suite ordonnée de réponses uniques aux boutons. Le script continue
# immédiatement ; une fenêtre absente ne le bloque pas pendant 30 secondes.
#
# Unit — aucune valeur renvoyée : ni succès, ni nouvelle valeur, ni confirmation du serveur.

SUB Main()
    # La chaîne 7|22|1 définit la même suite. TerminateAll efface ensuite toutes les actions de gump
    # en attente et arrête toutes les procédures ; son effet est global.

    UO.WaitGump('7|22|1')
    UO.TerminateAll()
END SUB
```

**Explication des paramètres et du déroulement:**

- La chaîne 7|22|1 définit la même suite. TerminateAll efface ensuite toutes les actions de gump en attente et arrête toutes les procédures ; son effet est global.
