# Manga Downloader

Este é um script em Python para baixar imagens de mangás do site [Manga Katana](https://mangakatana.com/) e convertê-las em arquivos PDF.

## Descrição

Este projeto foi desenvolvido exclusivamente para baixar mangás do site Manga Katana. Ele baixa as imagens de cada capítulo do mangá e as mescla em um único arquivo PDF.

## Requisitos

- Python 3.x
- [ChromeDriver](https://chromedriver.chromium.org/) (certifique-se de que o ChromeDriver está no seu PATH)

## Configuração

Antes de executar o script, você precisa configurar o arquivo `config.py` com as seguintes informações:

- `MANGA_URL`: URL do manga no site Manga Katana.
- `MANGA_NAME`: Nome do manga.
- `CHAPTER_NUMBER`: Número do capítulo inicial.
- `QUANTIDADE_CAPITULOS`: Quantidade de capítulos a serem baixados.

## Instalação das Dependências

Instale as dependências do projeto executando o seguinte comando:

bash:
pip install -r requirements.txt

##Uso

Após configurar o arquivo config.py, execute o script app.py com o seguinte comando:

bash:
python app.py

O script baixará as imagens do mangá de acordo com as configurações fornecidas em config.py, mesclá-las em arquivos PDF e salvá-los no diretório de saída especificado.

##Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para enviar pull requests ou abrir issues relatando problemas ou sugestões.

##Licença
Este projeto está licenciado sob a Licença Creative Commons Atribuição-NãoComercial-SemDerivações 4.0 Internacional. Veja o arquivo LICENSE.md para mais detalhes.
