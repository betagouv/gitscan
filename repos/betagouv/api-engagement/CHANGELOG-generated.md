## Changelog : api-engagement (30 derniers jours, au 9 juin 2026)

### Résumé
Ce mois-ci, l'API Engagement a bénéficié d'améliorations significatives en termes de gestion des missions, notamment concernant leur diffusion et leur enrichissement. Des corrections ont été apportées pour améliorer la robustesse de l'API et du back-office, ainsi que des optimisations pour la gestion des files d'attente et des erreurs. L'interface utilisateur de la plateforme a également été améliorée, notamment en termes d'accessibilité et d'expérience utilisateur.

### Évolutions fonctionnelles
- Ajout d'un mécanisme de diffusion des missions basé sur les règles de publication des diffuseurs [#1110](https://github.com/betagouv/api-engagement/pulls/1110).
- Amélioration de la recherche d'organisations parentes dans l'API [#1119](https://github.com/betagouv/api-engagement/issues/1119).
- Possibilité de gérer plusieurs adresses pour une plateforme [#1114](https://github.com/betagouv/api-engagement/issues/1114).
- Amélioration de la gestion des erreurs et ajout d'une file d'attente pour les messages en erreur [#1113](https://github.com/betagouv/api-engagement/issues/1113) et [#1116](https://github.com/betagouv/api-engagement/issues/1116).
- Ajout d'un système de limitation du taux d'appels (rate limit) basé sur l'adresse IP pour protéger l'API [#1075](https://github.com/betagouv/api-engagement/issues/1075).
- Ajout de journaux d'audit pour suivre les actions effectuées sur l'API [#1019](https://github.com/betagouv/api-engagement/issues/1019).
- Amélioration de l'interface utilisateur de la plateforme : refonte de la page des résultats de recherche, amélioration de l'accessibilité du quiz et des missions [#1060](https://github.com/betagouv/api-engagement/issues/1060), [#1084](https://github.com/betagouv/api-engagement/issues/1084), [#1058](https://github.com/betagouv/api-engagement/issues/1058), [#1057](https://github.com/betagouv/api-engagement/issues/1057), [#1055](https://github.com/betagouv/api-engagement/issues/1055), [#1054](https://github.com/betagouv/api-engagement/issues/1054), [#1053](https://github.com/betagouv/api-engagement/issues/1053).
- Amélioration des formulaires d'authentification et de gestion de compte avec des attributs d'autocomplétion et une meilleure gestion des erreurs [#1090](https://github.com/betagouv/api-engagement/issues/1090), [#1089](https://github.com/betagouv/api-engagement/issues/1089), [#1088](https://github.com/betagouv/api-engagement/issues/1088), [#1087](https://github.com/betagouv/api-engagement/issues/1087), [#1086](https://github.com/betagouv/api-engagement/issues/1086).

### Évolutions techniques
- Refactorisation de la logique d'enrichissement des missions pour limiter les mises à jour inutiles [#1120](https://github.com/betagouv/api-engagement/issues/1120).
- Remplacement de l'exclusion de diffusion par un moteur basé sur des règles [#1078](https://github.com/betagouv/api-engagement/issues/1078).
- Amélioration de la configuration Typesense pour la production [#1068](https://github.com/betagouv/api-engagement/issues/1068).
- Suppression du modèle de taxonomie hérité [#1079](https://github.com/betagouv/api-engagement/issues/1079).
- Ajout de tests et de workflows CI pour la plateforme [#1085](https://github.com/betagouv/api-engagement/issues/1085).
- Mise à jour des dépendances : React Toastify, Docker actions, Node.js [#983](https://github.com/betagouv/api-engagement/issues/983), [#1076](https://github.com/betagouv/api-engagement/issues/1076), [#1071](https://github.com/betagouv/api-engagement/issues/1071), [#1022](https://github.com/betagouv/api-engagement/issues/1022).
- Correction de problèmes liés à la configuration de Terraform [#1106](https://github.com/betagouv/api-engagement/issues/1106).

### Autres changements
- Correction d'un bug lié à la correspondance insensible à la casse des champs dans les règles du widget [#1117](https://github.com/betagouv/api-engagement/issues/1117).
- Correction d'un problème d'affichage de la page d'organisation [#1119](https://github.com/betagouv/api-engagement/issues/1119).
- Ajout d'un script pour générer le changelog [#1112](https://github.com/betagouv/api-engagement/issues/1112).
- Ajout d'un fichier AGENTS.md pour documenter les agents de la plateforme [#1082](https://github.com/betagouv/api-engagement/issues/1082).
- Amélioration de la gestion des erreurs et ajout d'un mécanisme de relance pour les tâches échouées [#1108](https://github.com/betagouv/api-engagement/issues/1108).
- Correction d'un bug dans l'API pour les missions de type incorrect [#1080](https://github.com/betagouv/api-engagement/issues/1080).
- Ajout de la possibilité de définir des règles de publication pour les missions [#1061](https://github.com/betagouv/api-engagement/issues/1061).
