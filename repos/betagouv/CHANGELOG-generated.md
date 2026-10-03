# Synthèse d'activité : betagouv (du 23/09 au 30/09)

## Résumé de l'activité
L'activité récente est marquée par une volonté de simplifier les parcours utilisateurs et d'enrichir les capacités d'aide à la décision. Des outils de comparaison et de simulation ont été renforcés [mon-entreprise](/repos/betagouv/mon-entreprise), tandis que l'intégration de l'intelligence artificielle ouvre de nouveaux usages pour la création de contenu [science-infuse](/repos/betagouv/science-infuse) et l'analyse de données [portail-rse-externe](/repos/betagouv/portail-rse-externe). 

Ces évolutions visent à offrir des services plus intuitifs et performants pour les citoyens et les professionnels, notamment à travers l'amélioration de la saisie de données terrain [sylvasan](/repos/betagouv/sylvasan) et le lancement de versions stables pour de nouveaux services [slack2tchap](/repos/betagouv/slack2tchap).

## Sécurité
- Renforcement massif de la protection contre les failles de type IDOR, CSRF et les injections pour [service-national-universel](/repos/betagouv/service-national-universel) et [recommandations-collaboratives](/repos/betagouv/recommandations-collaboratives).
- Amélioration de l'authentification (2FA, OAuth2, ProConnect) pour [transports-sanitaires-sites-conformes](/repos/betagouv/transports-sanitaires-sites-conformes), [reva](/repos/betagouv/reva) et [rdv-service-public](/repos/betagouv/rdv-service-public).
- Correction de vulnérabilités critiques, notamment sur la gestion des sessions pour [mon-suivi-justice](/repos/betagouv/mon-suivi-justice) et mise à jour des dépendances de sécurité pour [mon-profil-anssi](/repos/betagouv/mon-profil-anssi).
- Automatisation des contrôles de sécurité (CVE, Bandit, Checkov, Zizmor) dans les pipelines CI/CD pour [transports-sanitaires-sites-conformes](/repos/betagouv/transports-sanitaires-sites-conformes) et [mon-aide-cyber-journal](/repos/betagouv/mon-aide-cyber-journal).
- Protection de la confidentialité des données (RGPD) et sécurisation des échanges pour [service-national-universel](/repos/betagouv/service-national-universel).

## Autres changements notables
- Refontes architecturales et montées de versions technologiques majeures (PHP 8.5, Symfony 8.1, Node 24) pour [mon-indemnisation-justice](/repos/betagouv/mon-indemnisation-justice) et [transports-sanitaires](/repos/betagouv/transports-sanitaires).
- Intégration de nouveaux moteurs d'intelligence artificielle pour [portail-rse-externe](/repos/betagouv/portail-rse-externe) et [science-infuse](/repos/betagouv/science-infuse).
- Évolutions d'infrastructure et déploiements (Scalingo, IaC) pour [slack2tchap](/repos/betagouv/slack2tchap), [scalingo-gotenberg](/repos/betagouv/scalingo-gotenberg) et [nitrates-iac](/repos/betagouv/nitrates-iac).
- Publication de la version 2.0 des [standards](/repos/betagouv/standards).

## Dépôts les plus actifs
- [sylvasan](/repos/betagouv/sylvasan) : Améliorations de la saisie de données terrain, de la cartographie et de l'interface mobile.
- [mon-entreprise](/repos/betagouv/mon-entreprise) : Lancement d'un comparateur de modèles et nouveaux simulateurs pour artisans et commerçants.
- [seves](/repos/betagouv/seves) : Évolution majeure du module de Santé Animale et nouveaux tableaux de bord de pilotage.
- [mon-indemnisation-justice](/repos/betagouv/mon-indemnisation-justice) : Refonte de la gestion documentaire (PDF) et modernisation de l'architecture frontend.
- [transports-sanitaires](/repos/betagouv/transports-sanitaires) : Mise à jour des règles métier et refonte structurelle du simulateur.
- [recommandations-collaboratives](/repos/betagouv/recommandations-collaboratives) : Améliorations fonctionnelles et renforcement important de la sécurité.
