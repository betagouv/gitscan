## Changelog : playground (30 derniers jours, au 13 mai 2026)

### Résumé
Ce mois-ci, le projet a connu des améliorations significatives en termes de gestion des utilisateurs et de sécurité, avec une refonte de l'authentification et des permissions basée sur Supabase. Des corrections ont été apportées pour améliorer la stabilité de l'ingestion de données et de l'IA, ainsi que des améliorations de l'interface utilisateur pour faciliter la gestion des documents et des traductions.

### Évolutions fonctionnelles
- Refonte de l'authentification et de la gestion des rôles avec Supabase, incluant la gestion des invitations et la restriction d'accès basée sur les rôles. [#196](https://github.com/refugies-info/playground/pull/196)
- Ajout d'un indicateur d'urgence pour les traductions, permettant de prioriser certaines traductions. [#220](https://github.com/refugies-info/playground/pull/220)
- Amélioration de l'interface utilisateur pour la gestion des documents, incluant un sidebar global, des liens de publication et des popovers d'information. [#217](https://github.com/refugies-info/playground/pull/217), [#218](https://github.com/refugies-info/playground/pull/218), [#219](https://github.com/refugies-info/playground/pull/219)
- Ajout d'un filtre pour le type d'entrée dans la liste des documents. [#198](https://github.com/refugies-info/playground/pull/198)
- Ajout d'un indicateur de sauvegarde et d'une gestion des erreurs améliorée pour l'éditeur de documents. [#202](https://github.com/refugies-info/playground/pull/202)
- Correction d'un bug empêchant le fonctionnement des traductions. [#191](https://github.com/refugies-info/playground/pull/191)

### Évolutions techniques
- Refactorisation de l'ingestion de données pour améliorer la gestion des versions et la prévention de la duplication. [#223](https://github.com/refugies-info/playground/pull/223), [#224](https://github.com/refugies-info/playground/pull/224), [#225](https://github.com/refugies-info/playground/pull/225)
- Amélioration de la gestion des erreurs et de la journalisation. [#224](https://github.com/refugies-info/playground/pull/224)
- Optimisation des performances de la recherche grâce à l'ajout d'un index GIN trigram. [#205](https://github.com/refugies-info/playground/pull/205)
- Refactorisation de l'intégration de l'IA, avec passage à un workflow durable basé sur Supabase Realtime et une gestion améliorée des états. [#193](https://github.com/refugies-info/playground/pull/193), [#200](https://github.com/refugies-info/playground/pull/200)
- Mise en place d'une gestion des permissions plus robuste avec RBAC (Role-Based Access Control) et l'utilisation de la table `profiles` pour stocker les rôles. [#195](https://github.com/refugies-info/playground/pull/195)
- Utilisation de Zod pour la validation des requêtes API. [#196](https://github.com/refugies-info/playground/pull/196)
- Amélioration de la gestion des erreurs et de la journalisation. [#224](https://github.com/refugies-info/playground/pull/224)

### Autres changements
- Ajout d'une documentation pour l'exportation et l'importation de bases de données Supabase locales. [#222](https://github.com/refugies-info/playground/pull/222)
- Suppression des tâches cron d'ingestion de données inutiles. [#226](https://github.com/refugies-info/playground/pull/226)
- Ajout d'un point de terminaison de débogage pour inspecter les variables d'environnement DI. [#222](https://github.com/refugies-info/playground/pull/222)
- Ajout d'un délai entre les appels à l'API Letta pour éviter les limitations de débit. [#214](https://github.com/refugies-info/playground/pull/214)
- Mise à jour des labels et du wording pour plus de clarté. [#219](https://github.com/refugies-info/playground/pull/219), [#200](https://github.com/refugies-info/playground/pull/200)
