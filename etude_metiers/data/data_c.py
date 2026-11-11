# -*- coding: utf-8 -*-
"""Fiches metiers M13 a M18 + metiers alternatifs — donnees structurees."""

M13_ML = {
    "id": "ml_engineer",
    "nom": "Ingénieur IA / Machine Learning",
    "famille": "Intelligence artificielle — Ingénierie",
    "alt": "Data engineer, ML engineer, ingénieur IA, data scientist (variante analyse), MLOps engineer (variante production)",
    "acces": "Bac+5 quasi obligatoire (master IA/informatique ou école) — hors accès direct Bac Pro CIEL",
    "description": "L'ingénieur IA conçoit, entraîne et met en production des modèles de machine learning : prédiction, vision, langage, recommandation. En France, le métier s'est scindé en data scientist (analyse, modèles), ML engineer (mise en production) et data engineer (pipelines de données) — ce dernier étant le plus recruté. Salaires élevés, marché concurrentiel en entrée (beaucoup de candidats bac+5) mais en forte croissance. L'IA est ici à la fois le sujet du métier et l'outil de travail.",
    "missions": [
        "Collecter, nettoyer et préparer les données (souvent la majorité du temps réel)",
        "Entraîner et évaluer des modèles (classiques ou deep learning / LLM)",
        "Mettre en production : API, conteneurs, pipelines, monitoring (MLOps)",
        "Intégrer des modèles existants (fine-tuning, RAG, APIs) plutôt que tout réentraîner",
        "Collaborer avec les métiers pour traduire les besoins en problèmes de données",
        "Mesurer la performance réelle en production (dérive des données, biais)",
        "Veiller à la conformité (RGPD, AI Act pour les systèmes à risque)",
        "Veille scientifique et technologique permanente",
    ],
    "taches": "30 % données (collecte, nettoyage — la réalité cachée du métier), 25 % modélisation et entraînement, 20 % mise en production et MLOps, 15 % collaboration métier, 10 % veille.",
    "outils": "Python (numpy, pandas, scikit-learn), PyTorch/TensorFlow, Hugging Face, SQL, Spark, Docker/Kubernetes, MLflow/Kubeflow, APIs LLM (OpenAI/Anthropic/Mistral), Git, cloud ML (SageMaker, Azure ML, Vertex).",
    "difficulte": "Très élevée : mathématiques (statistiques, algèbre linéaire, optimisation) + développement sérieux + compréhension métier. Le master IA est exigeant.",
    "comp_req": [
        "Python solide et SQL",
        "Mathématiques du ML (statistiques, algèbre linéaire) — niveau master",
        "MLOps : conteneurisation, pipelines, monitoring",
        "Compréhension métier (traduire un besoin en problème de données)",
        "Anglais scientifique",
    ],
    "comp_opt": [
        "Deep learning avancé (transformers, vision, audio)",
        "Big data (Spark, Kafka)",
        "MLOps avancé (Kubeflow, CI/CD modèles)",
        "Conformité IA (AI Act, RGPD) — différenciant croissant",
    ],
    "qualites": "Rigueur scientifique, curiosité, persévérance (les modèles échouent souvent), communication (expliquer l'IA aux non-spécialistes), pragmatisme (un modèle simple en production vaut mieux qu'un modèle brillant en labo).",
    "repartition": "Données 30 %, modélisation 25 %, production 20 %, collaboration 15 %, veille 10 %.",
    "autonomie": "Moyenne à forte : problèmes confiés, méthodes libres, résultats attendus.",
    "equipe": "Équipes data/produit pluridisciplinaires (data scientists, développeurs, métier).",
    "teletravail": "Très élevé : 3 jours/semaine courant, full remote fréquent.",
    "horaires": "Journée standard ; entraînements longs surveillés hors horaires parfois ; peu d'astreintes.",
    "urgences": "Rares (incidents de production de modèles) ; déplacements limités.",
    "avantages": [
        "Salaires parmi les plus élevés du numérique français",
        "Domaine en explosion (18 % des entreprises de 10+ salariés utilisent l'IA en 2025 contre 10 % en 2024 — Insee) : la demande croît",
        "Travail intellectuel stimulant au plus près de la recherche",
        "Fort potentiel international et remote",
        "Compétences au cœur de la transformation économique",
    ],
    "inconvenients": [
        "Bac+5 quasi obligatoire : 5 ans d'études exigeantes (maths)",
        "Concurrence en entrée : beaucoup de candidats masters, y compris internationaux",
        "La réalité des données (nettoyage, qualité) déçoit par rapport à l'image « scientifique »",
        "Veille scientifique permanente (le domaine bouge tous les mois)",
        "Risque de spécialisation sur une mode technique (un framework peut mourir)",
    ],
    "stress": "Modéré : pression de résultats (les modèles doivent marcher), échéances produits ; peu d'urgences opérationnelles.",
    "realite": "Théorie : « concevoir des IA révolutionnaires ». Réalité : 60-70 % du travail est de la manipulation de données médiocres et de la mise en production laborieuse. La plupart des entreprises intègrent des modèles existants (API, fine-tuning) plutôt qu'elles n'entraînent. Le métier est moins « scientifique » et plus « ingénierie logicielle avec des maths » que l'image véhiculée.",
    "parcours": [
        {
            "nom": "Parcours master IA — voie standard",
            "desc": "BUT R&T/GEII ou licence maths-info (3 ans) puis master IA/data science (2 ans). Attention : le passage Bac Pro CIEL -> licence générale de maths-info est difficile (prérequis maths) ; le BUT est la voie recommandée.",
            "duree": "5 ans",
            "difficulte": "Très élevée (maths)",
            "selectivite": "Masters IA très demandés (sur dossier, parfois entretien) ; concurrence internationale",
            "cout": "0-1 000 €/an (public)",
            "financement": "Alternance M2 fréquente ; bourses",
            "prob": "65-80 % d'obtenir un premier poste data/ML dans l'année après le master",
            "paliers": ["Stagiaire data", "Data engineer / ML engineer junior", "ML engineer confirmé"],
            "reorient": "Vers développement, data engineering, sécurité IA, conseil",
        },
        {
            "nom": "Parcours école d'ingénieurs avec spécialisation IA",
            "desc": "École d'ingénieurs (via ATS après BTS CIEL possible) avec majeure IA, puis poste ML engineer. Les écoles offrent le meilleur accès aux grands employeurs.",
            "duree": "5 ans (2+3) ou 3 ans après BTS",
            "difficulte": "Très élevée",
            "selectivite": "ATS sélectif ; écoles sur dossier",
            "cout": "0-1 500 €/an (public) ; privées 8 000-13 000 €/an",
            "financement": "Alternance en école ; bourses",
            "prob": "75-85 %",
            "paliers": ["Ingénieur junior", "ML engineer", "Senior/Lead"],
            "reorient": "Vers développement, architecture, management",
        },
        {
            "nom": "Parcours data engineer (porte d'entrée alternative)",
            "desc": "Se spécialiser d'abord en data engineering (pipelines, SQL, Spark) — moins de maths, plus d'infrastructure — puis évoluer vers le ML. Voie plus accessible depuis un profil infrastructure (BTS CIEL).",
            "duree": "3-4 ans (BUT/licence pro) + 2-3 ans d'expérience",
            "difficulte": "Élevée mais moins mathématique",
            "selectivite": "Recrutement data engineer plus ouvert que data scientist",
            "cout": "0-800 €/an (public)",
            "financement": "Alternance",
            "prob": "60-75 % d'entrer dans la data par cette porte",
            "paliers": ["Data engineer junior", "Data engineer confirmé", "ML engineer"],
            "reorient": "Vers infrastructure cloud, DevOps, développement",
        },
    ],
    "salaires": [
        {"niveau": "Débutant (0-2 ans)", "brut": (38000, 44000, 52000),
         "region": "Province 38-44 k€ ; Île-de-France 44-54 k€ ; grandes tech et finance en haut",
         "variable": "Bonus 5-10 % ; actions dans les startups IA"},
        {"niveau": "Junior autonome (2-4 ans)", "brut": (45000, 52000, 64000),
         "region": "Province 45-50 k€ ; Île-de-France 52-66 k€",
         "variable": "Bonus 8-12 %"},
        {"niveau": "Confirmé (4-7 ans)", "brut": (52000, 64000, 80000),
         "region": "Île-de-France, remote international ; médiane big data ≈ 54-57 k€ (Apec)",
         "variable": "Bonus 10-15 %"},
        {"niveau": "Senior (7-12 ans) — expert ML", "brut": (65000, 80000, 105000),
         "region": "Grands groupes tech, finance, éditeurs IA",
         "variable": "Bonus 12-18 %, actions"},
        {"niveau": "Expert / lead ML", "brut": (80000, 95000, 125000),
         "region": "Éditeurs IA, hyperscalers, labs de recherche appliquée",
         "variable": "Bonus 15-20 %, LTI, actions"},
        {"niveau": "Manager / directeur data-IA", "brut": (90000, 110000, 145000),
         "region": "Grands groupes",
         "variable": "Bonus 15-25 %, LTI"},
    ],
    "sal_note": "Apec (médiane big data 54 k€), metiers-ia.fr, offres 2024-2025. Données observées jusqu'à confirmé ; estimations au-delà. Grande dispersion selon employeur : startup (actions, salaires moyens) vs hyperscaler (très haut).",
    "progression": "ML/data engineer junior -> confirmé (3-5 ans) -> senior/expert (6-9 ans) -> lead ou directeur data-IA (9-12 ans). Conditions : projets en production réels, spécialisation (LLM, vision, MLOps), communication. Bifurcations : sécurité IA (forte synergie), management, entrepreneuriat. Plafond technique ≈ 110-125 k€ ; management ≈ 130-145 k€ ; startups : actions potentiellement au-delà (risque élevé).",
    "ia": {"auto": 30, "recrut": 20, "transfo": 70, "creation": 80, "levier": 95,
           "h2030": "L'IA automatise une partie du travail de l'ingénieur IA lui-même (génération de code, AutoML) ; productivité multipliée, demande toujours croissante (18 % des entreprises utilisent l'IA en 2025, en accélération)",
           "h2035": "Métier transformé en profondeur : supervision de systèmes auto-améliorants, intégration de modèles de plus en plus capables",
           "h2040": "Incertitude maximale de l'étude : soit le métier explose (l'IA devient le socle de l'économie), soit il se concentre sur une élite (les modèles font le reste)",
           "notes": "Paradoxe : c'est le métier qui construit l'IA et celui qu'elle transforme le plus vite. Les tâches de codage et de préparation de données s'automatisent ; la conception de systèmes, le jugement métier et la responsabilité restent humaines à moyen terme. Fort potentiel de création d'emplois (chaque entreprise devient une entreprise IA) mais forte incertitude à 15 ans. Le levier IA est maximal : tu utiliserais l'IA comme outil de travail quotidien."},
    "probs": {"premier_emploi": "65-80 % après master IA (marché en croissance mais concurrentiel en entrée)",
              "confirme": "70-80 %",
              "seuils": {"2500": "brut ≈ 43-45 k€ : 1-2 ans ; probabilité 80-90 % à 5 ans",
                         "3000": "brut ≈ 52-55 k€ : 3-5 ans ; probabilité 70-85 %",
                         "4000": "brut ≈ 72-76 k€ : 6-9 ans ; probabilité 55-65 %",
                         "5000": "brut ≈ 92-97 k€ : 9-13 ans ; probabilité 25-35 %"},
              "chomage": "Faible : 5-10 % (mais volatilité des startups)",
              "formation": "Intensive et permanente",
              "obsolescence": "Très rapide (frameworks, modèles) ; les maths et les fondamentaux restent",
              "base": "Estimations raisonnées ; salaires observés (Apec, offres) ; adoption IA documentée (Insee 2025) ; probabilités = fourchettes d'expert"},
    "scenarios": {"defav": "Désillusion IA + récession : contraction des recrutements data, concurrence accrue, salaires sous pression.",
                  "central": "Adoption IA croissante (Insee : 18 % des entreprises en 2025) : forte demande, salaires élevés.",
                  "fav": "L'IA devient le socle de l'économie + investissements massifs (France 2030, IA nationale) : explosion de la demande, salaires records.",
                  "bascule": "Vers le favorable : percées technologiques créant de nouveaux besoins industriels. Vers le défavorable : plateau technologique + automatisation du métier par les modèles eux-mêmes."},
}

