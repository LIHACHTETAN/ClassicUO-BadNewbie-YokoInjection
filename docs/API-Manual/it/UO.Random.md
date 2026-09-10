# UO.Random

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: it -->

Sceglie un intero pseudocasuale. Random(min,max) include entrambi gli estremi; la forma precedente Random(max) esclude quello superiore.

## Sintassi esatta

```text
UO.Random(max:Integer) -> Integer
UO.Random(min:Integer, max:Integer) -> Integer
```

## Parametri

- `min` — Limite inferiore, solo con due argomenti. Intero con segno a 32 bit da -2147483648 a 2147483647; deve essere <= max.
- `max` — Due argomenti: limite superiore incluso, qualsiasi Integer con segno. Un argomento: limite superiore escluso, 0..2147483647. Random(0) restituisce 0.

## Restituisce

Integer — un numero scelto, non un valore booleano né un serial. Due argomenti: min <= risultato <= max. Un argomento positivo: 0 <= risultato < max. I valori possono ripetersi.

## Comportamento

- Nessuna forma senza argomenti. Limiti uguali restituiscono quel valore. Limiti invertiti o un unico argomento negativo causano un errore dello script; non vengono scambiati.
- È supportato l’intero intervallo con segno a 32 bit senza overflow di max+1. Per frazioni discrete, dividere interi: Random(0,100)/100.0.
- Il generatore appartiene al runtime dello script; le chiamate simultanee sono sincronizzate. Nessun parametro seed; la funzione è diversa da BASIC Rnd. Salvare il risultato per riutilizzarlo.
- La chiamata è locale: non attende, non muove e non invia pacchetti. Verificare le coordinate casuali; Random(0)=0 non rende valido un indice di un array vuoto.

## Esempi

### Lanciare un dado

```vb
# Lanciare un dado
#
# Sceglie un intero pseudocasuale. Random(min,max) include entrambi gli estremi; la forma
# precedente Random(max) esclude quello superiore.
#
# Integer — un numero scelto, non un valore booleano né un serial. Due argomenti: min <=
# risultato <= max. Un argomento positivo: 0 <= risultato < max. I valori possono ripetersi.

SUB Main()
    # min=1 e max=6 includono tutti e sei i valori. roll memorizza un’estrazione; STR la converte in
    # testo. Una chiamata successiva può dare lo stesso valore.

    VAR roll = UO.Random(1, 6)
    UO.Print(STR(roll))
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- min=1 e max=6 includono tutti e sei i valori. roll memorizza un’estrazione; STR la converte in testo. Una chiamata successiva può dare lo stesso valore.

### Attendere un intervallo casuale

```vb
# Attendere un intervallo casuale
#
# Sceglie un intero pseudocasuale. Random(min,max) include entrambi gli estremi; la forma
# precedente Random(max) esclude quello superiore.
#
# Integer — un numero scelto, non un valore booleano né un serial. Due argomenti: min <=
# risultato <= max. Un argomento positivo: 0 <= risultato < max. I valori possono ripetersi.

SUB Main()
    # min=350 e max=700 sono limiti inclusi in millisecondi. Random calcola delay; UO.Wait(delay)
    # esegue l’attesa. Rispettare il ritardo minimo richiesto dal server.

    VAR delay = UO.Random(350, 700)
    UO.Print(STR(delay))
    UO.Wait(delay)
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- min=350 e max=700 sono limiti inclusi in millisecondi. Random calcola delay; UO.Wait(delay) esegue l’attesa. Rispettare il ritardo minimo richiesto dal server.

### Indici precedenti e limiti uguali

```vb
# Indici precedenti e limiti uguali
#
# Sceglie un intero pseudocasuale. Random(min,max) include entrambi gli estremi; la forma
# precedente Random(max) esclude quello superiore.
#
# Integer — un numero scelto, non un valore booleano né un serial. Due argomenti: min <=
# risultato <= max. Un argomento positivo: 0 <= risultato < max. I valori possono ripetersi.

SUB Main()
    # Random(10) dà 0..9, mai 10. Random(7,7) dà sempre 7. Random(-2,2) può dare -2,-1,0,1,2. Ogni
    # espressione è un’estrazione separata.

    VAR index = UO.Random(10)
    VAR fixedValue = UO.Random(7, 7)
    VAR offset = UO.Random(-2, 2)
    UO.Print(STR(index) + ', ' + STR(fixedValue) + ', ' + STR(offset))
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- Random(10) dà 0..9, mai 10. Random(7,7) dà sempre 7. Random(-2,2) può dare -2,-1,0,1,2. Ogni espressione è un’estrazione separata.
