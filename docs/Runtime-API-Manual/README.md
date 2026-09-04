# Yoko ClassicUO Runtime API Manual

This is the GitHub copy of the **complete** Runtime-backed API Manual. The project and client keep the canonical single-file Manual; GitHub uses deterministic alphabetical parts so no command card is omitted by file-size limits.

- Command cards: **738**
- Canonical SHA-256: `8d72cc7804a9f02e72429248ea901b00765bdd7bc3d01520dc673f725b82237e`
- Source: current registered Runtime + generated runtime contracts + release manifest.
- Every card contains signatures/overloads, parameters, return type/contract, behavior, limitations and examples.

## Parts

| Part | Range | Cards | Bytes |
| --- | --- | ---: | ---: |
| [Part-01.md](Part-01.md) | `ActivateHandle` → `CastAbility` | 54 | 89436 |
| [Part-02.md](Part-02.md) | `CastToObject` → `Dead` | 58 | 88289 |
| [Part-03.md](Part-03.md) | `DeleteFindList` → `FindNotoriety` | 56 | 90274 |
| [Part-04.md](Part-04.md) | `FindQuantity` → `GetGumpCount` | 65 | 88809 |
| [Part-05.md](Part-05.md) | `GetGumpFullLines` → `GetResist` | 62 | 90162 |
| [Part-06.md](Part-06.md) | `GetResistCold` → `GListSize` | 68 | 90251 |
| [Part-07.md](Part-07.md) | `GlobalChatActiveChannel` → `IsMovable` | 54 | 90111 |
| [Part-08.md](Part-08.md) | `IsMoving` → `MaxStamina` | 61 | 90166 |
| [Part-09.md](Part-09.md) | `MaxWeight` → `PetsCurrent` | 50 | 88869 |
| [Part-10.md](Part-10.md) | `PetsMax` → `SetAutoSellDelay` | 66 | 88940 |
| [Part-11.md](Part-11.md) | `SetBadLocation` → `StopScript` | 53 | 88963 |
| [Part-12.md](Part-12.md) | `Str` → `Version` | 61 | 88579 |
| [Part-13.md](Part-13.md) | `Wait` → `Z` | 30 | 63376 |

## Important current semantics

- `UO.Hide()` opens an object Target; `UO.Hide(serial)` hides the loaded item/mobile locally without destroying the world entity.
- `UO.InfoGump()` opens the Yoko Gump Inspector; `UO.InfoGumps()` lists active server Gumps for inspection.
- Profile directories use the connected server/shard **display name**, not the legacy `v2` folder.
- `SetRec`, `UseRec` and global `remain()` are historical Script.dll-only compatibility surfaces whose original help pages did not define behavior; this runtime does not invent fake recorder semantics.

Regenerate with `python3 scripts/GenerateGithubApiManual.py` after changing Runtime/API documentation.