M14_DEVSECOPS = {
    "id": "devsecops",
    "nom": "Développeur spécialisé sécurité / DevSecOps",
    "famille": "Développement & sécurité",
    "alt": "Security developer, ingénieur DevSecOps, application security engineer (AppSec), développeur d'outils de sécurité",
    "acces": "Bac+3/5 ou expérience développeur — Zeroday 2025 : segment favorable aux juniors",
    "description": "Le développeur sécurité écrit du code pour sécuriser : outils de détection, automatisation de sécurité, correctifs applicatifs, intégration de la sécurité dans les pipelines de développement (DevSecOps). Il peut aussi développer des produits de sécurité (éditeurs). C'est le croisement le plus rentable du marché : le développement est la compétence la plus transférable de l'informatique, et la sécurité ajoute la prime de rareté. Deux variantes : AppSec (sécuriser les applications de l'entreprise) et sécurité offensive/défensive outillée (éditeurs, SOC engineering).",
    "missions": [
        "Intégrer la sécurité dans les pipelines CI/CD (SAST, DAST, SCA, secrets scanning)",
        "Développer des outils de sécurité internes (automatisation, tri d'alertes, remédiation)",
        "Corriger les vulnérabilités applicatives avec les équipes dev (code review sécurité)",
        "Écrire du code sécurisé et définir les standards de développement",
        "Automatiser la conformité (tests de sécurité continus)",
        "Contribuer aux produits de sécurité (chez les éditeurs) : détection, agents, consoles",
        "Former les développeurs aux bonnes pratiques (OWASP)",
        "Participer aux investigations techniques des incidents applicatifs",
    ],
    "taches": "45 % développement (code réel), 20 % intégration pipeline et outils, 15 % revues de code et conseil aux devs, 10 % incidents, 10 % veille et documentation.",
    "outils": "Python, JavaScript/TypeScript, Go, Java ; Docker/Kubernetes ; GitLab CI/GitHub Actions ; SAST/DAST (SonarQube, Semgrep, OWASP ZAP), SCA ( Dependabot, Snyk) ; Terraform ; OWASP ; cloud ; Burp (profil AppSec).",
    "difficulte": "Élevée : il faut être un vrai développeur ET comprendre la sécurité. La double compétence est rare et donc bien payée.",
    "comp_req": [
        "Développement solide (au moins un langage majeur : Python, JS, Go, Java)",
        "Sécurité applicative : OWASP Top 10, authentification, chiffrement",
        "CI/CD et automatisation",
        "Cloud et conteneurs",
        "Anglais technique",
    ],
    "comp_opt": [
        "Certifications : OSCP (profil offensif), CSSLP, cloud security",
        "Reverse engineering (éditeurs de sécurité)",
        "Sécurité des chaînes d'approvisionnement (supply chain)",
        "Sécurité IA (les éditeurs recrutent des devs sécurité pour les produits IA)",
    ],
    "qualites": "Qualité de code, rigueur, pédagogie (travailler avec des devs qui n'aiment pas la sécurité), pragmatisme, autonomie.",
    "repartition": "Développement 45 %, intégration/outillage 20 %, revues/conseil 15 %, incidents 10 %, veille 10 %.",
    "autonomie": "Forte : sujets confiés, méthodes libres.",
    "equipe": "Équipes dev/produit ou équipe sécurité outillée (5-15 personnes).",
    "teletravail": "Très élevé : 3 jours/semaine courant, full remote fréquent (métier 100 % code).",
    "horaires": "Journée standard ; déploiements hors horaires occasionnels ; astreintes rares.",
    "urgences": "Vulnérabilités critiques à corriger vite (quelques fois par an) ; incidents applicatifs. Sinon rythme calme.",
    "avantages": [
        "Double compétence rare (dev + sécurité) : parmi les meilleurs salaires techniques",
        "Le développement est la compétence la plus transférable de l'IT (tous secteurs, tous pays, freelance)",
        "Segment favorable aux juniors (Zeroday 2025)",
        "Full remote largement disponible",
        "Porte vers les éditeurs de sécurité, les produits, l'entrepreneuriat",
    ],
    "inconvenients": [
        "Il faut d'abord être un bon développeur : l'apprentissage du code est long",
        "Frustration possible : les devs n'aiment pas les contraintes de sécurité (rôle de « police »)",
        "Veille permanente (frameworks, vulnérabilités)",
        "Moins de postes dédiés que l'ingénierie sécurité classique (souvent fusionné avec AppSec)",
        "Pression de la qualité de code (revues, tests)",
    ],
    "stress": "Modéré : échéances de développement, vulnérabilités urgentes ponctuelles. Peu d'astreintes.",
    "realite": "Théorie : « codeur de sécurité de pointe ». Réalité : beaucoup d'intégration d'outils existants, de correction de vulnérabilités banales et de pédagogie auprès des équipes dev. Chez les éditeurs, le travail est un vrai développement produit. Le métier est souvent appris « sur le tas » par des développeurs qui se spécialisent — c'est d'ailleurs la voie la plus courante.",
    "parcours": [
        {
            "nom": "Parcours développement puis sécurité (voie standard)",
            "desc": "BUT informatique/école (développement), 2-3 ans de développement, spécialisation sécurité (projets, certifications, missions AppSec).",
            "duree": "5-6 ans depuis le Bac Pro",
            "difficulte": "Élevée",
            "selectivite": "Admission BUT info modérée ; la spécialisation dépend des opportunités",
            "cout": "0-800 €/an (public)",
            "financement": "Alternance",
            "prob": "65-80 % d'atteindre un poste sécurité-développement à 5-6 ans",
            "paliers": ["Développeur junior", "Développeur confirmé", "DevSecOps/AppSec"],
            "reorient": "Vers développement pur, architecture, pentest, produit",
        },
        {
            "nom": "Parcours DevSecOps direct (alternance)",
            "desc": "BUT/licence pro avec alternance dans une équipe DevSecOps (les équipes recrutent des alternants : segment favorable, Zeroday 2025), poste direct à la sortie.",
            "duree": "3 ans",
            "difficulte": "Élevée (double compétence à acquérir vite)",
            "selectivite": "Trouver l'alternance DevSecOps : plus accessible que le pentest",
            "cout": "0 € en alternance",
            "financement": "Alternance rémunérée",
            "prob": "60-75 %",
            "paliers": ["Alternant DevSecOps", "Ingénieur DevSecOps junior", "Confirmé"],
            "reorient": "Vers DevOps, cloud, développement, SOC engineering",
        },
    ],
    "salaires": [
        {"niveau": "Débutant (0-2 ans)", "brut": (40000, 46000, 54000),
         "region": "Province 40-45 k€ ; Île-de-France 45-55 k€ ; éditeurs et startups tech en haut",
         "variable": "Bonus 5-10 % ; actions startups"},
        {"niveau": "Junior autonome (2-4 ans)", "brut": (46000, 53000, 64000),
         "region": "Province 46-52 k€ ; Île-de-France 52-66 k€",
         "variable": "Bonus 8-12 %"},
        {"niveau": "Confirmé (4-7 ans)", "brut": (54000, 64000, 80000),
         "region": "Province 54-62 k€ ; Île-de-France 62-82 k€ ; TJM 600-1 000 €",
         "variable": "Bonus 10-15 %"},
        {"niveau": "Senior (7-12 ans) — expert sécurité produit", "brut": (65000, 80000, 100000),
         "region": "Éditeurs de sécurité, hyperscalers, remote international",
         "variable": "Bonus 12-18 %, actions"},
        {"niveau": "Expert / lead AppSec", "brut": (78000, 92000, 115000),
         "region": "Éditeurs, grands groupes tech",
         "variable": "Bonus 15-20 %, LTI"},
        {"niveau": "Manager / directeur ingénierie sécurité", "brut": (88000, 105000, 135000),
         "region": "Éditeurs, grands groupes",
         "variable": "Bonus 15-25 %, LTI"},
    ],
    "sal_note": "Silkhom 2026, Zeroday 2025, offres 2024-2025. La double compétence dev+sécurité paie une prime de 10-15 % vs développement seul. Données observées jusqu'à confirmé ; estimations au-delà.",
    "progression": "Développeur -> DevSecOps/AppSec (3-5 ans) -> senior/lead (6-9 ans) -> directeur ingénierie sécurité ou architecte produit (9-12 ans). Conditions : qualité de code reconnue, spécialisation (supply chain, cloud, IA), leadership technique. Plafond ≈ 100-115 k€ technique, 115-135 k€ management. Sorties : éditeurs de sécurité, entrepreneuriat, sécurité IA.",
    "ia": {"auto": 40, "recrut": 20, "transfo": 60, "creation": 70, "levier": 90,
           "h2030": "L'IA assiste le développement (génération de code, revues automatiques) : productivité accrue ; la sécurité des applications IA crée de la demande",
           "h2035": "Développement fortement assisté par IA ; le DevSecOps se concentre sur l'architecture, la validation et les systèmes IA",
           "h2040": "Métier transformé : moins de code manuel, plus de conception et de supervision",
           "notes": "Le développement est à la fois la compétence la plus automatisable et la plus transférable. L'IA écrit du code, mais ce code doit être sécurisé, audité et intégré — ce qui augmente paradoxalement la valeur des profils qui savent à la fois coder et sécuriser. Fort levier IA."},
    "probs": {"premier_emploi": "60-75 % (via alternance DevSecOps ou détour développement)",
              "confirme": "70-80 %",
              "seuils": {"2500": "brut ≈ 43-45 k€ : 1-2 ans ; probabilité 85-90 % à 5 ans",
                         "3000": "brut ≈ 52-55 k€ : 3-5 ans ; probabilité 75-85 %",
                         "4000": "brut ≈ 72-76 k€ : 6-9 ans ; probabilité 55-65 %",
                         "5000": "brut ≈ 92-97 k€ : 9-13 ans ; probabilité 25-35 %"},
              "chomage": "Faible : 4-8 % (développement = compétence universelle)",
              "formation": "Permanente (langages, frameworks, vulnérabilités)",
              "obsolescence": "Frameworks en 3-5 ans ; fondamentaux (code, sécurité) en 10 ans+",
              "base": "Estimations raisonnées ; salaires observés ; tension junior documentée (Zeroday 2025)"},
    "scenarios": {"defav": "Récession tech : moins de recrutements, concurrence accrue des développeurs en reconversion.",
                  "central": "Demande soutenue (logiciels, cloud, IA) : croissance stable, double compétence recherchée.",
                  "fav": "Explosion IA + cybersécurité : pénurie de profils double compétence, salaires records.",
                  "bascule": "Vers le favorable : boom des produits de sécurité IA (les éditeurs recrutent massivement). Vers le défavorable : automatisation du développement plus rapide que prévu + récession."},
}
M15_AUDITEUR = {
    'id': 'auditeur_secu', 'nom': 'Auditeur de sécurité informatique (GRC)',
    'alt': "Auditeur cybersécurité, auditeur SI, consultant GRC, auditeur ISO 27001",
    'famille': 'Gouvernance et conformité', 'acces': 'Bac+3 à Bac+5',
    'description': "L'auditeur de sécurité évalue la conformité des systèmes d'information "
        "aux référentiels (ISO 27001, NIS2, DORA, RGPD) et la réalité des mesures de "
        "protection. Il interviewe les équipes, examine les preuves, rédige des rapports "
        "d'audit avec des constats hiérarchisés et des plans d'action. Le métier est moins "
        "spectaculaire que le pentest mais plus régulier : il repose sur la rigueur "
        "documentaire, la connaissance des référentiels et la capacité à dialoguer avec "
        "des directions métier.",
    'missions': [
        "Préparer et conduire des audits de sécurité (revue documentaire, entretiens, tests de conformité)",
        "Évaluer la conformité aux référentiels ISO 27001, NIS2, DORA, RGPD, PCI-DSS",
        "Rédiger des rapports d'audit : constats, risques, recommandations, plans d'action",
        "Accompagner les organisations vers la certification ou la mise en conformité",
        "Réaliser des analyses de risques (EBIOS RM) et cartographier les actifs critiques",
        "Contrôler la gestion des accès, la journalisation, les sauvegardes, la continuité",
        "Assurer une veille réglementaire (NIS2, DORA, Cyber Resilience Act)",
        "Participer aux comités de sécurité et présenter les résultats aux directions"],
    'taches': "Pratique manuelle 20 % (tests de conformité, extraction de preuves), analyse "
        "et réflexion 30 %, rédaction 30 %, réunions et entretiens 20 %. Le métier est très "
        "écrit : un auditeur passe autant de temps à rédiger qu'à auditer.",
    'outils': "Référentiels ISO 27001/27002, EBIOS RM, FAIR, NIST CSF ; GRC (ServiceNow GRC, "
        "Megamatch/Exaion, Excel) ; outils de scan de conformité (Nessus, Qualys, OpenVAS) ; "
        "SIEM (lecture de journaux) ; Word/Excel avancé ; notions de scripts Python.",
    'difficulte': "Moyenne à élevée : la technique exigée est parfois moindre qu'en SOC ou en "
        "pentest, mais la charge méthodologique (référentiels, preuves, argumentation) et la "
        "niveau rédactionnel sont élevés. Un Bac+3 solide peut suffire en cabinet.",
    'comp_req': [
        "Maîtrise d'au moins un référentiel (ISO 27001, EBIOS RM, NIST CSF)",
        "Bonne culture générale du SI : réseaux, systèmes, applications, cloud",
        "Rédaction professionnelle en français (rapports, plannings, synthèses)",
        "Anglais technique lu et écrit",
        "Méthodologie d'audit : planification, collecte de preuves, argumentation"],
    'comp_opt': [
        "Lead Auditor ISO 27001 (IRCA/PECB)",
        "Connaissance DORA, NIS2, RGPD, PCI-DSS, HDS",
        "Notions de pentest et de scan de vulnérabilités",
        "Automatisation en Python",
        "Expérience sectorielle (banque, santé, industrie)"],
    'qualites': "Rigueur, écoute active, diplomatie (annoncer des non-conformités), "
        "organisation, capacité de synthèse, aisance rédactionnelle, curiosité réglementaire.",
    'repartition': "Pratique 20 % / Réflexion 30 % / Rédaction 30 % / Réunions 20 %",
    'autonomie': "Forte sur les missions confiées, sous supervision de chef de mission ou de "
        "manager de cabinet pour la signature des rapports.",
    'equipe': "Travail en binôme ou petite équipe de mission ; beaucoup d'échanges avec les "
        "équipes audités. Missions souvent en clientèle (déplacements).",
    'teletravail': "Modéré : 2-3 jours possible selon cabinets ; déplacements chez les clients "
        "fréquents (1-3 jours par semaine en période de campagne d'audit).",
    'horaires': "Journée standard ; pics de charge avant les comités d'audit, clôtures "
        "annuelles et échéances NIS2/DORA.",
    'urgences': "Rares ; le métier est planifié à l'avance. Quelques audits flash après "
        "incident, plus stressants.",
    'avantages': [
        "Demande portée par NIS2 et DORA (10 000 à 15 000 entités assujetties en France)",
        "Excellente porte d'entrée vers RSSI, consultant GRC, chef de projet sécurité",
        "Métier moins exposé à l'astreinte que le SOC ou la réponse à incident",
        "Compétences transférables vers la gouvernance, la conformité, le management du risque"],
    'inconvenients': [
        "Très forte part de rédaction et de documentation",
        "Moins de technique que le pentest ou l'ingénierie : frustration possible",
        "Salaires de départ souvent inférieurs aux métiers techniques",
        "Déplacements chez les clients, parfois répétitifs",
        "Marché junior saturé côté candidats (profil GRC très demandé par les écoles)"],
    'stress': "Modéré : délais de livraison, entretiens difficiles, exigence de qualité "
        "documentaire. Peu d'urgences compare au SOC. Risque de routine sur les mêmes "
        "référentiels.",
    'realite': "Sur le terrain, l'audit est souvent perçu par les équipes audités comme une "
        "contrainte : l'auditeur passe autant de temps à convaincre qu'à analyser. La "
        "technique est parfois superficielle (revue de preuves plutôt que tests réels), ce "
        "que les candidats attirés par la technique découvrent parfois trop tard.",
    'parcours': [
        {'nom': "BUT + licence pro + poste GRC junior",
         'desc': "BUT Informatique ou Réseaux & Télécoms, puis licence professionnelle "
             "sécurité, premier poste d'auditeur junior en cabinet.",
         'duree': "3 ans (BUT) + 1 an (licence pro ou direct)",
         'difficulte': "Moyenne", 'selectivite': "Accès BUT sur dossier ; licence pro accessible",
         'cout': "Public : ~170-600 EUR/an ; alternance possible en BUT3 et licence pro",
         'financement': "Alternance (contrat d'apprentissage), bourses CROUS",
         'prob': "45-60 % d'atteindre un poste d'auditeur en 3-4 ans",
         'paliers': ["Technicien support/réseau", "Analyste conformité junior",
             "Auditeur junior", "Auditeur confirmé"],
         'reorient': "Vers consultant GRC, RSSI adjoint, chef de projet sécurité, qualité SI."},
        {'nom': "Master audit/cybersécurité (Bac+5)",
         'desc': "Master 2 sécurité de l'information, audit ou droit du numérique ; le profil "
             "le plus recherché par les grands cabinets (Big Four, ESN).",
         'duree': "5 ans", 'difficulte': "Élevée",
         'selectivite': "Sélectif en M1/M2 ; cabinets recrutent surtout en M2",
         'cout': "Public : ~600-2 000 EUR ; école privée : 8 000-15 000 EUR/an",
         'financement': "Alternance très répandue en M1/M2 (rythme 3-4 semaines/1-2)",
         'prob': "60-75 % d'atteindre un poste d'auditeur/consultant GRC",
         'paliers': ["Stage M2", "Auditeur junior", "Auditeur confirmé", "Chef de mission"],
         'reorient': "Vers RSSI, DPO, consultant gouvernance, contrôle interne IT."},
        {'nom': "Certifications + expérience terrain",
         'desc': "Entrée en SOC, support ou admin, puis certifications ISO 27001 Lead "
             "Implementer/Auditor, CISA ou CRISC, et bascule vers l'audit.",
         'duree': "4-7 ans", 'difficulte': "Moyenne (exige de l'autodiscipline)",
         'selectivite': "Faible à l'entrée (postes techniques), forte sur les certifications",
         'cout': "Certifications : 1 000-3 500 EUR (souvent payées par l'employeur)",
         'financement': "Plan de développement des compétences, CPF",
         'prob': "30-45 % (voie longue, dépend de l'employeur)",
         'paliers': ["Technicien/admin", "Analyste conformité", "Auditeur junior"],
         'reorient': "Retour facile vers l'exploitation (admin, SOC) si l'audit ne convient pas."}],
    'salaires': [
        {'niveau': 'Débutant (0-2 ans)', 'brut': (34000, 40000, 48000),
         'region': "Province/ARA : 34-42k ; IDF : 38-48k ; cabinet vs entreprise finale : -5 %",
         'variable': "Frais de mission remboursés ; prime annuelle 0-8 %"},
        {'niveau': 'Junior (2-4 ans)', 'brut': (40000, 47000, 56000),
         'region': "ARA : 40-50k ; IDF : 44-56k", 'variable': "Prime 5-10 %"},
        {'niveau': 'Confirmé (4-7 ans)', 'brut': (48000, 58000, 72000),
         'region': "ARA : 48-62k ; IDF : 52-72k", 'variable': "Prime 8-12 %"},
        {'niveau': 'Senior (7-12 ans)', 'brut': (58000, 70000, 90000),
         'region': "IDF dominante ; ARA : 55-75k", 'variable': "Prime 10-15 %"},
        {'niveau': 'Expert / chef de mission', 'brut': (70000, 85000, 110000),
         'region': "IDF/Grandes métropoles", 'variable': "Prime 12-18 %"},
        {'niveau': 'Manager / associé cabinet', 'brut': (85000, 105000, 130000),
         'region': "IDF/Grandes métropoles", 'variable': "Intéressement, participation ; associé : dividendes"}],
    'sal_note': "Estimations croisées à partir des barèmes cabinets (Apec, Robert Half 2025) "
        "et offres observées ; l'audit GRC paie 5-15 % de moins que l'ingénierie sécurité au "
        "même niveau d'expérience, mais offre une meilleure stabilité et moins d'astreintes.",
    'progression': "Auditeur junior (0-2 ans) -> auditeur confirmé (2-5 ans, autonomie sur "
        "missions) -> chef de mission (5-8 ans, pilotage d'équipe et signature) -> manager ou "
        "RSSI/DPO (8-12 ans) -> associé de cabinet ou directeur risque (12+ ans, rare). "
        "Bifurcations fréquentes vers la conformité (DPO), le contrôle interne IT et la "
        "gouvernance. La voie technique pure (pentest, ingénierie) reste ouverte mais exige "
        "une remise à niveau technique volontaire.",
    'ia': {'auto': 55, 'recrut': 35, 'transfo': 60, 'creation': 40, 'levier': 55,
        'h2030': "L'IA automatisera la collecte de preuves, le mapping de conformité et les "
            "premiers jets de rapports ; l'auditeur se concentrera sur l'interprétation, les "
            "entretiens et la gestion des cas limites. Le nombre d'auditeurs devrait rester "
            "stable, porté par NIS2 et DORA.",
        'h2035': "Les outils d'audit assisté par IA réduiront le temps passé sur les tâches "
            "répétitives de 30-50 % ; le métier se recentre sur l'analyse de risques et la "
            "relation client. Risque de baisse des recrutements juniors si la productivité "
            "augmente plus vite que la demande.",
        'h2040': "L'audit de conformité de base sera largement assisté, voire automatisé pour "
            "les petits périmètres ; les auditeurs de haut niveau (secteurs régulés, "
            "souveraineté, IA Act) resteront recherchés. Nouveau champ : audit des systèmes "
            "d'IA (conformité AI Act).",
        'notes': "L'IA est ici un levier de productivité autant qu'une menace : la demande "
            "réglementaire (NIS2, DORA, AI Act) augmente la charge d'audit plus vite que "
            "l'IA ne réduit le temps par mission. Le score d'automatisation élevé porte sur "
            "les tâches documentaires, pas sur le jugement d'auditeur."},
    'probs': {'premier_emploi': "50-65 % avec un Bac+3/5 et une alternance ; 30-40 % sans "
        "alternance (marché GRC junior concurrentiel)",
        'confirme': "70-80 % à 5-7 ans pour ceux qui restent dans le métier",
        'seuils': {'2500': "Dès le poste d'auditeur junior (brut 40k => ~2 580 EUR net)",
            '3000': "Probable à 3-5 ans (brut 47-52k)",
            '4000': "Plausible à 7-10 ans (brut 62-70k)",
            '5000': "Rare avant 10-12 ans ; nécessite poste de manager ou indépendant"},
        'chomage': "Faible : 3-5 % (compétences transférables vers la conformité)",
        'formation': "Élevée : référentiels et réglementation évoluent sans cesse (NIS2, "
            "DORA, AI Act) ; veille continue obligatoire",
        'obsolescence': "Modérée : les référentiels changent, mais l'expérience d'audit "
            "reste valorisée ; risque plus élevé côté outils que côté méthode",
        'base': "Estimation raisonnée croisant ANSSI (offre GRC), barèmes Apec et dynamique "
            "réglementaire ; aucune statistique publique par métier n'existe."},
    'scenarios': {
        'defav': "Report des audits non obligatoires, concurrence des plateformes "
            "d'auto-évaluation ; salaires stables, moins de postes juniors.",
        'central': "NIS2 et DORA soutiennent la demande ; l'IA augmente la productivité mais "
            "la charge réglementaire absorbe le gain ; salaires +1-2 %/an réel.",
        'fav': "Montée en charge NIS2/DORA/AI Act plus rapide que prévu, pénurie d'auditeurs "
            "habilités ; salaires et honoraires en hausse, forte demande d'indépendants.",
        'bascule': "Moratoire ou allègement réglementaire (dérégulation européenne) ; "
            "réduction brutale des missions de conformité non obligatoires."}
}

