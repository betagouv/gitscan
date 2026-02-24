## Changelog : reva (30 derniers jours)

### Résumé
Les dernières semaines ont été marquées par des améliorations significatives de l'intégration France Connect, avec une gestion plus complète des informations utilisateur et une simplification du processus d'inscription. Des corrections et des améliorations ont également été apportées à l'administration, à la génération de documents VAE et à l'interface utilisateur, notamment pour les cohortes VAE collectives. Plusieurs optimisations et refactorings techniques ont été réalisés pour améliorer la sécurité, la performance et la maintenabilité du code.

### Évolutions fonctionnelles

*   **France Connect :** Amélioration de l'intégration avec France Connect, incluant la gestion des informations de nationalité, de code postal, d'adresse et de numéro de téléphone. Création automatique de candidatures lors de la connexion via France Connect. (#d1a0587, #d593161, #4a67b7b, #21f3a9e)
*   **VAE Collective :** Ajout de la possibilité de sélectionner plusieurs certifications pour une cohorte VAE collective. Ajout d'une page de sélection des certifications avec une interface améliorée. (#262e066, #66bbaee, #130586c, #b74c66e)
*   **Administration :** Amélioration de la confirmation de la complétion du DF par les organismes certificateurs. Ajout d'un modèle de confirmation pour la complétion du DF. (#77c1234)
*   **Génération de documents :** Correction de problèmes de couleurs dans la génération du DF dématérialisé. (#0246659)
*   **Interface utilisateur :** Amélioration de l'interface des pages de statut, notamment sur mobile. Ajout d'une page de confirmation d'inscription. (#21cac93, #f068acb, #d290c70)
*   **Candidature :** Simplification du processus de création de candidature et suppression de la prise en charge de l'ID de certification. (#420c8c2)
*   **FAQ :** Correction de l'espacement réactif sur la page FAQ. (#92f3659)

### Évolutions techniques

*   **Sécurité :** Intégration de plugins Fastify pour la gestion des cookies et la limitation du taux de requêtes (rate limiting) pour renforcer la sécurité. (#21f3a9e)
*   **Refactoring :** Refactorisation du code pour améliorer la lisibilité, la maintenabilité et la performance, notamment dans les modules d'authentification et de gestion des candidatures. (#55e3b13, #1107b52, #76b0d2e, #47ebdc5, #c44c6b2, #311a945, #1086438, #cada316, #3718a0b, #e6e132b)
*   **Dépendances :** Mise à jour de plusieurs dépendances, notamment Fastify, Webpack, Lodash et les librairies React. (#1d04048, #d76c9b4, #feea1ed, #c7f87a1, #fb25daa, #9e369fa, #d340887, #a010319, #1b75b65, #6534b93)
*   **Tests :** Ajout et mise à jour de tests unitaires et d'intégration pour garantir la qualité du code et la couverture des fonctionnalités. (#79ddc12, #86ebfcd, #bcbe381, #ed7dda9, #995d15e, #431164a, #5294b18)

### Autres changements

*   **Documentation :** Mise à jour de la documentation pour refléter les changements apportés au code.
*   **Configuration :** Ajout de variables d'environnement pour configurer le comportement de l'application.
*   **Nettoyage de code :** Suppression de code obsolète et amélioration de la structure du code. (#c57738a, #39fb0cd)
*   **Metabase :** Ajout d'une nouvelle configuration de tableau de bord Metabase pour le CPNEFP de la Métallurgie. (#1056e3b)
*   **.gitignore :** Mise à jour du fichier .gitignore pour ignorer les fichiers liés à Claude. (#c57738a)
*   **Feature Flags :** Ajout d'un feature flag pour activer la sélection multiple de certifications dans les cohortes VAE collectives. (#d2eed02)
