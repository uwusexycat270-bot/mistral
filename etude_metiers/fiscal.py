"""Module fiscal : conversion brut -> net et calcul IR (bareme 2026).

Hypotheses (documentees dans le PDF, section methodologie) :
- Cotisations salariales : 23 % du brut (cadre, regime general + retraite
  complementaire + APEC). Approximation valide pour un cadre en entreprise privee.
- Abattement forfaitaire de 10 % pour frais professionnels (plafonne a 14 555 EUR,
  plancher 509 EUR en 2026), celibataire, 1 part fiscale.
- Bareme IR 2026 (revenus 2025, loi de finances pour 2026 n° 2026-103 du 19/02/2026,
  revalorisation +0,9 %) par part :
  0 - 11 600 : 0 % ; 11 600 - 29 579 : 11 % ; 29 579 - 84 577 : 30 % ;
  84 577 - 181 917 : 41 % ; > 181 917 : 45 %.
- Decote celibataire : 897 - 45,25 % x IR si IR <= 1 982 EUR.
- Pas de prime non soumise, pas de revenus annexes, pas de case T/P.
Source : service-public.gouv.fr (F1419, verifie 2026) ; impots.gouv.fr ; loi n° 2026-103.
"""
PLAFOND_ABAT = 14555.0
MIN_ABAT = 509.0
BAREME = [(11600, 0.0), (29579, 0.11), (84577, 0.30), (181917, 0.41), (float('inf'), 0.45)]
DECOTE_FORFAIT = 897.0
DECOTE_SEUIL = 1982.0

def ir_annuel(rni):
    """Impot sur le revenu annuel, celibataire 1 part, apres decote."""
    imp = 0.0
    prev = 0.0
    for plafond, taux in BAREME:
        if rni > prev:
            imp += (min(rni, plafond) - prev) * taux
            prev = plafond
        else:
            break
    if imp < DECOTE_SEUIL:
        imp = max(0.0, imp - (DECOTE_FORFAIT - 0.4525 * imp))
    return imp

def net_mensuel(brut_annuel, taux_cotis=0.23):
    """Net apres IR, celibataire 1 part, en EUR/mois."""
    if brut_annuel <= 0:
        return 0.0, 0.0, 0.0
    net_avant_ir = brut_annuel * (1 - taux_cotis) / 12.0
    abat = min(max(brut_annuel * 0.10, MIN_ABAT), PLAFOND_ABAT)
    rni = max(0.0, brut_annuel - abat)
    ir = ir_annuel(rni)
    net_apres_ir = net_avant_ir - ir / 12.0
    return round(net_avant_ir, 0), round(net_apres_ir, 0), round(ir, 0)

if __name__ == '__main__':
    for b in (25000, 40000, 60000, 90000, 150000):
        n0, n1, ir = net_mensuel(b)
        print(f"brut {b:>7} -> net avant IR {n0:>6.0f} /mois, apres IR {n1:>6.0f} /mois (IR {ir:.0f}/an)")