M16_TECH_IT = {
    'id': 'technicien_it', 'nom': 'Technicien informatique et réseaux',
    'alt': "Technicien support, technicien d'exploitation, technicien réseau, helpdesk N1/N2, "
        "technicien micro-réseaux, technicien de proximité",
    'famille': 'Exploitation et support', 'acces': 'Accessible dès Bac Pro CIEL',
    'description': "Le technicien informatique et réseaux installe, maintient et dépanne les "
        "postes de travail, les équipements réseau, les imprimantes, la téléphonie et les "
        "services de premier niveau. C'est le métier le plus accessible directement après un "
        "Bac Pro CIEL, et le tremplin le plus courant vers l'administration, le SOC ou "
        "l'ingénierie. Il est souvent sous-estimé : les salaires y sont modestes mais "
        "l'expérience terrain y est irremplaçable.",
    'missions': [
        "Installer, configurer et dépanner postes de travail, périphériques et logiciels",
        "Administer le réseau local : switches, bornes Wi-Fi, câblage, VLAN de base",
        "Traiter les tickets de support N1, escalader les incidents complexes en N2",
        "Préparer et déployer des postes (imagerie, MDM/Intune, GPO)",
        "Assurer la maintenance préventive : sauvegardes, mises à jour, inventaire",
        "Accompagner et former les utilisateurs",
        "Participer aux projets : migrations, déploiements, ouvertures de sites",
        "Documenter les procédures et la base de connaissances"],
    'taches': "Pratique manuelle 55 %, diagnostic et réflexion 20 %, rédaction (tickets, "
        "procédures) 15 %, communication utilisateur 10 %. Très orienté terrain.",
    'outils': "Windows Server/Client, Active Directory, GPO, Intune/MDM ; Office 365, "
        "Exchange ; switches Cisco/HP, VLAN, TCP/IP, Wi-Fi ; GLPI, OTRS, ServiceNow ; "
        "VMware/Hyper-V (bases) ; PowerShell (débutant) ; outils de télémaintenance.",
    'difficulte': "Faible à moyenne à l'entrée : les fondamentaux du Bac Pro CIEL suffisent. "
        "La difficulté croît avec la diversité des environnements et l'exigence de "
        "polyvalence (réseau, système, sécurité, utilisateur).",
    'comp_req': [
        "Bases solides en réseaux TCP/IP, Ethernet, Wi-Fi",
        "Administration Windows (AD, GPO, déploiement)",
        "Diagnostic matériel et logiciel méthodique",
        "Communication avec des utilisateurs non techniques",
        "Rigueur documentaire (tickets, procédures)"],
    'comp_opt': [
        "Linux (Ubuntu Server, Debian) - très valorisé",
        "Virtualisation VMware/Hyper-V/Proxmox",
        "Scripting PowerShell/Bash",
        "Notions de cybersécurité (durcissement, sauvegardes, MFA)",
        "Certification CCNA ou CompTIA Network+"],
    'qualites': "Patience, service, méthode, autonomie sur le terrain, bonne humeur face aux "
        "utilisateurs stressés, capacité à gérer plusieurs tickets en parallèle.",
    'repartition': "Pratique 55 % / Réflexion 20 % / Rédaction 15 % / Communication 10 %",
    'autonomie': "Moyenne : procédures encadrées, escalade systématique au-delà du N1. "
        "Autonomie réelle en itinérance et en PME.",
    'equipe': "Souvent seul sur site ou en équipe de 2-5 techniciens ; lien étroit avec "
        "l'administrateur ou l'infogéreur.",
    'teletravail': "Faible : le métier est physique (postes, câblage, salles serveurs). "
        "Une part de support à distance existe (prise en main, helpdesk).",
    'horaires': "Journée standard en entreprise ; horaires élargis ou 3x8 en infogérance et "
        "datacenter ; astreintes possibles (week-end, nuit) avec majoration.",
    'urgences': "Fréquentes mais de faible gravité : pannes bloquantes pour les utilisateurs, "
        "rarement critiques pour l'entreprise. Pression de volume de tickets en helpdesk.",
    'avantages': [
        "Accessible immédiatement après le Bac Pro CIEL, sans études supplémentaires",
        "Demande constante partout en France, y compris autour d'Annonay (PME, collectivités, ESN locales)",
        "Expérience terrain très valorisée pour évoluer vers admin, SOC ou ingénierie",
        "Formation continue souvent financée par l'employeur (certifications constructeur)",
        "Peu de stress de responsabilité : les décisions critiques sont ailleurs"],
    'inconvenients': [
        "Salaires parmi les plus bas du secteur IT, surtout en début de carrière",
        "Tâches répétitives (tickets, réinstallations) et peu valorisées",
        "Peu de télétravail, déplacements fréquents",
        "Plafond de verre rapide si aucune montée en compétences n'est engagée",
        "Risque réel de rester bloqué en support 5-10 ans sans plan de progression"],
    'stress': "Faible à modéré : pression de volume en helpdesk, frustrations utilisateur, "
        "urgence permanente mais de faible gravité. Peu de stress de responsabilité.",
    'realite': "Le métier décrit dans les annonces (polyvalence, projets, évolution) est rare "
        "au quotidien : la réalité est souvent une file de tickets, des utilisateurs "
        "impatients et des procédures imposées. La différence se joue sur l'employeur : une "
        "PME où le technicien fait tout offre plus d'apprentissage mais moins de formation "
        "que la grande structure.",
    'parcours': [
        {'nom': "Entrée directe après Bac Pro CIEL",
         'desc': "Poste de technicien support/réseau en PME, collectivité ou ESN locale, "
             "avec montée en compétences sur le tas.",
         'duree': "0 an d'études supplémentaires",
         'difficulte': "Faible", 'selectivite': "Faible ; la concurrence vient des BTS/BUT en recherche d'alternance",
         'cout': "Néant (formation par l'employeur)",
         'financement': "Plan de développement des compétences, CPF",
         'prob': "60-75 % d'obtenir un premier poste dans les 6 mois (marché de masse)",
         'paliers': ["Technicien N1", "Technicien N2", "Administrateur (avec formation)"],
         'reorient': "Vers commercial IT, maintenance électronique, formation."},
        {'nom': "BTS CIEL ou SIO en alternance",
         'desc': "Consolidation du Bac Pro par un BTS en 2 ans, rémunéré, avec un premier "
             "véritable réseau professionnel.",
         'duree': "2 ans", 'difficulte': "Moyenne",
         'selectivite': "Faible à moyenne ; l'alternance est le vrai filtre (trouver un employeur)",
         'cout': "Néant pour l'apprenti (alternance)",
         'financement': "Contrat d'apprentissage (rémunération 53-100 % du SMIC selon âge)",
         'prob': "70-85 % d'obtenir un poste de technicien/admin junior à la sortie",
         'paliers': ["Apprenti", "Technicien N2", "Administrateur junior"],
         'reorient': "Vers réseaux télécoms, électronique embarquée, cybersécurité (BUT3 ou licence pro)."},
        {'nom': "Passerelle vers BUT3 ou licence pro puis ingénierie",
         'desc': "Après BTS ou 2-3 ans d'expérience, admission en BUT3, licence pro "
             "sécurité/réseaux, puis éventuellement master ou école en alternance.",
         'duree': "1-3 ans après le BTS", 'difficulte': "Moyenne à élevée",
         'selectivite': "Admission sur dossier ; places limitées en BUT3",
         'cout': "Public : ~600-3 000 EUR ; école en alternance : souvent gratuite pour l'apprenti",
         'financement': "Alternance, CPF, plan de formation employeur",
         'prob': "40-55 % d'atteindre un poste d'ingénieur ou d'administrateur confirmé",
         'paliers': ["Technicien", "Licence pro/BUT3", "Admin/ingénieur junior"],
         'reorient': "Très large : cybersécurité, cloud, réseaux, gestion de projet."}],
    'salaires': [
        {'niveau': 'Débutant (0-2 ans)', 'brut': (22000, 25000, 29000),
         'region': "ARA/Province : 22-27k ; IDF : 25-30k ; Hellowork 2025 : 22-25k junior",
         'variable': "Astreintes : +100-300 EUR/mois si concerné"},
        {'niveau': 'Junior (2-4 ans)', 'brut': (26000, 30000, 34000),
         'region': "ARA : 26-32k ; IDF : 29-35k", 'variable': "Prime annuelle 0-5 %"},
        {'niveau': 'Confirmé (4-7 ans)', 'brut': (30000, 35000, 40000),
         'region': "ARA : 30-38k ; IDF : 33-42k", 'variable': "Prime 5-10 %"},
        {'niveau': 'Senior (7-12 ans)', 'brut': (34000, 39000, 45000),
         'region': "ARA : 34-42k ; IDF : 38-48k", 'variable': "Prime 5-10 %"},
        {'niveau': 'Expert / responsable technique', 'brut': (38000, 44000, 52000),
         'region': "Grandes métropoles ; souvent après passage admin/responsable",
         'variable': "Prime 10 %"},
        {'niveau': 'Manager support/exploitation', 'brut': (42000, 50000, 60000),
         'region': "IDF/Grandes métropoles", 'variable': "Prime 10-15 %"}],
    'sal_note': "Chiffres proches des données observées (Hellowork 2025 : technicien IT junior "
        "22-25k brut ; moyenne nationale admin/technicien 40,6-43,5k). Le plafond est atteint "
        "vite : la progression salariale passe par le changement de métier (admin, SOC, "
        "ingénieur) plus que par l'ancienneté.",
    'progression': "Technicien N1 (0-2 ans) -> technicien N2 (2-4 ans, avec certifications "
        "CCNA/MS-500) -> administrateur systèmes et réseaux junior (4-6 ans, souvent en "
        "formation continue ou alternance) -> administrateur confirmé/ingénieur (7-12 ans) "
        "-> responsable exploitation (12+ ans). Sans montée en compétences, le plafond "
        "réaliste est technicien confirmé à 3 000-3 500 EUR net/mois après 10-15 ans.",
    'ia': {'auto': 65, 'recrut': 45, 'transfo': 65, 'creation': 30, 'levier': 50,
        'h2030': "L'assistance IA (diagnostic automatisé, agents de support, self-service "
            "utilisateur) réduira le volume de tickets N1 de 30-50 %. Le métier se "
            "déplacera vers le N2, la sécurité du poste de travail et le support de "
            "l'outillage IA lui-même.",
        'h2035': "Le support N1 sera largement automatisé ; le technicien restera nécessaire "
            "pour le physique (câblage, matériel, terrain) et pour les cas complexes. "
            "Baisse probable des effectifs N1, maintien voire hausse des profils N2/N3.",
        'h2040': "Le métier de technicien N1 pur sera très réduit ; les fonctions de "
            "proximité (déploiement, matériel, sécurité du poste) subsisteront. Les "
            "compétences réseau et sécurité resteront la clé de la pérennité.",
        'notes': "Le score d'automatisation élevé (65) porte sur le support à distance et le "
            "diagnostic, pas sur le travail physique. La meilleure protection est de monter "
            "vite vers l'administration et la sécurité."},
    'probs': {'premier_emploi': "60-75 % dans les 6 mois après Bac Pro (marché de masse, "
        "concurrence des BTS en alternance)",
        'confirme': "75-85 % à 5-7 ans (faible barrière d'entrée, forte attrition vers d'autres métiers)",
        'seuils': {'2500': "Rare avant 3-5 ans (brut 39-42k, souvent en IDF ou avec astreintes)",
            '3000': "Peu probable avant 7-10 ans sans changement de métier",
            '4000': "Très improbable dans ce métier ; nécessite évolution vers admin/ingénieur",
            '5000': "Quasi impossible en tant que technicien"},
        'chomage': "Modéré : 5-8 % (métier exposé à l'automatisation du support, mais "
            "compétences réutilisables partout)",
        'formation': "Modérée à élevée : les technologies évoluent, mais la base "
            "réseau/système est stable ; certifications à renouveler tous les 3-5 ans",
        'obsolescence': "Modérée : le matériel et les outils changent, les fondamentaux non",
        'base': "Chiffres proches des données observées (Hellowork, INSEE, France Travail) ; "
            "probabilités estimées à partir de la taille du marché et de la concurrence."},
    'scenarios': {
        'defav': "Automatisation du support plus rapide, externalisation vers des centres "
            "low-cost, baisse des salaires réels ; le métier reste mais se précarise.",
        'central': "Demande stable portée par le renouvellement technologique (IA, cloud, "
            "sécurité) ; salaires +0,5-1 %/an réel ; le N1 se réduit, le N2 progresse.",
        'fav': "Réindustrialisation et souveraineté numérique, besoin de techniciens de "
            "terrain ; pénurie de profils polyvalents, salaires en hausse dans les zones "
            "industrielles.",
        'bascule': "Généralisation d'agents IA de support autonomes dès 2028-2030 ; "
            "réduction brutale des postes N1, report de la demande sur la sécurité et le "
            "terrain."}
}
M17_GENDARME = {
    'id': 'gendarme_cyber', 'nom': 'Gendarme, spécialité cyber (militaire du rang puis sous-officier)',
    'alt': "Sous-officier de gendarmerie, enquêteur cyber, technicien enquêtes numériques, "
        "gendarme spécialisé cyber (C3N, ComCyberGend, STIG), OPJ cyber",
    'famille': 'Défense et sécurité publique', 'acces': "Concours sous-officier (bac + sélection) ; spécialisation cyber ensuite",
    'description': "Gendarme est d'abord un métier de militaire : missions de police de "
        "proximité, enquêtes, maintien de l'ordre. La spécialité cyber arrive ensuite : "
        "enquêtes sur les cyberdélinquances (escroqueries en ligne, cyberharcèlement, "
        "fraude aux moyens de paiement), saisie et exploitation de preuves numériques, "
        "appui technique aux unités. Les unités spécialisées (C3N à Pontoise, "
        "ComCyberGend, STIG) recrutent des militaires expérimentés, pas des débutants. "
        "C'est un métier à statut : solde selon grille indiciaire, sécurité de l'emploi, "
        "mobilité géographique obligatoire.",
    'missions': [
        "Missions générales de gendarmerie : patrouilles, enquêtes de proximité, secours",
        "Enquêtes sur les atteintes aux personnes et aux biens, y compris à composante numérique",
        "Traitement des plaintes pour escroquerie en ligne, cyberharcèlement, fraude en ligne",
        "Saisie, acquisition et exploitation de preuves numériques (téléphones, ordinateurs)",
        "Signalement et remontée des atteintes à la cybersécurité vers les unités spécialisées",
        "Dans les unités spécialisées : traçage d'auteurs, réquisitions, coopération internationale",
        "Sensibilisation du public (jeunes, personnes âgées) aux risques numériques"],
    'taches': "Pratique et terrain 40-70 % selon l'affectation, procédure et rédaction 20-30 % "
        "(procès-verbaux, réquisitions), coordination 10-20 %. Les unités cyber sont plus "
        "sédentaires et analytiques que les brigades de proximité.",
    'outils': "Outils d'enquête numériques (NT, X-Ways, Cellebrite selon habilitation), "
        "(procédure pénale, réquisitions, HTJ), PLA (plateforme d'analyse), systèmes "
        "d'information de la gendarmerie ; en unité spécialisée : outils d'analyse de "
        "journaux, de traçage de crypto-actifs et de coopération internationale.",
    'difficulte': "Moyenne : le concours de sous-officier est accessible (taux de réussite "
        "environ 1 sur 3-4), la formation initiale (12 mois à l'école de Châteaulin ou "
        "Montluçon) est exigeante militairement. La spécialisation cyber exige ensuite de la "
        "technique et de la procédure pénale.",
    'comp_req': [
        "Réussite du concours de sous-officier de gendarmerie (bac requis, épreuves écrites, sport, psychotechnique)",
        "Formation initiale de gendarme (12 mois)",
        "Rigueur procédurale (procédure pénale, chaîne de preuve numérique)",
        "Bases techniques numériques (le Bac Pro CIEL est un atout réel pour la spécialisation)",
        "Acceptation du statut militaire : disponibilité, mobilité, hiérarchie"],
    'comp_opt': [
        "Formation de technicien d'enquêtes numériques (TEC) puis OPJ",
        "Anglais (coopération internationale, C3N)",
        "Connaissances en crypto-actifs, réseaux, systèmes",
        "Licence (accès au concours OSC-S, voie officier)",
        "Permis de conduire (indispensable)"],
    'qualites': "Sens du service, sang-froid, discipline, équilibre personnel (horaires, "
        "mobilité), capacité à gérer des situations humaines difficiles, discrétion.",
    'repartition': "Brigade : terrain 60 % / procédure 25 % / coordination 15 %. Unité "
        "spécialisée : analyse 50 % / procédure 30 % / coordination 20 %.",
    'autonomie': "Encadrée : procédure militaire et pénale, hiérarchie forte. Autonomie "
        "réelle sur les enquêtes confiées une fois OPJ.",
    'equipe': "Toujours en équipe (brigade de 5-30 personnes) ; unités spécialisées plus "
        "larges. Cohésion militaire forte.",
    'teletravail': "Quasi nul : métier de présence et d'opérationnel.",
    'horaires': "Équipe alternante (matin/soir/nuit), week-end, jours fériés. Congés annuels "
        "(9 semaines) mais non choisis. Astreintes selon l'unité.",
    'urgences': "Constantes et parfois graves : interventions, urgences judiciaires, "
        "garde-à-vue. Stress opérationnel réel, notamment en unité spécialisée (contenus "
        "pénibles : pédopornographie, fraudes sur personnes vulnérables).",
    'avantages': [
        "Sécurité de l'emploi quasi totale (statut militaire)",
        "Solde + primes + logement de fonction (ou indemnité de logement) + couverture santé militaire",
        "Congés annuels : 9 semaines",
        "Pension militaire après service",
        "Formation continue gratuite et qualifiante (TEC, OPJ, cyber, C3N)",
        "Le Bac Pro CIEL est directement utile pour la spécialisation cyber"],
    'inconvenients': [
        "Mobilité géographique obligatoire (affectations partout en France et Outre-mer)",
        "Horaires alternants, week-end, nuits, jours fériés",
        "Solde de débutant modeste (~1 850-2 100 EUR net/mois en poste selon primes)",
        "Hiérarchie et discipline militaires : peu de liberté d'organisation",
        "Accès aux unités cyber après plusieurs années en brigade (pas d'entrée directe)",
        "Exposition à des contenus et situations pénibles en enquête cyber"],
    'stress': "Modéré à élevé : urgences, responsabilité pénale (OPJ), horaires, exposition à "
        "des situations humaines dures. Compensé par la cohésion d'équipe et le cadre.",
    'realite': "La réalité est d'abord celle d'un gendarme de brigade : patrouilles, plaintes, "
        "routière, secours. La part de cyber dans le travail d'un gendarme non spécialisé "
        "est limitée (réception de plaintes, premiers constats, saisies). Les unités "
        "spécialisées (C3N, ComCyberGend) sont des affectations convoitées, obtenues après "
        "plusieurs années, sur dossier et formation. Beaucoup de candidats découvrivent "
        "trop tard que le métier est militaire avant d'être technique.",
    'parcours': [
        {'nom': "Concours sous-officier de gendarmerie (voie directe)",
         'desc': "Concours externe ouvert aux titulaires du bac (ou bac pro) : épreuves "
             "écrites d'admissibilité, then épreuves d'admission (sport, entretien, "
             "psychotechnique). Formation initiale de 12 mois en école (GSO), puis "
             "affectation en brigade.",
         'duree': "12 mois de formation après réussite du concours",
         'difficulte': "Moyenne", 'selectivite': "Environ 1 admis pour 3-4 candidats (concours 2024-2025)",
         'cout': "Néant (rémunéré dès l'école)",
         'financement': "Rémunération d'élève gendarme",
         'prob': "70-80 % d'obtenir le métier de gendarme pour un candidat admis ; "
             "probabilité d'entrer aux concours incluses : 25-35 % par tentative",
         'paliers': ["Élève gendarme", "Gendarme (brigade)", "Gendarme TEC/OPJ",
             "Spécialisation cyber (unité régionale ou nationale)"],
         'reorient': "Vers police nationale (concours), sécurité privée, technicien IT après "
             "sortie ; l'expérience cyber militaire est très valorisée dans le civil."},
        {'nom': "Spécialisation cyber après 3-6 ans en brigade",
         'desc': "Formation de technicien d'enquêtes numériques (TEC), puis OPJ, puis "
             "candidature aux unités spécialisées (sections régionales d'enquêtes "
             "numériques, C3N, ComCyberGend) sur dossier.",
         'duree': "3-6 ans après l'entrée en brigade",
         'difficulte': "Moyenne à élevée (sur dossier, places limitées)",
         'selectivite': "Élevée : peu de postes, beaucoup de candidats motivés",
         'cout': "Néant (formation militaire)",
         'financement': "Néant (en service)",
         'prob': "20-35 % d'accéder à une unité spécialisée cyber à 5-8 ans de carrière",
         'paliers': ["Gendarme", "TEC", "OPJ", "Enquêteur cyber (section régionale ou C3N)"],
         'reorient': "Vers gendarmerie générale (routière, research), ou sortie vers des "
             "postes civils d'enquêteur interne, analyste fraudes, investigator."},
        {'nom': "Officier via OSC-S (licence requise)",
         'desc': "Concours sur titres pour officier sous contrat spécialité (OSC-S) avec "
             "licence, puis école des officiers, commandement et spécialisation possible "
             "vers la cyberdéfense.",
         'duree': "1-2 ans de formation après concours",
         'difficulte': "Élevée", 'selectivite': "Très sélectif (peu de postes)",
         'cout': "Néant", 'financement': "Rémunération d'élève officier",
         'prob': "10-20 % (sélectivité du concours et des places cyber)",
         'paliers': ["Élève officier", "Lieutenant", "Capitaine (spécialisation)"],
         'reorient': "Vers armée de terre, air, cyberdéfense ministérielle."}],
    'salaires': [
        {'niveau': "Élève gendarme (école, 12 mois)",
         'brut': (19200, 19200, 19200),
         'region': "National (grille indiciaire unique)",
         'variable': "Solde + indemnité de logement ; environ 1 205 EUR net/mois pour un GAV "
             "(gendarme adjoint volontaire), plus pour un élève SOE"},
        {'niveau': "Gendarme débutant (0-2 ans, catégorie C/D)",
         'brut': (22200, 23400, 25000),
         'region': "National ; majoration Outre-mer et zones",
         'variable': "Solde brute ~1 605 EUR (indice majoré 375-382, point d'indice 4,92278 EUR) "
             "+ primes (GIPA, activités) + logement de fonction ou indemnité ; "
             "net en poste ~1 850-2 100 EUR/mois selon affectation et primes"},
        {'niveau': "Gendarme confirmé (4-8 ans, échelons 5-8)",
         'brut': (25000, 27000, 30000),
         'region': "National",
         'variable': "Solde ~1 800-2 100 EUR brute + primes ; net en poste ~2 100-2 400 EUR/mois"},
        {'niveau': "Adjudant (8-15 ans)",
         'brut': (28000, 31000, 34000),
         'region': "National",
         'variable': "Solde ~1 977-2 357 EUR net/mois selon échelon et primes"},
        {'niveau': "Major / adjudant-chef (15-25 ans)",
         'brut': (32000, 36000, 40000),
         'region': "National",
         'variable': "Net ~2 400-2 800 EUR/mois + primes et logement"},
        {'niveau': "Officier (sortie d'école puis carrière)",
         'brut': (36000, 42000, 55000),
         'region': "National",
         'variable': "Lieutenant en sortie d'école : ~2 843 EUR net/mois ; capitaine : "
             "~3 100-3 500 EUR net ; commandant et au-delà : 3 500-4 500+ EUR net"}],
    'sal_note': "Grilles indiciaires officielles (solde brute, point d'indice 4,92278 EUR au "
        "1er janvier 2025) ; le net en poste dépend des primes (ISSP, ICM, GIPA), de "
        "l'indemnité de logement et de la zone d'affectation. Ne pas comparer directement "
        "au privé : le logement, la sécurité d'emploi et la pension compensent partiellement "
        "un solde inférieur. Chiffres officiels gendarmerie/SGA 2025.",
    'progression': "Élève (12 mois) -> gendarme en brigade (0-4 ans, échelons) -> TEC puis "
        "OPJ (4-8 ans, concours ou examen professionnel) -> adjudant (8-15 ans, examen "
        "professionnel ou concours) -> major (15-25 ans) -> officier (par concours interne "
        "ou fin de carrière). La spécialité cyber est une branche horizontale : elle ne "
        "change pas le grade mais l'affectation et les primes possibles (ICM). "
        "Différence technique/manager : le gendarme technique (TEC, expert) peut rester "
        "spécialiste sans commander ; l'adjudant et l'officier encadrent.",
    'ia': {'auto': 25, 'recrut': 15, 'transfo': 45, 'creation': 50, 'levier': 55,
        'h2030': "L'IA transformera l'enquête (tri de plaintes, analyse de contenus, "
            "détection de fraudes) mais pas le métier : la police reste une tâche humaine, "
            "légale et physique. La demande de spécialistes cyber militaires augmentera "
            "(LPM 2024-2030 : +953 ETP cyber dans les armées).",
        'h2035': "Les outils d'analyse assistée par IA seront généralisés dans les enquêtes "
            "numériques ; les effectifs de proximité resteront stables ; la spécialité "
            "cyber grossira et se professionnalisa (filière cyber structurée).",
        'h2040': "Les unités cyber seront plus nombreuses et plus techniques ; le gendarme "
            "de proximité utilisera l'IA au quotidien ; le métier restera un métier de "
            "présence humaine, très résistant à l'automatisation.",
        'notes': "Métier parmi les plus résistants à l'IA (présence, autorité publique, "
            "procédure pénale humaine). Le risque principal n'est pas technologique mais "
            "budgétaire et statutaire (réformes des effectifs, des retraites)."},
    'probs': {'premier_emploi': "25-35 % par tentative au concours (taux de réussite "
            "observés) ; 70-80 % pour un candidat admis d'atteindre le métier",
        'confirme': "85-95 % (progression statutaire quasi automatique)",
        'seuils': {'2500': "Atteint dès le début de carrière en poste (~1 850-2 100 EUR net "
            "selon primes ; 2 500 EUR net vers 4-8 ans en adjudant avec primes)",
            '3000': "Vers 8-15 ans (adjudant-chef/major avec primes et logement) ou officier",
            '4000': "Officier supérieur seulement (rare, 20+ ans)",
            '5000': "Quasi jamais dans la carrière d'un sous-officier"},
        'chomage': "Quasi nul (statut militaire)",
        'formation': "Élevée : formations continues imposées, montée en grade obligatoire "
            "pour progresser",
        'obsolescence': "Faible : la procédure et le métier sont stables ; la technique "
            "cyber évolue mais la formation est fournie",
        'base': "Grilles indiciaires officielles (SGA/gendarmerie 2025), taux de réussite "
            "aux concours publiés ; probabilités de spécialisation estimées."},
    'scenarios': {
        'defav': "Gel du point d'indice, réduction des effectifs, baisse du pouvoir "
            "d'achat ; départs vers le privé, difficultés de recrutement.",
        'central': "LPM 2024-2030 maintenue : recrutements cyber soutenus (+953 ETP), "
            "solde indexé sur l'inflation avec rattrapages ponctuels.",
        'fav': "Priorité sécurité et cyberdéfense renforcée : effectifs et primes en "
            "hausse, filière cyber structurée, meilleures évolutions de carrière.",
        'bascule': "Réforme statutaire majeure ou contrainte budgétaire sévère ; "
            "démotivation, départs, baisse d'attractivité des spécialisations."}
}
M18_RSSI = {
    'id': 'rssi', 'nom': "RSSI - Responsable de la sécurité des systèmes d'information",
    'alt': "CISO, responsable cybersécurité, directeur sécurité SI, RSSI group, CISO adjoint",
    'famille': 'Gouvernance et direction', 'acces': "Bac+5 + 10-15 ans d'expérience (poste d'expérience, pas d'entrée)",
    'description': "Le RSSI définit et pilote la politique de sécurité des systèmes "
        "d'information d'une organisation : analyse de risques, budget, conformité, "
        "sensibilisation, gestion de crise, relations avec la direction et les "
        "régulateurs. C'est un poste de cadre dirigeant technique : la moitié du travail "
        "est de la communication, de l'arbitrage budgétaire et du management, l'autre "
        "moitié de la maîtrise technique et réglementaire. Le métier est très demandé "
        "(obligation de RSSI dans plusieurs secteurs régulés, NIS2) et parmi les mieux "
        "payés de la filière, mais inaccessible en début de carrière.",
    'missions': [
        "Définir la politique de sécurité du SI et la faire adopter par la direction générale",
        "Piloter le budget sécurité, les projets et les équipes (interne et prestataires)",
        "Conduire les analyses de risques globales (EBIOS RM) et prioriser les investissements",
        "Assurer la conformité réglementaire (NIS2, DORA, RGPD, obligations sectorielles)",
        "Gérer les incidents majeurs et piloter les crises cyber",
        "Sensibiliser les directions et les collaborateurs (culture sécurité)",
        "Négocier avec les assureurs cyber, les auditeurs, les clients et les régulateurs",
        "Suivre les menaces et arbitrer entre protection, détection et réponse"],
    'taches': "Réunions et communication 35 %, réflexion et arbitrage 25 %, rédaction "
        "(politiques, comités, reporting) 20 %, pilotage technique 20 %. Le RSSI passe plus "
        "de temps à convaincre qu'à configurer.",
    'outils': "Référentiels (ISO 27001, NIST CSF, EBIOS RM, ANSSI) ; GRC ; SIEM/SOC (suivi "
        "des indicateurs) ; outils de gestion de projet ; tableaux de bord risques ; "
        "connaissance large du paysage technique (cloud, réseau, AD, OT) sans être "
        "spécialiste de chaque domaine.",
    'difficulte': "Élevée sur toute la ligne : technique large, réglementaire dense, "
        "management, communication à des non-techniques, gestion de crise. Exige 10-15 ans "
        "d'expérience cumulée.",
    'comp_req': [
        "10-15 ans d'expérience en sécurité (SOC, ingénierie, audit, consultant)",
        "Maîtrise des référentiels et de la réglementation (NIS2, DORA, RGPD, ISO 27001)",
        "Analyse de risques et budgétisation",
        "Management d'équipes techniques et de prestataires",
        "Communication à la direction générale et aux métiers"],
    'comp_opt': [
        "CISSP, CISM, ISO 27001 Lead Implementer",
        "Expérience sectorielle régulée (banque, santé, industrie, énergie)",
        "Anglais courant (groupes internationaux)",
        "Connaissance OT/ICS et cloud",
        "Expérience de gestion de crise réelle"],
    'qualites': "Leadership, pédagogie, sang-froid en crise, diplomatie, capacité à dire "
        "non, vision à long terme, résistance au stress et à la solitude du rôle.",
    'repartition': "Réunions 35 % / Réflexion 25 % / Rédaction 20 % / Pilotage 20 %",
    'autonomie': "Très forte sur le périmètre sécurité, sous autorité de la direction "
        "générale (DSI, DG, comité exécutif selon les organisations).",
    'equipe': "Encadre une équipe sécurité (2-30 personnes selon taille) et pilote des "
        "prestataires ; très transversal (DSI, métiers, juridique, achats).",
    'teletravail': "Élevé selon les organisations (2-4 jours), mais présence exigée en "
        "période de crise et pour les comités.",
    'horaires': "Journée standard théorique ; réunions tôt/tard, astreinte de niveau 3, "
        "disponibilité en crise (incidents majeurs, week-end).",
    'urgences': "Rares mais intenses : incident majeur, crise de rançongiciel, fuite de "
        "données. Dans ces moments, le RSSI est en première ligne, y compris la nuit et le "
        "week-end.",
    'avantages': [
        "Parmi les salaires les plus élevés de la filière (médiane Apec 2025 : 60 kEUR pour les cadres sécurité, jusqu'à 99 kEUR pour les 20 % supérieurs)",
        "Demande structurelle (NIS2, DORA, obligations sectorielles)",
        "Poste stratégique, visibilité direction, évolution vers DSI ou direction des risques",
        "Fort levier d'indépendance en fin de carrière (RSSI à temps partagé, consultant)",
        "Métier très résistant à l'IA (responsabilité, arbitrage, crise)"],
    'inconvenients': [
        "Inaccessible avant 10-15 ans d'expérience",
        "Responsabilité personnelle forte (obligation de moyens et parfois de résultats)",
        "Solitude du rôle : peu de pairs, pression de la direction et des techniciens",
        "Exposition en cas d'incident majeur (licenciements possibles après crise)",
        "Charge mentale élevée, astreinte de fait permanente"],
    'stress': "Élevé et permanent : responsabilité, arbitrages budgétaires, menace réelle, "
        "gestion de crise. L'Observatoire ANSSI 2025 note qu'un quart des professionnels "
        "envisage de quitter le métier, souvent pour ces raisons.",
    'realite': "Le RSSI des annonces est un stratège équilibré ; le RSSI réel est souvent un "
        "ingénieur sécurité promu malgré lui, seul face à un budget insuffisant, une DSI "
        "concurrente et des directions qui découvrent la sécurité après un incident. La "
        "réalité dépend énormément de la taille et de la culture de l'organisation : RSSI "
        "d'une PME (seul, budget minimal, très large) et RSSI de groupe (équipe, budget, "
        "spécialisation) sont deux métiers différents.",
    'parcours': [
        {'nom': "Voie technique longue (SOC/ingénierie -> RSSI)",
         'desc': "Bac+5, entrée en SOC ou ingénierie sécurité, montée en compétences, "
             "puis chef de projet sécurité, puis RSSI adjoint, puis RSSI (souvent dans "
             "une organisation de taille moyenne).",
         'duree': "12-15 ans", 'difficulte': "Élevée",
         'selectivite': "Poste d'expérience : la sélection se fait sur le parcours réel",
         'cout': "Coût du Bac+5 (public ou alternance)",
         'financement': "Alternance, plan de formation employeur, CPF",
         'prob': "15-25 % d'atteindre un poste de RSSI (beaucoup s'arrêtent avant, par "
             "choix ou par manque d'opportunités)",
         'paliers': ["Analyste/ingénieur", "Chef de projet sécurité", "RSSI adjoint", "RSSI"],
         'reorient': "Vers consultant sécurité, DSI, directeur des risques, indépendant."},
        {'nom': "Voie audit/GRC -> RSSI",
         'desc': "Entrée par l'audit ou la conformité, montée vers chef de mission puis "
             "responsable risque, puis RSSI dans une organisation régulée.",
         'duree': "10-14 ans", 'difficulte': "Élevée",
         'selectivite': "Élevée ; les cabinets Big Four sont un vivier reconnu",
         'cout': "Coût du Bac+5",
         'financement': "Alternance",
         'prob': "20-30 % (voie classique et reconnue)",
         'paliers': ["Auditeur junior", "Chef de mission", "Responsable risque", "RSSI"],
         'reorient': "Vers DPO, contrôle interne, direction des risques."},
        {'nom': "RSSI à temps partagé / indépendant",
         'desc': "Après une carrière de RSSI salarié ou de consultant confirmé, exercer "
             "comme RSSI externalisé pour plusieurs PME/ETI (obligations NIS2).",
         'duree': "Après 10-15 ans", 'difficulte': "Élevée (commercialisation difficile)",
         'selectivite': "Dépend du réseau et de la réputation",
         'cout': "Néant (statut micro-entrepreneur ou société)",
         'financement': "ACRE possible à la création",
         'prob': "30-45 % de vivre durablement de cette activité (marché réel, dépend de "
             "la prospection)",
         'paliers': ["Consultant", "RSSI partagé 2-3 clients", "Portefeuille stable"],
         'reorient': "Retour au salariat facile (demande forte)."}],
    'salaires': [
        {'niveau': "N/A (poste d'expérience ; voir ingénieur/consultant pour 0-7 ans)",
         'brut': (0, 0, 0),
         'region': "N/A", 'variable': "N/A"},
        {'niveau': "RSSI adjoint / responsable sécurité (7-12 ans)",
         'brut': (65000, 78000, 95000),
         'region': "ARA : 60-80k ; IDF : 70-95k",
         'variable': "Prime 10-20 % ; véhicule parfois"},
        {'niveau': "RSSI PME/ETI (10-15 ans)",
         'brut': (75000, 90000, 115000),
         'region': "ARA : 70-95k ; IDF : 80-115k",
         'variable': "Prime 10-20 % ; intéressement"},
        {'niveau': "RSSI grand groupe (12-20 ans)",
         'brut': (95000, 120000, 150000),
         'region': "IDF/Grandes métropoles",
         'variable': "Bonus 15-30 % ; actions, LDD"},
        {'niveau': "RSSI secteur régulé / CISO groupe international",
         'brut': (120000, 150000, 170000),
         'region': "IDF ; grandes métropoles",
         'variable': "Bonus 20-40 % ; actions"},
        {'niveau': "RSSI indépendant (temps partagé)",
         'brut': (100000, 140000, 170000),
         'region': "National (déplacements clients)",
         'variable': "TJM 1 200-1 800 EUR ; CA brut, pas un salaire : cotisations ~24,6 %, "
             "frais et jours non travaillés à déduire ; revenu net typique 60-110 kEUR/an"}],
    'sal_note': "Chiffres cohérents avec Apec 2025 (médiane cadre sécurité 60 kEUR, 80 % "
        "entre 43 et 99 kEUR) et offres observées pour les postes RSSI. Les niveaux 1 "
        "(débutant) n'existent pas pour ce métier : c'est un poste d'expérience. Le "
        "chiffre d'affaires d'un RSSI indépendant n'est pas un salaire (cotisations, "
        "frais, jours non facturés).",
    'progression': "Ingénieur/analyste sécurité (0-5 ans) -> chef de projet sécurité ou "
        "consultant confirmé (5-10 ans) -> RSSI adjoint ou responsable sécurité (8-12 ans) "
        "-> RSSI PME/ETI (10-15 ans) -> RSSI grand groupe ou CISO (15-20 ans, rare) -> "
        "DSI, directeur des risques, consultant indépendant (20+ ans). La voie technique "
        "pure s'arrête à architecte ; au-delà, c'est de la gouvernance. Le passage au "
        "management est presque irréversible dans les grandes organisations.",
    'ia': {'auto': 10, 'recrut': 10, 'transfo': 35, 'creation': 45, 'levier': 70,
        'h2030': "L'IA automatisera la remontée d'indicateurs, la détection et une partie "
            "de l'analyse de risques ; le RSSI arbitrera plus vite avec de meilleurs "
            "tableaux de bord. Le poste est renforcé par NIS2 et par l'obligation de "
            "gouvernance humaine des systèmes d'IA.",
        'h2035': "Les SOC et l'analyse de risques seront largement assistés par IA ; le "
            "rôle de RSSI se recentre sur la gouvernance de l'IA elle-même (AI Act, "
            "risques liés aux modèles), sur la crise et sur la relation avec les "
            "régulateurs. Salaires en hausse pour les profils capables d'arbitrer entre "
            "sécurité classique et risques IA.",
        'h2040': "Le RSSI deviendra probablement un responsable des risques numériques et "
            "IA, couvrant sécurité classique, risques des modèles et conformité. Métier "
            "parmi les plus résistants : la responsabilité reste humaine.",
        'notes': "Scores faibles en automatisation et en risque de recrutement : la "
            "demande est portée par la réglementation et la responsabilité humaine. "
            "Le levier (70) est parmi les plus élevés : un RSSI outillé par l'IA "
            "couvre plus de périmètre avec la même équipe."},
    'probs': {'premier_emploi': "N/A (poste d'expérience ; voir ingénieur sécurité, "
            "consultant, auditeur pour l'entrée dans la filière)",
        'confirme': "N/A ; probabilité d'atteindre un poste de RSSI après 10-15 ans : "
            "15-30 % selon la voie (estimation raisonnée, aucune statistique publique)",
        'seuils': {'2500': "Automatique dès l'entrée dans la filière sécurité (postes à "
            "40 kEUR brut et plus)",
            '3000': "Automatique à 3-5 ans",
            '4000': "Probable à 7-10 ans (responsable sécurité, RSSI PME)",
            '5000': "Probable à 10-15 ans (RSSI, architecte senior, consultant indépendant)"},
        'chomage': "Très faible : 1-3 % (pénurie de profils expérimentés)",
        'formation': "Élevée : réglementation, menaces, technologies ; veille et formation "
            "continue permanentes",
        'obsolescence': "Faible : l'expérience de gouvernance et de crise se cumule",
        'base': "Estimation raisonnée à partir d'Apec 2025, ANSSI 2025 et du marché "
            "observé ; aucune statistique publique sur les trajectoires RSSI."},
    'scenarios': {
        'defav': "Ralentissement réglementaire, arbitrages budgétaires défavorables ; "
            "postes de RSSI consolidés dans des périmètres plus larges (risque+qualité), "
            "salaires stables.",
        'central': "NIS2 et DORA créent des centaines de postes de RSSI (obligations) ; "
            "salaires +2-3 %/an réel sur les profils expérimentés.",
        'fav': "Vague de conformité NIS2/DORA/AI Act, pénurie de RSSI expérimentés ; "
            "salaires et TJM en forte hausse, essor du temps partagé.",
        'bascule': "Consolidation des rôles (RSSI+DPO+risques en un poste) dans les PME ; "
            "marché du temps partagé saturé par des profils peu qualifiés."}
}

