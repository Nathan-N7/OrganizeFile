# OrganizeFile - Bot Organizador de Arquivos

## O que é?

OrganizeFile é um bot simples em Python que organiza automaticamente os arquivos de uma pasta, separando-os em pastas específicas como `text`, `image` e `document` com base no tipo do arquivo.

---

## Como funciona?

- O bot verifica todos os arquivos da pasta onde ele é executado.
- Ele identifica o tipo dos arquivos usando a extensão e o tipo MIME.
- Arquivos de texto e arquivos sem extensão são movidos para a pasta `text`.
- Imagens (`.png`, `.jpg`, `.jpeg`, `.webp`, `.gif`) são movidas para a pasta `image`.
- Documentos (`.pdf`, `.doc`, `.docx`) são movidos para a pasta `document`.
- Outros arquivos não identificados são ignorados (ou você pode personalizar).

---

## Como usar?

1. Coloque o script `bot.py` na pasta que deseja organizar.
2. Execute o script com Python:

   ```bash
   python bot.py
