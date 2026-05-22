## Changelog : nosgestesclimat-app (30 derniers jours, au 21 mai 2026)

### Résumé
Ce mois-ci, l'application a bénéficié d'améliorations significatives concernant les actions, le suivi des données, la synchronisation avec Brevo, et la correction de plusieurs bugs affectant l'interface utilisateur et le bon fonctionnement de certaines fonctionnalités. Des optimisations ont également été apportées à l'infrastructure de déploiement et au suivi des erreurs.

### Évolutions fonctionnelles
- Ajout de la fonctionnalité "actions" avec la liste des pages et le détail des actions. [#1791](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1791) et [#1784](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1784)
- Possibilité de sauvegarder de nouveaux attributs pour les contacts Brevo dans l'administration des organisations. [#1774](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1774)
- Correction de l'affichage des noms des participants et des administrateurs. [#1773](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1773)
- Correction du blocage du bouton "Terminer" après avoir atteint la dernière question du questionnaire. [#1776](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1776)
- Suppression de la bannière JVA. [#1779](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1779)

### Évolutions techniques
- Migration de l'ORM vers le core. [#1771](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1771)
- Suppression du déploiement en pré-production pendant la phase de pentest. [#1787](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1787)
- Correction du suivi des données du site et de l'iframe avec Matomo. [#1783](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1783) et [#1782](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1782)
- Amélioration de la gestion des erreurs de session avec ajout de logs. [#1786](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1786)
- Correction d'un problème empêchant la création d'un `VerifiedUser` sans `User` associé. [#1792](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1792)
- Correction de l'ordre d'affichage des points sur les graphiques. [#1780](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1780)

### Autres changements
- Correction d'une erreur d'unité pour l'empreinte hydrique totale. [#1798](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1798) et [#1797](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1797)
- Correction de la synchronisation du script Brevo. [#1794](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1794)
- Déplacement des boutons de langue pour corriger les pages d'atterrissage de campagne. [#1789](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1789)
- Suppression de la définition du mois sur le calendrier de réservation de démo. [#1795](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1795)
- Ajout d'un flag de fonctionnalité pour les actions. [#1775](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1775)
- Amélioration de la récupération des données Matomo avec un token sécurisé. [#1770](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1770)
- Ajout de logs pour les erreurs de session. [#1786](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1786)
- Correction de logs pour les sessions non trouvées. [#1786](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1786)
