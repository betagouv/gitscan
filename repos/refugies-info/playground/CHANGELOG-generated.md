## Changelog : playground (30 derniers jours, au 04 mai 2026)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur l'amélioration de l'interface utilisateur, en particulier la liste des fiches, avec un nouveau design et des fonctionnalités de filtrage plus performantes. Des corrections importantes ont également été apportées à l'authentification Supabase et à la gestion des traductions. Enfin, des optimisations de performance et des mesures de sécurité ont été implémentées.

### Évolutions fonctionnelles
- **Liste des fiches :** Refonte complète de l'interface avec un nouveau design, incluant des en-têtes de colonnes améliorés, des couleurs actualisées et une pagination plus intuitive. [#186](https://github.com/refugies-info/playground/pull/186), [#192](https://github.com/refugies-info/playground/pull/192), [#193](https://github.com/refugies-info/playground/pull/193), [#189](https://github.com/refugies-info/playground/pull/189)
- **Filtrage :** Ajout d'un filtre par type d'entrée (BOMO, etc.) dans la liste des documents. [#198](https://github.com/refugies-info/playground/pull/198)
- **Liens de publication :** Ajout de liens de publication avec une popover interactive affichant l'URL externe et un indicateur de statut en ligne. [#208](https://github.com/refugies-info/playground/pull/208), [#209](https://github.com/refugies-info/playground/pull/209)
- **Copie d'URL :** Amélioration de la gestion des erreurs et ajout d'une indication de succès lors de la copie de l'URL de la fiche. [#203](https://github.com/refugies-info/playground/pull/203)
- **Authentification :** Correction du lien d'invitation Supabase qui redirige maintenant vers la page de connexion. [#195](https://github.com/refugies-info/playground/pull/195)
- **Traduction :** Correction d'un problème empêchant le fonctionnement des traductions de fiches. [#191](https://github.com/refugies-info/playground/pull/191)
- **Éditeur de document :** Ajout d'un panneau de comparaison côte à côte avec la source originale. [#210](https://github.com/refugies-info/playground/pull/210)

### Évolutions techniques
- **Architecture :** Refactorisation de l'architecture de la sidebar pour une meilleure réutilisabilité et intégration avec le nouveau design global. [#204](https://github.com/refugies-info/playground/pull/204), [#206](https://github.com/refugies-info/playground/pull/206), [#207](https://github.com/refugies-info/playground/pull/207)
- **Performance :** Ajout d'un index GIN trigram sur le champ ID des enregistrements d'ingestion pour optimiser les performances de recherche. [#205](https://github.com/refugies-info/playground/pull/205)
- **Sécurité :** Implémentation d'un hook pre-commit GitLeaks pour la détection de secrets. [#188](https://github.com/refugies-info/playground/pull/188)
- **RBAC :** Migration de la source de vérité pour le contrôle d'accès basé sur les rôles (RBAC) des métadonnées JWT vers la table `profiles` et implémentation d'un routage basé sur les rôles centralisé. [#195](https://github.com/refugies-info/playground/pull/195)
- **Workflow :** Remplacement du streaming éditorial basé sur SSE par un workflow durable utilisant Supabase Realtime avec un fallback de polling. [#202](https://github.com/refugies-info/playground/pull/202)
- **Supabase :** Mise à jour de la configuration Supabase avec des URL de redirection de développement locales et correction des permissions RBAC. [#195](https://github.com/refugies-info/playground/pull/195)

### Autres changements
- **Documentation :** Amélioration de la documentation Storybook pour les composants UI. [#200](https://github.com/refugies-info/playground/pull/200)
- **Refactoring :** Divers refactorings pour améliorer la lisibilité et la maintenabilité du code.
- **Corrections :** Correction de divers bugs et améliorations mineures de l'interface utilisateur.
- **Labels :** Mise à jour des labels pour les entrées permanentes dans la cellule ModalitesEntreesSortiesCell. [#200](https://github.com/refugies-info/playground/pull/200)
- **Gestion des erreurs :** Ajout de la gestion des erreurs pour la mise à jour du workflow Supabase. [#203](https://github.com/refugies-info/playground/pull/203)
