# Yoko ClassicUO Runtime API Manual — v50.0.0

This index tracks the **complete Runtime-backed API Manual** generated from the current v50.0.0 Runtime. The canonical single-file Manual is shipped in both the project and client and is byte-identical there.

- Product/API source version: **50.0.0**
- Command cards: **738**
- Manifest UO coverage: **734/734**
- Runtime compatibility catalogue: **422 commands / 444 overloads**
- Canonical SHA-256: `4528740e9d5a461847f0f23ebfe4862157edc9d6be26a0b69bec8795cce81d71`
- Every card contains signatures/overloads, parameters, return type/contract, behavior, limitations and examples.

## Important current semantics

- `UO.Hide()` opens an object Target; `UO.Hide(serial)` hides the loaded item/mobile locally without destroying the world entity.
- `UO.InfoGump()` opens the Yoko Gump Inspector; `UO.InfoGumps()` lists active server Gumps for inspection.
- Profile directories use the connected server/shard **display name**, not the legacy `v2` folder.
- `CastToObject` reports real success/failure instead of unconditional success.
- `Version` / `StealthInfo` use the live ClassicUO/Yoko product version.

## Complete GitHub manual parts

The generator produces deterministic `Part-01.md` through `Part-13.md` from the same canonical Manual. They must be published together with this index; regenerate with:

```text
python3 scripts/GenerateGithubApiManual.py
```

Current ranges:

1. `ActivateHandle` → `CastAbility`
2. `CastToObject` → `Dead`
3. `DeleteFindList` → `FindNotoriety`
4. `FindQuantity` → `GetGumpCount`
5. `GetGumpFullLines` → `GetResist`
6. `GetResistCold` → `GListSize`
7. `GlobalChatActiveChannel` → `IsMovable`
8. `IsMoving` → `MaxStamina`
9. `MaxWeight` → `PetsCurrent`
10. `PetsMax` → `SetAutoSellDelay`
11. `SetBadLocation` → `StopScript`
12. `Str` → `Version`
13. `Wait` → `Z`

The v50 source package also includes an automated publisher so all generated parts can be copied/committed/pushed together from a normal Git environment.