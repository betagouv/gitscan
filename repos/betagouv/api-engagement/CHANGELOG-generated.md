## Changelog : api-engagement (30 derniers jours, au 12 juin 2026)

### Résumé
Ce mois-ci, l'API Engagement a bénéficié d'améliorations significatives en termes de diffusion des missions, d'analytics, d'accessibilité et de performance. Des corrections ont été apportées pour améliorer la robustesse du système et l'expérience utilisateur, notamment sur la plateforme et le back-office. L'ajout de règles de diffusion plus fines et l'amélioration de la gestion des données analytiques sont également des points forts de cette période.

### Évolutions fonctionnelles
- Amélioration de l'accessibilité (RGAA) sur l'ensemble du back-office [#1128](https://github.com/betagouv/api-engagement/issues/1128).
- Ajout d'un paramètre de débogage pour afficher un bouton de débogage sur la plateforme [#1126](https://github.com/betagouv/api-engagement/issues/1126).
- Possibilité de filtrer les diffuseurs par valeur de champ dans les règles de diffusion [#1111](https://github.com/betagouv/api-engagement/issues/1111).
- Amélioration de la gestion des adresses multiples sur la plateforme [#1114](https://github.com/betagouv/api-engagement/issues/1114).
- Ajout d'un bouton pour afficher le contenu de l'email de matching de mission [#1118](https://github.com/betagouv/api-engagement/issues/1118).
- Amélioration de la compatibilité de l'endpoint v2/activity pour les diffuseurs [#1110](https://github.com/betagouv/api-engagement/issues/1110).
- Amélioration de l'interface utilisateur du quiz et des missions sur la plateforme [#1053](https://github.com/betagouv/api-engagement/issues/1053), [#1054](https://github.com/betagouv/api-engagement/issues/1054), [#1055](https://github.com/betagouv/api-engagement/issues/1055), [#1057](https://github.com/betagouv/api-engagement/issues/1057), [#1058](https://github.com/betagouv/api-engagement/issues/1058), [#1084](https://github.com/betagouv/api-engagement/issues/1084).
- Amélioration des champs de formulaire et de la gestion des erreurs sur l'application [#1086](https://github.com/betagouv/api-engagement/issues/1086), [#1087](https://github.com/betagouv/api-engagement/issues/1087), [#1088](https://github.com/betagouv/api-engagement/issues/1088), [#1089](https://github.com/betagouv/api-engagement/issues/1089), [#1090](https://github.com/betagouv/api-engagement/issues/1090).

### Évolutions techniques
- Refactor de l'export des données analytiques pour améliorer la performance [#1145](https://github.com/betagouv/api-engagement/issues/1145).
- Mise en place d'une file d'attente de lettres mortes pour l'API [#1113](https://github.com/betagouv/api-engagement/issues/1113).
- Amélioration de la gestion des règles de diffusion, avec un moteur basé sur des règles [#1078](https://github.com/betagouv/api-engagement/issues/1078).
- Suppression de l'exclusion des diffuseurs par `publisher_diffusion_exclusion` au profit du nouveau moteur de règles.
- Optimisation de l'utilisation de la diffusion pour Grimpio [#1107](https://github.com/betagouv/api-engagement/issues/1107).
- Amélioration de la gestion des requêtes avec limitation du taux (rate limiting) sur les routes de l'API de la plateforme [#1075](https://github.com/betagouv/api-engagement/issues/1075).
- Configuration de Typesense pour la production [#1068](https://github.com/betagouv/api-engagement/issues/1068).
- Amélioration de la gestion des dépendances et des versions de Python et dbt-core [#1147](https://github.com/betagouv/api-engagement/issues/1147).
- Refactor de la gestion des enrichissements de missions pour limiter les mises à jour inutiles [#1120](https://github.com/betagouv/api-engagement/issues/1120).
- Suppression de la taxonomie legacy [#1079](https://github.com/betagouv/api-engagement/issues/1079).

### Autres changements
- Amélioration de la documentation des règles de diffusion [#1142](https://github.com/betagouv/api-engagement/issues/1142).
- Nettoyage du script de génération du changelog [#1137](https://github.com/betagouv/api-engagement/issues/1137).
- Ajout d'un fichier `AGENTS.md` pour la plateforme [#1125](https://github.com/betagouv/api-engagement/issues/1125).
- Correction de plusieurs conflits de merge et réversions de commits [#1131](https://github.com/betagouv/api-engagement/issues/1131), [#1140](https://github.com/betagouv/api-engagement/issues/1140).
- Correction de l'ordre des colonnes pour les tests sqlfluff [#1131](https://github.com/betagouv/api-engagement/issues/1131).
- Corrections de typographie sur la page d'accueil [#1127](https://github.com/betagouv/api-engagement/issues/1127).
