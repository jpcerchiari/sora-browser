# Especificação visual do Zen (padrão, Windows)

Extraída do código do Zen 1.24.3b (Firefox 160), [zen-browser/desktop](https://github.com/zen-browser/desktop) no commit
`535ccb0`. Caminhos relativos a esse repo. **[FF]** = valor herdado do Firefox, lido do `main`
do Firefox (pode diferir um pouco do FF160). Build release (`@IS_TWILIGHT@` = false).

Regra do Sora: o que é Zen entra 1:1; o que é só o padrão do Firefox fica com o padrão do
Chromium (ver a última seção).

## 0. Valores globais

- **Squircle:** todo canto é `superellipse(2.3)` no Windows (`zen-theme.css:218-222,354-362`).
  Um raio R squircle equivale a ~R/2.3 redondo. Pílulas e círculos ficam redondos.
  No Views: path superelipse no Skia ou raio redondo R/2.3.
- **Fonte:** `Segoe UI Variable`, `Segoe UI`; abas com 14px (`vertical-tabs.css:316-318`).
- **Separação:** `--zen-element-separation` = 8px (`prefs/zen/theme.yaml:8`).
- **Raio:** `--zen-border-radius` = 9px no Windows (`zenThemeModifier.js:136-141`).
  Raio interno `--zen-native-inner-radius` = (9 − 4) × 2.3 = 11.5px squircle.
- **Esquema:** segue o sistema (claro/escuro).
- **Fundo da janela:** Mica/acrílico (`DWMSBT_TRANSIENTWINDOW`) sem a tinta do Firefox.
- **Borda superior no modo janela:** 0.5px `ActiveBorder` / `InactiveBorder`.
- **Altura mínima da janela:** 495px.

## 1. Layout da janela

Padrões: barra única (`zen.view.use-single-toolbar=true`), abas verticais à esquerda, barra
lateral expandida, modo compacto desligado, botões da janela escondidos até o hover.

- **Barra lateral, altura total:**
  - Linha de botões do topo, 36px: ☰ menu, botão do modo compacto, espaço flexível,
    voltar / avançar / recarregar. Botões de extensão vão para dentro da barra de endereço;
    o botão de extensões fica escondido.
  - Linha da barra de endereço, 37px, só com a barra de endereço.
  - Grade de essentials, indicador do workspace, "+ Nova aba", fixadas, separador, abas.
  - Rodapé: Biblioteca, ícones dos workspaces, botão "+".
- **Cartão da página:** margem de 8px à direita e embaixo, 0 à esquerda (o padding de 5px da
  lateral faz o vão), faixa de 8px em cima.
- **Botões da janela (Windows):** na faixa de 8px acima da página, canto superior direito.
  Em repouso: altura 8px, opacidade 0. No hover crescem para 34px, `0.15s ease-in-out` com
  0.2s de atraso. A página não se move: só a borda de cima do cartão desce 26px.
  O visual dos botões é o padrão do sistema.
- **Largura da lateral:** padrão 186px, mínimo 152px, máximo 500px. Clique duplo na alça
  volta ao padrão.
- **Padding da lateral:** 5px nos lados e embaixo, 0 em cima.
- **Alça de redimensionar:** 5px de largura, na borda direita, de 8px a 100% − 16px de altura,
  raio 4px, cor `--zen-accent-button-background`. Opacidade 0, 0.8 no hover ou ao arrastar
  (0.2s com 0.2s de atraso).
- **Lateral recolhida** (não é o padrão): 60px.

## 2. Cartão da página

- Vãos: direita 8px, embaixo 8px, esquerda 0 (+5px da lateral), em cima 8px.
- Raio: **5px redondo** (11.5 / 2.3, `zen-browser-container.css:11-15`).
- Sombra: `rgba(0,0,0,0.24) 0 3px 8px`. Conteúdo recortado. Sem borda nem contorno.
- Fundo atrás da página: `#ffffff` / `#202020`.
- Vão entre páginas do split view: 8px.
- Tela cheia com modo compacto: separação 0.1px, sem raio nem sombra.

## 3. Barra lateral e abas

### Abas

| item | valor |
|---|---|
| altura | 36px [FF], margem vertical 2px → passo de 40px |
| margem horizontal | 2px |
| raio | 14px squircle ≈ 6px redondo |
| padding horizontal | 8px |
| favicon | 16px, raio 4px; sem favicon: `blank.svg` sobre `--zen-toolbar-element-bg` |
| margens do favicon | 3.33px antes, 10px depois |
| texto | 14px, line-height 1.7, cor do texto da barra (a selecionada usa a mesma) |
| hover | `#101010` a 7% (claro), `#e2e2e2` a 7% (escuro) |
| selecionada, claro | `rgba(255,255,255,.8)` 98% + destaque 2% |
| selecionada, escuro | `rgba(255,255,255,.18)` 95% + destaque 5% |
| sombra da selecionada | `0 0.8px 1.5px 0`, `rgba(0,0,0,.15)` claro / `.05` escuro |
| pressionada | `scale(0.98)`, 0.1s ease |
| aba descarregada | opacidade 0.5, sem escala de cinza |
| carregando | sem throbber: o favicon continua |

### Botão de fechar

- Só aparece no hover (e nas selecionadas em multisseleção).
- Caixa 24×24, padding 4px, raio 8px.
- "X" feito com duas barras de 15 × 1.5px, raio 1px, `currentColor`, giradas ±45°.
  Ao aparecer, vão de 0°/12px para 45°/15px em 0.12s ease.
- Hover: `currentColor` 10%; pressionado: 20%.

### Fixadas

- Como abas normais, sem botão de fechar; no lugar, um botão de "reset" (barra de 12px a 0°).
- URL mudou: botão de reset à esquerda (barra 2.5 × 16px, raio 2px, 15°,
  `rgba(66,61,61,.3)` / branco 30%) e subtítulo de 10px com opacidade 0.6.
- Separador fixadas/normais: linha de 22px de altura, traço 1px `rgba(0,0,0,.1)` /
  `rgba(255,255,255,.1)`, recuo de 4px. No hover da lateral vira um botão "limpar" de 10px,
  peso 500, opacidade 0.5 (1 no hover). Transições 0.08s / 0.06s.

### Essentials (vazio por padrão)

- Grade com ~4 colunas, vão 4px, padding lateral 5px, máximo 12. Topo 6px, base 2px.
- Bloco de 46px de altura, raio 14px squircle, só o favicon centralizado.
- Fundo `--zen-toolbar-element-bg`; hover `rgba(0,0,0,.1)` / fundo da selecionada.
- Selecionado: o favicon desfocado (20px) atrás do bloco, com `inset: -50%`, e por cima uma
  camada recuada 2px, raio 12px, `rgba(255,255,255,.85)` / `rgba(68,64,64,.85)`
  (`.8` / `.75` no hover).
- Transições da grade: 0.3s ease-out.

### Indicador do workspace

- 44px de altura. Texto 13px peso 500; o nome em peso 600.
- Padding 16px à esquerda, 12px à direita. Ícone de 16px.
- Fundo no hover: recuo de 4px em cima e 7px à esquerda, raio 14px, cor do hover das abas.
- Botão "…" de 26px, raio 10px, aparece no hover em 0.1s.

### "+ Nova aba"

- Mesma caixa da aba (36px, raio 14px), texto `currentColor` 70%.
- Pressionado: `scale(0.985)`, 0.1s.
- Abre a barra de endereço flutuante; enquanto ela está aberta, a linha fica com o fundo e a
  sombra da aba selecionada.

### Rodapé

- Linha flex, `space-between`, vão 4px, botões padrão da barra (seção 5) sem padding.
- Ícones dos workspaces: botões de 30×30, raio 6px, ícone de 12px (emoji) ou 14px (imagem).
  Sem ícone: ponto de 8px, preto/branco 40%.
- Inativos: escala de cinza, opacidade 0.7. Ativo ou hover: cor e opacidade 1; fundo
  `--zen-toolbar-element-bg` no hover. Transição 0.2s, vão 0.5ch.

### Rolagem da lista

- Polegar da barra de rolagem: `currentColor` 35%.
- Linhas de 1px em cima e embaixo (`rgba(0,0,0,.08)` / `rgba(255,255,255,.08)`) quando a lista
  não está no começo ou no fim.

## 4. Barra de endereço

### Parada, na lateral

- Linha de 37px com 1px de padding; a caixa tem ~32–35px (valor herdado do Firefox, não
  confirmado).
- Fundo: texto da barra a 8% (claro) / 15% (escuro). Raio 14px squircle, margem 1px.
  Sem borda, contorno nem sombra.
- Hover: `rgba(0,0,0,.08)` / `rgba(255,255,255,.1)`.
- Texto peso 500, **só o domínio**, cursor padrão. Padding interno 4px.
- Ícone de identidade à direita. Ações da página e identidade ficam invisíveis até o hover
  da lateral (aparecem em 0.15s).
- Escondidos: proteção contra rastreamento, modo leitura, estrela, botão ir, PiP, zoom.
- Ícones de ação: largura mínima 26px, padding 5px, raio 8px.

### Flutuante (`floating-on-type`)

- Flutua quando aberta pelo teclado ou pela nova aba, não pelo clique do mouse.
- Centralizada. Topo = metade da janela − max(333px, altura)/2.
- Largura: `min(janela/1.5, 750px)`, com mínimo `min(90%, 62rem)`.
- Altura do campo 62px, margem lateral 12px, fonte 1.15em.
- Raio 15px squircle. Fundo `rgba(255,255,255,.93)` / `rgba(20,20,20,.92)` com desfoque de 40px
  (sem desfoque: `#fff` / `rgb(24,24,24)`).
- Sombra `0 30px 140px -15px` `rgba(0,0,0,.8)` claro / `.6` escuro.
- Contorno 0.5px `rgba(0,0,0,.2)` / `#4a4a4a`.
- O lugar dela na lateral fica com um marcador de raio 14px e a cor do hover.
- O resto da janela não escurece.
- **Resultados:**
  - Altura máxima 244px, sem barra de rolagem, padding 12px, sem os botões de busca.
  - Linhas com altura mínima de 45px, padding 10px × 8px, texto preto/branco 70%.
  - Título e URL com 14px e peso 500; URL em `#4a4a4a` / `#aaaaaa`.
  - Favicon com padding 4px, raio 4px, margem direita 12px.
  - Hover: 5% do inverso do fundo da marca.
  - **Selecionada:** `--zen-accent-button-background` a 60%, texto branco, favicon sobre um
    chip branco a 90%.
  - Atalho: maiúsculas, 10px, padding 6 × 8px, raio 4px, 5% de fundo, contorno 1px 10%.
  - Nome do buscador: 12px, peso 600, padding 4 × 6px, raio 4px, 10% de fundo.
  - "Ir para a aba": seta de 28px, opacidade 0.7 (1 na selecionada).
  - Rótulo do modo de busca: pílula de 14px, padding 4 × 8px, destaque 50% + preto 50% /
    branco 20%, texto branco. Ao entrar: pulso 1 → 0.98 → 1 em 0.25s.

## 5. Botões da barra

| item | valor |
|---|---|
| ícone | 16px |
| tamanho | 28×28 (padding interno 6px), padding externo 1px |
| raio | 8px squircle |
| cor do ícone | `currentColor` 70% |
| hover | inverso do fundo da marca a 7% |
| ativo/aberto | 10% |
| pressionado | `scale(0.95)`, 0.2s; fundo 0.1s |

## 6. Modo compacto (desligado por padrão)

- Esconde só a lateral (em barra única). Atrasos: 150ms para manter no hover, 1000ms para
  esconder a barra. Detecção fora da janela: 200px na horizontal, 100px na vertical.
- Página com margem de 8px dos dois lados.
- Lateral flutuante: fixa, topo 4px (+1px no Windows em janela), altura 100% − 8px,
  esquerda −4px, padding horizontal 8px. Painel com raio 11.5px squircle e a sombra grande.
  Fundo `rgb(240,240,244)` / `rgb(23,23,26)`. Contorno 1px `rgba(255,255,255,.15)`, offset −1px.
- Escondida: sobra uma faixa de ~5px na borda esquerda. Some em 0.15s ease.
- Aparece no hover da faixa (ou saindo da janela a menos de 10px da borda) em 0.25s, com
  uma mola que passa do ponto até 1.0109 em ~72%.
- Ligar o modo compacto anima a margem com mola sem quique, duração 0.1.

## 7. Cores

| token | claro | escuro |
|---|---|---|
| fundo da marca | `#e2e2e2` | `#101010` |
| fundo principal (sem Mica) | `#e9e9e9` | `#131313` |
| fundo principal com Mica | transparente | `rgba(0,0,0,.4)` sobre o acrílico |
| fundo do app por baixo | `#e2e2e2` | `#171717` |
| barra do modo compacto | `rgb(240,240,244)` | `rgb(23,23,26)` |
| elemento da barra | texto 8% (oklch) | 15% |
| hover de elemento | `rgba(0,0,0,.08)` | `rgba(255,255,255,.10)` |
| popups | `rgb(244,244,244)` | `rgb(31,31,31)` |
| diálogos | `#fafafa` | `#1c1c1c` |
| barra de endereço | destaque 3% + `#f4f4f4` | destaque 4% + `rgb(24,24,24)` |
| borda de campo | `#cccccc` | `rgb(66,65,77)` |
| separador de painel | `currentColor` 15% | idem |
| texto da barra | `rgba(0,0,0,.8)` | `rgba(255,255,255,.8)` |

- Sem textura (grain 0).
- **Cor de destaque** (a do sistema):
  - Mistura com a base `[240,240,244]` (claro, 50%) ou `[23,23,26]` (escuro, 80%); no escuro,
    depois fica só 40% dela sobre o preto (`blendColors(rgb, [0,0,0], 40)`).
  - No claro: saturação +0.3 e luminosidade = l × 0.4 + 0.252. Cinzas puros não mudam.
- **Texto** (`--toolbox-textcolor`): destaque 12% + preto 88% (claro) ou branco 88% (escuro),
  alfa 0.9.
- **Botão de destaque** (`--zen-accent-button-background`): oklch do destaque com a luminosidade
  presa em .35–.6 (claro) ou .55–.7 (escuro). Usado na alça, no resultado selecionado e nos
  contornos de foco.
- **Ícones temáticos:** destaque 50% + preto (claro); primária 15% + `#ebebeb` (escuro).
- **Barra de carregamento:** destaque + 70% de preto 50% / branco 50%.
- **Janela anônima:** primária `rgb(11,10,11)`, texto branco 80%, sempre escuro.

## 8. Animações

| o quê | especificação |
|---|---|
| abrir aba | opacidade 0→1, escala 0.95→1, 0.12s easeOut |
| fechar aba | opacidade 1→0, escala →0.95, margem inferior →−altura, 0.1s easeOut |
| trocar workspace | mola sem quique, 0.25s; cross-fade do fundo |
| barra dos botões da janela | 0.15s ease-in-out com 0.2s de atraso |
| "+" do rodapé | gira 0→45° em 0.2s com o popup aberto |
| indicador de carregamento | pílula de 5rem × 0.4rem centrada no topo (−4px), pulsa a cada 1s; em carga longa vai a 10rem em 0.3s |
| diálogos | entram em 0.3s ease-out, saem em 0.2s ease-in |

## 9. Padrão do Firefox: no Sora fica o padrão do Chromium

- Visual dos botões da janela (só a posição é do Zen).
- Menus de contexto (o Zen só muda padding e cor).
- Menu do app, painéis, downloads, favoritos, barra de busca na página.
- Páginas `about:`, preferências, biblioteca, barra de status, barras de rolagem da página.
- Diálogos (o Zen só muda raio, borda e sombra da caixa), barras de notificação, PiP,
  DevTools, tooltips, barra de menus, barra de favoritos.

## 10. Glance

Prévia de um link numa janela flutuante por cima da página (`src/zen/glance/`). Ligado por
padrão (`zen.glance.enabled`, `prefs/zen/glance.yaml:5-6`). Caminhos desta seção relativos a
`src/zen/glance/`, salvo indicação; `GM` = `ZenGlanceManager.mjs`, `GC` =
`actors/ZenGlanceChild.sys.mjs`.

- **Gatilho:** **Alt + clique** esquerdo num link (`zen.glance.activation-method = "alt"`,
  `glance.yaml:14-15`; opções ctrl, alt, shift, meta). O ator usa "ctrl" só como valor de
  reserva se a pref sumir (`GC:20-25`).
  - Só com um modificador (a checagem é um XOR, `GC:46-48,155`), botão esquerdo, evento não
    cancelado pela página (`GC:151-158`).
  - Não abre se o mouse andou mais de 4px entre o mousedown e o click: é seleção de texto
    (`GC:29,136-148`). Não abre links `javascript:` nem URLs que a página não pode carregar
    (`GC:102-120`). O clique original é cancelado (`GC:172-174`).
  - Também abrem no Glance: Alt + clique num favorito (`GM:1925-1940`); "Abrir link no
    Glance" no menu de contexto de links (`GM:223-244`,
    `src/browser/base/content/nsContextMenu-sys-mjs.patch:10`); links de abas essenciais para
    outro domínio, só http/https/file (`zen.glance.open-essential-external-links = true`,
    `glance.yaml:11-12`; `GM:1731-1758`).
  - Com a barra de abas escondida, o link abre numa aba normal (`GM:546-553`).
