## Changelog : nosgestesclimat-app (30 derniers jours, au 18 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la correction de bugs, l'amélioration du suivi des données analytiques et l'implémentation de nouvelles fonctionnalités, notamment l'ajout d'une fonctionnalité "Actions" et l'amélioration de l'intégration avec Brevo. Des optimisations ont également été apportées à l'infrastructure de déploiement et aux workflows CI/CD.

### Évolutions fonctionnelles
- Ajout de la fonctionnalité "Actions" avec un flag de fonctionnalité pour faciliter le déploiement progressif [#1784](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1784) et [#1775](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1775).
- Amélioration de l'intégration avec Brevo : sauvegarde des nouveaux attributs des organisations [#1774](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1774).
- Correction de l'affichage des noms des participants et des administrateurs [#1773](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1773).
- Correction du blocage du bouton "Terminer" après avoir répondu à la dernière question [#1776](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1776).
- Correction de l'ordre d'affichage des points sur les graphiques [#1780](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1780).
- Correction d'une erreur d'unité pour l'empreinte hydrique totale [#1797](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1797) et [#1798](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1798).
- Suppression de la bannière JVA [#1779](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1779).
- Ajout de traductions [#1769](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1769).

### Évolutions techniques
- Migration de l'ORM vers le core [#1771](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1771).
- Amélioration du suivi des données analytiques (Matomo) : récupération sécurisée des données [#1783](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1783) et [#1782](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1782).
- Refonte des workflows CI/CD et des configurations ESLint [#1765](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1765).
- Création d'un package core et d'une entité "Action" [#1759](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1759).
- Correction pour permettre l'utilisation de l'opérateur `!=` dans les conditions des "funfacts" [#1755](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1755).
- Suppression du déploiement en pré-production pendant les tests de pénétration [#1787](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1787).
- Prévention de la création d'un `VerifiedUser` sans `User` associé [#1792](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1792).
- Correction du chargement des iframes en évitant les collisions avec les variables globales [#1786](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1786).

### Autres changements
- Déplacement des boutons de langue pour corriger les pages d'atterrissage de campagne [#1789](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1789).
- Suppression de la définition du mois dans le calendrier de réservation de démonstration [#1795](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1795).
- Correction d'un script de synchronisation Brevo [#1794](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1794).
- Amélioration de la journalisation des erreurs de session [#1766](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1766) et [#1763](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1763).
- Ajout de logs pour les erreurs de session non attachées [#1766](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1766).
