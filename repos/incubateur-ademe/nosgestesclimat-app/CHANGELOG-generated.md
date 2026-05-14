## Changelog : nosgestesclimat-app (30 derniers jours, au 13 mai 2026)

### Résumé
Ce mois-ci, l'application a bénéficié d'améliorations significatives en termes de fonctionnalités pour les organisations, de corrections de bugs pour une meilleure expérience utilisateur, et d'optimisations techniques pour le déploiement et les tests. L'ajout de nouvelles actions et la gestion des attributs des contacts Brevo pour les organisations sont des points forts.

### Évolutions fonctionnelles
- Possibilité de sauvegarder de nouveaux attributs pour les contacts Brevo dans l'administration des organisations. [#1774](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1774)
- Ajout d'une fonctionnalité "Je ne sais pas" en test A/B pour améliorer l'expérience utilisateur lors des simulations. [#1737](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1737)
- Suppression de la simulation depuis l'espace personnel. [#1747](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1747)
- Ajout d'une bannière JVA (Justice Verte et Agriculture). [#1748](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1748)
- Suppression de la bannière JVA. [#1779](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1779)
- Correction de l'affichage du nom des participants et des administrateurs. [#1773](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1773)
- Correction du blocage du bouton "Terminer" après avoir répondu à toutes les questions. [#1776](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1776)
- Ajout de nouvelles actions (feature flag en cours de déploiement). [#1775](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1775)
- Ajout de traductions. [#1769](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1769)

### Évolutions techniques
- Migration de l'ORM vers le core. [#1771](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1771)
- Suppression du déploiement en pré-production en raison d'un test de sécurité en cours. [#1787](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1787)
- Correction du chargement des iframes pour éviter les conflits de variables globales. [#1786](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1786)
- Correction du suivi des événements sur le site et dans les iframes. [#1783](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1783) et [#1782](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1782)
- Correction de l'ordre d'affichage des points sur les graphiques. [#1780](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1780)
- Amélioration de la récupération des statistiques Matomo avec un token sécurisé. [#1770](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1770)
- Refactorisation des workflows CI et configuration ESLint. [#1765](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1765)
- Création du package core et ébauche de l'entité action. [#1759](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1759)
- Correction du script de déploiement. [#1766](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1766)
- Mise en place de devcontainers pour faciliter le développement. [#1751](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1751)
- Correction de divers problèmes liés aux tests (E2E, serveur). [#1754](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1754), [#1763](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1763)
- Correction d'une erreur de configuration `tsconfigRootDir`. [#1757](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1757)

### Autres changements
- Ajout de logs pour les erreurs de session. [#1723](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1723)
- Autorisation de l'opérateur `!=` dans les conditions des funfacts. [#1755](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1755)
- Correction de l'affichage des logs.
- Amélioration de la gestion des erreurs lors de la création d'applications de preview.
- Mise à jour de la commande `poststart` en `postcreate`.
- Suppression du hook `prestart`.