METIERS_C = [M13_ML, M14_DEVSECOPS, M15_AUDITEUR, M16_TECH_IT, M17_GENDARME, M18_RSSI]
A1_TELECOM = {
    'id': 'technicien_telecom', 'nom': 'Technicien télécoms et fibre optique',
    'alt': "Technicien FTTH, technicien déploiement télécoms, câbleur réseau, technicien HLO",
    'famille': 'Réseaux et infrastructures', 'acces': 'Accessible dès Bac Pro CIEL (voie pro)',
    'description': "Déploiement et maintenance des réseaux de télécommunications : fibre "
        "optique jusqu'à l'abonné (FTTH), infrastructures mobiles, réseaux d'entreprises. "
        "Métier de terrain, très demandé avec le plan France Très Haut Débit et le "
        "renouvellement des réseaux. Point d'entrée rapide, salaires modestes mais "
        "expérience réseau concrète.",
    'missions': [
        "Raccorder les abonnés en fibre optique (soudures, mesures optiques)",
        "Installer et maintenir les équipements actifs (ONT, box, switches)",
        "Diagnostiquer les pannes de liaison, mesurer l'atténuation (OTDR)",
        "Intervenir sur les infrastructures (boîtiers, chambres, câbles)",
        "Documenter les interventions et respecter les règles de sécurité (travaux en hauteur, GN1/GN2)"],
    'salaires': [
        {'niveau': 'Débutant (0-2 ans)', 'brut': (22000, 26000, 30000),
         'region': "ARA : 22-28k ; IDF : 25-32k", 'variable': "Paniers, déplacements, primes de chantier"},
        {'niveau': 'Confirmé (4-7 ans)', 'brut': (28000, 33000, 38000),
         'region': "National", 'variable': "Astreintes possibles"},
        {'niveau': "Chef d'équipe / conducteur travaux", 'brut': (34000, 40000, 47000),
         'region': "National", 'variable': "Prime de chantier"}],
    'ia': {'auto': 30, 'transfo': 30, 'levier': 30,
        'note': "Travail physique peu automatisable à 10 ans ; la demande suit les "
            "déploiements, pas l'IA. Risque principal : cycles d'investissement télécom."},
    'pourquoi': "Embauche rapide et locale (sous-traitants partout en ARA), porte d'entrée "
        "vers les réseaux d'entreprise, peu de concurrence des diplômés.",
    'garde_fous': "Salaires plafonnés, travail physique, dépendance aux cycles de "
        "déploiement et à la sous-traitance en cascade."}

