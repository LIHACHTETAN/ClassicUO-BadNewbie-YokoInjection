## `UO.UseRec`

### Manifest-registered overloads

- `UO.UseRec() -> Any`
  - **Return type:** `Any`
  - **Return contract:** Compatibility metadata exposes an adapted return slot; the zero-argument command returns no script value.

### Legacy Yoko overloads

- `UO.UseRec()`
  - **Return type:** `Unit`
  - **Return contract:** No value. Replays the command most recently captured by `UO.SetRec()`.

### Parameters

- None. The command is strictly zero-argument.

### Behavior

`UO.UseRec()` decodes the command and typed arguments stored by the v50 `UO.SetRec()` recorder and routes them back through the same legacy compatibility dispatcher. Playback does not consume the recording, so the same action may be replayed repeatedly. If no valid recording exists, `UO.UseRec()` performs no action; in a connected client it reports that no recorded action is available.

### Notes / limitations

- Call `UO.SetRec()`, execute one recordable legacy `UO.*` command, then call `UO.UseRec()`.
- Replay is guarded against recursive re-recording.
- `remain()` returns `1` while a valid recorded action is available and `0` when none is stored.
- The historical Script.dll help did not define playback internals; the behavior above is the explicit v50 ClassicUO/Yoko compatibility contract.

### Examples

```basic
UO.SetRec()
UO.SetDefault('healbag', 0x40001234)

IF remain() = 1 THEN
    UO.UseRec()
END IF
```

---
