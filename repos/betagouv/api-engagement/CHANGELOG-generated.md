## Changelog : api-engagement (30 derniers jours, au 11 juin 2026)

### Résumé
Ce mois-ci, l'API Engagement a bénéficié d'améliorations significatives en termes de diffusion des missions, d'analytics et d'expérience utilisateur sur la plateforme. Des corrections de bugs ont également été apportées pour améliorer la stabilité et la fiabilité du système. L'ajout de règles de diffusion basées sur les diffuseurs permet un ciblage plus précis des missions.

### Évolutions fonctionnelles
- Ajout d'un paramètre de débogage pour afficher un bouton de débogage sur la plateforme ([#1126](https://github.com/betagouv/api-engagement/pull/1126)).
- Amélioration de la gestion des diffuseurs dans les règles de diffusion, permettant de filtrer par valeur de champ ([#1111](https://github.com/betagouv/api-engagement/pull/1111)).
- Implémentation d'un moteur de règles de diffusion pour remplacer l'exclusion manuelle des diffuseurs ([#1078](https://github.com/betagouv/api-engagement/pull/1078)).
- Amélioration du contenu des emails de matching de missions (en-tête et liste) ([#1118](https://github.com/betagouv/api-engagement/pull/1118)).
- Ajout de la possibilité d'utiliser les règles de diffusion pour le service Grimp ([#1107](https://github.com/betagouv/api-engagement/pull/1107)).
- Utilisation de la diffusion par éditeur dans l'endpoint de navigation des missions ([#1110](https://github.com/betagouv/api-engagement/pull/1110)).
- Amélioration de l'interface utilisateur du quiz et de la page de résultats sur la plateforme ([#1074](https://github.com/betagouv/api-engagement/pull/1074), [#1058](https://github.com/betagouv/api-engagement/pull/1058), [#1057](https://github.com/betagouv/api-engagement/pull/1057), [#1055](https://github.com/betagouv/api-engagement/pull/1055), [#1054](https://github.com/betagouv/api-engagement/pull/1054), [#1053](https://github.com/betagouv/api-engagement/pull/1053)).
- Ajout de la possibilité de gérer plusieurs adresses sur la liste des missions ([#1114](https://github.com/betagouv/api-engagement/pull/1114)).
- Amélioration de la gestion des champs requis et des erreurs dans les composants de formulaire de l'application ([#1090](https://github.com/betagouv/api-engagement/pull/1090)).
- Amélioration de l'accessibilité de la plateforme (étiquettes, champs, progress bar, dialogs) ([#1087](https://github.com/betagouv/api-engagement/pull/1087), [#1086](https://github.com/betagouv/api-engagement/pull/1086), [#1084](https://github.com/betagouv/api-engagement/pull/1084)).

### Évolutions techniques
- Refactorisation de l'export des données analytics pour utiliser un seul appel ([#1145](https://github.com/betagouv/api-engagement/pull/1145)).
- Optimisation de l'enrichissement des missions pour limiter les mises à jour inutiles ([#1120](https://github.com/betagouv/api-engagement/pull/1120)).
- Amélioration de la gestion des erreurs et de la résilience de l'enfilement des missions ([#1108](https://github.com/betagouv/api-engagement/pull/1108)).
- Ajout d'une file d'attente de lettres mortes pour améliorer la robustesse du système ([#1113](https://github.com/betagouv/api-engagement/pull/1113)).
- Mise en place d'une limite de débit IP sur les routes de l'API de la plateforme ([#1075](https://github.com/betagouv/api-engagement/pull/1075)).
- Configuration de Typesense pour la production ([#1068](https://github.com/betagouv/api-engagement/pull/1068)).
- Ajout de tests et de workflows lint pour la plateforme ([#1066](https://github.com/betagouv/api-engagement/pull/1066)).
- Refactorisation de la gestion de la diffusion des missions ([#1079](https://github.com/betagouv/api-engagement/pull/1079)).
- Suppression de la taxonomie legacy ([#1069](https://github.com/betagouv/api-engagement/pull/1069)).

### Autres changements
- Amélioration de la documentation des règles de diffusion ([#1142](https://github.com/betagouv/api-engagement/pull/1142)).
- Correction de bugs mineurs et améliorations de la stabilité.
- Mise à jour des dépendances (actions/checkout, react-toastify, docker/build-push-action, docker/login-action, actions/setup-node).
- Publication des versions v1.11.0, v1.10.0, v1.9.3, v1.9.2, v1.9.1 et v1.9.0.
- Ajout d'un fichier AGENTS.md.
- Correction de problèmes de merge et de conflits.
