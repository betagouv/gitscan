## Changelog : nosgestesclimat-app (30 derniers jours, au 26 mai 2026)

### Résumé
Ce mois-ci, l'application a connu des améliorations significatives en termes de fonctionnalités, notamment l'introduction d'un mode scolaire, l'ajout de la gestion des actions et des corrections de bugs pour améliorer l'expérience utilisateur. Des optimisations techniques ont également été apportées pour améliorer la performance et la fiabilité de l'application.

### Évolutions fonctionnelles
- **Mode scolaire** : Ajout d'un nouveau mode dédié aux établissements scolaires, avec des ajustements d'affichage et de fonctionnalités spécifiques. [#1758](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1758)
- **Gestion des actions** : Implémentation de la gestion des actions, incluant la liste des actions, les détails d'une action et l'intégration avec l'API. [#1793](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1793), [#1791](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1791), [#1784](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1784), [#1775](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1775)
- **Intégration Brevo** : Amélioration de l'intégration avec Brevo (Sendinblue) pour enregistrer de nouveaux attributs lors de la création de contacts d'organisation. [#1774](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1774)
- **Amélioration de l'affichage** : Correction de l'affichage de l'unité de mesure de l'empreinte hydrique et de l'ordre des points sur les graphiques. [#1798](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1798), [#1797](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1797), [#1780](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1780)
- **Texte mode étudiant** : Amélioration du texte affiché en mode étudiant pour une meilleure clarté. [#1803](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1803)
- **Masquage d'éléments** : Possibilité de masquer des éléments pour les intégrateurs utilisant des régions de modèles différentes. [#1804](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1804)
- **Correction bouton "Terminer"** : Correction d'un bug empêchant le bouton "Terminer" de fonctionner après avoir répondu à toutes les questions. [#1776](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1776)

### Évolutions techniques
- **Migration Zod vers Valibot** : Remplacement de la librairie de validation Zod par Valibot pour potentiellement améliorer les performances et réduire la taille du bundle. [#1801](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1801)
- **Préchargement de l'illustration** : Préchargement de l'illustration de la page d'accueil pour améliorer le Largest Contentful Paint (LCP) et donc la performance perçue. [#1802](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1802)
- **Activation du suivi Posthog** : Activation du suivi Posthog sur l'ensemble de l'application pour une meilleure analyse des données d'utilisation. [#1800](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1800)
- **Gestion des flags de fonctionnalités** : Amélioration de la gestion des flags de fonctionnalités avec la possibilité de les overrider via des paramètres d'URL et ajout de fixtures pour les tests E2E. [#1799](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1799)
- **Migration ORM** : Migration de l'ORM (Object-Relational Mapper) vers le core. [#1771](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1771)
- **Correction de la synchronisation Brevo** : Correction d'un script de synchronisation avec Brevo. [#1794](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1794)
- **Correction de l'iframe** : Correction d'un problème de chargement d'iframe causé par des collisions de variables globales. [#1786](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1786)
- **Correction du suivi Matomo** : Correction du suivi Matomo pour ne récupérer que les données avec un token sécurisé. [#1770](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1770)

### Autres changements
- **Ajout de la table ActionAssessment** : Ajout d'une nouvelle table `ActionAssessment` dans la base de données. [#1808](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1808)
- **Suppression de la bannière JVA** : Suppression de la bannière JVA (Journées de Visite d'Ateliers). [#1779](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1779)
- **Correction de la création de VerifiedUser** : Empêcher la création d'un `VerifiedUser` sans `User` associé. [#1792](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1792)
- **Correction du calendrier de réservation démo** : Suppression de la définition du mois sur le calendrier de réservation démo. [#1795](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1795)
- **Déplacement des boutons de langue** : Déplacement des boutons de langue pour corriger un problème sur les pages d'atterrissage de campagne. [#1789](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1789)
- **Suppression du déploiement en pré-production** : Suppression temporaire du déploiement en pré-production pendant les tests de pentest. [#1787](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1787)
