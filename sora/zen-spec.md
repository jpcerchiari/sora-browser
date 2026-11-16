# Zen visual specification (default, Windows)

Extracted from the Zen 1.24.3b (Firefox 160) source, [zen-browser/desktop](https://github.com/zen-browser/desktop) at commit
`535ccb0`. Paths are relative to that repo. **[FF]** = value inherited from Firefox, read from Firefox's
`main` (may differ slightly from FF160). Release build (`@IS_TWILIGHT@` = false).

Sora's rule: whatever is Zen goes in 1:1; whatever is only Firefox's default keeps Chromium's
default (see the last section).

## 0. Global values

- **Squircle:** every corner is `superellipse(2.3)` on Windows (`zen-theme.css:218-222,354-362`).
  A squircle radius R is equivalent to ~R/2.3 round. Pills and circles stay round.
  In Views: a superellipse path in Skia or a round radius of R/2.3.
- **Font:** `Segoe UI Variable`, `Segoe UI`; tabs at 14px (`vertical-tabs.css:316-318`).
- **Separation:** `--zen-element-separation` = 8px (`prefs/zen/theme.yaml:8`).
- **Radius:** `--zen-border-radius` = 9px on Windows (`zenThemeModifier.js:136-141`).
  Inner radius `--zen-native-inner-radius` = (9 − 4) × 2.3 = 11.5px squircle.
- **Scheme:** follows the system (light/dark).
- **Window background:** Mica/acrylic (`DWMSBT_TRANSIENTWINDOW`) without Firefox's tint.
- **Top border in windowed mode:** 0.5px `ActiveBorder` / `InactiveBorder`.
- **Minimum window height:** 495px.

## 1. Window layout

Defaults: single toolbar (`zen.view.use-single-toolbar=true`), vertical tabs on the left, sidebar
expanded, compact mode off, window buttons hidden until hover.

- **Sidebar, full height:**
  - Top button row, 36px: ☰ menu, compact mode button, flexible space,
    back / forward / reload. Extension buttons go inside the URL bar;
    the extensions button is hidden.
  - URL bar row, 37px, containing only the URL bar.
  - Essentials grid, workspace indicator, "+ New Tab", pinned tabs, separator, tabs.
  - Footer: Library, workspace icons, "+" button.
- **Page card:** 8px margin on the right and bottom, 0 on the left (the sidebar's 5px padding
  provides the gap), 8px strip on top.
- **Window buttons (Windows):** in the 8px strip above the page, top-right corner.
  At rest: height 8px, opacity 0. On hover they grow to 34px, `0.15s ease-in-out` with a
  0.2s delay. The page does not move: only the card's top edge moves down 26px.
  The buttons' visuals are the system default.
- **Sidebar width:** default 186px, minimum 152px, maximum 500px. Double-clicking the handle
  restores the default.
- **Sidebar padding:** 5px on the sides and bottom, 0 on top.
- **Resize handle:** 5px wide, on the right edge, from 8px to 100% − 16px of the height,
  radius 4px, color `--zen-accent-button-background`. Opacity 0, 0.8 on hover or while dragging
  (0.2s with a 0.2s delay).
- **Collapsed sidebar** (not the default): 60px.

## 2. Page card

- Gaps: right 8px, bottom 8px, left 0 (+5px from the sidebar), top 8px.
- Radius: **5px round** (11.5 / 2.3, `zen-browser-container.css:11-15`).
- Shadow: `rgba(0,0,0,0.24) 0 3px 8px`. Content clipped. No border or outline.
- Background behind the page: `#ffffff` / `#202020`.
- Gap between split view pages: 8px.
- Fullscreen with compact mode: separation 0.1px, no radius or shadow.

## 3. Sidebar and tabs

### Tabs

| item | value |
|---|---|
| height | 36px [FF], vertical margin 2px → 40px pitch |
| horizontal margin | 2px |
| radius | 14px squircle ≈ 6px round |
| horizontal padding | 8px |
| favicon | 16px, radius 4px; no favicon: `blank.svg` on `--zen-toolbar-element-bg` |
| favicon margins | 3.33px before, 10px after |
| text | 14px, line-height 1.7, toolbar text color (the selected tab uses the same) |
| hover | `#101010` at 7% (light), `#e2e2e2` at 7% (dark) |
| selected, light | `rgba(255,255,255,.8)` 98% + accent 2% |
| selected, dark | `rgba(255,255,255,.18)` 95% + accent 5% |
| selected shadow | `0 0.8px 1.5px 0`, `rgba(0,0,0,.15)` light / `.05` dark |
| pressed | `scale(0.98)`, 0.1s ease |
| unloaded tab | opacity 0.5, no grayscale |
| loading | no throbber: the favicon stays |

### Close button

- Only appears on hover (and on selected tabs in multiselection).
- 24×24 box, padding 4px, radius 8px.
- "X" made of two 15 × 1.5px bars, radius 1px, `currentColor`, rotated ±45°.
  When appearing, they go from 0°/12px to 45°/15px in 0.12s ease.
- Hover: `currentColor` 10%; pressed: 20%.

### Pinned tabs

- Like normal tabs, without a close button; in its place, a "reset" button (12px bar at 0°).
- URL changed: reset button on the left (2.5 × 16px bar, radius 2px, 15°,
  `rgba(66,61,61,.3)` / white 30%) and a 10px subtitle at opacity 0.6.
- Pinned/normal separator: 22px tall line, 1px stroke `rgba(0,0,0,.1)` /
  `rgba(255,255,255,.1)`, 4px inset. On sidebar hover it becomes a 10px "clear" button,
  weight 500, opacity 0.5 (1 on hover). Transitions 0.08s / 0.06s.

### Essentials (empty by default)

- Grid with ~4 columns, gap 4px, side padding 5px, maximum 12. Top 6px, bottom 2px.
- 46px tall tile, radius 14px squircle, only the centered favicon.
- Background `--zen-toolbar-element-bg`; hover `rgba(0,0,0,.1)` / selected background.
- Selected: the blurred favicon (20px) behind the tile, with `inset: -50%`, and on top a
  layer inset 2px, radius 12px, `rgba(255,255,255,.85)` / `rgba(68,64,64,.85)`
  (`.8` / `.75` on hover).
- Grid transitions: 0.3s ease-out.

### Workspace indicator

- 44px tall. Text 13px weight 500; the name at weight 600.
- Padding 16px on the left, 12px on the right. 16px icon.
- Hover background: inset 4px on top and 7px on the left, radius 14px, tab hover color.
- "…" button, 26px, radius 10px, appears on hover in 0.1s.

### "+ New Tab"

- Same box as a tab (36px, radius 14px), text `currentColor` 70%.
- Pressed: `scale(0.985)`, 0.1s.
- Opens the floating URL bar; while it is open, the row takes the background and
  shadow of the selected tab.

### Footer

- Flex row, `space-between`, gap 4px, standard toolbar buttons (section 5) without padding.
- Workspace icons: 30×30 buttons, radius 6px, 12px icon (emoji) or 14px (image).
  No icon: 8px dot, black/white 40%.
- Inactive: grayscale, opacity 0.7. Active or hover: color and opacity 1; background
  `--zen-toolbar-element-bg` on hover. Transition 0.2s, gap 0.5ch.

### List scrolling

- Scrollbar thumb: `currentColor` 35%.
- 1px lines on top and bottom (`rgba(0,0,0,.08)` / `rgba(255,255,255,.08)`) when the list
  is not at the start or the end.

## 4. URL bar

### At rest, in the sidebar

- 37px row with 1px padding; the box is ~32–35px (value inherited from Firefox, not
  confirmed).
- Background: toolbar text at 8% (light) / 15% (dark). Radius 14px squircle, margin 1px.
  No border, outline or shadow.
- Hover: `rgba(0,0,0,.08)` / `rgba(255,255,255,.1)`.
- Text weight 500, **domain only**, default cursor. Inner padding 4px.
- Identity icon on the right. Page actions and identity stay invisible until sidebar
  hover (they appear in 0.15s).
- Hidden: tracking protection, reader mode, star, go button, PiP, zoom.
- Action icons: minimum width 26px, padding 5px, radius 8px.

### Floating (`floating-on-type`)

- Floats when opened from the keyboard or from a new tab, not from a mouse click.
- Centered. Top = half the window − max(333px, height)/2.
- Width: `min(window/1.5, 750px)`, with a minimum of `min(90%, 62rem)`.
- Field height 62px, side margin 12px, font 1.15em.
- Radius 15px squircle. Background `rgba(255,255,255,.93)` / `rgba(20,20,20,.92)` with a 40px blur
  (without blur: `#fff` / `rgb(24,24,24)`).
- Shadow `0 30px 140px -15px` `rgba(0,0,0,.8)` light / `.6` dark.
- Outline 0.5px `rgba(0,0,0,.2)` / `#4a4a4a`.
- Its place in the sidebar keeps a placeholder with radius 14px and the hover color.
- The rest of the window is not dimmed.
- **Results:**
  - Maximum height 244px, no scrollbar, padding 12px, no search buttons.
  - Rows with a minimum height of 45px, padding 10px × 8px, text black/white 70%.
  - Title and URL at 14px and weight 500; URL in `#4a4a4a` / `#aaaaaa`.
  - Favicon with padding 4px, radius 4px, right margin 12px.
  - Hover: 5% of the inverse of the brand background.
  - **Selected:** `--zen-accent-button-background` at 60%, white text, favicon on a
    white chip at 90%.
  - Shortcut: uppercase, 10px, padding 6 × 8px, radius 4px, 5% background, 1px outline at 10%.
  - Search engine name: 12px, weight 600, padding 4 × 6px, radius 4px, 10% background.
  - "Switch to tab": 28px arrow, opacity 0.7 (1 on the selected row).
  - Search mode label: 14px pill, padding 4 × 8px, accent 50% + black 50% /
    white 20%, white text. On entering: pulse 1 → 0.98 → 1 in 0.25s.

## 5. Toolbar buttons

| item | value |
|---|---|
| icon | 16px |
| size | 28×28 (inner padding 6px), outer padding 1px |
| radius | 8px squircle |
| icon color | `currentColor` 70% |
| hover | inverse of the brand background at 7% |
| active/open | 10% |
| pressed | `scale(0.95)`, 0.2s; background 0.1s |

## 6. Compact mode (off by default)

- Hides only the sidebar (with the single toolbar). Delays: 150ms to keep it on hover, 1000ms to
  hide the bar. Detection outside the window: 200px horizontally, 100px vertically.
- Page with an 8px margin on both sides.
- Floating sidebar: fixed, top 4px (+1px on Windows when windowed), height 100% − 8px,
  left −4px, horizontal padding 8px. Panel with radius 11.5px squircle and the big shadow.
  Background `rgb(240,240,244)` / `rgb(23,23,26)`. Outline 1px `rgba(255,255,255,.15)`, offset −1px.
- Hidden: a ~5px strip remains on the left edge. Disappears in 0.15s ease.
- Appears on hovering the strip (or leaving the window less than 10px from the edge) in 0.25s, with
  a spring that overshoots to 1.0109 at ~72%.
- Turning compact mode on animates the margin with a spring without bounce, duration 0.1.

## 7. Colors

| token | light | dark |
|---|---|---|
| brand background | `#e2e2e2` | `#101010` |
| main background (no Mica) | `#e9e9e9` | `#131313` |
| main background with Mica | transparent | `rgba(0,0,0,.4)` over the acrylic |
| app background underneath | `#e2e2e2` | `#171717` |
| compact mode bar | `rgb(240,240,244)` | `rgb(23,23,26)` |
| toolbar element | text 8% (oklch) | 15% |
| element hover | `rgba(0,0,0,.08)` | `rgba(255,255,255,.10)` |
| popups | `rgb(244,244,244)` | `rgb(31,31,31)` |
| dialogs | `#fafafa` | `#1c1c1c` |
| URL bar | accent 3% + `#f4f4f4` | accent 4% + `rgb(24,24,24)` |
| field border | `#cccccc` | `rgb(66,65,77)` |
| panel separator | `currentColor` 15% | same |
| toolbar text | `rgba(0,0,0,.8)` | `rgba(255,255,255,.8)` |

- No texture (grain 0).
- **Accent color** (the system's):
  - Mixed with the base `[240,240,244]` (light, 50%) or `[23,23,26]` (dark, 80%); in dark mode,
    only 40% of it is then kept over black (`blendColors(rgb, [0,0,0], 40)`).
  - In light mode: saturation +0.3 and lightness = l × 0.4 + 0.252. Pure grays do not change.
- **Text** (`--toolbox-textcolor`): accent 12% + black 88% (light) or white 88% (dark),
  alpha 0.9.
- **Accent button** (`--zen-accent-button-background`): oklch of the accent with lightness
  clamped to .35–.6 (light) or .55–.7 (dark). Used for the handle, the selected result and
  focus outlines.
- **Themed icons:** accent 50% + black (light); primary 15% + `#ebebeb` (dark).
- **Loading bar:** accent + 70% of black 50% / white 50%.
- **Private window:** primary `rgb(11,10,11)`, text white 80%, always dark.

## 8. Animations

| what | specification |
|---|---|
| open tab | opacity 0→1, scale 0.95→1, 0.12s easeOut |
| close tab | opacity 1→0, scale →0.95, bottom margin →−height, 0.1s easeOut |
| switch workspace | spring without bounce, 0.25s; background cross-fade |
| window button bar | 0.15s ease-in-out with a 0.2s delay |
| footer "+" | rotates 0→45° in 0.2s while the popup is open |
| loading indicator | 5rem × 0.4rem pill centered at the top (−4px), pulses every 1s; on a long load it grows to 10rem in 0.3s |
| dialogs | enter in 0.3s ease-out, exit in 0.2s ease-in |

## 9. Firefox defaults: Sora keeps Chromium's defaults

- Window button visuals (only the position is Zen's).
- Context menus (Zen only changes padding and color).
- App menu, panels, downloads, bookmarks, find-in-page bar.
- `about:` pages, preferences, library, status bar, page scrollbars.
- Dialogs (Zen only changes the box's radius, border and shadow), notification bars, PiP,
  DevTools, tooltips, menu bar, bookmarks toolbar.

## 10. Glance

Preview of a link in a floating window on top of the page (`src/zen/glance/`). On by
default (`zen.glance.enabled`, `prefs/zen/glance.yaml:5-6`). Paths in this section are relative to
`src/zen/glance/` unless stated otherwise; `GM` = `ZenGlanceManager.mjs`, `GC` =
`actors/ZenGlanceChild.sys.mjs`.

- **Trigger:** **Alt + left click** on a link (`zen.glance.activation-method = "alt"`,
  `glance.yaml:14-15`; options ctrl, alt, shift, meta). The actor uses "ctrl" only as a fallback
  value if the pref is missing (`GC:20-25`).
  - Only with a single modifier (the check is an XOR, `GC:46-48,155`), left button, event not
    canceled by the page (`GC:151-158`).
  - Does not open if the mouse moved more than 4px between mousedown and click: that is text selection
    (`GC:29,136-148`). Does not open `javascript:` links or URLs the page cannot load
    (`GC:102-120`). The original click is canceled (`GC:172-174`).
  - Also open in Glance: Alt + click on a bookmark (`GM:1925-1940`); "Open link in
    Glance" in the link context menu (`GM:223-244`,
    `src/browser/base/content/nsContextMenu-sys-mjs.patch:10`); links from essential tabs to
    another domain, http/https/file only (`zen.glance.open-essential-external-links = true`,
    `glance.yaml:11-12`; `GM:1731-1758`).
  - With the tab bar hidden, the link opens in a normal tab (`GM:546-553`).
- **What it is:** a real tab, child of the source tab, drawn inside the parent tab's row
  in the sidebar (`GM:344-404`). One Glance at a time (`GM:555-562`). Switching tabs hides the
  Glance; returning to the parent tab shows it again (`GM:1588-1635`).
- **Window:** 80% of the page area's width, 100% of its height, centered
  (`zen-glance.css:123-143`; `GM:808,1018-1019`). Radius equal to the card's, 5px round
  (`zen-glance.css:145-150`). Shadow `--zen-big-shadow` = `rgba(0,0,0,0.24) 0 3px 8px`
  (`zen-glance.css:147`, `zen-tokens.css:463`). Page background `#ffffff` / `#101010`
  (`zen-glance.css:152-153`, `zen-tokens.css:236`). No URL bar of its own.
- **Source page:** shrinks to scale 0.97 and takes opacity 0.3 (`GM:9,647-667`),
  meaning it almost fades into the window background. No blur. Clicking it closes the Glance
  (`GM:294-301`).
- **Buttons:** a column attached to the right of the Glance (`left: 100%`; on the left if the sidebar is
  on the right), `top` 15px, padding 12px, gap 12px, maximum width 56px (`zen-glance.css:7-27`;
  `zen-tokens.css:20,23,26,73`). From top to bottom: close (X), open as tab (fullscreen
  icon), split (`zen-glance.inc.xhtml:6-10`; `src/browser/themes/shared/zen-icons/icons.css:41,291,469`).
  - Each one: 34px circle (`--size-item-large`, `src/zen/common/styles/zen-buttons.css:14`),
    padding 8px, icon only, shadow `0 0 12px 1px rgba(0,0,0,0.07)` (`zen-glance.css:29-41`,
    `zen-tokens.css:239`).
  - Background `#1c1c1c` (light) / `#e2e2e2` (dark) with 4% of the accent color; icon in the accent
    color (`zen-glance.css:32,41`, `zen-tokens.css:233`).
  - Hover: `#292929` / `#cccccc` and scale 1.02; pressed: scale 0.98; transition 0.05s
    (`zen-glance.css:33-50`, `zen-tokens.css:234`).
- **Close:** X button, Esc, click on the source page, closing the parent tab (`GM:1641-1645`) or
  closing the Glance tab (Ctrl+W, `GM:1670-1694`). Respects `beforeunload` (`GM:1118-1121`).
  If the parent tab is the only tab, a new tab is opened (`GM:1174-1177`).
  - Esc with a page element focused does not close at first: the X turns red
    `rgb(220,53,69)`, gets the label "Confirm" (max. 4rem) for 3s, and a second Esc closes
    (`GC:177-186`; `GM:1131-1149`; `zen-glance.css:68-94`; `zen-tokens.css:235,242`).
- **Open as tab** (button or Ctrl+O, `src/browser/base/content/zen-keysets.inc.xhtml:39`):
  becomes a normal tab right after the parent and becomes active (`GM:1817-1863`). Fullscreen (DOM
  fullscreen) inside the Glance does the same (`GM:1652-1662`).
- **Split:** opens as a tab and creates a side-by-side split view with the parent, the Glance on the right
  (`GM:1999-2020`).

| animation (`zen.glance.animation-duration` = 350ms, `glance.yaml:17-18`) | specification |
|---|---|
| open | the Glance leaves the clicked link's rectangle and flies in an arc (height 40% of the distance, max. 30px) to the center, growing to 80% × 100%; spring with bounce 0.2 tuned to settle in 350ms (`GM:10,36-41,732-783,800-930,951-957`). A snapshot of the link follows the flight (`GM:695-730`); the page fades in with opacity 0→1 in 87.5ms (350/4) ease-in-out (`GM:746-759`) |
| source page on open | scale 1→0.97 and opacity 1→0.3, same spring (`GM:647-667`) |
| buttons on open | opacity 0→1 and x −20px→0 in 200ms, with a 150ms delay (`GM:448-469`) |
| close | arc back to the link's rectangle, 350ms ease-out (`GM:1275-1316`); the page fades out with opacity 0.15s ease-in-out (`zen-glance.css:163-168`); buttons fade out in 120ms (`GM:1203-1215`); the source page returns to scale 1 and opacity 1 in ~233ms (350/1.5) (`GM:1248-1266`) |
| open as tab | width 80%→100% and scale 1→1.005→1, 250ms ease-in-out (`GM:1897-1918`) |

## 11. Workspaces

Zen's "Spaces" (`src/zen/spaces/`). On by default. Paths in this section are relative to
`src/zen/spaces/` unless stated otherwise; `SM` = `ZenSpaceManager.mjs`.

- **What it is:** name, optional icon (emoji or SVG) and theme (gradient that defines the window's
  accent color), plus an optional container (`SM:2876-2898`).
- **Default:** the window starts with one workspace, "Space", with no icon, no theme and no container
  (`SM:867-870`). Container 0 is the all-containers one, so the essentials are the same in every
  workspace (`zen.workspaces.separate-essentials` only separates by container).
- **Tabs:** every normal or pinned tab belongs to a workspace (`zen-workspace-id`); the
  essentials belong to none. A tab without a workspace (new, restored, coming from another
  window) joins the active one (`SM:2601-2647`). New tabs go to the active one.
- **Switching:** only the normal and pinned tabs of the active workspace are shown; the essentials stay.
  Selects the last tab used in that workspace, or the empty tab if there is none
  (`SM:2649-2700`). Selecting a tab from another workspace (search, shortcut, link) switches to it
  (`SM:2580-2599`). The theme changes with it, with a cross-fade; the animation is in section 8.
- **Creating:** the footer "+" opens a menu (create Space, folder, empty split, new tab). Creating a
  Space makes a "Space" right after the current one, switches to it and shows a form with name,
  icon and profile (`SM:1656-1690`, `ZenSpaceCreation.mjs`).
- **Context menu** (right click on the indicator or on a footer icon, or the indicator's "…"):
  change name, change icon, change theme, profile, the list of workspaces to switch to,
  manage, unload, unload the others, create, share, delete
  (`src/browser/base/content/zen-panels/popups.inc:13-38`). Delete asks for confirmation ("Delete
  Space?") and closes the workspace's tabs (`SM:1272-1285`, `SM:1488-1507`).
- **Indicator:** at the top of the list, after the essentials and before "+ New Tab": icon and name
  (measurements in section 3). Double-clicking the name renames it in place; double-clicking the icon changes the icon
  (`ZenSpace.mjs:179-210`).
- **Footer:** one icon per workspace, in their order (measurements in section 3). Click switches;
  dragging reorders. Ctrl + mouse wheel over the sidebar and the swipe gesture also switch
  (`SM:660-700`, `ZenSpacesSwipe.mjs`), wrapping around at the end (`zen.workspaces.wrap-around-navigation`).
- **Shortcuts** (`src/browser/base/content/zen-keysets.inc.xhtml:10-28`): Alt+1…9 and Alt+0 go to
  the 1st…10th workspace (Ctrl on macOS); Ctrl+Alt+→ and Ctrl+Alt+← go to the next and the previous one.
  Creating has no shortcut.
- **Persistence:** the list and the active one are kept in the window's session store (`spaces`,
  `activeZenSpace`, `SM:854-878`).
- **Last tab:** closing the workspace's last normal tab selects the empty tab; the workspace
  remains (`zen.workspaces.open-new-tab-if-last-unpinned-tab-is-closed` = false).

## 12. Split view

Two to four tabs side by side in the page area (`src/zen/split-view/`). Paths in this section are
relative to `src/zen/split-view/` unless stated otherwise; `VS` = `ZenViewSplitter.mjs`,
`SV` = `zen-split-view.css`, `SG` = `zen-split-group.inc.css`.

- **What it is:** a special tab group (`tab-group[split-view-group]`) with 2 to 4 tabs
  (`MAX_TABS = 4`, `VS:87`). Selecting any tab in the group shows all of them; the selected tab is
  the active pane. Clicking a pane selects its tab (`VS:1865-1876`). Closing a tab removes
  it from the split; with 2 tabs, the split is dissolved (`VS:230-245`). The split is restored with the session
  (`VS:2418`).
- **Layouts:** `grid` (default, `VS:1502`), `vsep` (columns) and `hsep` (rows). With 2 tabs,
  `grid` is the same as `vsep`; with 3 or 4 it becomes columns of two rows (`VS:1639-1668`).
- **Cards:** each pane is its own card, with the page card's radius and shadow
  (5px, `rgba(0,0,0,.24) 0 3px 8px`; `src/zen/common/styles/zen-browser-container.css:11-15`).
  Between them, the frame.
- **Gap:** 8px between columns (`--zen-split-row-gap` = `--zen-element-separation`) and 9px between
  rows (`--zen-split-column-gap` = separation + 1px) (`SV:92-95`). The cards' outer edges
  sit where the single card would be (negative margins, `SV:13-15,97-102`).
- **Active pane:** 2px outline outside the card, in the color
  `hsl(from primary h s l−20)` in light mode and `--button-background-color-primary` in dark mode
  (`SV:72,80-83`). Inactive panes have no outline. Hidden in fullscreen.
- **Resizing:** the whole gap is the handle, invisible; only the cursor changes (`ew-resize`/`ns-resize`,
  `SV:125-130`, `VS:1882-1952`). Minimum of 7% per pane (`zen.splitView.min-resize-width`).
  Panes move with `inset 0.09s ease-out` (`SV:74`).
- **Header on hover:** hovering a pane shows, after 0.1s and with a 0.1s fade,
  a tab attached to the top of the pane, centered, in the active outline color, with the
  rearrange (drag) and remove-from-split buttons (`SV:139-191`, `VS:1704-1720`).
- **In the tab list** (expanded sidebar, `SG`): the group becomes a single tab-shaped row
  (tab height, tab radius, 2px padding on the sides), with the tabs sharing the width
  (`flex: 1`). Each tab inside is 28px tall (`SG:66-68`).
  - Without the active tab: transparent row, 1px × 16px separator (`--size-item-small` [FF])
    between the tabs, black at 10% / white at 20% (`SG:73-82`; `src/zen/common/styles/zen-tokens.css:383`).
    Hover: background `--zen-toolbar-element-bg` (text at 8%/15%) (`SG:128-130`).
  - With the active tab: the whole row has the selected tab background; the active pane's tab has
    on top `--zen-split-view-active-tab-bg` = `--zen-toolbar-element-bg` at 60% (`SG:18-22,101-116`);
    no separator.
  - Close button only on hover, and only on tabs 70px or wider (`SG:135-155`).
  - Collapsed sidebar: the tabs stack in a column with a 2px outline
    `--zen-colors-border-contrast` (`SG:49-57,158-166`).
- **Creating:**
  - Tab context menu: "Add Split View..." (one tab: split with an empty tab), "Join N
    Tabs" (several selected), "Split Out Tab" (a tab already in a split)
    (`VS:1177-1203,1278-1318`; `locales/en-US/browser/browser/zen-split-view.ftl`).
  - Link context menu: "Split Link to New Tab" (`VS:1243-1264`).
  - Dragging a tab to the page edge: in the outer quarter of the width or height the preview
    appears (half the area, 2px outline in the primary color, big shadow), and dropping creates the split
    (`VS:285-450`; `SV:204-232`). On by default (`zen.splitView.enable-tab-drop`).
  - Glance: split button (section 10).
  - Shortcuts (`src/browser/base/content/zen-keysets.inc.xhtml:31-35`): Ctrl+Alt+G grid,
    Ctrl+Alt+V columns, Ctrl+Alt+H rows (with the next tab, or the selected ones), Ctrl+Alt+U
    unsplit, Ctrl+Shift+* empty split (`VS:2062-2098,2567`).

**In Sora** (`split-view.patch`), on top of Chromium's native split (2 tabs, side by side or
stacked): per-pane cards with Zen's shadow, 8px gap, outer edges where the single card
would be, invisible handle (the grip only appears with keyboard focus), without Chromium's
mini toolbar and, in the list, the single row with the separator and the active pane highlight. Creating keeps
what Chromium already has: context menu ("New split view with current tab", two tabs
selected, "Arrange" with swap/unsplit), dragging a tab or link to the page edge, and the
Glance button.

## 13. Folders

Folders of pinned tabs (`src/zen/folders/`). Paths in this section are relative to
`src/zen/folders/`; `ZF` = `ZenFolders.mjs`, `F` = `ZenFolder.mjs`, `CSS` = `zen-folders.css`.

- **What it is:** a tab group (`zen-folder`, subclass of Firefox's `tab-group`, `F:7`) that
  only exists in a workspace's pinned section; the tabs inside stay pinned (`ZF:743-750`).
  It does not go into the essentials. Folders can have subfolders, up to 5 levels
  (`zen.folders.max-subfolders`, `ZF:737-741`). Every folder keeps a hidden empty tab
  so it does not disappear when it runs out of tabs (`ZF:765-775`).
- **Folder row:** the height of a tab (`--tab-min-height` + 2 × margin), 28px folder icon
  5px from the edge, name in semibold weight with a 32px indent, hover with the tab hover background
  in a rectangle 2px smaller on each side, tab radius (`CSS:68-170`). Folder color derived from the
  primary: back fill `primary 60% + gray`, front `primary + white 70%`, stroke
  `primary 50% + black` (light; `CSS:13-18`). No group color or group line (`CSS:7-9,74-75`).
- **Icon:** an SVG folder with a back sheet and a front sheet (`F:24-60`). When open, the sheets
  tilt 16° in opposite directions and shrink to 0.85, in 0.3s
  `cubic-bezier(.42,0,0,1)` (`zen-folder-icon.inc.css`). When closed with an active tab inside, the
  icon swaps its glyph for three dots (`CSS:122-136`, `ZF:1092-1108`).
- **Contents:** tabs and subfolders indented 14px (`CSS:52-57`).
- **Collapsing:** click on the row. When collapsed, the folder keeps showing its active tabs
  (`has-active`, `ZF:403-425`); selecting a tab inside it by another route reveals it.
  0.18s easeInOut animation to collapse and expand, 0.2s to reveal (`ZF:1710-1716`).
  With active tabs, a button on the row unloads all of them (`F:14`, `CSS:183-190`).
- **Creating:** tab context menu, "Move to Folder" › existing folders or "New Folder"
  (`ZF:68-78`); sidebar context menu, "New Folder" (`ZF:79`); the footer "+" (section 11).
  The new folder is named "New Folder", goes before the pinned separator and opens ready to
  rename (`ZF:604-645,743-808`).
- **Folder menu:** rename, new subfolder, ungroup ("Unpack"), unload all,
  convert to Space, move to another Space, delete
  (`locales/en-US/browser/browser/zen-folders.ftl`).
- **Search:** with `zen.folders.search.enabled`, a popup with the folder's tabs and a search
  field (`ZF:197-222,884-1090`).
- **Persistence:** the window's session store (`ZF:1255-1450`).

**In Sora:** not implemented yet. Pinned tabs are the essentials (global) and workspaces are tab
groups, so there are no per-workspace pinned tabs where folders would live, and Chromium's model does not
nest collections: `PinnedTabCollection` only accepts `SPLIT` and `TabGroupTabCollection` only accepts
`SPLIT` (`components/tabs/impl/*_tab_collection.cc`). The path is on the roadmap.

## Not determined by the code

- Exact height of the URL bar box at rest.
- Effective width of the floating URL bar (the "90%" depends on the container).
- Which tab hover color wins, Zen's or Firefox's (`currentColor` 11%).
- FF160 values marked as [FF].
