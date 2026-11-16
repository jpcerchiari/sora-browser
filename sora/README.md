# Desenvolvimento do Sora Browser

Navegador pessoal: o [ungoogled-chromium](https://github.com/ungoogled-software/ungoogled-chromium)
com a aparência e os recursos do [Zen Browser](https://github.com/zen-browser/desktop)
reescritos em C++/Views.

Este repositório é um fork do
[ungoogled-chromium-windows](https://github.com/ungoogled-software/ungoogled-chromium-windows)
(remote `upstream`). O que é do Sora fica separado, para que as atualizações do upstream
entrem com o mínimo de conflito:

- `sora/`: esta documentação e as ferramentas;
- `patches/sora/`: os patches do Sora, listados no fim de `patches/series`;
- `.gitattributes`: mantém os patches com LF.

O Zen é um fork do Firefox e a interface dele é CSS, JS e XUL. Nada disso roda na
interface do Chromium. Por isso ele entra aqui como **referência de design e de
comportamento**, não como código. Referência: [zen-browser/desktop](https://github.com/zen-browser/desktop), commit `535ccb0`.

## Decisões

- Base: **ungoogled-chromium** (2026-11-16), na versão do submódule
  (`ungoogled-chromium/chromium_version.txt`, hoje 157.0.8103.78). Substitui a decisão
  anterior de usar o Chromium puro.
- Primeiro build: **Windows**.
- Nome: **Sora Browser**. "Sora" é "céu" em japonês, na linha do Zen.

## Como compilar

Igual ao ungoogled-chromium-windows: seguir [`docs/building.md`](../docs/building.md) (Visual Studio, Python,
`python build.py`). O `build.py` baixa o Chromium, poda os binários, aplica
`ungoogled-chromium/patches/series` e depois `patches/series` (onde estão os do Sora),
roda `sora/tools/rebrand_strings.py` (ver abaixo), faz a substituição de domínios e compila. Precisa de ~100 GB livres.

## Como escrever um patch sem a árvore do Chromium

`sora/tools/minitree.py` baixa só os arquivos pedidos, na versão do ungoogled, e aplica neles
os patches anteriores da série, na ordem do build:

```bash
python3 sora/tools/minitree.py /tmp/mt chrome/browser/ui/color/chrome_color_mixers.cc
# editar em /tmp/mt
git -C /tmp/mt add -N .   # se criou arquivos novos
git -C /tmp/mt diff > patches/sora/<nome>.patch
```

Depois, acrescentar `sora/<nome>.patch` ao fim de `patches/series`. Para refazer um patch que
já está na série, usar `--upto sora/<nome>.patch`. Conferir com `patch -p1 --ignore-whitespace
--forward`, que é o que o `build.py` usa.

Ao atualizar o upstream (`git fetch upstream && git merge upstream/master`), rodar o minitree
com todos os arquivos tocados pelo Sora para ver se os patches ainda aplicam.

## Patches

Todos aplicam sobre a 157.0.8103.78 (conferir com `python3 sora/tools/check_patches.py`).
A especificação visual do Zen que eles seguem está em [`zen-spec.md`](zen-spec.md).

| patch | o que faz |
|---|---|
| `sora/branding.patch` | Nome do produto e pasta de dados (`%LOCALAPPDATA%\Sora\User Data`), ProgIDs `SoraHTM`/`SoraPDF` e esquema `sora:`. Os GUIDs e CLSIDs de COM continuam os do Chromium. |
| `sora/vertical-tabs-by-default.patch` | Abas verticais ligadas por padrão (pref `vertical_tabs.enabled`). |
| `sora/color-mixer.patch` | `sora_color_mixer.cc`: paleta do Zen sem Mica. Moldura, barra e lateral em `#e9e9e9`/`#131313`; texto com 12% de destaque a 90%; hover de aba 7%; aba ativa com véu branco de 80%/18% e 2%/5% de destaque; barra de endereço com o texto a 8%/15%; botões da barra com ícone a 70%, hover 7% e pressionado 10%. Tema instalado, alto contraste e cores forçadas continuam valendo. |
| `sora/floating-contents.patch` | Página como cartão flutuante: margem de 8px (0 do lado das abas), cantos de 5px, sombra sempre visível, sem separadores, sem os cantos côncavos e sem o contorno da faixa. Reaproveita o `shadow_box` do painel lateral. |
| `sora/vertical-tab-metrics.patch` | Lateral com 186px (mín. 152, máx. 500, recolhida 60), abas de 36px com raio 6 e 4px entre elas, padding de 7px nos lados e 5px em cima e embaixo. |
| `sora/sidebar-toolbar.patch` | Barra única do Zen: com a lateral expandida, a barra fica no topo dela, em duas linhas (☰ e botões à esquerda, voltar/avançar/recarregar à direita; barra de endereço embaixo). A página sobe até o topo, deixando só a faixa dos botões da janela. |
| `sora/toolbar-shapes.patch` | Botões da barra com 28px e raio 4; barra de endereço e lista de resultados com raio 6. |
| `sora/vertical-tab-style.patch` | Título da aba com 14px e botão de fechar só no hover ou no foco. |
| `sora/omnibox-idle.patch` | Barra de endereço do Zen: sem foco mostra só o domínio (`ShouldTrimDisplayUrlAfterHostName`), com foco mostra a URL completa já no clique; texto em peso 500; estrela, modo leitura, zoom e cookies de terceiros escondidos (as ações e os atalhos continuam funcionando). |
| `sora/sidebar-rows.patch` | Lateral expandida sem a fileira nativa de botões (busca de abas, recolher) e sem o separador; linha "+ Nova aba" no topo da lista, no formato de aba, com texto a 70% e `scale(0.985)` ao pressionar; rodapé com Downloads à esquerda e o botão de recolher à direita. Recolhida, tudo volta ao padrão do Chromium. |
| `sora/glance.patch` | Glance: Alt+clique num link http(s) abre a página num cartão flutuante sobre a aba (80% da largura, raio 5, sombra do Zen, fundo da aba escurecido), com os botões fechar, abrir como aba (Ctrl+O) e split. Fecha com Esc, clique fora ou o X. Substitui o Alt+clique de download. Spec na seção 10 de `zen-spec.md`. |
| `sora/compact-mode.patch` | Modo compacto do Zen: botão logo depois do ☰ (pref `sora.compact_mode.enabled`, desligado por padrão). A lateral vira um painel flutuante que entra por uma faixa de 5px na borda esquerda (250ms para entrar, 150ms para sair, 150ms de tolerância no hover), com cantos de 5px e sombra; o cartão ganha 8px dos dois lados. Com o painel aberto, a barra fica no topo dele, nas duas linhas; Ctrl+L revela o painel (`window-controls.patch`). |
| `sora/essentials.patch` | As fixadas viram os Essentials do Zen: grade com o `auto-fit` do Zen (vão de 4px, colunas pelas regras de 2/4/5/6/9 blocos), blocos de 46px só com o favicon, sem contorno, fundo do elemento da barra; o bloco ativo pinta o favicon desfocado (sigma 20) atrás de um cartão branco 85% / `rgba(68,64,64,.85)`. Três cores novas em `sora_color_mixer.cc`. |
| `sora/floating-urlbar.patch` | Barra de endereço flutuante do Zen: aberta pelo teclado (Ctrl+L, Alt+D, F6) ou numa nova aba, o campo vai para uma camada sobre a página, centralizado (62px de altura, largura do Zen, raio 6.5, contorno de 0.5px e a sombra grande), com os resultados colados embaixo; o lugar na lateral fica como marcador com a cor de hover. Clique do mouse abre no lugar. Esc fecha e devolve o foco à página. |
| `sora/omnibox-results.patch` | Lista de resultados do popup WebUI clássico com o visual do Zen: até 244px sem barra de rolagem, padding de 12px, linhas de 45px com raio 6, texto 14px peso 500 a 70%, URL `#4a4a4a`/`#aaaaaa`, hover de 5%, selecionada na cor de destaque a 60% com texto branco e favicon num chip branco, chip do buscador de 12px/600. Regras novas só valem dentro de `omnibox-popup-app`, então a busca da NTP não muda. |
| `sora/workspaces.patch` | Workspaces do Zen sobre o modo foco de grupos de abas (`TabGroupsFocusing`, ligado por padrão, sem congelar as abas dos outros): workspace = grupo de abas, ativo = grupo em foco. Só as abas do ativo e as fixadas (essentials) aparecem; abas novas e abas sem grupo entram no ativo; selecionar uma aba de outro workspace troca para ele; nome, cor e o ativo voltam com a restauração da sessão (o ativo é o grupo da aba ativa). Indicador de 44px acima de "+ Nova aba" (ponto na cor do grupo, nome 13px/600, fundo de hover) e, no rodapé, um ponto por workspace (30×30, raio 6, cinza a 70% quando inativo) e o "+". Clique no indicador ou clique direito num ícone abre o editor de grupo do Chromium (nome, cor, apagar). Ctrl+Alt+→/← e Alt+Shift+X/Z trocam. Spec na seção 11 de `zen-spec.md`. |
| `sora/window-controls.patch` | Botões da janela do Zen: com a barra na lateral, uma faixa de 8px acima do cartão (arrastável) com os botões invisíveis; no hover ela cresce para 34px (200ms de atraso, 150ms ease-in-out), os botões aparecem e a borda de cima do cartão desce sem mover a página. No modo compacto, a barra vai no topo do painel flutuante, acima da página. |
| `sora/frame-polish.patch` | Acabamento da moldura. Cor de destaque do Zen: o destaque do Windows misturado com a base (50% no claro, 80% no escuro, e no escuro só 40% dele sobre o preto) dá a cor dominante, que tinge o texto em 12%; no claro, saturação +0.3 e luminosidade puxada 60% para 0.42 dão a primária (`kColorSoraAccent`), que tinge a aba ativa; `kColorSoraAccentButtonBackground` é a primária em oklch com a luminosidade presa em .35–.6 / .55–.7. A cor do workspace ativo (ou a escolhida em Personalizar o Chrome) vence o destaque do sistema e entra sem a mistura, como um tema de workspace do Zen; janela anônima usa a primária `rgb(11,10,11)` do Zen. Sombra do cartão exata, `0 3px 8px rgba(0,0,0,.24)`, com uma fonte de sombra própria no `ShadowFrameView`. Painel do modo compacto com fundo `rgb(240,240,244)`/`rgb(23,23,26)` e contorno de 1px branco a 15% por dentro, que continua na barra do topo do painel. |
| `sora/tabs-polish.patch` | Acabamento das abas verticais. Linha "+ Nova aba" sem ink drop, com o fundo de hover das abas (véu de 7%). Alça de redimensionar do Zen no `ResizeArea` da lateral: barra de 5px com raio 4, de 8px do topo a 8px da base, em `kColorSoraAccentButtonBackground`, invisível em repouso e a 0.8 no hover, no foco ou ao arrastar (200ms de atraso para aparecer, 200ms ease-in-out); clique duplo volta aos 186px. Aba pressionada em `scale(0.98)` por 100ms, numa camada que o `TabCollectionAnimatingLayoutManager` não destrói enquanto dura (`kSoraKeepLayerKey`). Abrir e fechar aba com opacidade e escala 0.95, dentro da animação de layout de 200ms do Chromium e terminando em 120ms/100ms. "X" de fechar desenhado com duas barras de 1.5px que vão de 0°/12px a 45°/15px em 120ms a cada vez que o botão aparece. Favicon sem throbber (o título "Carregando..." continua) e aba descarregada com favicon e título a 50%, sem o anel nem o favicon encolhido. Só nas abas verticais. |
| `sora/split-view.patch` | Split view do Zen sobre o split nativo do Chromium (2 abas). Com a página como cartão (abas verticais, fora da tela cheia), cada painel vira um cartão próprio com o raio de 5px e a sombra do Zen (pintada pelo `MultiContentsBackgroundView`, então aparece também no vão), os painéis ocupam o lugar do cartão único e ficam a 8px um do outro; o contorno do painel (o do Chromium, 1px) encosta no cartão por fora. A alça de redimensionar é o vão, invisível (a pegada só aparece com foco do teclado), e a mini barra do Chromium some. Na lista de abas, o split vira uma linha única no formato de aba: fundo da aba selecionada quando ativo, separador de 1px × 16px quando não, e a aba do painel ativo com um destaque de 28px (texto a 4.8%/9%). Spec na seção 12 de `zen-spec.md`. |
| `sora/workspaces-polish.patch` | Acabamento dos workspaces. Sem tema: grupo cinza é workspace sem tema, e o `BrowserWidget` ignora a cor do modo foco para ele, então aparece o destaque do sistema (ou a cor de Personalizar o Chrome); o workspace padrão nasce cinza, e escolher cinza no editor tira o tema. A cor do workspace ativo acompanha o editor na hora (o Chromium só a atualiza ao trocar de grupo). Ícone: um emoji no começo do nome, seguido de espaço ("🚀 Trabalho"), fica no título do grupo e por isso volta com a sessão; aparece no indicador e no rodapé no lugar do ponto (14px; inativo em cinza a 70%). Troca: a lista de abas entra deslizando do lado do workspace novo (largura inteira, 250ms, ease-out forte no lugar da mola sem bounce), recortada à lateral; sem o cross-fade do tema. Alt+1…9 e Alt+0 vão para o 1º…10º workspace (só a fileira de cima; só no Windows), selecionando a última aba usada nele. Fechar a última aba do workspace ativo reabre o workspace no mesmo lugar, com nome e cor, numa aba nova (o Chromium apaga o grupo com a última aba; apagar pelo editor ou fechar a janela continua apagando). Indicador como no Zen: clique duplo no nome renomeia ali mesmo (Enter ou sair salva, Esc cancela, nome vazio é ignorado), clique duplo no ícone abre o editor; clique direito, Enter e Espaço abrem o editor; clique simples não faz nada. |
| `sora/glance-polish.patch` | Acabamento do Glance. Botões na cor de destaque do Zen (`kColorSoraAccent`: fundo `#1c1c1c`/`#e2e2e2` com 4% dela, ícone nela), hover `#292929`/`#cccccc` com escala 1.02 e pressionado 0.98 (50ms). Abrir: o cartão voa em arco do ponto do clique (o navegador não conhece o retângulo do link; quadrado de 24px) até o lugar, numa mola com bounce 0.2 que para em 350ms, sem relayout da página (`SetNativeViewSize`); a página entra em 87.5ms; a aba de trás encolhe para 0.97 (transform na janela aura da página) enquanto o véu de 70% aparece; os botões entram com opacidade e 20px em 200ms depois de 150ms. Fechar: arco de volta, página some em 0.15s, botões em 120ms, aba de trás volta em 233ms. Esc com um elemento da página focado deixa o X vermelho `rgb(220,53,69)` com "Confirm" por 3s; o segundo Esc fecha. Ctrl+W e Ctrl+F4 fecham só o Glance (`PreHandleKeyboardEvent` do Glance). Item "Open Link in Glance" no menu de contexto de links http(s). A página do Glance ganha os tab helpers que ainda não estão nas `TabFeatures` (autofill, zoom, infobars, id de sessão; `friend` em `tab_helpers.h`) e `alert`/`confirm`/`prompt` como diálogos da janela, como no DevTools. Textos "Confirm" e "Open Link in Glance" ainda sem tradução. |

### Textos da interface

O nome "Chromium" está escrito por extenso em cada mensagem de `chromium_strings.grd`
(e `settings_chromium_strings.grdp`, `components_chromium_strings.grd`) e nas traduções `.xtb`;
o grit não tem variável para ele e o `BRANDING` só vale para os recursos do executável. Um patch
disso teria milhares de linhas, então a troca é um script: `sora/tools/rebrand_strings.py`, que o
`build.py` roda logo depois dos patches (passo marcado "Sora:", a única mudança no arquivo do
upstream). Ele troca "Chromium" por "Sora" só no texto das mensagens (não em atributos, `<ph>`,
"Chromium Authors", "Chromium OS"/"ChromiumOS", `Chromium.exe`, minúsculas) e remapeia os ids
das traduções, que são a impressão digital do texto em inglês, usando o grit da árvore. É
idempotente. Para testar numa árvore parcial: minitree com os `.grd`/`.grdp`, alguns `.xtb` e
`tools/grit`, e `python3 sora/tools/rebrand_strings.py <árvore>`.

Nenhum patch foi compilado ainda. O primeiro build vai mostrar os erros de compilação e os
ajustes de cor que faltam.

O que falta fazer está em [`roadmap/README.md`](../roadmap/README.md).