- **O que é:** uma aba de verdade, filha da aba de origem, desenhada dentro da linha da
  aba-mãe na lateral (`GM:344-404`). Um Glance por vez (`GM:555-562`). Trocar de aba esconde o
  Glance; voltar à aba-mãe mostra de novo (`GM:1588-1635`).
- **Janela:** 80% da largura da área da página, 100% da altura, centralizada
  (`zen-glance.css:123-143`; `GM:808,1018-1019`). Raio igual ao do cartão, 5px redondo
  (`zen-glance.css:145-150`). Sombra `--zen-big-shadow` = `rgba(0,0,0,0.24) 0 3px 8px`
  (`zen-glance.css:147`, `zen-tokens.css:463`). Fundo da página `#ffffff` / `#101010`
  (`zen-glance.css:152-153`, `zen-tokens.css:236`). Sem barra de endereço própria.
- **Página de origem:** encolhe para escala 0.97 e fica com opacidade 0.3 (`GM:9,647-667`),
  ou seja, quase some no fundo da janela. Sem desfoque. Clicar nela fecha o Glance
  (`GM:294-301`).
- **Botões:** coluna colada à direita do Glance (`left: 100%`; à esquerda se a lateral estiver
  à direita), `top` 15px, padding 12px, vão 12px, largura máxima 56px (`zen-glance.css:7-27`;
  `zen-tokens.css:20,23,26,73`). De cima para baixo: fechar (X), abrir como aba (ícone de tela
  cheia), dividir (`zen-glance.inc.xhtml:6-10`; `src/browser/themes/shared/zen-icons/icons.css:41,291,469`).
  - Cada um: círculo de 34px (`--size-item-large`, `src/zen/common/styles/zen-buttons.css:14`),
    padding 8px, só ícone, sombra `0 0 12px 1px rgba(0,0,0,0.07)` (`zen-glance.css:29-41`,
    `zen-tokens.css:239`).
  - Fundo `#1c1c1c` (claro) / `#e2e2e2` (escuro) com 4% da cor de destaque; ícone na cor de
    destaque (`zen-glance.css:32,41`, `zen-tokens.css:233`).
  - Hover: `#292929` / `#cccccc` e escala 1.02; pressionado: escala 0.98; transição 0.05s
    (`zen-glance.css:33-50`, `zen-tokens.css:234`).
