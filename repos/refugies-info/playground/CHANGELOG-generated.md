## Changelog : playground (30 derniers jours, au 07 mai 2026)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur l'amélioration de l'expérience utilisateur, notamment au niveau de la gestion des documents et des workflows de publication. Des corrections de bugs et des optimisations de performance ont également été apportées, en particulier concernant la gestion des traductions et l'intégration avec l'IA. L'interface utilisateur a été revue pour plus de clarté et d'accessibilité.

### Évolutions fonctionnelles
- Ajout d'un indicateur d'urgence pour les traductions, permettant de prioriser les traductions urgentes dans le workflow de publication [#220](https://github.com/refugies-info/playground/pull/220).
- Amélioration de la gestion des erreurs lors de la récupération des données enrichies. [#220](https://github.com/refugies-info/playground/pull/220)
- Ajout d'un popover de confirmation pour l'archivage des documents, avec restriction du basculement en mode éditeur au seul onglet "Contenu". [#219](https://github.com/refugies-info/playground/pull/219)
- Correction du libellé du popover de publication pour plus de clarté. [#219](https://github.com/refugies-info/playground/pull/219)
- Ajout de liens de publication avec un popover pour afficher les URLs externes. [#208](https://github.com/refugies-info/playground/pull/208)
- Correction du fonctionnement des liens d'invitation Supabase qui renvoient maintenant vers la page de connexion. [#195](https://github.com/refugies-info/playground/pull/195)
- Ajout d'un filtre pour le type d'entrée dans la liste des documents. [#198](https://github.com/refugies-info/playground/pull/198)
- Amélioration de l'affichage de la liste des documents avec des retours de conception (couleurs, typographie, espacements). [#192](https://github.com/refugies-info/playground/pull/192), [#190](https://github.com/refugies-info/playground/pull/190), [#189](https://github.com/refugies-info/playground/pull/189)
- Correction du fonctionnement des traductions de fiches. [#191](https://github.com/refugies-info/playground/pull/191)

### Évolutions techniques
- Refactor de la gestion de l'importation de Markdown pour améliorer le code-splitting et la sécurité SSR. [#218](https://github.com/refugies-info/playground/pull/218)
- Mise en place d'un système de workflows nocturnes pour l'ingestion de données DI, avec une planification mise à jour. [#221](https://github.com/refugies-info/playground/pull/221)
- Optimisation des performances de recherche grâce à l'ajout d'un index GIN trigram sur le champ ID des enregistrements d'ingestion. [#205](https://github.com/refugies-info/playground/pull/205)
- Refactor de l'intégration de l'IA pour la réécriture, passant d'un système de polling à un workflow durable avec Supabase Realtime. [#194](https://github.com/refugies-info/playground/pull/194)
- Migration de la source de vérité pour les rôles RBAC des métadonnées JWT vers la table `profiles` et implémentation d'un routage basé sur les rôles centralisé. [#195](https://github.com/refugies-info/playground/pull/195)
- Amélioration de la gestion des erreurs et de la sécurité des migrations Supabase. [#196](https://github.com/refugies-info/playground/pull/196)
- Ajout d'un délai entre les appels à l'API Letta pour éviter les limitations de débit. [#214](https://github.com/refugies-info/playground/pull/214)

### Autres changements
- Mise à jour de la documentation concernant la planification des workflows d'ingestion DI. [#215](https://github.com/refugies-info/playground/pull/215)
- Nettoyage du code et suppression de la logique inutilisée.
- Correction de divers problèmes de style et d'accessibilité.
- Mise à jour des dépendances et des configurations.
- Ajout de tests unitaires.
- Correction de bugs mineurs et améliorations de la stabilité.
