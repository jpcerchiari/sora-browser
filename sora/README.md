# Sora Browser development

A personal browser: [ungoogled-chromium](https://github.com/ungoogled-software/ungoogled-chromium)
with the look and features of [Zen Browser](https://github.com/zen-browser/desktop)
rewritten in C++/Views.

This repository is a fork of
[ungoogled-chromium-windows](https://github.com/ungoogled-software/ungoogled-chromium-windows)
(remote `upstream`). Everything specific to Sora is kept separate, so that upstream updates
come in with as few conflicts as possible:

- `sora/`: this documentation and the tools;
- `patches/sora/`: the Sora patches, listed at the end of `patches/series`;
- `.gitattributes`: keeps the patches with LF line endings.

Zen is a Firefox fork and its UI is CSS, JS and XUL. None of that runs in the Chromium
UI. That is why it is used here as a **design and behavior reference**, not as code.
Reference: [zen-browser/desktop](https://github.com/zen-browser/desktop), commit `535ccb0`.

## Decisions

- Base: **ungoogled-chromium** (2026-11-16), at the submodule version
  (`ungoogled-chromium/chromium_version.txt`, currently 157.0.8103.78). Replaces the earlier
  decision to use plain Chromium.
- First build: **Windows**.
- Name: **Sora Browser**. "Sora" means "sky" in Japanese, in line with Zen.

## Building

Same as ungoogled-chromium-windows: follow [`docs/building.md`](../docs/building.md) (Visual Studio, Python,
`python build.py`). `build.py` downloads Chromium, prunes the binaries, applies
`ungoogled-chromium/patches/series` and then `patches/series` (where the Sora patches are),
runs `sora/tools/rebrand_strings.py` (see below), does the domain substitution and compiles. It needs ~100 GB free.

## Writing a patch without the Chromium tree

`sora/tools/minitree.py` downloads only the requested files, at the ungoogled version, and applies
the earlier patches in the series to them, in build order:

```bash
python3 sora/tools/minitree.py /tmp/mt chrome/browser/ui/color/chrome_color_mixers.cc
# edit in /tmp/mt
git -C /tmp/mt add -N .   # if you created new files
git -C /tmp/mt diff > patches/sora/<name>.patch
```

Then append `sora/<name>.patch` to the end of `patches/series`. To redo a patch that
is already in the series, use `--upto sora/<name>.patch`. Check it with `patch -p1 --ignore-whitespace
--forward`, which is what `build.py` uses.

When updating from upstream (`git fetch upstream && git merge upstream/master`), run minitree
with every file touched by Sora to check that the patches still apply.

## Patches

All of them apply on top of 157.0.8103.78 (check with `python3 sora/tools/check_patches.py`).
The Zen visual spec they follow is in [`zen-spec.md`](zen-spec.md).

| patch | what it does |
|---|---|
| `sora/branding.patch` | Product name and data folder (`%LOCALAPPDATA%\Sora\User Data`), ProgIDs `SoraHTM`/`SoraPDF` and the `sora:` scheme. Own Active Setup GUID and CLSIDs (notifications, elevation service and tracing service), so it does not collide with a Chromium installed on the same machine. The IIDs and TypeLibs remain Chromium's: they are in the `.idl` files and in the checked-in MIDL output in `third_party/win_build_output`, which can only be regenerated on Windows. |
| `sora/vertical-tabs-by-default.patch` | Vertical tabs enabled by default (pref `vertical_tabs.enabled`). |
| `sora/color-mixer.patch` | `sora_color_mixer.cc`: Zen palette without Mica. Frame, toolbar and sidebar in `#e9e9e9`/`#131313`; text with 12% accent at 90%; tab hover 7%; active tab with an 80%/18% white veil and 2%/5% accent; address bar with text at 8%/15%; toolbar buttons with the icon at 70%, hover 7% and pressed 10%. Installed themes, high contrast and forced colors still apply. |
| `sora/floating-contents.patch` | Page as a floating card: 8px margin (0 on the tab side), 5px corners, shadow always visible, no separators, no concave corners and no tab strip outline. Reuses the side panel's `shadow_box`. |
| `sora/vertical-tab-metrics.patch` | Sidebar at 186px (min. 152, max. 500, collapsed 60), 36px tabs with radius 6 and 4px between them, 7px padding on the sides and 5px on top and bottom. |
| `sora/sidebar-toolbar.patch` | Zen's single toolbar: with the sidebar expanded, the toolbar sits at its top, in two rows (☰ and buttons on the left, back/forward/reload on the right; address bar below). The page extends up to the top, leaving only the window-controls strip. |
| `sora/toolbar-shapes.patch` | Toolbar buttons at 28px with radius 4; address bar and results list with radius 6. |
| `sora/vertical-tab-style.patch` | Tab title at 14px and close button only on hover or focus. |
| `sora/omnibox-idle.patch` | Zen address bar: unfocused it shows only the domain (`ShouldTrimDisplayUrlAfterHostName`), focused it shows the full URL right on click; text at weight 500; star, reading mode, zoom and third-party cookies hidden (the actions and shortcuts still work). |
| `sora/sidebar-rows.patch` | Expanded sidebar without the native button row (tab search, collapse) and without the separator; a "+ New tab" row at the top of the list, shaped like a tab, with text at 70% and `scale(0.985)` when pressed; footer with Downloads on the left and the collapse button on the right. When collapsed, everything reverts to Chromium's default. |
| `sora/glance.patch` | Glance: Alt+click on an http(s) link opens the page in a floating card over the tab (80% of the width, radius 5, Zen shadow, tab background dimmed), with close, open as tab (Ctrl+O) and split buttons. Closes with Esc, a click outside or the X. Replaces Alt+click download. Spec in section 10 of `zen-spec.md`. |
| `sora/compact-mode.patch` | Zen compact mode: button right after ☰ (pref `sora.compact_mode.enabled`, off by default). The sidebar becomes a floating panel that comes in from a 5px strip on the left edge (250ms to enter, 150ms to leave, 150ms hover tolerance), with 5px corners and a shadow; the card gets 8px on both sides. With the panel open, the toolbar sits at its top, in two rows; Ctrl+L reveals the panel (`window-controls.patch`). |
| `sora/essentials.patch` | Pinned tabs become Zen's Essentials: grid with Zen's `auto-fit` (4px gap, columns following the 2/4/5/6/9 tile rules), 46px tiles with only the favicon, no outline, toolbar element background; the active tile paints the blurred favicon (sigma 20) behind an 85% white / `rgba(68,64,64,.85)` card. Three new colors in `sora_color_mixer.cc`. |
| `sora/floating-urlbar.patch` | Zen floating address bar: opened from the keyboard (Ctrl+L, Alt+D, F6) or in a new tab, the field moves to a layer over the page, centered (62px tall, Zen width, radius 6.5, 0.5px outline and the large shadow), with the results attached below; its place in the sidebar stays as a placeholder in the hover color. A mouse click opens it in place. Esc closes it and returns focus to the page. |
| `sora/omnibox-results.patch` | Results list of the classic WebUI popup with Zen's look: up to 244px without a scrollbar, 12px padding, 45px rows with radius 6, 14px text at weight 500 at 70%, URL `#4a4a4a`/`#aaaaaa`, 5% hover, selected row in the accent color at 60% with white text and the favicon in a white chip, 12px/600 search engine chip. New rules only apply inside `omnibox-popup-app`, so the NTP search box is unchanged. |
| `sora/workspaces.patch` | Zen Workspaces on top of the tab group focus mode (`TabGroupsFocusing`, on by default, without freezing the tabs of other groups): workspace = tab group, active = focused group. Only the active workspace's tabs and the pinned ones (essentials) are shown; new tabs and ungrouped tabs go into the active one; selecting a tab from another workspace switches to it; name, color and the active workspace come back with session restore (the active one is the active tab's group). 44px indicator above "+ New tab" (dot in the group color, 13px/600 name, hover background) and, in the footer, one dot per workspace (30×30, radius 6, gray at 70% when inactive) and the "+". Clicking the indicator or right-clicking an icon opens Chromium's group editor (name, color, delete). Ctrl+Alt+→/← and Alt+Shift+X/Z switch. Spec in section 11 of `zen-spec.md`. |
| `sora/window-controls.patch` | Zen window controls: with the toolbar in the sidebar, an 8px strip above the card (draggable) with invisible buttons; on hover it grows to 34px (200ms delay, 150ms ease-in-out), the buttons appear and the card's top edge moves down without moving the page. In compact mode, the toolbar goes at the top of the floating panel, above the page. |
| `sora/frame-polish.patch` | Frame polish. Zen accent color: the Windows accent mixed with the base (50% in light, 80% in dark, and in dark only 40% of it over black) gives the dominant color, which tints the text by 12%; in light, saturation +0.3 and lightness pulled 60% toward 0.42 give the primary (`kColorSoraAccent`), which tints the active tab; `kColorSoraAccentButtonBackground` is the primary in oklch with lightness clamped to .35–.6 / .55–.7. The active workspace's color (or the one chosen in Customize Chrome) wins over the system accent and is applied without the mix, like a Zen workspace theme; incognito windows use Zen's primary `rgb(11,10,11)`. Exact card shadow, `0 3px 8px rgba(0,0,0,.24)`, with its own shadow source in `ShadowFrameView`. Compact mode panel with background `rgb(240,240,244)`/`rgb(23,23,26)` and a 1px inner outline in white at 15%, which continues into the toolbar at the top of the panel. |
| `sora/tabs-polish.patch` | Vertical tab polish. "+ New tab" row without ink drop, with the tabs' hover background (7% veil). Zen resize handle on the sidebar's `ResizeArea`: 5px bar with radius 4, from 8px below the top to 8px above the bottom, in `kColorSoraAccentButtonBackground`, invisible at rest and at 0.8 on hover, focus or drag (200ms delay to appear, 200ms ease-in-out); double-click resets to 186px. Pressed tab at `scale(0.98)` for 100ms, on a layer that `TabCollectionAnimatingLayoutManager` does not destroy while it lasts (`kSoraKeepLayerKey`). Opening and closing a tab with opacity and 0.95 scale, inside Chromium's 200ms layout animation and finishing in 120ms/100ms. Close "X" drawn with two 1.5px bars that go from 0°/12px to 45°/15px in 120ms each time the button appears. Favicon without throbber (the "Loading..." title remains) and discarded tab with favicon and title at 50%, without the ring or the shrunken favicon. Vertical tabs only. |
| `sora/split-view.patch` | Zen Split view on top of Chromium's native split (2 tabs). With the page as a card (vertical tabs, not fullscreen), each pane becomes its own card with the 5px radius and Zen shadow (painted by `MultiContentsBackgroundView`, so it also shows in the gap), the panes take the place of the single card and sit 8px apart; the pane outline (Chromium's, 1px) touches the card from outside. The resize handle is the gap, invisible (the grip only shows with keyboard focus), and Chromium's mini toolbar is gone. In the tab list, the split becomes a single tab-shaped row: selected tab background when active, a 1px × 16px separator when not, and the active pane's tab with a 28px highlight (text at 4.8%/9%). Spec in section 12 of `zen-spec.md`. |
| `sora/workspaces-polish.patch` | Workspace polish. No theme: a gray group is a workspace without a theme, and `BrowserWidget` ignores the focus mode color for it, so the system accent (or the Customize Chrome color) shows; the default workspace starts gray, and choosing gray in the editor removes the theme. The active workspace's color follows the editor immediately (Chromium only updates it when switching groups). Icon: an emoji at the start of the name, followed by a space ("🚀 Work"), stays in the group title and therefore comes back with the session; it shows in the indicator and the footer in place of the dot (14px; inactive in gray at 70%). Switching: the tab list slides in from the side of the new workspace (full width, 250ms, strong ease-out instead of the no-bounce spring), clipped to the sidebar; no theme cross-fade. Alt+1…9 and Alt+0 go to the 1st…10th workspace (top row only; Windows only), selecting the last tab used in it. Closing the last tab of the active workspace reopens the workspace in the same place, with its name and color, in a new tab (Chromium deletes the group with its last tab; deleting from the editor or closing the window still deletes it). Indicator as in Zen: double-clicking the name renames it in place (Enter or leaving saves, Esc cancels, an empty name is ignored), double-clicking the icon opens the editor; right-click, Enter and Space open the editor; a single click does nothing. |
| `sora/glance-polish.patch` | Glance polish. Buttons in the Zen accent color (`kColorSoraAccent`: background `#1c1c1c`/`#e2e2e2` with 4% of it, icon in it), hover `#292929`/`#cccccc` with scale 1.02 and pressed 0.98 (50ms). Open: the card flies in an arc from the click point (the browser does not know the link's rectangle; 24px square) to its place, on a spring with bounce 0.2 that stops at 350ms, without relayout of the page (`SetNativeViewSize`); the page comes in over 87.5ms; the tab behind shrinks to 0.97 (transform on the page's aura window) while the 70% veil appears; the buttons come in with opacity and 20px over 200ms after 150ms. Close: arc back, page fades out in 0.15s, buttons in 120ms, tab behind returns in 233ms. Esc with a page element focused turns the X red `rgb(220,53,69)` with "Confirm" for 3s; a second Esc closes. Ctrl+W and Ctrl+F4 close only the Glance (Glance's `PreHandleKeyboardEvent`). "Open Link in Glance" item in the context menu of http(s) links. The Glance page gets the tab helpers that are not yet in `TabFeatures` (autofill, zoom, infobars, session id; `friend` in `tab_helpers.h`) and `alert`/`confirm`/`prompt` as window dialogs, as in DevTools. |
| `sora/app-icon.patch` | Bumps `kCurrentProfileIconVersion` to 11, so Windows profile shortcuts are rebuilt with the new icon (as required by Chromium's `win/README`). The icons themselves are not a patch: see "Icon" below. |
| `sora/strings.patch` | Sora's own strings in `chrome/app/sora_strings.grdp` (included in `generated_resources.grd`), with the pt-BR translation in the `.xtb`: name of a new workspace ("Space"), tooltip of the workspaces "+", the compact mode button, the "Open link in Glance" context menu item and Glance's "Confirm". Replaces the literals from the earlier patches with the messages. Other languages fall back to English (`fallback_to_english`). Each translation's id is the fingerprint of the English text (grit's `tclib.GenerateMessageId`): change the text and the id changes. |
| `sora/tab-close-box.patch` | Vertical tab close button box as in Zen: 24×24 with radius 8 instead of the circle (ink drop and focus ring), 10% veil on hover and 20% when pressed. Only where Zen's "X" is enabled (`SetSoraAnimatedCross`). |

### UI strings

The name "Chromium" is spelled out in each message of `chromium_strings.grd`
(and `settings_chromium_strings.grdp`, `components_chromium_strings.grd`) and in the `.xtb` translations;
grit has no variable for it and `BRANDING` only applies to the executable's resources. A patch
for that would be thousands of lines long, so the replacement is a script: `sora/tools/rebrand_strings.py`, which
`build.py` runs right after the patches (step marked "Sora:"; together with copying the icons, the
only changes to the upstream file). It replaces "Chromium" with "Sora" only in message text (not in attributes, `<ph>`,
"Chromium Authors", "Chromium OS"/"ChromiumOS", `Chromium.exe`, lowercase) and remaps the ids
of the translations, which are the fingerprint of the English text, using the tree's grit. It is
idempotent. To test on a partial tree: minitree with the `.grd`/`.grdp` files, a few `.xtb` files and
`tools/grit`, then `python3 sora/tools/rebrand_strings.py <tree>`.

### Icon

Dawn: a rounded square (224/256, radius 52) with a blue sky `#2F6FE4`→`#8EC4FF`,
a rising white sun and a `#FFA27C`→`#EE6E8C` horizon. Sources in `sora/branding/icon/` (`sora.svg`
and `sora-mono.svg`, the single-color version). `sora/tools/render_icons.py` (requires `cairosvg` and
`pillow`) generates in `sora/branding/theme/` the PNGs, the `.ico` files (16, 32, 48 and 256) and the
Start menu tiles, at the same paths as in `chrome/app/theme/`; `build.py` copies that folder over
the tree after the patches. A binary file does not fit in a text patch, hence the copy.
The HTML and PDF document icons (`chromium_doc.ico`, `chromium_pdf.ico`) are a page with the
Sora icon, built from `doc-page.svg` and `pdf-label.svg`. The incognito icon
(`incognito.ico`) is the same tile at night, from `sora-incognito.svg`: navy sky
`#0B1433`→`#2B3F86`, a white crescent moon in place of the sun, two stars and a violet horizon
`#4A3A7A`→`#2A1F4F`. Still using the Chromium icon: `app_list.ico`, the
Linux/Mac/ChromeOS ones and the `webstore_icon*` files.

No patch has been compiled yet. The first build will show the compile errors and the
color adjustments still missing.

What is left to do is in [`roadmap/README.md`](../roadmap/README.md).
