## Changelog : docs (30 derniers jours, au 13 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la stabilité, de la performance et de la sécurité de la plateforme. Des optimisations ont été apportées à la gestion des fichiers, à la collaboration en temps réel et à l'infrastructure sous-jacente. Une migration vers de nouveaux outils de gestion des dépendances et une mise à jour majeure de la spécification des documents (DocSpec) sont également notables.

### Évolutions fonctionnelles
- Ajout d'un lien vers la documentation dans le menu d'aide.
- Amélioration de l'expérience utilisateur avec l'ajout de squelettes de chargement pour le contenu.
- Correction de problèmes d'affichage et de fonctionnement des liens internes (interlinking).
- Possibilité de créer des sous-documents à partir de fichiers.
- Support de la création de sous-documents à partir de fichiers [#1987](https://github.com/suitenumerique/docs/issues/1987).
- Amélioration de la gestion des commentaires et des transactions associées.
- Ajout de la possibilité d'utiliser une nouvelle fonctionnalité d'IA via le SDK Mistral.
- Amélioration de la gestion des accès et des invitations lors du déplacement de documents.

### Évolutions techniques
- Migration de la gestion des dépendances de `pip` à `uv` pour l'ensemble du projet (core, actions).
- Mise à jour de la spécification des documents (DocSpec) vers la version 3.0.0, nécessitant une adaptation de l'API de conversion.
- Utilisation de l'outil `trivy` pour l'analyse de vulnérabilités.
- Amélioration de l'infrastructure CI/CD avec l'utilisation de runners `arm64` pour la construction d'images.
- Refactorisation de certains modules backend pour une meilleure organisation et maintenabilité.
- Mise en place d'une stratégie de retry pour la création de documents afin d'éviter les blocages.
- Implémentation d'en-têtes `etag` et `last_modified` pour optimiser la récupération du contenu.
- Utilisation de `uvicorn` pour exécuter l'application Django en environnement de développement.
- Ajout de support pour le streaming du contenu des fichiers S3 via un endpoint dédié.
- Suppression de contenu inutile dans les réponses de l'API.
- Amélioration de la gestion des erreurs 5xx pour l'accessibilité.
- Mise à jour des dépendances `axios`, `lxml` et `uuid` pour corriger des failles de sécurité.

### Autres changements
- Mise à jour des traductions.
- Correction de problèmes de tests (flakiness).
- Amélioration de la gestion des logs en mode debug.
- Nettoyage du code et suppression de code obsolète.
- Adaptation des types TypeScript aux dernières versions des bibliothèques utilisées (i18next, Cunningham, ui-kit).
- Mise à jour de la configuration pour l'environnement Tilt.
- Correction de problèmes de positionnement des éléments dans l'interface utilisateur.
- Amélioration de la gestion des connexions WebSocket.
- Ajout de la possibilité de configurer l'URI de la requête d'authentification forward.
- Correction de problèmes liés à l'importation de fichiers CSV.
- Amélioration de la gestion des accès lors de la création de documents.
- Correction de problèmes de validation des emojis.
- Suppression de la logique de suppression manuelle des accès depuis le hook de déplacement de document.
- Correction de la gestion des espaces blancs dans les URLs des médias.
- Ajout de la possibilité de définir un timeout d'inactivité pour les connexions WebSocket.
