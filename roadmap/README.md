# Roadmap

O que já entrou e o que falta no Sora Browser. Cada item vira um patch em
[`patches/sora/`](../patches/sora/). Antes de escrever código novo, ver se o Chromium já tem
o recurso: estender o que existe custa bem menos que reimplementar.

## Feito
- [x] Base no ungoogled-chromium-windows (Chromium 157.0.8103.78).
- [x] Marca: nome, pasta de dados, ProgIDs e esquema `sora:` (`branding.patch`).
- [x] Abas verticais por padrão (`vertical-tabs-by-default.patch`).
- [x] Paleta do Zen: moldura, barra, abas, texto e barra de endereço (`color-mixer.patch`).
- [x] Página como cartão flutuante com margem, cantos e sombra (`floating-contents.patch`).
- [x] Medidas da lateral e das abas (`vertical-tab-metrics.patch`).
- [x] Barra única no topo da lateral, em duas linhas (`sidebar-toolbar.patch`).
- [x] Formas dos botões e da barra de endereço (`toolbar-shapes.patch`).
- [x] Fonte das abas e botão de fechar só no hover (`vertical-tab-style.patch`).
- [x] Botões da barra com ícone a 70% e hover de 7% (`color-mixer.patch`).
- [x] Barra de endereço parada: só o domínio, peso 500, ícones que o Zen esconde (`omnibox-idle.patch`).
- [x] Lateral sem a fileira nativa, "+ Nova aba" no topo e rodapé (`sidebar-rows.patch`).
- [x] Lista de resultados com o visual do Zen (`omnibox-results.patch`).
- [x] Barra de endereço flutuante ao abrir pelo teclado ou nova aba (`floating-urlbar.patch`).
- [x] Essentials: fixadas em grade com o visual do Zen (`essentials.patch`).
- [x] Botões da janela escondidos numa faixa de 8px que cresce no hover; barra dentro do painel do compacto (`window-controls.patch`).
- [x] Modo compacto com painel flutuante e faixa de 5px (`compact-mode.patch`).
- [x] Workspaces sobre o modo foco de grupos de abas: indicador, ícones e "+" no rodapé (`workspaces.patch`).
- [x] Glance: Alt+clique abre o link num cartão flutuante com fechar, abrir como aba e split (`glance.patch`).
- [x] Cor de destaque derivada do sistema como no Zen, com a cor do workspace vencendo (`frame-polish.patch`).
- [x] Sombra exata do cartão, `0 3px 8px rgba(0,0,0,.24)` (`frame-polish.patch`).
- [x] Cor própria do painel do modo compacto e contorno de 1px (`frame-polish.patch`).
- [x] Hover da linha "+ Nova aba" com o véu de 7% das abas; os botões do rodapé já usavam o
  véu de 7% da barra (`tabs-polish.patch`).
- [x] Alça de redimensionar da lateral: 5px, cor de destaque, aparece no hover ou ao arrastar,
  clique duplo volta aos 186px (`tabs-polish.patch`).
- [x] Animações de pressionar (aba a 0.98), de abrir/fechar aba (opacidade e escala 0.95) e do
  "X" de fechar (`tabs-polish.patch`).
- [x] Aba descarregada a 50% sem escala de cinza nem anel; favicon no lugar do throbber
  (`tabs-polish.patch`).
- [x] Split view com o visual do Zen sobre o split nativo: um cartão com sombra por painel, vão
  de 8px, alça invisível, sem a mini barra; na lista, uma linha única com separador e destaque
  do painel ativo (`split-view.patch`).
- [x] Workspaces, acabamento: workspace padrão sem tema (cinza = sem tema, o destaque do sistema
  aparece), emoji no começo do nome como ícone, troca deslizando a lista (0.25s), Alt+1…9 e
  Alt+0, workspace que sobrevive ao fechar a última aba (reaberto com uma aba nova), renomear
  com clique duplo no indicador (`workspaces-polish.patch`).
- [x] Glance, acabamento: botões na cor de destaque com hover 1.02, arco a partir do clique com
  mola, aba de trás em escala 0.97, botões entrando depois do arco, fechar em arco de volta,
  confirmação do Esc, Ctrl+W fechando só o Glance, "Open Link in Glance" no menu de contexto,
  tab helpers que não dependem de aba e diálogos JS (`glance-polish.patch`).