- **Fechar:** botão X, Esc, clique na página de origem, fechar a aba-mãe (`GM:1641-1645`) ou
  fechar a aba do Glance (Ctrl+W, `GM:1670-1694`). Respeita o `beforeunload` (`GM:1118-1121`).
  Se a aba-mãe for a única aba, abre uma aba nova (`GM:1174-1177`).
  - Esc com um elemento da página focado não fecha de primeira: o X fica vermelho
    `rgb(220,53,69)`, ganha o rótulo "Confirm" (máx. 4rem) por 3s, e um segundo Esc fecha
    (`GC:177-186`; `GM:1131-1149`; `zen-glance.css:68-94`; `zen-tokens.css:235,242`).
- **Abrir como aba** (botão ou Ctrl+O, `src/browser/base/content/zen-keysets.inc.xhtml:39`):
  vira uma aba normal logo depois da mãe e fica ativa (`GM:1817-1863`). Tela cheia (DOM
  fullscreen) dentro do Glance faz o mesmo (`GM:1652-1662`).
- **Dividir:** abre como aba e faz split view lado a lado com a mãe, o Glance à direita
  (`GM:1999-2020`).

| animação (`zen.glance.animation-duration` = 350ms, `glance.yaml:17-18`) | especificação |
|---|---|
| abrir | o Glance sai do retângulo do link clicado e voa em arco (altura 40% da distância, máx. 30px) até o centro, crescendo até 80% × 100%; mola com bounce 0.2 ajustada para parar em 350ms (`GM:10,36-41,732-783,800-930,951-957`). Uma captura do link acompanha o voo (`GM:695-730`); a página entra com opacidade 0→1 em 87.5ms (350/4) ease-in-out (`GM:746-759`) |
| página de origem ao abrir | escala 1→0.97 e opacidade 1→0.3, mesma mola (`GM:647-667`) |
| botões ao abrir | opacidade 0→1 e x −20px→0 em 200ms, com 150ms de atraso (`GM:448-469`) |
| fechar | arco de volta ao retângulo do link, 350ms ease-out (`GM:1275-1316`); a página some com opacidade 0.15s ease-in-out (`zen-glance.css:163-168`); botões somem em 120ms (`GM:1203-1215`); a página de origem volta a escala 1 e opacidade 1 em ~233ms (350/1.5) (`GM:1248-1266`) |
| abrir como aba | largura 80%→100% e escala 1→1.005→1, 250ms ease-in-out (`GM:1897-1918`) |