A2_ELEC_EMB = {
    'id': 'electronicien_embarque', 'nom': "Technicien/ingénieur électronique embarquée et IoT",
    'alt': "Technicien électronicien, développeur embarqué, intégrateur IoT, testeur matériel",
    'famille': 'Électronique et systèmes embarqués', 'acces': "BTS/BUT accessible depuis Bac Pro CIEL (l'électronique du CIEL est l'atout)",
    'description': "Conception, prototypage, test et maintenance de cartes électroniques et "
        "d'objets connectés : microcontrôleurs, capteurs, firmware, protocoles radio. "
        "Métier qui exploite directement la partie électronique du Bac Pro CIEL, souvent "
        "délaissée par les candidats de l'informatique pure. La sécurité des objets "
        "connectés (IoT) est une spécialité en croissance (Cyber Resilience Act).",
    'missions': [
        "Développer et tester du firmware (C/C++, MicroPython)",
        "Concevoir et router des cartes (KiCad, Altium) côté technicien : assembler, mesurer, déboguer",
        "Intégrer capteurs, bus (I2C, SPI, UART), modules radio (LoRa, BLE, Wi-Fi)",
        "Tester la conformité et la sécurité des équipements (CRA, CE)",
        "Industrialiser : tests en série, bancs de test automatisés"],
    'salaires': [
        {'niveau': 'Débutant (0-2 ans)', 'brut': (24000, 28000, 33000),
         'region': "ARA (Grenoble, Lyon, Clermont) : 24-32k", 'variable': "Prime 13e mois fréquent"},
        {'niveau': 'Confirmé (4-7 ans)', 'brut': (33000, 40000, 48000),
         'region': "ARA/IDF", 'variable': "Prime, intéressement"},
        {'niveau': 'Ingénieur confirmé (7-12 ans)', 'brut': (45000, 55000, 70000),
         'region': "ARA/IDF", 'variable': "Prime 10 %"}],
    'ia': {'auto': 35, 'transfo': 55, 'levier': 55,
        'note': "L'IA assiste la génération de code embarqué et les bancs de test ; le "
            "matériel et l'intégration restent humains. Le CRA (exigences de sécurité IoT "
            "obligatoires) crée une demande de profils double électronique+sécurité."},
    'pourquoi': "Double compétence électronique+informatique rare, industrie forte en ARA "
        "(électronique, objets connectés, industrie 4.0), évolutions vers l'ingénierie ou "
        "la sécurité matérielle.",
    'garde_fous': "Salaires de départ inférieurs au logiciel ; secteurs cycliques "
        "(automobile, grand public) ; nécessite souvent un BUT/BTS GEII ou équivalent."}

