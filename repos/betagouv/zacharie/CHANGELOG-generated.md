## Changelog : zacharie (30 derniers jours)

### Résumé
Ce changelog résume les améliorations apportées à Zacharie au cours des 30 derniers jours. Les modifications incluent des corrections de bugs, des améliorations de l'interface utilisateur, des optimisations de la synchronisation des données et des fonctionnalités supplémentaires pour la gestion des carcasses, des FEI et des SVI. Des améliorations de la documentation ont également été apportées.

### Évolutions fonctionnelles
- Ajout de la possibilité de créer un contact circuit court directement lors du flux de création d'une FEI (#147).
- Synchronisation des contacts circuit court avec Brevo (#144).
- Ajout de champs de propriété à la modèle Carcasse (#145).
- Possibilité de sauter des étapes lors de l'onboarding (#138).
- Acceptation automatique des carcasses (#143).
- Ajout d'un affichage des motifs SVI dans le tableau de bord.
- Amélioration de l'affichage des FEI assignées pour les SVI.
- Correction du tri des FEI (#189).
- Correction de l'affichage des champs automatiques lors de la fermeture d'une FEI.
- Amélioration du chargement des entités et des utilisateurs.
- Ajout d'une vue de débogage FEI.
- Correction de l'affichage du message d'aide pour les lots.
- Ajout d'une gestion des utilisateurs administrateurs.
- Ajout d'un onglet administrateur.
- Amélioration de la gestion des carcasses et de leur transmission.
- Correction de la pagination.
- Amélioration de la gestion des utilisateurs non activés.

### Évolutions techniques
- Refactorisation de l'architecture de synchronisation locale-first avec un nouveau endpoint `/sync` pour les requêtes en masse.
- Extraction de la logique de sauvegarde des FEI et des carcasses dans des fonctions dédiées.
- Amélioration de la gestion des effets de bord dans les contrôleurs FEI et carcasses.
- Optimisation du chargement des entités pour éviter les problèmes de concurrence.
- Correction d'une condition de course lors de la transmission des données.
- Mise à jour de la documentation CLAUDE.md pour refléter l'architecture locale-first.
- Amélioration de la gestion des données en local pour éviter les problèmes de concurrence.
- Correction de la gestion des données dans IndexedDB.
- Suppression de l'utilisation de `stringify` dans IndexedDB.
- Amélioration de la gestion des relations entre les entités.
- Correction de la gestion du cache administrateur.

### Autres changements
- Mise à jour des dépendances : `minimatch`, `@getbrevo/brevo`, `tar`, `ajv`.
- Correction de la configuration de gitignore.
- Ajout de tests pour les relations.
- Suppression de Cailles et Oies de la liste des espèces.
- Nettoyage du code et refactorisation de certains composants.
- Amélioration de la qualité du code avec des linters.
- Correction de la gestion des types.
- Suppression de code inutile.
- Renommage de certains contrôleurs.
- Ajout de commentaires et de documentation.
