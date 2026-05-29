## Changelog : nosgestesclimat-app (30 derniers jours, au 28 mai 2026)

### Résumé
Ce mois-ci, l'application a connu des avancées significatives dans l'intégration des actions individuelles pour réduire l'empreinte carbone, notamment avec l'implémentation d'une nouvelle version des actions et un mode scolaire dédié. Des améliorations ont également été apportées à l'expérience utilisateur, à la performance et au suivi des données.

### Évolutions fonctionnelles
- **Actions individuelles :** Intégration de la liste des actions v2 avec pagination et détails des actions [#1784](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1784), [#1791](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1791), [#1793](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1793), [#1812](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1812).
- **Mode scolaire :** Ajout d'un mode scolaire dédié, permettant une utilisation spécifique dans un contexte pédagogique [#1758](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1758).
- **Amélioration de l'interface utilisateur :**
    - Le bloc des actions est désormais entièrement cliquable sur la page de résultats [#1805](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1805).
    - Amélioration du texte dans le mode étudiant [#1803](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1803).
    - Correction de l'unité d'affichage de l'empreinte hydrique [#1798](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1798), [#1797](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1797).
    - Suppression de la définition du mois sur le calendrier de réservation de démos [#1795](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1795).
    - Déplacement des boutons de langue pour corriger les pages de campagne [#1789](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1789).
- **Intégration Brevo :** Sauvegarde de nouveaux attributs pour les contacts Brevo dans l'administration des organisations [#1774](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1774).
- **Mise à jour du modèle :** Mise à jour de la version du modèle utilisé pour les calculs [#1810](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1810).
- **Amélioration du texte :** Mise à jour de la formulation "empreinte moyenne" sur la page d'accueil [#1809](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1809).

### Évolutions techniques
- **Migration ORM :** Migration de l'ORM vers le core [#1771](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1771).
- **Validation :** Migration de Zod vers Valibot pour la validation des données [#1801](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1801).
- **Performance :** Amélioration du LCP (Largest Contentful Paint) en préchargeant l'illustration de la page d'accueil [#1802](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1802).
- **Suivi :** Activation du suivi PostHog sur l'ensemble de l'application [#1800](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1800).
- **Feature Flags :** Implémentation de overrides de feature flags via des paramètres d'URL et ajout de fixtures E2E [#1799](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1799).
- **Déploiement :** Suppression du déploiement en preprod pendant les tests de pénétration [#1787](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1787).
- **Correction d'un bug :** Empêcher la création d'un `VerifiedUser` sans `User` associé [#1792](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1792).
- **Correction d'un bug :** Correction d'un script de synchronisation Brevo [#1794](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1794).
- **Correction d'un bug :** Correction de l'ordre d'affichage des points sur les graphiques [#1780](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1780).
- **Correction d'un bug :** Correction du blocage du bouton "Terminer" après avoir atteint la dernière question [#1776](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1776).
- **Correction d'un bug :** Correction de l'affichage du nom des participants et des administrateurs [#1773](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1773).
- **Correction d'un bug :** Correction du chargement des iframes en évitant les collisions avec les variables globales [#1786](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1786).
- **Correction d'un bug :** Correction du suivi du site [#1783](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1783) et de l'iframe [#1782](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1782).

### Autres changements
- Suppression de la bannière JVA [#1779](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1779).
- Mise à jour du titre de la page d'accueil [#1815](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1815).
- Ajout d'un worker de calcul pour les actions [#1811](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1811).