## Primeiro build
- [ ] Riscos a conferir: listados por patch nos relatórios; os principais estão em `sora/README.md`.
- [ ] Compilar no Windows, no PC pessoal, e corrigir o que quebrar.
- [ ] Conferir as cores com o Zen lado a lado, nos temas claro e escuro.

## Visual
- [ ] Rodapé da lateral: trocar Downloads pela Biblioteca (os ícones dos workspaces e o "+" já
  entraram; o botão de recolher sai do rodapé quando o modo compacto ganhar o botão da primeira linha).
- [ ] Ações da página e chip do site só no hover da lateral (fade de 150ms); cursor padrão e padding interno de 4px na barra parada.
- [ ] Barra flutuante, o que falta: chip de atalho em maiúsculas, seta de 28px do "ir para a aba",
  sombra e raio do quadro dos resultados, fundo translúcido com desfoque, ícone e pílula do modo
  de busca dentro do campo, animações, abrir ao digitar na página.
- [ ] Fixadas: botão de reset no lugar do fechar e separador fixadas/normais.
- [ ] Cantos squircle do cartão (`superellipse(2.3)`, raio 11.5): o recorte da página é o canto
  redondo do compositor, então a sombra e os cantos pintados ficam redondos até haver recorte
  por caminho.
- [ ] Destaque do Zen no que ainda usa `kColorSysPrimary`: resultado
  selecionado da barra de endereço (`--color-sys-primary` no CSS; trocar pelo
  `kColorSoraAccentButtonBackground` se o popup carregar as cores do Chrome).
- [ ] Animações de abrir/fechar aba, o que falta: hoje vão junto com a animação de layout do
  Chromium (200ms, a linha cresce ou encolhe), terminando nos 0.12s/0.1s do Zen; curva easeOut.
- [ ] Botão de fechar: caixa 24×24 com raio 8, fundo de 10% no hover e 20% pressionado,
  `scale(0.97)` ao pressionar.

## Recursos do Zen
Os recursos próprios do Zen entram no Sora também, não só o visual. O que no Zen é só o
padrão do Firefox fica com o padrão do Chromium.

- [ ] Modo compacto, o que falta: mola com overshoot, revelar ao sair da janela perto da borda,
  atalho Ctrl+Alt+C e texto do botão traduzido.
- [ ] Essentials, o que falta: limite de 12, padding de 6/2px da grade, transição de 0.3s, ponto de não lido, favicon no lugar do indicador de áudio.
- [ ] Workspaces, o que falta: cross-fade do tema na troca (precisa de uma foto da moldura ou de
  interpolar as cores do `ColorProvider`), a lista que sai junto com a que entra na animação de
  troca, escolher o ícone num seletor (hoje o emoji é digitado no nome, Win+.), menu do "+"
  (pasta, split vazio, nova aba), reordenar arrastando, Ctrl + roda do mouse, lista de workspaces
  no menu de contexto, workspaces iguais em todas as janelas, o mesmo grupo (e não um novo) ao
  reabrir o workspace da última aba fechada, e textos traduzidos ("Space", "New space").
- [ ] Split view, o que falta: contorno de 2px na cor do Zen só no painel ativo (hoje é o
  contorno de 1px do Chromium, com cor também no inativo: `kColorMultiContentsView*ContentOutline`
  no `sora_color_mixer.cc` e `kThickness`/`kCornerRadius` em `contents_container_outline.h`),
  cabeçalho no hover com reorganizar e tirar do split, até 4 abas e layout em grade (o
  `SplitTabCollection` do Chromium tem 2), vão de 9px entre linhas no empilhado, prévia do
  arrastar no estilo do Zen (metade da área, sem atraso), atalhos Ctrl+Alt+V/H/U e
  Ctrl+Shift+* (`accelerator_table.cc`), "Dividir link em nova aba" no menu de contexto de
  links, linha empilhada com contorno na lateral recolhida.
