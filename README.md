# Étude approfondie des métiers et de leur avenir — Bac Pro CIEL

Dossier d'aide à la décision : cybersécurité, IA, systèmes et réseaux, métiers publics.
Profil : France, région Auvergne-Rhône-Alpes (secteur d'Annonay), Bac Pro CIEL.

## Le document final

**[etude_metiers/out/Etude_metiers_avenir_BacPro_CIEL.pdf](etude_metiers/out/Etude_metiers_avenir_BacPro_CIEL.pdf)** — 90 pages :
- 18 métiers étudiés en détail (fiches A-F : métier, parcours, salaires 6 niveaux brut/net/net après IR, progression, impact IA, probabilités)
- 8 métiers alternatifs méconnus
- 10 graphiques (salaires, IA, scénarios politiques, multicritère…)
- Scénarios politiques 2030/2035/2040, fiscalité et aides 2025, plan d'action 1/3/5/10 ans
- Sources officielles datées (ANSSI, Apec, Légifrance, gendarmerie, Insee…) + méthodologie complète

## Régénérer le PDF

```bash
pip install reportlab matplotlib pillow pypdf
python3 make_charts.py   # génère les 10 graphiques dans charts/
python3 build_pdf.py     # génère le PDF dans out/
```

## Structure

- `data/data_a.py`, `data_b.py`, `data_c.py` — base de données des 18 métiers + 8 alternatifs
- `fiscal.py` — module brut → net → net après IR (barème 2025, célibataire 1 part)
- `scoring.py` — moteur multicritère (10 critères pondérés) et jugements experts documentés
- `make_charts.py` — génération des 10 graphiques
- `build_pdf.py` — construction du PDF (18 sections, table des matières, pagination)
