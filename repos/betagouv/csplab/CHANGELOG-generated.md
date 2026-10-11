## Changelog : csplab (30 derniers jours, au 08/10/2026)

### Résumé
Ce mois a été marqué par une amélioration significative de l'expérience de gestion des recrutements. L'introduction d'un système de messagerie intégré et d'un panneau de détails pour les candidatures permet désormais une collaboration plus fluide entre les recruteurs. Parallèlement, l'automatisation et la précision de l'importation des données (notamment via Talentsoft) ont été renforcées pour garantir une meilleure fiabilité des informations.

### Évolutions fonctionnelles
- **Gestion des candidatures** :
    - Mise en place d'un panneau de candidature complet permettant de visualiser le CV, les documents, l'historique d'activité et d'ajouter des notes [#1562](https://github.com/betagouv/csplab/issues/1562).
    - Amélioration de la navigation et de l'ergonomie du Kanban pour la sélection et le passage d'une étape à l'autre [#1753](https://github.com/betagouv/csplab/issues/1753), [#1477](https://github.com/betagouv/csplab/issues/1477).
    - Ajout de la possibilité de saisir un motif lors du refus d'une candidature [#1506](https://github.com/betagouv/csplab/issues/1506).
- **Messagerie et collaboration** :
    - Déploiement d'un système de messagerie permettant de créer des conversations, d'échanger des messages et de joindre des fichiers directement dans le cadre d'une candidature [#1678](https://github.com/betagouv/csplab/issues/1678), [#1666](https://github.com/betagouv/csplab/issues/1666), [#1747](https://github.com/betagouv/csplab/issues/1747).
- **Pilotage du recrutement** :
    - Amélioration de la gestion des équipes de recrutement (ajout, modification et révocation de membres/rôles) [#1409](https://github.com/betagouv/csplab/issues/1409), [#1416](https://github.com/betagouv/csplab/issues/1416).
    - Possibilité d'assigner des responsables à plusieurs recrutements de manière groupée [#1483](https://github.com/betagouv/csplab/issues/1483).
- **Ingestion de données** :
    - Optimisation de l'importation des offres (Talentsoft) avec une meilleure gestion des champs critiques (dates de vacance, export UNIF, entités DGAFP) [#1815](https://github.com/betagouv/csplab/issues/1815), [#1716](https://github.com/betagouv/csplab/issues/1716).
    - Ajout de la possibilité d'afficher les offres actives par source [#1763](https://github.com/betagouv/csplab/issues/1763).

### Évolutions techniques
- **Architecture et Backend** :
    - Refactoring majeur de la gestion des permissions et des rôles (conformément à l'ADR-009) pour une structure plus robuste [#1771](https://github.com/betagouv/csplab/issues/1771), [#1427](https://github.com/betagouv/csplab/issues/1427).
    - Migration du système de messagerie vers un stockage en base de données pour assurer la persistance des échanges [#1681](https://github.com/betagouv/csplab/issues/1681).
    - Mise en place du stockage des documents candidats sur S3 pour une meilleure gestion des fichiers [#1472](https://github.com/betagouv/csplab/issues/1472).
- **Sécurité et Identité** :
    - Renforcement de la sécurité de l'authentification via la limitation du débit (rate limiting) sur les rejets d'API-Key [#1807](https://github.com/betagouv/csplab/issues/1807) et la journalisation des tentatives de connexion [#1660](https://github.com/betagouv/csplab/issues/1660).
    - Sécurisation des accès en bloquant automatiquement les agents révoqués ou les organismes supprimés [#1762](https://github.com/betagouv/csplab/issues/1762), [#1597](https://github.com/betagouv/csplab/issues/1597).
- **Infrastructure et Qualité** :
    - Automatisation de la création de "review apps" pour faciliter les tests et les revues de code [#1760](https://github.com/betagouv/csplab/issues/1760).
    - Adoption des *Conventional Commits* pour automatiser la génération du changelog [#1415](https://github.com/betagouv/csplab/issues/1415).
    - Amélioration de la couverture de tests front-end avec l'intégration de `testing-library` [#1481](https://github.com/betagouv/csplab/issues/1481).

### Autres changements
- Mise à jour de la documentation de l'API d'ingestion [#1727](https://github.com/betagouv/csplab/issues/1727).
- Nettoyage général du code et des tests.