## 11. Workspaces

Os "Spaces" do Zen (`src/zen/spaces/`). Ligados por padrão. Caminhos desta seção relativos a
`src/zen/spaces/`, salvo indicação; `SM` = `ZenSpaceManager.mjs`.

- **O que é:** nome, ícone opcional (emoji ou SVG) e tema (gradiente que define a cor de
  destaque da janela), mais um container opcional (`SM:2876-2898`).
- **Padrão:** a janela começa com um workspace "Space", sem ícone, sem tema e sem container
  (`SM:867-870`). Container 0 é o de todos, então as essentials são as mesmas em todos os
  workspaces (`zen.workspaces.separate-essentials` só separa por container).
- **Abas:** toda aba normal ou fixada pertence a um workspace (`zen-workspace-id`); as
  essentials não pertencem a nenhum. Aba sem workspace (nova, restaurada, vinda de outra
  janela) entra no ativo (`SM:2601-2647`). Abas novas vão para o ativo.
- **Trocar:** só as abas normais e fixadas do workspace ativo aparecem; as essentials ficam.
  Seleciona a última aba usada naquele workspace, ou a aba vazia se não houver
  (`SM:2649-2700`). Selecionar uma aba de outro workspace (busca, atalho, link) troca para ele
  (`SM:2580-2599`). O tema muda junto, com cross-fade; a animação está na seção 8.