A3_CTI = {
    'id': 'analyste_cti', 'nom': "Analyste en renseignement sur la menace (Threat Intelligence)",
    'alt': "Analyste CTI, analyste cyberrenseignement, threat analyst, analyste OSINT",
    'famille': 'Détection et analyse', 'acces': "Bac+3/5, souvent après une première expérience en SOC",
    'description': "L'analyste CTI collecte, analyse et diffuse des informations sur les "
        "menaces : groupes d'attaquants, vulnérabilités, campagnes, fuites de données. Il "
        "produit des rapports qui orientent la détection (SOC) et la stratégie de "
        "défense. Métier d'analyse et de rédaction, à l'interface entre technique et "
        "stratégique, en croissance dans les grands SOC et les éditeurs (CERT, éditeurs "
        "de threat intel).",
    'missions': [
        "Collecter et analyser les indicateurs de compromission (IoC) et les rapports de menaces",
        "Suivre les groupes d'attaquants, leurs outils et leurs cibles (MITRE ATT&CK)",
        "Produire des notes de menace adaptées aux destinataires (technique, direction)",
        "Alimenter les règles de détection du SOC et les priorités de correction",
        "Surveiller les fuites de données et les réseaux criminels (OSINT, dark web)"],
    'salaires': [
        {'niveau': 'Débutant (via SOC, 0-2 ans)', 'brut': (34000, 40000, 46000),
         'region': "ARA : 34-42k ; IDF : 38-48k", 'variable': "Prime 5-10 %"},
        {'niveau': 'Confirmé (4-7 ans)', 'brut': (46000, 55000, 68000),
         'region': "IDF dominante ; remote fréquent", 'variable': "Prime 8-12 %"},
        {'niveau': 'Senior / responsable CTI', 'brut': (60000, 75000, 95000),
         'region': "IDF/remote", 'variable': "Prime 10-15 %"}],
    'ia': {'auto': 45, 'transfo': 65, 'creation': 60, 'levier': 75,
        'note': "L'IA transforme déjà le métier : tri automatique des alertes, "
            "synthèse des rapports, déduplication d'IoC. Les analystes qui maîtrisent "
            "l'IA gagnent en productivité ; le tri brut recrute moins. Bon métier "
            "hybride IA+cyber pour un profil curieux et rédacteur."},
    'pourquoi': "Métier hybride technique/analyse, moins d'astreintes que le SOC L1, forte "
        "croissance des équipes CTI, valorise l'anglais et la rédaction.",
    'garde_fous': "Rare en poste d'entrée directe (passe par le SOC) ; forte concurrence "
        "sur les postes confirmés ; demande concentrée dans les grandes structures."}

