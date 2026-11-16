# Roadmap

What has landed in Sora Browser and what is still missing. Each item becomes a patch in
[`patches/sora/`](../patches/sora/). Before writing new code, check whether Chromium already has
the feature: extending what exists costs far less than reimplementing it.

## Done
- [x] Based on ungoogled-chromium-windows (Chromium 157.0.8103.78).
- [x] Branding: name, data folder, ProgIDs and `sora:` scheme (`branding.patch`).
- [x] Vertical tabs by default (`vertical-tabs-by-default.patch`).
- [x] Zen palette: frame, toolbar, tabs, text and address bar (`color-mixer.patch`).
- [x] Page as a floating card with margin, corners and shadow (`floating-contents.patch`).
- [x] Sidebar and tab metrics (`vertical-tab-metrics.patch`).
- [x] Single toolbar at the top of the sidebar, in two rows (`sidebar-toolbar.patch`).
- [x] Button and address bar shapes (`toolbar-shapes.patch`).
- [x] Tab font and close button only on hover (`vertical-tab-style.patch`).
- [x] Toolbar buttons with icons at 70% and a 7% hover (`color-mixer.patch`).
- [x] Idle address bar: domain only, weight 500, icons that Zen hides (`omnibox-idle.patch`).
- [x] Sidebar without the native row, "+ New tab" at the top, and footer (`sidebar-rows.patch`).
- [x] Results list with the Zen look (`omnibox-results.patch`).
- [x] Floating address bar when opened from the keyboard or a new tab (`floating-urlbar.patch`).
- [x] Essentials: pinned tabs in a grid with the Zen look (`essentials.patch`).
- [x] Window buttons hidden in an 8px strip that grows on hover; toolbar inside the compact panel (`window-controls.patch`).
- [x] Compact mode with a floating panel and a 5px strip (`compact-mode.patch`).
- [x] Workspaces on top of tab group focus mode: indicator, icons and "+" in the footer (`workspaces.patch`).
- [x] Glance: Alt+click opens the link in a floating card with close, open as tab and split (`glance.patch`).
- [x] Accent color derived from the system as in Zen, with the workspace color taking precedence (`frame-polish.patch`).
- [x] Exact card shadow, `0 3px 8px rgba(0,0,0,.24)` (`frame-polish.patch`).
- [x] Dedicated compact mode panel color and 1px outline (`frame-polish.patch`).
- [x] "+ New tab" row hover with the tabs' 7% overlay; the footer buttons already used the
  toolbar's 7% overlay (`tabs-polish.patch`).
- [x] Sidebar resize handle: 5px, accent color, shown on hover or while dragging,
  double-click resets to 186px (`tabs-polish.patch`).
- [x] Animations for press (tab at 0.98), tab open/close (opacity and 0.95 scale) and the
  close "X" (`tabs-polish.patch`).
- [x] Discarded tab at 50% without grayscale or ring; favicon instead of the throbber
  (`tabs-polish.patch`).
- [x] Split view with the Zen look on top of the native split: one shadowed card per pane, 8px
  gap, invisible handle, no mini toolbar; in the list, a single row with a separator and the
  active pane highlighted (`split-view.patch`).
- [x] Workspaces, polish: default workspace without a theme (gray = no theme, the system accent
  shows), emoji at the start of the name as the icon, switching slides the list (0.25s), Alt+1…9
  and Alt+0, a workspace that survives closing its last tab (reopened with a new tab), rename
  by double-clicking the indicator (`workspaces-polish.patch`).
- [x] Glance, polish: accent-colored buttons with a 1.02 hover, spring arc from the click point,
  background tab at 0.97 scale, buttons entering after the arc, closing in a reverse arc,
  Esc confirmation, Ctrl+W closing only the Glance, "Open Link in Glance" in the context menu,
  tab helpers that do not depend on a tab, and JS dialogs (`glance-polish.patch`).

