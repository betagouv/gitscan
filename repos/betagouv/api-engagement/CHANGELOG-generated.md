## Changelog : api-engagement (30 derniers jours, au 19 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des règles de diffusion des missions, l'accessibilité de l'interface utilisateur, et la correction de plusieurs bugs, notamment sur la plateforme et l'API. Des optimisations ont également été apportées à l'enrichissement des missions et à l'intégration avec des services tiers.

### Évolutions fonctionnelles
- Amélioration de l'accessibilité de l'interface utilisateur du back-office, notamment avec des corrections RGAA. [#1179](https://github.com/betagouv/api-engagement/issues/1179)
- Ajout de badges de compensation sur la plateforme. [#1173](https://github.com/betagouv/api-engagement/issues/1173)
- Affichage des règles de diffusion dans le tableau de bord de l'éditeur. [#1151](https://github.com/betagouv/api-engagement/issues/1151)
- Amélioration de la gestion des filtres et des valeurs de champs dans les règles de diffusion. [#1111](https://github.com/betagouv/api-engagement/issues/1111)
- Possibilité de filtrer les diffuseurs par valeur de champ dans les règles de diffusion. [#1111](https://github.com/betagouv/api-engagement/issues/1111)
- Amélioration de la page de détails des missions sur la plateforme. [#1081](https://github.com/betagouv/api-engagement/issues/1081)
- Refonte de la page d'accueil mobile et des témoignages. [#1060](https://github.com/betagouv/api-engagement/issues/1060)
- Ajout de la possibilité de gérer plusieurs adresses sur la plateforme. [#1114](https://github.com/betagouv/api-engagement/issues/1114)
- Amélioration de la gestion des critères de mot de passe et des champs de formulaire. [#1086](https://github.com/betagouv/api-engagement/issues/1086), [#1087](https://github.com/betagouv/api-engagement/issues/1087), [#1088](https://github.com/betagouv/api-engagement/issues/1088), [#1089](https://github.com/betagouv/api-engagement/issues/1089), [#1090](https://github.com/betagouv/api-engagement/issues/1090)

### Évolutions techniques
- Refactorisation de la gestion des règles de diffusion, avec stockage de l'ID de l'organisation publiant. [#1183](https://github.com/betagouv/api-engagement/issues/1183)
- Suppression de l'utilisation des tables `publisher_diffusion`. [#1135](https://github.com/betagouv/api-engagement/issues/1135)
- Amélioration du middleware d'accès aux éditeurs. [#1157](https://github.com/betagouv/api-engagement/issues/1157)
- Optimisation de l'enrichissement des missions pour éviter les injections. [#1141](https://github.com/betagouv/api-engagement/issues/1141)
- Mise en place d'une file d'attente pour l'enrichissement des missions, avec gestion des erreurs et des limitations de débit. [#1073](https://github.com/betagouv/api-engagement/issues/1073)
- Ajout d'une file d'attente des lettres mortes pour les jobs. [#1116](https://github.com/betagouv/api-engagement/issues/1116)
- Amélioration de la configuration de Typesense pour la production. [#1068](https://github.com/betagouv/api-engagement/issues/1068)
- Suppression de l'utilisation de taxonomies legacy. [#1079](https://github.com/betagouv/api-engagement/issues/1079)
- Mise à jour des dépendances (actions/checkout, docker/build-push-action, docker/login-action, react-toastify, etc.).
- Amélioration de la configuration CI/CD.
- Suppression de code obsolète.

### Autres changements
- Amélioration de la documentation des règles de diffusion. [#1142](https://github.com/betagouv/api-engagement/issues/1142)
- Correction de plusieurs bugs mineurs et améliorations de la qualité du code.
- Ajout d'un paramètre de débogage pour afficher un bouton de débogage sur la plateforme. [#1126](https://github.com/betagouv/api-engagement/issues/1126)
- Ajout d'un fichier `AGENTS.md` pour la plateforme. [#1082](https://github.com/betagouv/api-engagement/issues/1082)
- Publication des versions v1.13.0, v1.12.0, v1.11.0, v1.10.0, v1.9.3, v1.9.2, v1.9.1 et v1.9.0.