A4_IAM = {
    'id': 'ingenieur_iam', 'nom': "Ingénieur gestion des identités et des accès (IAM)",
    'alt': "Ingénieur IAM/IGA, consultant identity, administrateur AD/Entra ID, ingénieur PAM",
    'famille': 'Ingénierie sécurité', 'acces': "Bac+3/5 ; accessible aussi par l'exploitation (admin sys)",
    'description': "L'ingénieur IAM gère le cycle de vie des identités : qui accède à quoi, "
        "quand, avec quelles règles. Il met en oeuvre les annuaires (Active Directory, "
        "Entra ID), les MFA, le SSO, la gestion des privilèges (PAM) et les projets de "
        "conformité des accès. Métier très demandé (projet obligatoire dans presque "
        "toutes les organisations), moins médiatisé que le pentest, marché junior "
        "classé neutre à favorable (Zeroday 2025).",
    'missions': [
        "Administrer les annuaires (AD, Entra ID, LDAP) et la fédération d'identités (SAML, OIDC)",
        "Déployer MFA, SSO et accès conditionnels",
        "Mettre en oeuvre des solutions IGA (provisioning, revues d'accès, réconciliation RH)",
        "Gérer les accès privilégiés (PAM : CyberArk, Delinea) et les comptes à risque",
        "Traiter les demandes d'accès, les audits et les re-certifications",
        "Automatiser les workflows d'identités (scripts, API)"],
    'salaires': [
        {'niveau': 'Débutant (0-2 ans)', 'brut': (33000, 38000, 44000),
         'region': "ARA : 33-40k ; IDF : 36-46k", 'variable': "Prime 5-8 %"},
        {'niveau': 'Confirmé (4-7 ans)', 'brut': (42000, 50000, 62000),
         'region': "ARA/IDF", 'variable': "Prime 8-12 %"},
        {'niveau': 'Expert / architecte IAM', 'brut': (58000, 72000, 90000),
         'region': "IDF/remote", 'variable': "Prime 10-15 % ; TJM indépendant 550-800 EUR"}],
    'ia': {'auto': 50, 'transfo': 60, 'creation': 40, 'levier': 60,
        'note': "L'IA automatisera les revues d'accès et le provisioning ; la conception "
            "des modèles d'identités et la gestion des cas complexes restent humaines. "
            "Métier stable car les projets IAM sont longs et réglementaires."},
    'pourquoi': "Demande constante et réglementaire, moins saturé que le pentest, "
        "accessible depuis l'administration systèmes (voie réaliste depuis Bac Pro CIEL "
        "+ exp.), compétence transférable partout.",
    'garde_fous': "Travail parfois perçu comme répétitif (tickets d'accès) selon "
        "l'organisation ; peu de postes juniors dans les petites structures."}
