# Polyformalismi: Ajattelu monessa kielessä

> **Suomenkielinen opas polyformalismiin, 9-kanavaiseen intentiomalliin ja monikieliseen ohjelmointiajatteluun**

---

## Sisällys

1. [Mitä polyformalismi on?](#1-mitä-polyformalismi-on)
2. [Yhdeksän kanavan intentiomalli](#2-yhdeksän-kanavan-intentiomalli)
3. [Säilymislaki γ + η = C](#3-säilymislaki-γ--η--c)
4. [Miksi useat kielet paljastavat piilotason?](#4-miksi-useat-kielet-paljastavat-piilotason)
5. [Koodiesimerkit ja käytännöt](#5-koodiesimerkit-ja-käytännöt)
6. [Harjoitus: Monikielinen analyysi](#6-harjoitus-monikielinen-analyysi)
7. [Suomen kielen ja polyformalismin suhde](#7-suomen-kielen-ja-polyformalismin-suhde)
8. [Yhteenveto](#8-yhteenveto)

---

## 1. Mitä polyformalismi on?

Polyformalismi on ajattelutapa, jossa sama matemaattinen tai looginen rakenne ilmaistaan useissa formaaleissa järjestelmissä — ohjelmointikielissä, matemaattisissa notaatioissa ja loogisissa kalkyyleissä — sen sijaan, että valittaisiin yksi "oikea" esitystapa.

Sanan alkuperä on kreikassa: *poly* (πολύ, moni) + *formalism* (formaalisuus, muoto). Polyformalismi sanoo: **muoto on moninainen, mutta rakenne on yksi.**

Tämä on radikaali väite. Perinteinen tietojenkäsittelytiede etsii "parasta kieltä" tietylle ongelmalle. Polyformalismi sanoo, että paras kieli on **useita kieliä samanaikaisesti** — koska jokainen kieli paljastaa rakenteen eri puolen ja kätkee toisen.

### Vertauskuva: Suomi ja murteet

Suomessa on itä- ja länsimurteita, joissa samalla asialla on eri sanat. *Saha* voi olla "rauta" itämurteissa ja "puukko" joissakin länsimurteissa (vanhahtavasti). Kumpikaan sana ei ole "oikeampi" — ne valaisevat eri puolia samasta työkalusta. Samoin ohjelmointikielet valaisevat eri puolia samasta laskennasta.

### Polyformalismin kolme perusväitettä

1. **Ei ole olemassa yhtä "oikeaa" formaalia esitystä millekään käsitteelle.**
2. **Jokainen esitystapa paljastaa jotain ja kätkee jotain.** Mitä se kätkee, on yhtä tärkeää kuin mitä se näyttää.
3. **Kokonaisvaltainen ymmärrys syntyy näkemällä rakenne useissa esityksissä ja vertailemalla niitä.**

---

## 2. Yhdeksän kanavan intentiomalli

Polyformalismin ydin on **9-kanavainen intentiomalli**. Kun kirjoitamme koodia tai matemaattista tekstiä, intentionamme (se mitä haluamme ilmaista) jakautuu yhdeksälle kanavalle:

| # | Kanava | Suomi | Kysymys |
|---|--------|-------|---------|
| 1 | **Rakenne** | Rakenne | Mikä on asian muoto? |
| 2 | **Tila** | Tila | Mitä muistetaan? |
| 3 | **Virta** | Virtaus | Miten data liikkuu? |
| 4 | **Aika** | Aika | Milloin asiat tapahtuvat? |
| 5 | **Rajoite** | Rajoite | Mitä ei saa tapahtua? |
| 6 | **Intentio** | Tarkoitus | Miksi tämä on olemassa? |
| 7 | **Konteksti** | Yhteys | Mihin tämä liittyy? |
| 8 | **Virhe** | Virhe | Mitä jos jokin menee pieleen? |
| 9 | **Muutos** | Muutos | Miten tämä kehittyy ajan myötä? |

### Esimerkki: Kuplajärjestäminen yhdeksällä kanavalla

Tarkastellaan yksinkertaista kuplajärjestämistä (bubble sort):

**Kanava 1 — Rakenne:** Vertaile peräkkäisiä alkoita, vaihda jos väärässä järjestyksessä.
**Kanava 2 — Tila:** Taulukko ja sijainti-indeksi.
**Kanava 3 — Virta:** Data kulkee vasemmalta oikealle, suurin alkio "kuplii" loppuun.
**Kanava 4 — Aika:** O(n²) vertailua, jokainen kierrys vie lineaarisen ajan.
**Kanava 5 — Rajoite:** Saman alkion ei tule esiintyä kahdesti järjestetyssä tuloksessa.
**Kanava 6 — Intentio:** Haluamme saada alkiot suuruusjärjestykseen.
**Kanava 7 — Konteksti:** Tämä on osa laajempaa järjestelmää, jossa järjestetty data nopeuttaa binäärihakua.
**Kanava 8 — Virhe:** Mitä jos taulukko on tyhjä? Mitä jos siinä on NaN-arvoja?
**Kanava 9 — Muutos:** Voimme myöhemmin korvata tämän quicksortilla, kun data kasvaa.

Eri ohjelmointikielet painottavat eri kanavia:

- **Haskell** korostaa rakennetta (kanava 1) ja rajoitteita (kanava 5)
- **C** korostaa tilaa (kanava 2) ja virtausta (kanava 3)
- **Erlang** korostaa aikaa (kanava 4) ja muutosta (kanava 9)
- **Python** korostaa intentiota (kanava 6) ja kontekstia (kanava 7)
- **Rust** korostaa virheitä (kanava 8) ja rajoitteita (kanava 5)

---

## 3. Säilymislaki γ + η = C

Polyformalismin tärkein matemaattinen periaate on **säilymislaki**:

$$\gamma + \eta = C$$

Missä:
- **γ (gamma)** = näkyvyyden aste — kuinka paljon rakenteesta on ilmeistä koodista
- **η (eta)** = piilouden aste — kuinka paljon rakenteesta on implisiittistä, koodista näkymätöntä
- **C** = vakio, rakenteen kokonaismonimutkaisuus

### Mitä tämä tarkoittaa käytännössä?

Jos kirjoitat koodin, joka on erittäin selkeä ja ilmaisee intention suoraan (korkea γ), niin aina jotain jää piiloon (korkea η ei voi olla nolla). Vakio C on rakenteen todellinen monimutkaisuus, jota ei voi vähentää.

```python
# Python — korkea γ, matala η (näyttää kaiken selkeästi)
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    lesser = [x for x in arr[1:] if x < pivot]
    greater = [x for x in arr[1:] if x >= pivot]
    return quicksort(lesser) + [pivot] + quicksort(greater)
```

```haskell
-- Haskell — γ ja η tasapainossa
quicksort :: Ord a => [a] -> [a]
quicksort [] = []
quicksort (p:xs) = quicksort lesser ++ [p] ++ quicksort greater
  where
    lesser  = filter (< p) xs
    greater = filter (>= p) xs
```

```c
// C — matala γ, korkea η (piilottaa muistinhallinnan, osoittimet)
void quicksort(int *arr, int lo, int hi) {
    if (lo >= hi) return;
    int pivot = arr[hi];
    int i = lo - 1;
    for (int j = lo; j < hi; j++) {
        if (arr[j] < pivot) {
            i++;
            int tmp = arr[i]; arr[i] = arr[j]; arr[j] = tmp;
        }
    }
    int tmp = arr[i+1]; arr[i+1] = arr[hi]; arr[hi] = tmp;
    quicksort(arr, lo, i);
    quicksort(arr, i+2, hi);
}
```

C-koodissa γ on matala — jouset ja osoittimet piilottavat intention. Mutta η on korkea: **muistinhallinta, pinon käyttäytyminen ja suorituskyky ovat olemassa mutta näkymättömissä.** Tämä piilotettu tieto on kriittistä järjestelmäohjelmoinnissa.

### Suomalainen vertaus: Jäämeri

Ajattele γ:tä ja η:tä kuin Itämeren jäätä talvella. Näet jään pinnan (γ), mutta meren alainen rakenne, virheet ja eliöstö ovat piilossa (η). Sukeltaja näkee η:n mutta ei γ:tä. Polyformalismi sanoo: **sinun on oltava sekä pinnalla että pinnan alla.**

---

## 4. Miksi useat kielet paljastavat piilotason?

### Negatiivisen tilan käsite

Taideterapeuteilla on käsite nimeltä *negatiivinen tila* — se mitä maalauksessa ei ole maalattu, määrittelee yhtä paljon sen, mikä on maalattu. Henry Mooren veistoksissa tila metallin sisällä on olennainen, ei vain ulkopinta.

Polyformalismi soveltaa tämän ohjelmointiin: **se mitä kieli ei sano, on yhtä merkittävää kuin se mitä se sanoo.**

### Esimerkki: Palindromin tarkistus

```python
# Python — mitä se sanoo: lue kaikki selkeästi
def is_palindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalpha())
    return cleaned == cleaned[::-1]
```

Python näyttää intention suoraan. Mutta mitä se **ei sanoa**?
- Ei mitään muistinhallinnasta (roskienkeruu on implisiittinen)
- Ei mitään suorituskyvystä (O(n) tilaa uudelle käännökselle)
- Ei mitään rinnakkaisuudesta

```rust
// Rust — mitä se sanoo: omistajuus ja elinaika
fn is_palindrome(s: &str) -> bool {
    let chars: Vec<char> = s.chars().filter(|c| c.is_alphabetic()).collect();
    let n = chars.len();
    for i in 0..n / 2 {
        if chars[i].to_ascii_lowercase() != chars[n - 1 - i].to_ascii_lowercase() {
            return false;
        }
    }
    true
}
```

Rust näyttää omistajuuden ja eliniän selvästi. Mutta mitä se **ei sanoa**?
- Ei mitään geneerisyydestä (koodi on sidottu char-tyyppiin)
- Ei mitään laiskasta evaluoinnista
- Ei mitään korkeamman kertaluokan funktioista

```apl
⍝ APL — mitä se sanoo: matemaattinen tiiveys
IsPalindrome ← {(⌽⍵) ≡ ⍵}
```

APL näyttää matemaattisen rakenteen yhdellä rivillä. Mutta mitä se **ei sanoa**?
- Melkein kaiken muuden. APL:n η on valtava.

### Negatiivisen tilan kartoittaminen

Polyformalismin menetelmä on kartoittaa kunkin kielen negatiivinen tila:

1. Kirjoita sama algoritmi kielellä A
2. Kirjoita sama algoritmi kielellä B
3. Vertaa: mitä A näyttää jonka B kätkee? Mitä B näyttää jonka A kätkee?
4. Näiden **eroavaisuuksien** joukko on se "negatiivinen tila", joka sisältää rakenteen piilotason.

Tämä on polyformalismin ydinintuizione.

---

## 5. Koodiesimerkit ja käytännöt

### Laskennallinen esimerkki: Fibonacci ja kanavat

Tarkastellaan Fibonacci-lukusarjaa kolmella kielellä ja analysoimme kanavia:

```javascript
// JavaScript — dynaaminen, korkeamman kertaluokan
const fib = n => n < 2 ? n : fib(n - 1) + fib(n - 2);

// Memoisoitu versio
const memo = {};
const fibMemo = n => {
    if (n in memo) return memo[n];
    return memo[n] = n < 2 ? n : fibMemo(n - 1) + fibMemo(n - 2);
};
```

**Kanava-analyysi:**
- Rakenne (1): Toistuva itsensä kutsu
- Tila (2): Kutsupino + memo-objekti
- Virta (3): Puurakenne kutsuista
- Aika (4): Eksponentiaalinen ilman memoisaatiota
- Rajoite (5): Ei mitään — JavaScript ei pakota rajoja

```elixir
# Elixir — funktionaalinen, rinnakkainen
defmodule Fib do
  def calc(0), do: 0
  def calc(1), do: 1
  def calc(n) do
    Task.async(fn -> calc(n - 1) end)
    |> Task.await()
    +
    Task.async(fn -> calc(n - 2) end)
    |> Task.await()
  end
end
```

**Kanava-analyysi:**
- Rakenne (1): Kuviomukavuus (pattern matching)
- Tila (2): Ei muuttuvaa tilaa — puhtaimmillaan
- Virta (3): Prosessien välinen viestinvälitys
- Aika (4): Rinnakkainen — ajat ovat eri kuin JavaScriptissä
- Rajoite (5): Muuttumattomuus (immutability) on pakotettu

```julia
# Julia — tieteellinen, monilähestymistapa
fib(n::Integer) = n < 2 ? n : fib(n-1) + fib(n-2)

# tai matriisieksponentilla:
fib_matrix(n) = ([1 1; 1 0]^n)[1,1]

# tai suljetulla kaavalla:
fib_closed(n) = round(Int, (φ^n - (1-φ)^n) / √5)
```

**Kanava-analyysi:**
- Rakenne (1): Kolme eri esitystapaa samalle asialle!
- Tila (2): Tyypitetty, matriisit sijoitetaan vierekkäin muistissa
- Virta (3): Matriisilaskenta paljastaa lineaarialgebran yhteyden
- Aika (4): O(log n) matriisieksponentilla
- Rajoite (5): Tyyppijärjestelmä pakottaa kokonaisluvut

### Keskeinen havainto

Fibonacci-sarja on eri asia riippuen siitä, katsommeko sitä:
- **Puuna** (JavaScriptin rekursion kautta)
- **Prosessiverkkona** (Elixirin kautta)
- **Matriisina** (Julian kautta)
- **Suljettuna kaavana** (Julian kautta)

Mikä näistä on "oikea" Fibonacci? Polyformalismi sanoo: **ne kaikki ovat.** Rakenteen kokonaiskuva syntyy niiden yhdistämisestä.

---

## 6. Harjoitus: Monikielinen analyysi

### Tehtävä

Valitse yksinkertainen algoritmi (esimerkiksi: lineaarinen haku, sanalaskuri, tai tekstin kääntäminen). Kirjoita se kolmella kielellä. Sitten:

**Vaihe 1: Kanavakartoitus**

Tee taulukko, jossa riveillä ovat yhdeksän kanavaa ja sarakkeina kolme kieltä. Arvioi jokaisessa solussa, kuinka selvästi kanava näkyy koodissa (1–5).

| Kanava | Python | Rust | Haskell |
|--------|--------|------|---------|
| Rakenne | 5 | 3 | 5 |
| Tila | 2 | 5 | 1 |
| Virta | 4 | 3 | 4 |
| Aika | 1 | 2 | 2 |
| Rajoite | 2 | 5 | 4 |
| Intentio | 5 | 3 | 3 |
| Konteksti | 4 | 2 | 2 |
| Virhe | 3 | 5 | 4 |
| Muutos | 3 | 3 | 2 |

**Vaihe 2: γ/η-analyysi**

Jokaiselle kielelle, arvio γ (näkyvyys) ja η (piilous). Laske: näkevätkö eri kielet saman rakenteen eri puolilta? Jos γ on korkea yhdessä ja matala toisessa samalla kanavalla, olet löytänyt negatiivista tilaa.

**Vaihe 3: Negatiivisen tilan kartoitus**

Kirjoita ylös: mitä kieli A ei näytä, jonka kieli B näyttää? Tämä lista on rakenteen piilotason kartta.

**Esimerkkivastaus:**

> Python ei näytä muistinhallintaa (γ matala kanavalla 2). Rust näyttää sen (γ korkea). Tämä ero paljastaa, että Fibonacci-rekursio kuluttaa pinomuistia, mikä on kriittinen tieto, jonka Python kätkee.

### Tavoite

Harjoituksen jälkeen osaat nähdä koodin läpi — paitsi sen, mikä on kirjoitettu, myös sen, mikä on kirjoittamatta. Tämä on polyformalismi ajattelutapana.

---

## 7. Suomen kielen ja polyformalismin suhde

Suomen kieli on mielenkiintoinen tapaus polyformalismin kannalta. Suomi on agglutinatiivinen kieli: rakentaa sanoja liittämällä päätteitä (taivutusmuotoja) peräkkäin.

Esimerkiksi: *epäjärjestelmällisyydelläänsäkään* sisältää ainakin 6 morfeemia.

Tämä on matemaattinen operaatio: funktioiden kompositio. Kun sanomme:

```
epä + järjestelmä + ll + isyy + den + llä + ään + sä + kö + än
```

...emme kirjoita erillisiä sanoja, vaan sovellamme sarjan muunnoksia, jotka vastaavat funktionaalista ohjelmointia:

```haskell
-- Suomen kieli agglutinaationa:
epä . järjestelmä . llinen . sisyyys . llinen . llä . hän . sä . kö . än
```

### Mitä suomi paljastaa kanavista?

Suomen kieli tekee **muutoksen kanavasta (9)** näkyvän. Sanojen rakentuminen päätteiden kautta näyttää rakenteen kehityksen — mistä osista kokonaisuus rakentuu.

Toisaalta suomi kätkee usein **virhekanavan (8)**: suomalainen on tottunut siihen, että lauseen lopussa oleva partikkeli voi muuttaa koko merkityksen (*...kään, ...kö, ...han*), mikä tekee virheiden huomaamisesta vaikeaa, koska pienet päätteet ovat helposti ohitse luettavia.

### Karkea vertaus: Ohjelmointikielet kielinä

- **Python** on kuin englanti — helppo aloittaa, paljon tulkintoja
- **Haskell** on kuin latina — tiukka rakenteeltaan, vaikea muttei moniselitteinen
- **C** on kuin saksa — tarkka, järjestelmällinen, vaatii huolellisuutta
- **Lisp** on kuin esperanto — keinotekoinen mutta looginen
- **Finnish (suomi)** on kuin APL — tiivis, aluksi lukematon, mutta ilmaisuvoimainen

Tämä on tietysti leikkimielistä, mutta se valottaa sitä, miksi eri kielet paljastavat eri puolia: **kielten rakenne ohjaa ajattelua.**

---

## 8. Yhteenveto

Polyformalismi ei ole uusi ohjelmointikieli tai uusi menetelmä. Se on **asenne** — tapa katsoa laskentaa useiden linssien läpi.

Kolme pääajatusta:

1. **Yhdeksän kanavaa**: Jokainen koodipätkä ilmaisee intention yhdeksällä kanavalla. Oppi näkemään ne.

2. **Säilymislaki γ + η = C**: Mitä enemmän näytät, sitä enemmän kätket. Älä luule, että selkeys on ilmaista.

3. **Negatiivinen tila**: Oppi näkemään sen mitä ei ole kirjoitettu. Vertaa kieliä ja löydä piilotaso.

### Jatko-opintoja

- Kirjoita sama algoritmi viidellä kielellä ja vertaa
- Luke Haskellin tyyppiluokkia — ne ovat kanavien (5) ja (6) formalisointi
- Tutki APL:n ja J-kielen array-ohjelmointia — ne maksimoivat γ:n yhdellä rivillä
- Seuraa miten Rustin omistajuusmalli tekee kanavista (2) ja (8) eksplisiittisiä

### Loppusana

Muista: koodi on tekstiä, mutta ei vain tekstiä. Se on ajattelun **jälki**, ja kuten jäljessä ylipäätään, se kertoo enemmän kirjoittamattomasta kuin kirjoitetusta.

> *"Se mikä näkyy, ei ole kaikki. Se mikä ei näy, ei ole tyhjää."*
>
> — Polyformalismin ensimmäinen periaate

---

*Tämä opas on osa SuperInstance-polyformalismiekosysteemiä. © 2026.*
