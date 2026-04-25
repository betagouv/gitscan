# Synthèse d'activité : betagouv (du 22/04 au 22/05)

## Résumé de l'activité
L'activité récente de l'organisation betagouv a été particulièrement riche, avec des mises à jour significatives sur de nombreux dépôts. On observe une forte concentration sur l'amélioration de l'expérience utilisateur, notamment via des interfaces plus intuitives et des fonctionnalités de recherche optimisées (portail-rse, doctorat-gouv). La sécurité a également été un axe majeur, avec des corrections de vulnérabilités et des renforcements de l'authentification (api-subventions-asso, infomedicament).  De nombreux dépôts ont bénéficié de mises à jour techniques importantes, incluant des refactorings, des optimisations de performance et l'adoption de nouvelles technologies (dsfr-view-components, eva, sylvasan). L'intégration de nouvelles données et l'amélioration des processus de gestion des données sont également des thèmes récurrents (depots-sauvages, anssi-recommandations-cyber-data, diagbruit.beta.gouv.fr).

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations en matière de sécurité :

- Correction d'une vulnérabilité potentielle d'IDOR sur la soumission de notes avancées dans [infomedicament](/repos/betagouv/infomedicament).
- Renforcement de la sécurité en désactivant le "device code grant" dans Passport dans [jeveuxaider-back](/repos/betagouv/jeveuxaider-back).
- Correction d'une vulnérabilité (CVE) dans [diagbruit.beta.gouv.fr](/repos/betagouv/diagbruit.beta.gouv.fr).

## Autres changements notables
Plusieurs évolutions techniques majeures ont été déployées :

- Mise à jour vers ViewComponent 4 dans [dsfr-view-components](/repos/betagouv/dsfr-view-components).
- Refonte du modèle de calcul pour les travailleurs indépendants dans [mon-entreprise](/repos/betagouv/mon-entreprise).
- Passage au crawler Playwright dans [agreste-crawler](/repos/betagouv/agreste-crawler).
- Intégration de l'API Amethis dans [doctorat-gouv](/repos/betagouv/doctorat-gouv).
- Mise en place d'une base de données réplica dans [jeveuxaider-back](/repos/betagouv/jeveuxaider-back).
- Refactoring et optimisation des requêtes dans [diagbruit.beta.gouv.fr](/repos/betagouv/diagbruit.beta.gouv.fr).

## Dépôts les plus actifs
- [mon-entreprise](/repos/betagouv/mon-entreprise) : Refonte majeure du modèle de calcul pour les travailleurs indépendants.
- [diagbruit.beta.gouv.fr](/repos/betagouv/diagbruit.beta.gouv.fr) : Amélioration de l'expérience utilisateur et intégration de données scolaires.
- [jeveuxaider-back](/repos/betagouv/jeveuxaider-back) : Amélioration de la gestion des invitations, intégration France Travail et renforcement de la sécurité.
- [anssi-recommandations-cyber-data](/repos/betagouv/anssi-recommandations-cyber-data) : Intégration de nouvelles sources de données et amélioration de la qualité des questions.
- [euphrosyne](/repos/betagouv/euphrosyne) et [euphrosyne-tools-api](/repos/betagouv/euphrosyne-tools-api) : Gestion du cycle de vie des données de projet et améliorations techniques.
- [portail-rse](/repos/betagouv/portail-rse) : Amélioration de la recherche et ajout du code postal des entreprises.
- [infomedicament](/repos/betagouv/infomedicament) : Optimisation des performances et correction de vulnérabilités.
