## Changelog : api-engagement (30 derniers jours)

### Résumé
Cette période a été marquée par d'importantes améliorations de l'accessibilité de l'application, notamment avec l'intégration de composants RGAA-compliant et des corrections pour une meilleure compatibilité avec les lecteurs d'écran.  Des corrections de bugs et des optimisations ont été apportées à l'API et au widget, ainsi que des améliorations de la gestion des erreurs et du monitoring.  Enfin, des refactorings ont été effectués pour simplifier l'architecture et améliorer la performance.

### Évolutions fonctionnelles

- Ajout d'un bouton "événements en direct" sur les listes de campagnes et du widget (#809).
- Possibilité d'ajouter un identifiant de publisher en préfixe dans l'URL (#807).
- Amélioration de la gestion des missions en permettant de refuser automatiquement les missions en modération (#813).
- Ajout d'un support pour l'ID client d'événement dans l'API (#714).
- Intégration de nouveaux composants RGAA-compliant pour les tooltips, les tabs et les toasts (#719, #720, #712).
- Amélioration de l'affichage des organisations désactivées (#771).
- Ajout de la possibilité de filtrer les missions par adresse (#776).

### Évolutions techniques

- Mise à jour de Node.js en version 24 (#802).
- Refactoring du modèle `publisher_organization` dans l'API (#758).
- Ajout d'alias pour simplifier le code (#810).
- Amélioration de la logique d'agrégation du widget (#790).
- Optimisation des requêtes de recherche géographique des missions (#806).
- Migration des activités de mission vers une table de jointure N-N (#757).
- Suppression de MongoDB (#761).
- Ajout d'un middleware de parsing dédié (#800).
- Ajout de logs plus détaillés et d'un suivi avec Sentry pour le widget (#795, #791, #789).
- Amélioration de la gestion des erreurs et ajout de logs pour l'envoi d'emails (#814).
- Ajout d'un header `request-id` avec support Sentry (#780).
- Ajout de tests d'intégration pour les endpoints du widget (#750).
- Refactoring de la gestion des statistiques et des vues matérialisées (#792, #788).
- Ajout d'un index composite sur l'adresse des missions (#774).
- Mise à jour de Vitest en version 4.0.8 (#749).
- Ajout de workflows Claude pour la revue de code (#716, #717).
- Ajout de tests E2E pour le SDK jstag.js (#715).
- Migration de la page "statistiques publiques" vers des cartes Metabase (#707).
- Suppression de l'ancien pipeline (#706).

### Autres changements

- Correction de divers problèmes d'interface utilisateur (couleurs, positionnement, etc.).
- Amélioration de la gestion des erreurs Sentry (#729, #797).
- Correction de problèmes liés à la duplication de campagnes (#727).
- Mise à jour des dépendances (Express, @types/express, NextJS, @sentry/cli, etc.).
- Correction de problèmes de compatibilité avec les lecteurs d'écran (#770).
- Amélioration des logs et du monitoring.
- Suppression de la prise en charge de Letudiant (#756).
- Correction de problèmes liés à la gestion des événements en direct (#784).
- Correction de problèmes liés à la gestion des missions supprimées et réactivées (#783).
- Correction de problèmes liés à la gestion des adresses (#759).
- Correction de problèmes liés à l'affichage des noms d'organisations et de villes (#759).
- Amélioration de la gestion des erreurs dans les modèles d'analyse (#760).
- Correction de problèmes liés à l'optimisation des images dans le widget (#793).
- Ajout de la configuration des conteneurs du widget (#786).
- Correction de problèmes liés à la connexion Prisma (#781).
- Correction de problèmes liés à la synchronisation incrémentale des événements (#753).
- Ajout de règles AGENTS.md (#734).
- Mise à jour du CHANGELOG.md.
