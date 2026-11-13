"""Moteur multicritere et scores de synthese.

Les criteres qualitatifs (demande, stabilite, conditions, interet, acces,
evolution, mobilite) sont des jugements experts codes sur 100, appuyes sur les
donnees citees dans le PDF (ANSSI 2025, Apec 2025, Zeroday 2025, France Travail).
Ils sont explicitement presentés comme des estimations, pas des mesures.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + '/data')
import data_a, data_b, data_c

ALL = data_a.METIERS_A + data_b.METIERS_B + data_c.METIERS_C
ALT = data_c.ALTERNATIFS
BY_ID = {m['id']: m for m in ALL + ALT}

# Jugements experts 0-100 (voir methodologie PDF, section 12)
QUAL = {
 'soc':               dict(demande=70, stabilite=75, conditions=45, interet=75, acces=55, evolution=70, intl=65),
 'dfir':              dict(demande=75, stabilite=80, conditions=40, interet=85, acces=40, evolution=75, intl=70),
 'pentest':           dict(demande=60, stabilite=70, conditions=55, interet=90, acces=35, evolution=75, intl=75),
 'pentest_ia':        dict(demande=65, stabilite=60, conditions=55, interet=95, acces=15, evolution=80, intl=80),
 'sec_ia':            dict(demande=70, stabilite=65, conditions=55, interet=95, acces=10, evolution=80, intl=75),
 'ingenieur_cyber':   dict(demande=80, stabilite=80, conditions=60, interet=80, acces=40, evolution=75, intl=70),
 'consultant_cyber':  dict(demande=80, stabilite=65, conditions=55, interet=70, acces=40, evolution=80, intl=75),
 'cloud_sec':         dict(demande=85, stabilite=75, conditions=70, interet=75, acces=30, evolution=80, intl=80),
 'ot_sec':            dict(demande=75, stabilite=85, conditions=65, interet=80, acces=55, evolution=70, intl=60),
 'admin_sys':         dict(demande=75, stabilite=70, conditions=60, interet=65, acces=75, evolution=65, intl=55),
 'ingenieur_sr':      dict(demande=75, stabilite=75, conditions=60, interet=70, acces=55, evolution=70, intl=60),
 'architecte_cyber':  dict(demande=85, stabilite=85, conditions=65, interet=85, acces=15, evolution=80, intl=70),
 'ml_engineer':       dict(demande=75, stabilite=65, conditions=60, interet=85, acces=20, evolution=75, intl=80),
 'devsecops':         dict(demande=80, stabilite=75, conditions=70, interet=80, acces=30, evolution=75, intl=75),
 'auditeur_secu':     dict(demande=70, stabilite=75, conditions=65, interet=60, acces=45, evolution=70, intl=55),
 'technicien_it':     dict(demande=70, stabilite=65, conditions=60, interet=55, acces=95, evolution=50, intl=40),
 'gendarme_cyber':    dict(demande=60, stabilite=98, conditions=35, interet=70, acces=45, evolution=55, intl=15),
 'rssi':              dict(demande=85, stabilite=85, conditions=45, interet=70, acces=5, evolution=85, intl=60),
 'technicien_telecom':dict(demande=75, stabilite=60, conditions=45, interet=50, acces=90, evolution=45, intl=30),
 'electronicien_embarque': dict(demande=70, stabilite=70, conditions=65, interet=75, acces=60, evolution=65, intl=55),
 'analyste_cti':      dict(demande=65, stabilite=70, conditions=60, interet=85, acces=35, evolution=70, intl=70),
 'ingenieur_iam':     dict(demande=80, stabilite=80, conditions=65, interet=65, acces=50, evolution=70, intl=65),
 'formateur_cyber':   dict(demande=55, stabilite=70, conditions=80, interet=70, acces=25, evolution=60, intl=40),
 'pentest_hardware':  dict(demande=45, stabilite=60, conditions=60, interet=95, acces=20, evolution=75, intl=70),
 'dpo':               dict(demande=60, stabilite=75, conditions=70, interet=55, acces=20, evolution=65, intl=45),
 'chef_projet_cyber': dict(demande=75, stabilite=75, conditions=60, interet=55, acces=25, evolution=75, intl=55),
}
# Duree d'etudes typique (annees apres le bac) et cout total estime (EUR)
ETUDES = {
 'soc': (3, 1500), 'dfir': (5, 3000), 'pentest': (4, 2500),
 'pentest_ia': (6, 8000), 'sec_ia': (6, 8000), 'ingenieur_cyber': (4, 2500),
 'consultant_cyber': (4, 2500), 'cloud_sec': (4, 3000), 'ot_sec': (4, 2500),
 'admin_sys': (2, 500), 'ingenieur_sr': (3, 1500), 'architecte_cyber': (6, 5000),
 'ml_engineer': (5, 4000), 'devsecops': (4, 3000), 'auditeur_secu': (4, 2500),
 'technicien_it': (0, 0), 'gendarme_cyber': (0.5, 0), 'rssi': (6, 5000),
 'technicien_telecom': (0, 0), 'electronicien_embarque': (3, 1500),
 'analyste_cti': (4, 2500), 'ingenieur_iam': (3, 1500), 'formateur_cyber': (4, 2500),
 'pentest_hardware': (5, 4000), 'dpo': (5, 4000), 'chef_projet_cyber': (4, 2500),
}

POIDS = {'salaire_lt': 15, 'salaire_depart': 10, 'demande': 15, 'stabilite': 12,
         'ia_resistance': 10, 'acces': 10, 'interet': 8, 'evolution': 8,
         'conditions': 7, 'intl': 5}

def _scale(v, lo, hi):
    return max(0.0, min(100.0, (v - lo) / (hi - lo) * 100.0))

def salaire_mid(m, idx):
    try:
        return m['salaires'][idx]['brut'][1]
    except (IndexError, KeyError):
        return 0

def scores(m):
    q = QUAL[m['id']]
    dep = salaire_mid(m, 0)
    lt = max(salaire_mid(m, 4), salaire_mid(m, 5))
    ia = m['ia']
    ia_resistance = 100 - (ia['auto'] * 0.5 + ia['recrut'] * 0.5)
    s = dict(
        salaire_depart=_scale(dep, 20000, 55000),
        salaire_lt=_scale(lt, 45000, 120000),
        demande=q['demande'], stabilite=q['stabilite'],
        ia_resistance=ia_resistance, acces=q['acces'],
        interet=q['interet'], evolution=q['evolution'],
        conditions=q['conditions'], intl=q['intl'])
    total = sum(s[k] * POIDS[k] for k in POIDS) / sum(POIDS.values())
    s['total'] = round(total, 1)
    s['salaire_depart_eur'] = dep
    s['salaire_lt_eur'] = lt
    return s

def classement():
    rows = []
    for m in ALL:
        s = scores(m)
        rows.append((m['nom'], m['id'], s))
    rows.sort(key=lambda r: -r[2]['total'])
    return rows

if __name__ == '__main__':
    for nom, mid, s in classement():
        print(f"{s['total']:5.1f}  {nom}")
