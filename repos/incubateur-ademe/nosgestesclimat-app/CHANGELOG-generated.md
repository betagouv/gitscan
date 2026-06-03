## Changelog : nosgestesclimat-app (30 derniers jours, au 2 juin 2026)

### Résumé
Ce mois-ci, l'application a connu des améliorations significatives concernant les actions individuelles pour réduire son impact carbone, avec l'intégration de nouvelles données et l'amélioration de leur affichage. Des corrections de bugs ont également été apportées pour améliorer la stabilité et l'expérience utilisateur, notamment concernant le mode scolaire, les calculs d'empreinte et l'intégration avec Brevo. Des optimisations techniques ont été réalisées pour améliorer la performance et la flexibilité de l'application.

### Évolutions fonctionnelles
- **Actions individuelles :**
    - Affichage de l'impact des actions individuelles [#1822](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1822).
    - Synchronisation des actions depuis Notion [#1812](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1812).
    - Détail des actions individuelles [#1791](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1791).
    - Liste des pages d'actions v2 [#1784](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1784).
    - Bloc d'actions entièrement cliquable sur la page de fin [#1805](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1805).
- **Mode scolaire :** Implémentation et correction de bugs concernant le mode scolaire [#1758](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1758).
- **Améliorations de l'interface utilisateur :**
    - Amélioration du texte "empreinte moyenne" sur la page d'accueil [#1809](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1809).
    - Amélioration du texte du mode étudiant [#1803](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1803).
    - Suppression de la bannière JVA [#1779](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1779).
- **Intégration Brevo :** Sauvegarde de nouveaux attributs pour les contacts Brevo dans l'administration de l'organisation [#1774](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1774).
- **Partage :** Correction de l'URL de partage avec les paramètres UTM [#1821](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1821).

### Évolutions techniques
- **Infrastructure :**
    - Suppression du déploiement en pré-production pendant les tests de pentest [#1787](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1787).
    - Activation du suivi Posthog sur l'ensemble de l'application [#1800](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1800).
- **Architecture :**
    - Migration de l'ORM vers Core [#1771](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1771).
    - Migration de Zod vers Valibot pour la validation des données [#1801](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1801).
    - Ajout d'une table `ActionAssessment` [#1808](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1808).
- **Performance :**
    - Amélioration du LCP (Largest Contentful Paint) en préchargeant l'illustration de la page d'accueil [#1802](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1802).
    - Utilisation de workers pour le calcul des actions [#1811](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1811).
- **Feature Flags :** Support des feature flags avec variantes (A/B tests) [#1816](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1816) et gestion des overrides via paramètres d'URL [#1799](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1799).

### Autres changements
- Mise à jour de la version du modèle [#1810](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1810).
- Corrections de bugs mineurs concernant l'empreinte hydrique [#1798](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1798), [#1797](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1797), le calendrier de réservation de démonstration [#1795](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1795) et le script Brevo [#1794](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1794).
- Correction d'un crash potentiel de `getClientCookie` pendant le rendu côté serveur (SSR) [#1819](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1819).
- Correction du forcing de la région avec le paramètre `region` [#1824](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1824).
- Correction d'un problème de création de `VerifiedUser` sans `User` [#1792](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1792).
- Correction du tracking du site et de l'iframe [#1783](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1783) et [#1782](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1782).
