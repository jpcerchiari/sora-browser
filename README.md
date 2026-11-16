<div align="center">
    <img src="sora/branding/icon/sora.svg" width="128" alt="Ícone do Sora Browser">
    <h1>Sora Browser</h1>
    <p>
        Um navegador calmo, com a cara do Zen e o motor do Chromium.
    </p>
</div>

## Downloads
> [!NOTE]
> O Sora está em pré-alfa e ainda não tem nenhuma versão compilada.
> Por enquanto, a única forma de usar é compilar a partir do código.

Quando houver versões, elas vão ficar na página de
[releases](../../releases) deste repositório. A primeira plataforma é o **Windows**.

## O que é o Sora
O Sora é o [ungoogled-chromium](https://github.com/ungoogled-software/ungoogled-chromium)
(o Chromium sem os serviços do Google) com a interface redesenhada a partir do
[Zen Browser](https://github.com/zen-browser/desktop):

- abas verticais na lateral, ligadas por padrão;
- moldura, barra de ferramentas e abas numa só superfície, com as cores do Zen;
- página flutuando com margem e cantos arredondados *(em andamento)*;
- modo compacto, workspaces, glance e split view *(planejados)*.

O Zen é um fork do Firefox e a interface dele é CSS, JS e XUL, que não rodam no Chromium.
Por isso o visual do Zen foi reescrito em C++/Views, e o Zen entra só como referência
de design.

## Roadmap
O que já foi feito e o que falta está em [roadmap/README.md](roadmap/README.md).

## Desenvolvimento
O repositório não guarda o código do Chromium, só os patches aplicados sobre ele:

- [`patches/sora/`](patches/sora/): os patches do Sora, aplicados depois dos do
  ungoogled-chromium e dos do Windows (ver [`patches/series`](patches/series));
- [`sora/`](sora/): as decisões do projeto, o guia de patches e as ferramentas;
- [`ungoogled-chromium/`](ungoogled-chromium/): o ungoogled-chromium, como submódulo.

[> Como compilar no Windows](docs/building.md)

[> Como escrever um patch sem baixar o Chromium](sora/README.md#como-escrever-um-patch-sem-a-árvore-do-chromium)

## Créditos

### O projeto Chromium
O [Chromium](https://www.chromium.org/) está no centro do Sora e é o que torna o
projeto possível.

### ungoogled-chromium
O Sora parte do [ungoogled-chromium](https://github.com/ungoogled-software/ungoogled-chromium)
e do [ungoogled-chromium-windows](https://github.com/ungoogled-software/ungoogled-chromium-windows),
de quem herda o histórico, os patches e as ferramentas de build.

### Zen Browser
O design, as cores e os recursos de interface vêm do
[Zen Browser](https://github.com/zen-browser/desktop). Nenhum código do Zen está aqui.
Se algum arquivo dele for copiado, ele mantém a licença MPL-2.0 e o cabeçalho original.

### Helium
A organização do projeto e este README se inspiram no
[Helium](https://github.com/imputnet/helium), outro navegador construído sobre o
ungoogled-chromium.

## Licença
O código e os patches do Sora seguem a licença BSD de 3 cláusulas do
ungoogled-chromium-windows, em [LICENSE](LICENSE). O conteúdo importado de outros
projetos mantém a licença original.