## First build
- [ ] Risks to check: listed per patch in the reports; the main ones are in `sora/README.md`.
- [ ] Build on Windows, on the personal PC, and fix whatever breaks.
- [ ] Compare the colors with Zen side by side, in the light and dark themes.

## Visual
- [ ] Sidebar footer: replace Downloads with the Library (the workspace icons and the "+" have
  landed; the collapse button leaves the footer once compact mode gets the first-row button).
- [ ] Page actions and site chip only on sidebar hover (150ms fade); default cursor and 4px inner padding on the idle bar.
- [ ] Floating bar, what is missing: uppercase shortcut chip, 28px "switch to tab" arrow,
  results frame shadow and radius, translucent background with blur, search mode icon and pill
  inside the field, animations, opening when typing on the page.
- [ ] Pinned tabs: reset button instead of close, and a pinned/normal separator.
- [ ] Squircle card corners (`superellipse(2.3)`, radius 11.5): the page clip is the
  compositor's rounded corner, so the shadow and painted corners stay rounded until there is
  path clipping.
- [ ] Zen accent in what still uses `kColorSysPrimary`: the selected
  address bar result (`--color-sys-primary` in the CSS; switch to
  `kColorSoraAccentButtonBackground` if the popup loads the Chrome colors).
- [ ] Tab open/close animations, what is missing: today they run together with Chromium's
  layout animation (200ms, the row grows or shrinks), ending at Zen's 0.12s/0.1s; easeOut curve.
- [x] Close button: 24×24 box with radius 8, 10% background on hover and 20% when pressed
  (`tab-close-box.patch`).
- [ ] Close button: `scale(0.97)` when pressed (needs its own layer on the button, which today
  shares layers with the ink drop).

## Zen features
Zen's own features come to Sora too, not just the look. Whatever in Zen is just the Firefox
default stays with the Chromium default.

- [ ] Compact mode, what is missing: spring with overshoot, reveal when leaving the window near
  the edge, Ctrl+Alt+C shortcut.
- [ ] Essentials, what is missing: limit of 12, 6/2px grid padding, 0.3s transition, unread dot, favicon instead of the audio indicator.
- [ ] Workspaces, what is missing: theme cross-fade on switch (needs a snapshot of the frame or
  interpolating the `ColorProvider` colors), the outgoing list moving together with the incoming
  one in the switch animation, picking the icon from a picker (today the emoji is typed into the
  name, Win+.), "+" menu (folder, empty split, new tab), drag to reorder, Ctrl + mouse wheel,
  workspace list in the context menu, the same workspaces in every window, the same group (not a
  new one) when reopening the workspace of the last closed tab.
- [ ] Split view, what is missing: 2px outline in the Zen color on the active pane only (today
  it is Chromium's 1px outline, colored on the inactive pane too: `kColorMultiContentsView*ContentOutline`
  in `sora_color_mixer.cc` and `kThickness`/`kCornerRadius` in `contents_container_outline.h`),
  header on hover with rearrange and remove from split, up to 4 tabs and grid layout (Chromium's
  `SplitTabCollection` holds 2), 9px gap between rows when stacked, Zen-style drag
  preview (half the area, no delay), Ctrl+Alt+V/H/U and
  Ctrl+Shift+* shortcuts (`accelerator_table.cc`), "Split link into new tab" in the link
  context menu, stacked row with an outline in the collapsed sidebar.
- [ ] Pinned tab folders. They do not fit without a new model: Sora's pinned tabs are the
  essentials (global) and workspaces are groups, and Chromium does not nest collections
  (`PinnedTabCollection` and `TabGroupTabCollection` only accept `SPLIT`). Path: (1) per-workspace
  pinned tabs, a section at the top of the workspace group; (2) a `FOLDER` type in
  `TabCollection::Type` (`components/tabs`), accepted inside `GROUP` and inside itself
  (5 levels), with name, collapsed state and id, and `TabStripModel` APIs to create, move and
  ungroup; (3) the `switch` statements on the type (`TabModel::UpdateProperties()`, which already
  walks up the ancestors and so still finds the workspace group, `TabCollectionNode`,
  `tab_strip_api`, observers); (4) a `FolderView` in the sidebar (row
  with the icon, 14px indent, collapsing shows the active tabs); (5) saving to the session
  (`chrome/browser/sessions`, which does not know about folders). Spec in section 13 of
  `zen-spec.md`.
