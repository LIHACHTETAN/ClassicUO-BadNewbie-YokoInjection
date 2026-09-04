## `UO.SetRec`

### Manifest-registered overloads

- `UO.SetRec() -> Any`
  - **Return type:** `Any`
  - **Return contract:** Compatibility metadata exposes an adapted return slot; the command itself is zero-argument and returns no script value.

### Legacy Yoko overloads

- `UO.SetRec()`
  - **Return type:** `Unit`
  - **Return contract:** No value. Arms a one-shot recorder for the next legacy `UO.*` compatibility command.

### Parameters

- None. The command is strictly zero-argument.

### Behavior

The recovered Injection help identifies `UO.SetRec()` as a Script.dll-only command introduced by `<=1501.17`, but the historical help page was unfinished and the public Injection source archives do not contain its Script.dll implementation. ClassicUO Yoko v50 therefore provides an explicit deterministic replacement instead of a no-op: `UO.SetRec()` clears the previous recorded action and arms recording. The next command routed through the legacy `UO.*` compatibility dispatcher executes normally and is saved together with its typed arguments. `UO.UseRec()` can then replay the saved command.

### Notes / limitations

- Recording is one-shot: after one compatible command is captured, the recorder automatically disarms.
- `UO.SetRec()` and `UO.UseRec()` themselves are never captured.
- The stored command is kept in Yoko runtime state and survives the normal runtime-state snapshot/restore path.
- `remain()` returns `0` immediately after `UO.SetRec()` and `1` after a command has been captured.
- This v50 behavior is a documented ClassicUO/Yoko compatibility definition because no authoritative public Script.dll implementation of the historical semantics is available.

### Examples

```basic
UO.SetRec()
UO.SetDefault('healbag', 0x40001234)  # executes and is recorded
IF remain() = 1 THEN
    UO.UseRec()                       # repeats SetDefault with the same arguments
END IF
```

---
