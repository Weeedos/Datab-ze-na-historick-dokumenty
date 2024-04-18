# Databáze na historické dokumenty

Databáze na historické dokumenty v jazyce Python, navržená pro efektivní správu dat týkajících se historických pramenů. Tento systém umožňuje uživatelům interakci s MySQL databází a poskytuje funkcionalitu pro vkládání, aktualizaci, mazání, importování z databáze. Jedná se o školní projekt.

Autor: Vít Vosol

Škola: SPŠE Ječná

Kontakt: vosol@spsejecna.cz

## Obsah
- [Struktura](#struktura)
- [Požadavky](#pozadavky)
- [Konfigurace](#konfigurace)
- [Použití](#pouziti)
- [Funkce](#funkce)

## Struktura
Návrhové vzory využívané aplikací:
   - Singleton
   - MVC

## Požadavky
- **Python**: Hlavní programovací jazyk použitý pro vývoj.
- **MySQL Server**: Relační databázový systém pro ukládání a správu dat.
- **Python balíčky**: Nainstalujte dodatečně vyžadované balíčky pomocí příkazu `pip install --user mysql-connector-python`.

## Konfigurace
1. **Konfigurace MySQL Databáze**
    - Vytvořte MySQL databázi pro aplikaci podle `doc/db.sql`.
    - Nastavte detaily připojení k databázi v souboru `cfg/config.ini`.

## Použití
Spusťte hlavní program pomocí následujícího příkazu:

```bash
python main.py
```

## Funkce
### 1. **Vkládání, Aktualizace, Mazání**
   - Snadná správa dat.

### 2. **Vyhledávání**
   - Podrobné vyhledávání v datech.

### 3. **Import a export**
   - Import a export dat z databáze ve formátu CSV. 