- **Criar:** o "+" do rodapé abre um menu (criar Space, pasta, split vazio, nova aba). Criar
  Space faz um "Space" logo depois do atual, troca para ele e mostra um formulário com nome,
  ícone e perfil (`SM:1656-1690`, `ZenSpaceCreation.mjs`).
- **Menu de contexto** (clique direito no indicador ou num ícone do rodapé, ou o "…" do
  indicador): mudar nome, mudar ícone, mudar tema, perfil, a lista de workspaces para trocar,
  gerenciar, descarregar, descarregar os outros, criar, compartilhar, apagar
  (`src/browser/base/content/zen-panels/popups.inc:13-38`). Apagar pede confirmação ("Delete
  Space?") e fecha as abas do workspace (`SM:1272-1285`, `SM:1488-1507`).
- **Indicador:** no topo da lista, depois das essentials e antes de "+ Nova aba": ícone e nome
  (medidas na seção 3). Clique duplo no nome renomeia ali mesmo; no ícone, troca o ícone
  (`ZenSpace.mjs:179-210`).
- **Rodapé:** um ícone por workspace, na ordem deles (medidas na seção 3). Clique troca;
  arrastar reordena. Ctrl + roda do mouse na lateral e o gesto de swipe também trocam
  (`SM:660-700`, `ZenSpacesSwipe.mjs`), dando a volta no fim (`zen.workspaces.wrap-around-navigation`).
- **Atalhos** (`src/browser/base/content/zen-keysets.inc.xhtml:10-28`): Alt+1…9 e Alt+0 vão para
  o 1º…10º workspace (Ctrl no macOS); Ctrl+Alt+→ e Ctrl+Alt+← vão para o próximo e o anterior.
  Criar não tem atalho.
- **Persistência:** a lista e o ativo ficam no session store da janela (`spaces`,
  `activeZenSpace`, `SM:854-878`).
- **Última aba:** fechar a última aba normal do workspace seleciona a aba vazia; o workspace
  continua (`zen.workspaces.open-new-tab-if-last-unpinned-tab-is-closed` = false).

## 12. Split view

Duas a quatro abas lado a lado na área da página (`src/zen/split-view/`). Caminhos desta seção
relativos a `src/zen/split-view/`, salvo indicação; `VS` = `ZenViewSplitter.mjs`,
`SV` = `zen-split-view.css`, `SG` = `zen-split-group.inc.css`.

- **O que é:** um grupo de abas especial (`tab-group[split-view-group]`) com 2 a 4 abas
  (`MAX_TABS = 4`, `VS:87`). Selecionar qualquer aba do grupo mostra todas; a aba selecionada é
  o painel ativo. Clicar num painel seleciona a aba dele (`VS:1865-1876`). Fechar uma aba tira
  ela do split; com 2 abas, o split se desfaz (`VS:230-245`). O split volta com a sessão
  (`VS:2418`).
- **Layouts:** `grid` (padrão, `VS:1502`), `vsep` (colunas) e `hsep` (linhas). Com 2 abas, o
  `grid` é igual ao `vsep`; com 3 ou 4 vira colunas de duas linhas (`VS:1639-1668`).
- **Cartões:** cada painel é um cartão próprio, com o raio e a sombra do cartão da página
  (5px, `rgba(0,0,0,.24) 0 3px 8px`; `src/zen/common/styles/zen-browser-container.css:11-15`).
  Entre eles, a moldura.
- **Vão:** 8px entre colunas (`--zen-split-row-gap` = `--zen-element-separation`) e 9px entre
  linhas (`--zen-split-column-gap` = separação + 1px) (`SV:92-95`). As bordas de fora dos
  cartões ficam onde estaria o cartão único (margens negativas, `SV:13-15,97-102`).
- **Painel ativo:** contorno de 2px por fora do cartão, na cor
  `hsl(from primária h s l−20)` no claro e `--button-background-color-primary` no escuro
  (`SV:72,80-83`). Painéis inativos não têm contorno. Some em tela cheia.
- **Redimensionar:** o vão inteiro é a alça, invisível; só o cursor muda (`ew-resize`/`ns-resize`,
  `SV:125-130`, `VS:1882-1952`). Mínimo de 7% por painel (`zen.splitView.min-resize-width`).
  Os painéis andam com `inset 0.09s ease-out` (`SV:74`).
- **Cabeçalho no hover:** passando o mouse num painel aparece, depois de 0.1s e com fade de 0.1s,
  uma aba colada no topo do painel, centralizada, na cor do contorno ativo, com os botões
  reorganizar (arrastar) e tirar do split (`SV:139-191`, `VS:1704-1720`).
- **Na lista de abas** (lateral expandida, `SG`): o grupo vira uma única linha no formato de aba
  (altura de aba, raio de aba, padding de 2px nos lados), com as abas dividindo a largura
  (`flex: 1`). Cada aba dentro tem 28px de altura (`SG:66-68`).
  - Sem a aba ativa: linha transparente, separador de 1px × 16px (`--size-item-small` [FF])
    entre as abas, preto a 10% / branco a 20% (`SG:73-82`; `src/zen/common/styles/zen-tokens.css:383`).
    Hover: fundo `--zen-toolbar-element-bg` (texto a 8%/15%) (`SG:128-130`).
  - Com a aba ativa: a linha toda tem o fundo da aba selecionada; a aba do painel ativo tem por
    cima `--zen-split-view-active-tab-bg` = `--zen-toolbar-element-bg` a 60% (`SG:18-22,101-116`);
    sem separador.
  - Botão de fechar só no hover, e só em abas com 70px ou mais (`SG:135-155`).
  - Lateral recolhida: as abas se empilham numa coluna com contorno de 2px
    `--zen-colors-border-contrast` (`SG:49-57,158-166`).
- **Criar:**
  - Menu de contexto da aba: "Add Split View..." (uma aba: split com uma aba vazia), "Join N
    Tabs" (várias selecionadas), "Split Out Tab" (aba que já está num split)
    (`VS:1177-1203,1278-1318`; `locales/en-US/browser/browser/zen-split-view.ftl`).
  - Menu de contexto de link: "Split Link to New Tab" (`VS:1243-1264`).
  - Arrastar uma aba para a borda da página: no quarto de fora da largura ou da altura aparece
    a prévia (metade da área, contorno de 2px na primária, sombra grande), e soltar faz o split
    (`VS:285-450`; `SV:204-232`). Ligado por padrão (`zen.splitView.enable-tab-drop`).
  - Glance: botão dividir (seção 10).
  - Atalhos (`src/browser/base/content/zen-keysets.inc.xhtml:31-35`): Ctrl+Alt+G grade,
    Ctrl+Alt+V colunas, Ctrl+Alt+H linhas (com a aba seguinte, ou as selecionadas), Ctrl+Alt+U
    desfaz, Ctrl+Shift+* split vazio (`VS:2062-2098,2567`).

**No Sora** (`split-view.patch`), sobre o split nativo do Chromium (2 abas, lado a lado ou
empilhadas): cartões por painel com a sombra do Zen, vão de 8px, bordas de fora no lugar do
cartão único, alça invisível (a pegada só aparece com foco do teclado), sem a mini barra do
Chromium e, na lista, a linha única com o separador e o destaque do painel ativo. Criar fica com
o que o Chromium já tem: menu de contexto ("Novo split view com a aba atual", duas abas
selecionadas, "Organizar" com trocar/desfazer), arrastar aba ou link para a borda da página e o
botão do Glance.

## 13. Pastas

Pastas de abas fixadas (`src/zen/folders/`). Caminhos desta seção relativos a
`src/zen/folders/`; `ZF` = `ZenFolders.mjs`, `F` = `ZenFolder.mjs`, `CSS` = `zen-folders.css`.

- **O que é:** um grupo de abas (`zen-folder`, subclasse do `tab-group` do Firefox, `F:7`) que
  só existe na seção de fixadas de um workspace; as abas dentro ficam fixadas (`ZF:743-750`).
  Não entra nas essentials. Pastas podem ter subpastas, até 5 níveis
  (`zen.folders.max-subfolders`, `ZF:737-741`). Toda pasta guarda uma aba vazia escondida
  para não sumir quando fica sem abas (`ZF:765-775`).
- **Linha da pasta:** altura de uma aba (`--tab-min-height` + 2 × margem), ícone de pasta de 28px
  a 5px da borda, nome em peso semibold com 32px de recuo, hover com o fundo de hover das abas
  num retângulo 2px menor de cada lado, raio de aba (`CSS:68-170`). Cor da pasta tirada da
  primária: fundo de trás `primária 60% + cinza`, frente `primária + branco 70%`, traço
  `primária 50% + preto` (claro; `CSS:13-18`). Sem cor de grupo nem linha de grupo (`CSS:7-9,74-75`).
- **Ícone:** pasta em SVG com uma folha de trás e uma da frente (`F:24-60`). Aberta, as folhas
  se inclinam 16° em sentidos opostos e encolhem para 0.85, em 0.3s
  `cubic-bezier(.42,0,0,1)` (`zen-folder-icon.inc.css`). Fechada com uma aba ativa dentro, o
  ícone troca o glifo por três pontos (`CSS:122-136`, `ZF:1092-1108`).
- **Conteúdo:** abas e subpastas recuadas 14px (`CSS:52-57`).
- **Recolher:** clique na linha. Recolhida, a pasta continua mostrando as abas ativas dela
  (`has-active`, `ZF:403-425`); selecionar uma aba de dentro por outro caminho a revela.
  Animação de 0.18s easeInOut para recolher e expandir, 0.2s para revelar (`ZF:1710-1716`).
  Com abas ativas, um botão na linha descarrega todas (`F:14`, `CSS:183-190`).
- **Criar:** menu de contexto da aba, "Move to Folder" › pastas existentes ou "New Folder"
  (`ZF:68-78`); menu de contexto da lateral, "New Folder" (`ZF:79`); o "+" do rodapé (seção 11).
  A pasta nova se chama "New Folder", entra antes do separador das fixadas e já abre para
  renomear (`ZF:604-645,743-808`).
- **Menu da pasta:** renomear, nova subpasta, desagrupar ("Unpack"), descarregar todas,
  converter em Space, mudar de Space, apagar
  (`locales/en-US/browser/browser/zen-folders.ftl`).
- **Busca:** com `zen.folders.search.enabled`, um popup com as abas da pasta e um campo de
  busca (`ZF:197-222,884-1090`).
- **Persistência:** session store da janela (`ZF:1255-1450`).

**No Sora:** ainda não entrou. Fixadas são as essentials (globais) e workspaces são grupos de
abas, então não há fixadas por workspace onde as pastas morariam, e o modelo do Chromium não
aninha coleções: `PinnedTabCollection` só aceita `SPLIT` e `TabGroupTabCollection` só aceita
`SPLIT` (`components/tabs/impl/*_tab_collection.cc`). O caminho está no roadmap.

## Não determinado pelo código

- Altura exata da caixa da barra de endereço parada.
- Largura efetiva da barra de endereço flutuante (o "90%" depende do contêiner).
- Qual cor de hover de aba vence, a do Zen ou a do Firefox (`currentColor` 11%).
- Valores do FF160 marcados como [FF].