- [ ] Glance, what is missing: Alt+click on bookmarks; arc from the link's rectangle (today a
  24px square at the click point) and the link snapshot flying along; passwords and find (Ctrl+F)
  inside the Glance, which today come from `TabFeatures` and only exist in a tab (Ctrl+F searches
  the background tab); `beforeunload` on close;
  "open as tab" with Zen's 80%→100% animation.

## Branding
- [x] Windows app icon: PNGs, `chromium.ico` and Start tiles (`sora/branding/`).
- [x] HTML and PDF document icons (`chromium_doc.ico`, `chromium_pdf.ico`).
- [x] Incognito icon: the tile at night, with a crescent moon (`sora-incognito.svg`).
- [ ] Linux and Mac icons (once there are builds for those platforms).
- [x] UI strings: "Chromium" → "Sora" in messages and translations
  (`sora/tools/rebrand_strings.py`, run by `build.py`).
- [x] Sora's own strings in a `.grdp`, with a pt-BR translation (`strings.patch`).
- [ ] Translations of Sora's strings into other languages (today they fall back to English).
- [x] Own Active Setup GUID and COM CLSIDs (`branding.patch`).
- [ ] Own IIDs and TypeLibs: new interfaces in the `.idl` files of the elevation service and the
  tracing service, and the MIDL output regenerated on Windows (`third_party/win_build_output/midl`).
  Only matters for a system-level install alongside a Chromium.

## Map: Zen module → where it lives in Chromium

Before writing new code, check whether Chromium already has the feature behind a flag.
Several Zen features already exist there, and extending what exists costs far less than
reimplementing it. Everything marked "verify" must be checked on the chosen tag.

| Zen (`src/zen/…`) | What it does | Chromium | Approach |
|---|---|---|---|
| `tokens/` (488 tokens, 185 external) | colors, radii, spacing, shadows | `ui/color/`, `chrome/browser/ui/color/chrome_color_mixer.cc`, `ChromeLayoutProvider` | **started**: `sora_color_mixer.cc` with the main surfaces |
| `common/styles/zen-theme.css`, `common/zenThemeModifier.js` | workspace gradient, accent color | `ThemeService`, dynamic `ui/color` mixers | extend the user color mixer |
| `tabs/` | vertical tabs in the sidebar | `chrome/browser/ui/views/tabs/vertical/`, pref `vertical_tabs.enabled` | **done**: on by default |
| `common/styles/zen-sidebar.css`, `zen-browser-ui.css` | sidebar, content with rounded border and margin | `BrowserView`, `ContentsWebView`, `side_panel/` | patch the `BrowserView` layout |
| `compact-mode/` | hides the sidebar and toolbar, which appear on hover | `BrowserView`, logic similar to immersive mode | new |
| `spaces/`, `space-routing/` | workspaces with their own tabs, color and icon | tab groups and saved tab groups (verify) | new, built on tab groups |
| `folders/`, `live-folders/` | pinned tab folders | none: collections do not nest, groups are already the workspaces | new collection type (see Zen features) |
| `split-view/` | two or more tabs side by side | split tabs (`MultiContentsView`, `SplitTabCollection`, 2 tabs) | **started**: Zen look on top of the native one |
| `glance/` | link preview in a floating window | link preview (verify) | extend or new |
| `urlbar/` | floating omnibox in the center | `chrome/browser/ui/views/omnibox/` | patch |
| `media/` | media controls in the sidebar | Global Media Controls | reuse |
| `downloads/`, `little-window/`, `share/` | download animation, little window, share | various | after the core |
| `boosts/`, `mods/`, `library/`, `welcome/` | per-site CSS, community themes, library, onboarding | — | out of the first milestone |