- [ ] Pastas de abas fixadas. Não cabem sem um modelo novo: as fixadas do Sora são as
  essentials (globais) e os workspaces são grupos, e o Chromium não aninha coleções
  (`PinnedTabCollection` e `TabGroupTabCollection` só aceitam `SPLIT`). Caminho: (1) fixadas por
  workspace, uma seção no topo do grupo do workspace; (2) um tipo `FOLDER` em
  `TabCollection::Type` (`components/tabs`), aceito dentro de `GROUP` e dentro de si mesmo
  (5 níveis), com nome, recolhida e id, e as APIs no `TabStripModel` para criar, mover e
  desagrupar; (3) os `switch` sobre o tipo (`TabModel::UpdateProperties()`, que já sobe pelos
  ancestrais e então continua achando o grupo do workspace, `TabCollectionNode`,
  `tab_strip_api`, observers); (4) uma `FolderView` na lateral (linha
  com o ícone, recuo de 14px, recolher mostrando as ativas); (5) salvar na sessão
  (`chrome/browser/sessions`, que não conhece pastas). Spec na seção 13 de
  `zen-spec.md`.
- [ ] Glance, o que falta: Alt+clique em favoritos; arco a partir do retângulo do link (hoje um
  quadrado de 24px no ponto do clique) e a captura do link voando junto; senhas e busca (Ctrl+F)
  dentro do Glance, que hoje vêm das `TabFeatures` e só existem em aba (o Ctrl+F busca na aba de
  trás); `beforeunload` ao fechar; textos "Confirm" e "Open Link in Glance" traduzidos (grd);
  "abrir como aba" com a animação de 80%→100% do Zen.

## Marca
- [ ] Logo e ícones (`chrome/app/theme/chromium/`).
- [x] Textos da interface: "Chromium" → "Sora" nas mensagens e traduções
  (`sora/tools/rebrand_strings.py`, rodado pelo `build.py`).
- [ ] GUIDs e CLSIDs de COM próprios (`chromium_install_modes.h` e os arquivos IDL).

## Mapa: módulo do Zen → onde fica no Chromium

Antes de escrever código novo, ver se o Chromium já tem o recurso atrás de uma flag.
Vários recursos do Zen já existem lá, e estender o que existe custa bem menos que
reimplementar. Tudo o que está marcado "verificar" precisa ser conferido na tag escolhida.

| Zen (`src/zen/…`) | O que faz | Chromium | Abordagem |
|---|---|---|---|
| `tokens/` (488 tokens, 185 externos) | cores, raios, espaçamentos, sombras | `ui/color/`, `chrome/browser/ui/color/chrome_color_mixer.cc`, `ChromeLayoutProvider` | **começado**: `sora_color_mixer.cc` com as superfícies principais |
| `common/styles/zen-theme.css`, `common/zenThemeModifier.js` | gradiente do workspace, cor de destaque | `ThemeService`, `ui/color` mixers dinâmicos | estender o mixer de cor do usuário |
| `tabs/` | abas verticais na barra lateral | `chrome/browser/ui/views/tabs/vertical/`, pref `vertical_tabs.enabled` | **feito**: ligadas por padrão |
| `common/styles/zen-sidebar.css`, `zen-browser-ui.css` | barra lateral, conteúdo com borda arredondada e margem | `BrowserView`, `ContentsWebView`, `side_panel/` | patch no layout do `BrowserView` |
| `compact-mode/` | esconde a barra lateral e a de ferramentas, que aparecem no hover | `BrowserView`, lógica parecida com o immersive mode | novo |
| `spaces/`, `space-routing/` | workspaces com aba, cor e ícone próprios | tab groups e saved tab groups (verificar) | novo, apoiado em tab groups |
| `folders/`, `live-folders/` | pastas de abas fixadas | nenhum: coleções não aninham, grupos já são os workspaces | novo tipo de coleção (ver Recursos do Zen) |
| `split-view/` | duas ou mais abas lado a lado | split tabs (`MultiContentsView`, `SplitTabCollection`, 2 abas) | **começado**: visual do Zen sobre o nativo |
| `glance/` | prévia do link numa janela flutuante | link preview (verificar) | estender ou novo |
| `urlbar/` | omnibox flutuante no centro | `chrome/browser/ui/views/omnibox/` | patch |
| `media/` | controle de mídia na barra lateral | Global Media Controls | reaproveitar |
| `downloads/`, `little-window/`, `share/` | animação de download, janela pequena, compartilhar | vários | depois do núcleo |
| `boosts/`, `mods/`, `library/`, `welcome/` | CSS por site, temas da comunidade, biblioteca, onboarding | — | fora do primeiro marco |
