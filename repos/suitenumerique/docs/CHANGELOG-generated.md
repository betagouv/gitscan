## Changelog : docs (30 derniers jours, au 29 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur avec l'ajout d'un panneau latéral pour les commentaires et la table des matières, ainsi que des corrections de bugs et des optimisations de performance. Des améliorations techniques ont été apportées à l'infrastructure de construction et de déploiement, ainsi qu'à la gestion des dépendances. La sécurité a également été renforcée avec des corrections et des validations supplémentaires.

### Évolutions fonctionnelles
- Ajout d'un panneau latéral pour les commentaires, améliorant l'accessibilité et l'organisation des discussions sur les documents. [#2279](https://github.com/suitenumerique/docs/issues/2279)
- Ajout d'un panneau latéral droit pour afficher la table des matières, facilitant la navigation dans les documents longs.
- Amélioration de la recherche : ajout d'une "breadcrumb" dans les résultats de recherche pour une meilleure navigation.
- Possibilité de créer un sous-document à partir d'un fichier. [#1987](https://github.com/suitenumerique/docs/issues/1987)
- Ajout d'un squelette de chargement pour le contenu, améliorant l'expérience utilisateur pendant le chargement des documents.
- Amélioration de l'accessibilité : ajout d'attributs `aria-hidden` aux SVG décoratifs dans la modale de partage. [#2324](https://github.com/suitenumerique/docs/issues/2324)
- Ajout de la possibilité de résoudre les threads de commentaires. [#2279](https://github.com/suitenumerique/docs/issues/2279)
- Ajout de la prise en charge de la création de sous-documents à partir de fichiers.

### Évolutions techniques
- Migration de l'outil de gestion des dépendances de `pip` à `uv` pour améliorer la performance et la fiabilité de la construction.
- Mise à jour de la version de Next.js vers v16.2.6, incluant des correctifs de sécurité.
- Utilisation de `uv_build` comme backend de construction.
- Amélioration de l'infrastructure CI/CD avec l'ajout de Trivy pour l'analyse de vulnérabilités.
- Utilisation de runners arm64 pour la construction d'images pour l'architecture arm64.
- Mise à jour de Blocknote vers la version 0.51.1.
- Centralisation des formats de conversion autorisés dans `ContentTypes`.
- Ajout de la prise en charge du déploiement sur PaaS, testé avec Scalingo.
- Configuration de l'environnement de développement Helm pour activer l'édition collaborative.
- Création d'un service et d'un déploiement dédiés pour le convertisseur Yjs.
- Utilisation d'une stratégie de nouvelle tentative pour gérer les blocages de table lors de la création de documents.

### Autres changements
- Correction de bugs liés à l'affichage des commentaires et de la table des matières.
- Correction de problèmes d'accessibilité.
- Mise à jour des chaînes de traduction.
- Amélioration de la gestion des erreurs et des messages d'alerte.
- Suppression de code obsolète.
- Correction de problèmes de compatibilité avec les mises à jour de Cunningham et de l'UI Kit.
- Mise à jour des types TypeScript pour s'adapter aux nouvelles versions des bibliothèques.
- Ajout de la configuration `COLLABORATION_WS_INACTIVITY_TIMEOUT` pour gérer la déconnexion des websockets.
- Amélioration de la gestion des erreurs lors de la conversion de documents Yjs vides.
- Correction d'un problème de race condition lors de la récupération et de la modification du contenu des documents.
- Validation de l'ID du document fourni par l'utilisateur pour assurer sa validité.
- Ajout de la possibilité de configurer l'endpoint utilisateur OIDC.
- Correction de la gestion des liens inter-documents en mode impression.
- Correction de problèmes de fluidité de l'interface utilisateur.
