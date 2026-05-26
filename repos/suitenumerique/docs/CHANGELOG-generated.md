## Changelog : docs (30 derniers jours, au 2026-05-21)

### Résumé
Ce changelog présente les améliorations apportées au projet Docs au cours des 30 derniers jours. Les changements incluent des améliorations de la configuration OIDC, des corrections de bugs, des optimisations de performance (notamment avec le passage à `uv` pour la gestion des dépendances), l'ajout de support pour le déploiement sur des plateformes PaaS comme Scalingo, et des améliorations de l'expérience utilisateur, notamment dans la gestion des commentaires et de la collaboration.

### Évolutions fonctionnelles
- Ajout du support pour le déploiement sur des plateformes PaaS, testé avec Scalingo. [#2293](https://github.com/suitenumerique/docs/issues/2293)
- Possibilité de configurer l'endpoint utilisateur OIDC via le paramètre `OIDC_OP_USER_ENDPOINT_FORMAT`.
- Amélioration de la gestion des commentaires : correction de bugs liés à l'affichage et à la soumission. [#2273](https://github.com/suitenumerique/docs/issues/2273)
- Ajout d'un squelette de chargement pour le contenu afin d'améliorer l'expérience utilisateur pendant le chargement. [#2254](https://github.com/suitenumerique/docs/issues/2254)
- Ajout d'un lien manquant dans la description de l'onboarding. [#2233](https://github.com/suitenumerique/docs/issues/2233)
- Support de la création de sous-documents à partir de fichiers. [#1987](https://github.com/suitenumerique/docs/issues/1987)
- Mise à jour de Docspec vers la version 3.0.0, avec adaptation de l'API du convertisseur. [#2220](https://github.com/suitenumerique/docs/issues/2220)
- Possibilité de configurer l'URI de la requête d'authentification forward. [#2241](https://github.com/suitenumerique/docs/issues/2241)

### Évolutions techniques
- Migration de la gestion des dépendances de `pip` à `uv` pour l'ensemble du projet (build, actions, core).
- Utilisation de runners ARM64 pour la construction d'images pour l'architecture ARM64.
- Ajout d'une étape Trivy pour l'analyse de vulnérabilités.
- Utilisation de `uvicorn` pour exécuter l'application Django en environnement de développement.
- Mise à jour de Next.js vers la version 16.2.6 (correction de sécurité). [#2271](https://github.com/suitenumerique/docs/issues/2271)
- Mise à jour de la librairie `uuid` vers la version 14 (correction de sécurité). [#2271](https://github.com/suitenumerique/docs/issues/2271)
- Mise à jour de la librairie `axios` vers la version 1.15.2 (correction de sécurité). [#2271](https://github.com/suitenumerique/docs/issues/2271)
- Amélioration de la gestion des erreurs et des conditions de course dans le backend.
- Refactoring de modules backend pour une meilleure organisation.
- Mise en place d'un système de retry pour les verrous de création de documents.
- Ajout d'en-têtes ETag et Last-Modified pour la récupération de contenu.
- Suppression d'endpoints dépréciés.
- Amélioration de la gestion des requêtes de streaming S3.
- Suppression du contenu des réponses de documents (pour optimiser les performances).

### Autres changements
- Correction de quelques problèmes de "flakiness" dans les tests E2E.
- Mise à jour des chaînes de traduction.
- Correction de bugs mineurs dans l'interface utilisateur.
- Correction de problèmes liés à l'affichage de l'interface utilisateur sur différents écrans.
- Suppression de commentaires inutiles dans le code frontend.
- Mise à jour des dépendances JavaScript.
- Correction de problèmes de validation d'emojis.
- Amélioration de la gestion des erreurs 5xx pour l'accessibilité.
- Amélioration de l'accessibilité des résultats de recherche de documents.
- Correction de problèmes de clipping de modales.
- Amélioration de la gestion des accès et des invitations lors du déplacement de documents.
- Ajout de la possibilité d'utiliser Mistral SDK pour les fonctionnalités d'IA.
- Amélioration du prompt pour la traduction automatique héritée.
- Mise à jour de la documentation UPGRADE.md pour refléter les changements majeurs.
- Dispatch de la version de l'application vers Posthog.
- Amélioration de la synchronisation front/back pour éviter les rechargements inutiles.
- Ajout de support hors ligne pour le contenu via Service Worker.
- Amélioration de la gestion des requêtes fallback dans le Service Worker.
- Adaptation des types pour les mises à jour de Cunningham, ui-kit et typescript.
- Adaptation du CSS pour Blocknote v0.49.
- Adaptation des types pour i18next v26.
