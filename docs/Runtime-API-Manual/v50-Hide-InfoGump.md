# v50.0.0 — Hide / InfoGump / InfoGumps

Source: canonical Runtime-backed API Manual.

## `UO.Hide`

### Direct runtime overloads

- `UO.Hide() -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. Opens an object Target. If the user selects a loaded item/mobile, that object is hidden locally in this ClassicUO client.
- `UO.Hide(serial) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. Hides the specified loaded item/mobile immediately without opening Target.

### Parameters

- `serial` — loaded item/mobile serial (`Integer`, normally written as hexadecimal such as `0x40000044`). `0`, self, or a serial not present in the loaded world is rejected/no-op.

### Behavior

`UO.Hide` is a **client-side visibility command**, not the Ultima Online **Hiding** skill.

- `UO.Hide()` opens a normal object Target. Selecting a loaded item or mobile sets its local drawing state to hidden.
- `UO.Hide(serial)` performs the same local hide directly by serial and does **not** open Target.
- The object remains in world state; it is not destroyed and no delete-object packet is sent to the server.
- A later server resend, world reload, reconnect, or object recreation may make the object visible again.

### Notes / limitations

- Only the two forms above are supported. `Hide(x, y, z)` does **not** exist.
- The player's own mobile is intentionally refused.
- This affects only the local ClassicUO rendering state; it does not make the object invisible to other players or to the server.
- `CancelTarget()` / Escape can cancel the interactive `Hide()` form before selection.

### Examples

Interactive Target:

```basic
UO.Hide()
```

Hide a known object immediately:

```basic
VAR obj = 0x40000044
UO.Hide(obj)
```

Typical guarded use:

```basic
VAR obj = UO.GetLastTarget()
IF obj <> 0 THEN
    UO.Hide(obj)
END IF
```

---

## `UO.InfoGump`

### Current Yoko overloads

- `UO.InfoGump() -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. Opens the Yoko **Gump Inspector** for the last active server Gump.
- `UO.InfoGump(gump) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. Opens the inspector for the requested Gump when it can be resolved by index, local serial, or server Gump ID.

### Parameters

- `gump` — Gump selector. The current bridge accepts an active-Gump index and also resolves matching local/server Gump IDs. Use `InfoGumps()` first when several Gumps are open and you do not know which selector to use.

### Behavior

Opens a dedicated **Yoko Gump Inspector**. The inspector is not a journal dump: it is an in-client information window built from the currently active ClassicUO Gump tree.

The inspector shows, when available:

- active Gump index;
- local `Serial`;
- server `GumpID`;
- screen `X` / `Y`;
- `Width` / `Height`;
- active `Page`;
- close capability;
- total control count;
- Buttons with **ButtonID**, action/page information and graphics;
- Checkbox / Radio controls with IDs, checked state and graphics;
- TextEntry values;
- text/HTML/cliloc-derived visible text where the ClassicUO control exposes it;
- a full per-control description for debugging scripts.

The inspected Gump also becomes the selected Gump used by `UO.SendGumpSelect(buttonId)`, so inspection and subsequent scripted button activation refer to the same window unless it is closed/disposed.

### Notes / limitations

- `InfoGump()` selects the **last active server Gump**.
- If the requested Gump cannot be resolved, no other Gump is silently substituted; an error is reported.
- The information reflects ClassicUO's currently loaded UI controls. Server-side data that was never sent to the client cannot be displayed.
- Control descriptions are intended for script development and may contain client-control type names in addition to shard-level IDs.

### Examples

Inspect the most recently opened Gump:

```basic
UO.InfoGump()
```

List all active Gumps first, then inspect Gump index `0`:

```basic
UO.InfoGumps()
UO.InfoGump(0)
```

After visually finding ButtonID `1001`, press it on the same selected Gump:

```basic
UO.InfoGump()
UO.SendGumpSelect(1001)
```

---

## `UO.InfoGumps`

### Current Yoko overloads

- `UO.InfoGumps() -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. Opens a list of all active server Gumps.
- `UO.InfoGumps(gump) -> Unit`
  - **Return type:** `Unit`
  - **Return contract:** No value. Compatibility form that opens the detailed inspector for the requested Gump.

### Parameters

- `gump` — optional active-Gump selector (index/local serial/server Gump ID) for the compatibility form.

### Behavior

Without arguments, opens the **Active Server Gumps** window. Each row identifies one currently active server Gump and includes the information needed to choose it for `InfoGump`, such as:

- index;
- `GumpID`;
- local `Serial`;
- screen position;
- size;
- active page;
- control count.

`InfoGumps()` is therefore the discovery/list command, while `InfoGump()` is the detailed control inspector.

### Notes / limitations

- Only active, non-disposed server Gumps are listed.
- Client-only UI Gumps with no server serial are intentionally excluded from this server-Gump list.
- The list is a snapshot; indexes can change when Gumps close/open. Resolve/inspect again before acting if the UI changed.

### Examples

Show every active server Gump:

```basic
UO.InfoGumps()
```

Inspect the first listed Gump:

```basic
UO.InfoGumps()
UO.InfoGump(0)
```

---