A5_FORMATEUR = {
    'id': 'formateur_cyber', 'nom': "Formateur / ingénieur pédagogique cybersécurité",
    'alt': "Formateur technique, formateur CFA, ingénieur pédagogique, formateur certifié (OSCP, CISCO)",
    'famille': 'Formation', 'acces': "Bac+3 + expérience technique (on ne débute pas formateur en cybersécurité)",
    'description': "Le formateur cybersécurité enseigne les compétences techniques : en "
        "CFA/BTS/BUT, en organisme de formation continue, en entreprise ou pour des "
        "éditeurs de certifications. Il conçoit les supports, anime des ateliers "
        "pratiques (labs, cyber-range) et évalue. Métier de seconde carrière : la "
        "règle implicite du marché est d'avoir exercé 5+ ans en production avant de "
        "transmettre. Avantage majeur : très peu d'astreintes, forte stabilité, "
        "télétravail partiel.",
    'missions': [
        "Concevoir modules, supports et labs pratiques (cyber-range, plateformes type TryHackMe)",
        "Animer des formations techniques (réseaux, sécurité, certifications)",
        "Évaluer les apprenants et ajuster la pédagogie",
        "Maintenir ses certifications pour valider les cursus (statut d'instructeur agréé)",
        "Veille technologique et mise à jour des contenus"],
    'salaires': [
        {'niveau': 'Formateur (après 5+ ans de terrain)', 'brut': (32000, 38000, 45000),
         'region': "ARA : 32-42k ; IDF/CFA privés : 35-48k", 'variable': "Heures supplémentaires, primes de résultats"},
        {'niveau': 'Formateur expert / référent', 'brut': (42000, 50000, 60000),
         'region': "National", 'variable': "Prime 8-12 %"},
        {'niveau': "Indépendant (cours et conseil)", 'brut': (45000, 65000, 90000),
         'region': "National", 'variable': "CA brut ; TJM 400-800 EUR ; revenu net typique 35-60 kEUR/an"}],
    'ia': {'auto': 50, 'transfo': 70, 'creation': 40, 'levier': 60,
        'note': "L'IA produira des contenus et des tuteurs adaptatifs ; la présence "
            "humaine, l'encadrement des labs et l'évaluation resteront demandés. Le "
            "rôle évolue vers le coaching et la conception de parcours."},
    'pourquoi': "Stabilité, horaires réguliers, pas d'astreinte, métier de fin de parcours "
        "complémentaire (double casquette production+formation) plutôt qu'objectif initial.",
    'garde_fous': "Salaires inférieurs à la production ; statuts précaires fréquents en "
        "organismes privés (vacataires) ; impossible d'y entrer sans expérience."}

A6_IOT_PENTEST = {
    'id': 'pentest_hardware', 'nom': "Pentester matériel, IoT et systèmes embarqués",
    'alt': "Hardware pentester, analyste IoT security, chercheur en sécurité embarquée",
    'famille': 'Attaque et test', 'acces': "Bac+4/5 ou profil autodidacte rare ; très niche",
    'description': "Teste la sécurité des objets connectés et du matériel : extraction de "
        "firmware, analyse de puces (UART, JTAG, SPI), attaques par canal auxiliaire, "
        "reverse engineering de composants. Niche très étroite mais en croissance avec "
        "le Cyber Resilience Act (exigences de sécurité des produits avec éléments "
        "numériques). Combine l'électronique du Bac Pro CIEL avec la sécurité : "
        "profil double extrêmement rare sur le marché.",
    'missions': [
        "Extraire et analyser des firmwares (binwalk, Ghidra, IDA)",
        "Identifier et exploiter les interfaces de debug (UART, JTAG, SWD)",
        "Tester les communications radio (BLE, LoRa, Zigbee) et les protocoles",
        "Auditer les mécanismes de démarrage sécurisé et de mise à jour",
        "Rédiger des rapports de vulnérabilités et accompagner les correctifs (CRA)"],
    'salaires': [
        {'niveau': "Débutant (rare, via labo/doctorat)", 'brut': (38000, 44000, 52000),
         'region': "IDF/Grenoble/Rennes surtout", 'variable': "Prime recherche"},
        {'niveau': 'Confirmé (4-7 ans)', 'brut': (50000, 62000, 78000),
         'region': "IDF/grandes métropoles", 'variable': "Prime, bug bounty"},
        {'niveau': 'Expert / chercheur', 'brut': (70000, 90000, 120000),
         'region': "International", 'variable': "Bug bounty, conférences, consulting"}],
    'ia': {'auto': 25, 'transfo': 50, 'creation': 65, 'levier': 70,
        'note': "L'IA aide au reverse engineering et à l'analyse binaire mais le travail "
            "matériel reste manuel. Le CRA crée une demande réglementaire durable de "
            "tests de sécurité des produits."},
    'pourquoi': "Niche à très faible concurrence, valorise l'électronique du Bac Pro CIEL "
        "(double compétence rare), salaires élevés, forte résistance à l'IA.",
    'garde_fous': "Très peu de postes en France (quelques dizaines par an) ; exige un "
        "niveau technique d'excellence ; marché local quasi inexistant hors grandes "
        "métropoles."}

A7_DPO = {
    'id': 'dpo', 'nom': "Délégué à la protection des données (DPO)",
    'alt': "Data Protection Officer, responsable conformité RGPD, consultant privacy",
    'famille': 'Gouvernance et conformité', 'acces': "Bac+4/5 (droit ou info) ; souvent après une première carrière",
    'description': "Le DPO veille à la conformité des traitements de données personnelles "
        "(RGPD) : registre des traitements, analyses d'impact (AIPD), relations avec la "
        "CNIL, sensibilisation. Métier à l'interface droit/technique, obligatoire dans "
        "les organisations publiques et les traitements à grande échelle. Souvent "
        "combiné avec le RSSI dans les PME (poste cumulé).",
    'missions': [
        "Tenir le registre des traitements et informer les responsables de traitement",
        "Réaliser les analyses d'impact (AIPD) sur les traitements à risque",
        "Gérer les demandes des personnes (accès, rectification, suppression)",
        "Instruire les violations de données et les notifications CNIL",
        "Former et sensibiliser les équipes",
        "Conseiller sur la privacy by design des nouveaux projets"],
    'salaires': [
        {'niveau': "DPO junior/adjoint (0-2 ans)", 'brut': (34000, 40000, 47000),
         'region': "ARA : 34-44k ; IDF : 38-50k", 'variable': "Prime 5-10 %"},
        {'niveau': 'DPO confirmé (4-7 ans)', 'brut': (45000, 55000, 68000),
         'region': "ARA/IDF", 'variable': "Prime 8-12 %"},
        {'niveau': "DPO groupe / indépendant", 'brut': (60000, 75000, 95000),
         'region': "National", 'variable': "DPO externalisé : 500-1 500 EUR/mois par client"}],
    'ia': {'auto': 45, 'transfo': 65, 'creation': 55, 'levier': 65,
        'note': "L'IA pose de nouveaux problèmes de conformité (données "
            "d'entraînement, AI Act) qui augmentent la charge de travail du DPO ; en "
            "parallèle, l'IA automatisera les registres et les AIPD de base. Métier "
            "transformé plutôt que menacé."},
    'pourquoi': "Demande réglementaire stable, compatible avec un profil technique + "
        "juridique, bonne voie de réorientation en milieu de carrière, cumul possible "
        "avec la sécurité (profil hybride recherché).",
    'garde_fous': "Peu de postes juniors ; forte part de juridique (éloigne des profils "
        "techniques purs) ; salaires inférieurs à l'ingénierie sécurité."}

A8_CHEF_PROJET = {
    'id': 'chef_projet_cyber', 'nom': "Chef de projet cybersécurité",
    'alt': "Chef de projet sécurité, PMO sécurité, responsable déploiement SOC, chef de projet conformité",
    'famille': 'Pilotage de projets', 'acces': "Bac+3/5 + 3-5 ans d'expérience technique ou en ESN",
    'description': "Pilote les projets de sécurité : déploiement de SOC, mise en "
        "conformité NIS2, refonte IAM, gestion de crise. Fait le lien entre les "
        "équipes techniques, les directions et les prestataires. Métier d'organisation "
        "et de communication plus que d'expertise technique, très demandé dans les "
        "ESN et les grandes entreprises, souvent une évolution naturelle pour un "
        "technicien ou ingénieur qui aime coordonner.",
    'missions': [
        "Planifier, budgéter et piloter les projets de sécurité",
        "Coordonner équipes internes, prestataires et MOA/MOE",
        "Gérer les risques projet, les jalons et le reporting de direction",
        "Animer les comités de pilotage et arbitrer les priorités",
        "Assurer la conformité des livrables (référentiels, réglementation)"],
    'salaires': [
        {'niveau': "Chef de projet junior (0-2 ans en rôle)", 'brut': (38000, 44000, 52000),
         'region': "ARA : 38-48k ; IDF : 42-55k", 'variable': "Prime 8-12 %"},
        {'niveau': 'Confirmé (4-7 ans)', 'brut': (50000, 60000, 75000),
         'region': "ARA/IDF", 'variable': "Prime 10-15 %"},
        {'niveau': "Directeur de programme / PMO sécurité", 'brut': (70000, 85000, 105000),
         'region': "IDF/grandes métropoles", 'variable': "Bonus 15-20 %"}],
    'ia': {'auto': 35, 'transfo': 55, 'creation': 35, 'levier': 65,
        'note': "L'IA assiste le reporting, la planification et la rédaction ; la "
            "coordination humaine et l'arbitrage restent le coeur du métier. Peu de "
            "risque de disparition, mais des attentes de productivité accrues."},
    'pourquoi': "Évolution naturelle et bien rémunérée pour les profils qui aiment "
        "organiser plutôt que coder, demande forte en ESN, compétences transférables "
        "à tous les secteurs.",
    'garde_fous': "Réunions permanentes, politique interne, responsabilité sans autorité "
        "hiérarchique ; éloigne progressivement de la technique."}

ALTERNATIFS = [A1_TELECOM, A2_ELEC_EMB, A3_CTI, A4_IAM, A5_FORMATEUR, A6_IOT_PENTEST, A7_DPO, A8_CHEF_PROJET]
