## Changelog : docs (30 derniers jours, au 27 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur avec l'ajout d'un panneau latéral pour les commentaires et la table des matières, ainsi que des corrections d'accessibilité et de stabilité. Des améliorations techniques importantes ont été apportées à l'infrastructure de build et de déploiement, ainsi qu'à la gestion des dépendances. Des corrections de sécurité ont également été implémentées.

### Évolutions fonctionnelles
- Ajout d'un panneau latéral pour les commentaires, améliorant l'interaction et la collaboration sur les documents. [#2279](https://github.com/suitenumerique/docs/issues/2279)
- Ajout d'un panneau latéral droit pour la table des matières, facilitant la navigation dans les documents longs.
- Amélioration de la recherche : ajout d'une "breadcrumb" dans les résultats de recherche pour une meilleure navigation.
- Possibilité de créer un sous-document à partir d'un fichier. [#1987](https://github.com/suitenumerique/docs/issues/1987)
- Ajout d'un support de déploiement sur PaaS, testé avec Scalingo. [#2293](https://github.com/suitenumerique/docs/issues/2293)
- Ajout d'un indicateur de chargement (skeleton) lors du chargement du contenu. [#2254](https://github.com/suitenumerique/docs/issues/2254)
- Ajout de la possibilité de configurer l'endpoint utilisateur pour l'authentification OIDC. [#24d58a1](https://github.com/suitenumerique/docs/commit/24d58a1)

### Évolutions techniques
- Migration de l'outil de build de `pip` à `uv` pour une meilleure performance et gestion des dépendances.
- Mise à jour de l'image Nginx vers la dernière version pour des raisons de sécurité et de performance.
- Amélioration de la gestion des erreurs de concurrence lors de la création de documents.
- Utilisation de runners ARM64 pour la construction d'images pour l'architecture ARM64.
- Mise en place d'une analyse de vulnérabilités avec Trivy dans le pipeline CI.
- Refactorisation de modules backend pour une meilleure organisation du code.
- Mise à jour de Blocknote à la version 0.51.1. [#41f76eb](https://github.com/suitenumerique/docs/commit/41f76eb)
- Mise à jour de Next.js à la version 16.2.6 (correction de sécurité). [#0501551](https://github.com/suitenumerique/docs/commit/0501551)
- Mise à jour de Axios à la version 1.15.2 (correction de sécurité). [#85128c7](https://github.com/suitenumerique/docs/commit/85128c7)

### Autres changements
- Corrections d'accessibilité : amélioration de l'accessibilité des avatars dans la modale de partage. [#2324](https://github.com/suitenumerique/docs/issues/2324)
- Correction de bugs liés à l'affichage des commentaires et de la table des matières.
- Amélioration de la gestion des erreurs et des conditions de course.
- Corrections de sécurité : validation de l'ID du document fourni par l'utilisateur. [#8d42f81](https://github.com/suitenumerique/docs/commit/8d42f81)
- Prévention de la réécriture des commentaires d'autres utilisateurs par les administrateurs. [#3264e29](https://github.com/suitenumerique/docs/commit/3264e29)
- Suppression de commentaires inutiles dans le code.
- Mise à jour des chaînes de traduction.
- Amélioration des tests E2E pour réduire les faux positifs.
- Suppression de code obsolète lié à une ancienne version de Cunningham.
- Correction de problèmes de compatibilité avec des bibliothèques mises à jour.
- Ajout de tests pour la compatibilité avec l'architecture ARM64.
- Correction de problèmes de gestion des espaces blancs lors du déplacement de documents.
- Validation des emojis pour les réactions.
- Amélioration de la gestion des erreurs CORS.
- Suppression de la logique de suppression manuelle des accès lors du déplacement d'un document.
- Correction de problèmes d'affichage de la table des matières.
- Correction de problèmes de scroll de la table des matières.
- Correction de problèmes liés à la gestion des couleurs lors de la collaboration.
- Amélioration de la gestion des liens dans le mode d'impression.
- Adaptation des types pour les mises à jour de Cunningham, ui-kit et typescript.
- Correction de problèmes de redimensionnement de la barre latérale pour les lecteurs d'écran.
- Correction de problèmes de chargement des commentaires.
- Correction de problèmes de clipping de la modale d'interlinking.
- Correction de problèmes de gestion des membres sur les petits écrans.
- Correction de problèmes de chargement de jwks.
