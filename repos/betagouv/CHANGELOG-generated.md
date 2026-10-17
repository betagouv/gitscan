# Synthèse d'activité : betagouv (du 01/09 au 14/10)

## Résumé de l'activité
L'activité de cette période est marquée par une montée en puissance des fonctionnalités d'intelligence artificielle [science-infuse](/repos/betagouv/science-infuse) et une modernisation profonde des parcours usagers via l'intégration de solutions d'authentification comme FranceConnect [pass-sport](/repos/betagouv/pass-sport) ou ProConnect [stage-direct](/repos/betagouv/stage-direct). 

Parallèlement, un effort majeur est porté sur la fiabilité des outils de terrain, notamment avec l'amélioration du mode hors ligne [zacharie](/repos/betagouv/zacharie) et des outils cartographiques [sylvasan](/repos/betagouv/sylvasan). L'organisation renforce également ses capacités d'analyse de données et de pilotage pour les gestionnaires à travers de nouveaux tableaux de bord et l'intégration d'outils de statistiques [turgot-metabase](/repos/betagouv/turgot-metabase).

## Sécurité
- **Corrections critiques** : Résolution d'une vulnérabilité de sécurité concernant la gestion des sessions utilisateurs [mon-suivi-justice](/repos/betagouv/mon-suivi-justice).
- **Authentification et accès** : Renforcement massif contre les failles de type IDOR (accès non autorisé) [service-national-universel](/repos/betagouv/service-national-universel), [recommandations-collaboratives](/repos/betagouv/recommandations-collaboratives) et [recoco-plugins-mi-depafi](/repos/betagouv/recoco-plugins-mi-depafi). Mise en place de la double authentification (2FA) [reva](/repos/betagouv/reva) et amélioration des protocoles OAuth2 [rdv-service-public](/repos/betagouv/rdv-service-public).
- **Protection des données et vie privée** : Mise en œuvre de mesures de protection des données personnelles (RGPD) via le masquage des logs [service-national-universel](/repos/betagouv/service-national-universel) et sécurisation de la transmission des données vers les outils de suivi [recoco-sync](/repos/betagouv/recoco-sync).
- **Sécurité du cycle de développement (DevSecOps)** : Intégration d'outils d'analyse automatique des vulnérabilités et de la configuration (Bandit, Checkov, Zizmor) directement dans les pipelines CI/CD [transports-sanitaires-sites-conformes](/repos/betagouv/transports-sanitaires-sites-conformes), [mon-aide-cyber-journal](/repos/betagouv/mon-aide-cyber-journal).

## Autres changements notables
- **Évolutions architecturales** : Refonte majeure de la logique métier vers le serveur [mon-indemnisation-justice](/repos/betagouv/mon-indemnisation-justice), intégration d'un nouveau moteur d'intelligence artificielle v2 [portail-rse-externe](/repos/betagouv/portail-rse-externe) et restructuration profonde du moteur de calcul [mon-entreprise](/repos/betagouv/mon-entreprise).
- **Versions et standards** : Publication de la version 2.0 des standards [standards](/repos/betagouv/standards) et lancement de la première version stable (V1.0.0) de [slack2tchap](/repos/betagouv/slack2tchap).
- **Infrastructure** : Initialisation de l'infrastructure en tant que code (IaC) [nitrates-iac](/repos/betagouv/nitrates-iac) et déploiement de nouveaux services sur la plateforme Scalingo [scalingo-gotenberg](/repos/betagouv/scalingo-gotenberg).

## Dépôts les plus actifs
- [zacharie](/repos/betagouv/zacharie) : Optimisation du mode hors ligne, de la sécurité des données et de l'expérience mobile.
- [service-national-universel](/repos/betagouv/service-national-universel) : Sécurisation intensive des accès et simplification des parcours utilisateurs.
- [maestro](/repos/betagouv/maestro) : Avancées majeures sur le paramétrage des plans et la gestion automatisée des prélèvements.
- [mon-service-securise](/repos/betagouv/mon-service-securise) : Lancement d'une API publique et organisation des services par groupes.
- [sylvasan](/repos/betagouv/sylvasan) : Amélioration des outils de terrain (cartographie, boussole, gestion photo).
- [mon-indemnisation-justice](/repos/betagouv/mon-indemnisation-justice) : Modernisation de la stack technique et de la gestion documentaire.
