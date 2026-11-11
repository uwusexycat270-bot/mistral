"""Module fiscal : conversion brut -> net et calcul IR (bareme 2025).

Hypotheses (documentees dans le PDF, section methodologie) :
- Cotisations salariales : 23 % du brut (cadre, regime general + retraite
  complementaire + APEC). Approximation valide pour un cadre en entreprise privee.
- Abattement forfaitaire de 10 % pour frais professionnels (plafonne a 14 426 EUR,
  plancher 505 EUR en 2025), celibataire, 1 part fiscale.
- Bareme IR 2025 (revenus 2024, indexe) par part :
  0 - 11 497 : 0 % ; 11 497 - 29 315 : 11 % ; 29 315 - 83 823 : 30 % ;
  83 823 - 180 294 : 41 % ; > 180 294 : 45 %.
- Decote celibataire : 889 - 45,25 % x IR si IR < 1 964 EUR.
- Pas de prime non soumise, pas de revenus annexes, pas de case T/P.
Source : impots.gouv.fr, bareme 2025 ; service-public.fr.
"""
PLAFOND_ABAT = 14426.0
MIN_ABAT = 505.0
BAREME = [(11497, 0.0), (29315, 0.11), (83823, 0.30), (180294, 0.41), (float('inf'), 0.45)]

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
    if imp < 1964:
        imp = max(0.0, imp - (889 - 0.4525 * imp))
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
