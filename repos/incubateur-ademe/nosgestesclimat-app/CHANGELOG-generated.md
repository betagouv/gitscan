## Changelog : nosgestesclimat-app (30 derniers jours, au 13 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la correction de bugs, l'amélioration du suivi des données analytiques, et le début du développement de nouvelles fonctionnalités liées aux actions proposées aux utilisateurs. Des corrections ont également été apportées à l'interface utilisateur et à la gestion des organisations.

### Évolutions fonctionnelles
- Possibilité d'enregistrer de nouveaux attributs pour les contacts Brevo dans l'administration des organisations. [#1774](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1774)
- Correction de l'affichage de l'ordre des points sur les graphiques. [#1780](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1780)
- Correction de l'affichage du nom des participants et des administrateurs. [#1773](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1773)
- Correction du blocage du bouton "Terminer" après avoir atteint la dernière question du questionnaire. [#1776](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1776)
- Ajout de la fonctionnalité "actions" via un *feature flag* (en cours de développement). [#1775](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1775)
- Suppression de la bannière JVA. [#1779](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1779)
- Ajout de traductions. [#1769](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1769)

### Évolutions techniques
- Migration de l'ORM vers le *core*. [#1771](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1771)
- Correction du chargement des iframes en évitant les collisions avec les variables globales. [#1786](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1786)
- Amélioration du suivi des données analytiques (Matomo) et correction de bugs associés. [#1783](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1783) et [#1782](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1782)
- Suppression du déploiement en pré-production en raison d'un test de sécurité en cours. [#1787](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1787)
- Création d'un package *core* et d'un brouillon de l'entité "action". [#1759](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1759)
- Fusion des workflows CI et des configurations ESLint. [#1765](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1765)
- Correction du script de déploiement. [#1766](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1766)
- Ajout d'un déploiement d'application de prévisualisation dans la CI (avec tests E2E). [#1761](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1761)
- Correction pour permettre l'utilisation de l'opérateur `!=` dans les conditions des *funfacts*. [#1755](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1755)

### Autres changements
- Amélioration de la journalisation des erreurs de session.
- Correction de la journalisation des erreurs "notfound" pour ne l'afficher que si une session est attachée.
- Suppression d'une tentative de restauration d'une configuration de build personnalisée.
- Ajout de listes de pages d'actions. [#1784](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1784)
