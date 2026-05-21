## Changelog : docs (30 derniers jours, au 2026-05-19)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la stabilité et la performance de la plateforme, avec des corrections de bugs significatives, notamment concernant la gestion des documents, la collaboration et l'intégration d'IA. Des optimisations ont été apportées à l'infrastructure et au processus de construction pour améliorer l'efficacité et la compatibilité. L'ajout de support pour le déploiement sur des plateformes PaaS comme Scalingo est également notable.

### Évolutions fonctionnelles
- Ajout du support pour le déploiement sur des plateformes PaaS, testé avec Scalingo [#2293](https://github.com/suitenumerique/docs/issues/2293).
- Amélioration de la création de sous-documents à partir de fichiers [#1987](https://github.com/suitenumerique/docs/issues/1987).
- Ajout d'un squelette de chargement pour le contenu, améliorant l'expérience utilisateur pendant le chargement des documents.
- Mise en place d'une gestion améliorée des interlinkings, avec des corrections de bugs et une amélioration de l'interface utilisateur.
- Possibilité d'utiliser une nouvelle fonctionnalité d'IA via le SDK Mistral.
- Amélioration de la gestion des erreurs 5xx avec une meilleure accessibilité.
- Ajout de la possibilité de configurer l'URI de la requête d'authentification forward.

### Évolutions techniques
- Migration du système de construction de `pip` vers `uv`, améliorant la gestion des dépendances et la performance.
- Mise à jour de l'image Nginx dans le Dockerfile vers la dernière version.
- Utilisation de runners arm64 pour la construction d'images pour l'architecture arm64.
- Mise en place d'un job Trivy pour l'analyse de vulnérabilités.
- Refactorisation de la gestion des erreurs et des conditions de course dans le backend.
- Mise à jour de la version de Next.js vers v16.2.6 (incluant des correctifs de sécurité).
- Mise à jour de la version de lxml vers v6.1.0 (incluant des correctifs de sécurité).
- Mise à jour de la version de uuid vers v14 (incluant des correctifs de sécurité).
- Mise à jour de la version de axios vers v1.15.2 (incluant des correctifs de sécurité).
- Mise à jour de la version de docspec vers v3.0.0 et adaptation de l'API du convertisseur.
- Suppression de l'endpoint déprécié `descendants`.
- Suppression de l'envoi du contenu du document dans les réponses API.
- Ajout d'un endpoint dédié pour la mise à jour du contenu des documents.
- Implémentation des headers `etag` et `last_modified` pour la récupération du contenu.
- Utilisation d'Uvicorn pour exécuter l'application Django en environnement de développement.

### Autres changements
- Correction de bugs mineurs concernant l'affichage, la gestion des commentaires et la synchronisation des sessions.
- Mise à jour des chaînes de traduction.
- Amélioration de la gestion des erreurs et des logs.
- Suppression de commentaires inutiles dans le code frontend.
- Correction de la gestion des espaces blancs dans les URLs des médias.
- Suppression de la logique de suppression manuelle des accès depuis le hook de déplacement de document.
- Suppression d'un patch suite à une mise à niveau de Cunningham.
- Correction de l'affichage des liens dans le mode d'impression.
- Suppression de la gestion manuelle de la suppression d'accès dans le hook de déplacement de document.
- Correction de la gestion des flakiness dans les tests E2E.
- Mise à jour de la documentation UPGRADE.md pour refléter les changements majeurs.
- Suppression de la dépendance à `setuptools` et migration vers `uv_build`.
- Fix d'un problème de race condition lors de la création de documents.
- Fix d'un problème de race condition entre les requêtes GET et PATCH du contenu.
- Fix d'un problème de verrouillage de la table de création de documents.
- Suppression de la gestion du contenu dans les réponses API.
- Fix d'un problème de chargement des jwks url.
- Correction de la gestion des erreurs 401.
- Amélioration de la gestion des erreurs et des logs.
- Suppression de la logique de suppression manuelle des accès depuis le hook de déplacement de document.
- Correction de l'affichage des liens dans le mode d'impression.
- Suppression de la gestion manuelle de la suppression d'accès dans le hook de déplacement de document.
- Correction de la gestion des flakiness dans les tests E2E.
- Mise à jour de la documentation UPGRADE.md pour refléter les changements majeurs.
- Suppression de la dépendance à `setuptools` et migration vers `uv_build`.
- Fix d'un problème de race condition lors de la création de documents.
- Fix d'un problème de race condition entre les requêtes GET et PATCH du contenu.
- Fix d'un problème de verrouillage de la table de création de documents.
- Suppression de la gestion du contenu dans les réponses API.
- Fix d'un problème de chargement des jwks url.
- Correction de la gestion des erreurs 401.
- Amélioration de la gestion des erreurs et des logs.
- Suppression de la logique de suppression manuelle des accès depuis le hook de déplacement de document.
- Correction de l'affichage des liens dans le mode d'impression.
- Suppression de la gestion manuelle de la suppression d'accès dans le hook de déplacement de document.
- Correction de la gestion des flakiness dans les tests E2E.
- Mise à jour de la documentation UPGRADE.md pour refléter les changements majeurs.
- Suppression de la dépendance à `setuptools` et migration vers `uv_build`.
- Fix d'un problème de race condition lors de la création de documents.
- Fix d'un problème de race condition entre les requêtes GET et PATCH du contenu.
- Fix d'un problème de verrouillage de la table de création de documents.
- Suppression de la gestion du contenu dans les réponses API.
- Fix d'un problème de chargement des jwks url.
- Correction de la gestion des erreurs 401.
- Amélioration de la gestion des erreurs et des logs.
- Suppression de la logique de suppression manuelle des accès depuis le hook de déplacement de document.
- Correction de l'affichage des liens dans le mode d'impression.
- Suppression de la gestion manuelle de la suppression d'accès dans le hook de déplacement de document.
- Correction de la gestion des flakiness dans les tests E2E.
- Mise à jour de la documentation UPGRADE.md pour refléter les changements majeurs.
- Suppression de la dépendance à `setuptools` et migration vers `uv_build`.
- Fix d'un problème de race condition lors de la création de documents.
- Fix d'un problème de race condition entre les requêtes GET et PATCH du contenu.
- Fix d'un problème de verrouillage de la table de création de documents.
- Suppression de la gestion du contenu dans les réponses API.
- Fix d'un problème de chargement des jwks url.
- Correction de la gestion des erreurs 401.
- Amélioration de la gestion des erreurs et des logs.
- Suppression de la logique de suppression manuelle des accès depuis le hook de déplacement de document.
- Correction de l'affichage des liens dans le mode d'impression.
- Suppression de la gestion manuelle de la suppression d'accès dans le hook de déplacement de document.
- Correction de la gestion des flakiness dans les tests E2E.
- Mise à jour de la documentation UPGRADE.md pour refléter les changements majeurs.
- Suppression de la dépendance à `setuptools` et migration vers `uv_build`.
- Fix d'un problème de race condition lors de la création de documents.
- Fix d'un problème de race condition entre les requêtes GET et PATCH du contenu.
- Fix d'un problème de verrouillage de la table de création de documents.
- Suppression de la gestion du contenu dans les réponses API.
