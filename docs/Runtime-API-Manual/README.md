# Yoko ClassicUO Runtime API Manual — v50.0.0

This is the GitHub copy of the **complete** Runtime-backed API Manual. The project and client keep the canonical single-file Manual; GitHub uses deterministic alphabetical parts so no command card is omitted by file-size limits.

- Product/API source version: **50.0.0**
- Command cards: **738**
- Manifest UO coverage: **734/734**
- Runtime compatibility catalogue: **422 commands / 444 overloads**
- Canonical SHA-256: `4528740e9d5a461847f0f23ebfe4862157edc9d6be26a0b69bec8795cce81d71`
- Source: current registered Runtime + generated runtime contracts + release manifest.
- Every card contains signatures/overloads, parameters, return type/contract, behavior, limitations and examples.

## v50 command help

- [Hide / InfoGump / InfoGumps — full v50 help](v50-Hide-InfoGump.md)

## Parts

| Part | Range | Cards | Bytes |
| --- | --- | ---: | ---: |
| [Part-01.md](Part-01.md) | `ActivateHandle` → `AddType` | 17 | 31178 |
| [Part-02.md](Part-02.md) | `AddUserStatic` → `BookSetText` | 22 | 34688 |
| [Part-03.md](Part-03.md) | `Bow` → `CharTitle` | 22 | 33755 |
| [Part-04.md](Part-04.md) | `CheckLag` → `ClientPrint` | 22 | 33574 |
| [Part-05.md](Part-05.md) | `ClientPrintEx` → `ContainerOff` | 23 | 33397 |
| [Part-06.md](Part-06.md) | `ConvertIntegerToFlags` → `Dress` | 22 | 34934 |
| [Part-07.md](Part-07.md) | `DressSavedSet` → `EUO2Type` | 21 | 35122 |
| [Part-08.md](Part-08.md) | `Exec` → `FindQuantity` | 20 | 34264 |
| [Part-09.md](Part-09.md) | `FindType` → `GetArrayLength` | 24 | 34163 |
| [Part-10.md](Part-10.md) | `GetARStatus` → `GetFlying` | 24 | 34684 |
| [Part-11.md](Part-11.md) | `GetFollowers` → `GetIgnoreList` | 26 | 34914 |
| [Part-12.md](Part-12.md) | `GetInfo` → `GetMobile` | 25 | 34051 |
| [Part-13.md](Part-13.md) | `GetMobiles` → `GetPrice` | 22 | 34587 |
| [Part-14.md](Part-14.md) | `GetProfile` → `GetStaticArt` | 28 | 35133 |
| [Part-15.md](Part-15.md) | `GetStaticTileAt` → `GetUserStatics` | 25 | 35129 |
| [Part-16.md](Part-16.md) | `GetWalkMountTimer` → `Gold` | 26 | 35114 |
| [Part-17.md](Part-17.md) | `Grab` → `Ignore` | 19 | 34652 |
| [Part-18.md](Part-18.md) | `IgnoreOff` → `IsFemale` | 21 | 34473 |
| [Part-19.md](Part-19.md) | `IsFlying` → `IsWaterTile` | 21 | 33730 |
| [Part-20.md](Part-20.md) | `IsWorldCellPassable` → `LineCount` | 27 | 35068 |
| [Part-21.md](Part-21.md) | `LineID` → `MaxStamina` | 21 | 34467 |
| [Part-22.md](Part-22.md) | `MaxWeight` → `MoverStop` | 19 | 34916 |
| [Part-23.md](Part-23.md) | `moveThroughCorner` → `Online` | 17 | 34176 |
| [Part-24.md](Part-24.md) | `OpenContainer` → `PredictedX` | 24 | 34852 |
| [Part-25.md](Part-25.md) | `PredictedY` → `RenameMobile` | 26 | 35132 |
| [Part-26.md](Part-26.md) | `ReqProfile` → `SetArm` | 27 | 33691 |
| [Part-27.md](Part-27.md) | `SetARStatus` → `SetJournalLine` | 16 | 35011 |
| [Part-28.md](Part-28.md) | `SetMulPath` → `SkillVal` | 24 | 34828 |
| [Part-29.md](Part-29.md) | `Snap` → `TargetByResource` | 21 | 34021 |
| [Part-30.md](Part-30.md) | `TargetID` → `Undress` | 27 | 34484 |
| [Part-31.md](Part-31.md) | `Unequip` → `UseSelfPaperdollScroll` | 23 | 34873 |
| [Part-32.md](Part-32.md) | `UseSkill` → `WaitingMenu` | 16 | 33838 |
| [Part-33.md](Part-33.md) | `WaitJournalLine` → `WarTargetID` | 14 | 33205 |
| [Part-34.md](Part-34.md) | `WearItem` → `Z` | 6 | 7937 |

## Important current semantics

- `UO.Hide()` opens an object Target; `UO.Hide(serial)` hides the loaded item/mobile locally without destroying the world entity.
- `UO.InfoGump()` opens the Yoko Gump Inspector; `UO.InfoGumps()` lists active server Gumps for inspection.
- Profile directories use the connected server/shard **display name**, not the legacy `v2` folder.
- `CastToObject` reports real success/failure instead of unconditional success.
- `Version` / `StealthInfo` use the live ClassicUO/Yoko product version.
- `SetRec`, `UseRec` and global `remain()` are historical Script.dll-only compatibility surfaces whose original help pages did not define behavior; this runtime does not invent fake recorder semantics.

Regenerate with `python3 scripts/GenerateGithubApiManual.py` after changing Runtime/API documentation.
