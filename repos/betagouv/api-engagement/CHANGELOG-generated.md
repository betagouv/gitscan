## Changelog : api-engagement (30 derniers jours, au 2 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration du suivi des engagements via l'intégration d'un service de tracking (Posthog), l'optimisation de la recherche de missions et la gestion des règles de diffusion. Des corrections et des refactorings ont également été effectués pour améliorer la stabilité et la performance de l'API et de la plateforme. Des améliorations d'accessibilité ont été apportées à l'interface utilisateur.

### Évolutions fonctionnelles
- Ajout de la possibilité de filtrer les missions par dispositif. [#1211](https://github.com/betagouv/api-engagement/issues/1211)
- Amélioration de la gestion des règles de diffusion pour les éditeurs, avec la possibilité de les consulter et de les modifier dans le back-office. [#1151](https://github.com/betagouv/api-engagement/issues/1151)
- Intégration de Demarches Simplifiées pour l'enrichissement des missions. [#1154](https://github.com/betagouv/api-engagement/issues/1154)
- Ajout d'une extension Chrome pour faciliter l'interaction avec la plateforme. [#1178](https://github.com/betagouv/api-engagement/issues/1178)
- Amélioration de l'affichage des missions sur la carte et dans la liste. [#1207](https://github.com/betagouv/api-engagement/issues/1207)
- Ajout d'un lien vers les résultats de la recherche dans les emails envoyés aux utilisateurs. [#1208](https://github.com/betagouv/api-engagement/issues/1208)
- Amélioration de la gestion des adresses sur la plateforme. [#1114](https://github.com/betagouv/api-engagement/issues/1114)
- Ajout d'un paramètre de débogage pour afficher un bouton de débogage sur la plateforme. [#1126](https://github.com/betagouv/api-engagement/issues/1126)

### Évolutions techniques
- Intégration d'un service de tracking (Posthog) pour le suivi des événements. [#1174](https://github.com/betagouv/api-engagement/issues/1174) et [#1218](https://github.com/betagouv/api-engagement/issues/1218)
- Refactor de la logique de recherche de missions pour utiliser Typesense multi-search, améliorant ainsi les performances. [#1200](https://github.com/betagouv/api-engagement/issues/1200)
- Suppression des tables de diffusion des éditeurs, simplifiant ainsi l'architecture. [#1206](https://github.com/betagouv/api-engagement/issues/1206)
- Mise à jour des dépendances (Vite, ESLint, etc.).
- Amélioration de la gestion des files d'attente pour l'enrichissement des missions. [#1108](https://github.com/betagouv/api-engagement/issues/1108)
- Ajout d'une file d'attente de lettres mortes pour améliorer la robustesse. [#1113](https://github.com/betagouv/api-engagement/issues/1113)
- Refactor de la gestion des règles de diffusion des éditeurs. [#1187](https://github.com/betagouv/api-engagement/issues/1187) et [#1188](https://github.com/betagouv/api-engagement/issues/1188)

### Autres changements
- Amélioration de la documentation sur les règles de diffusion. [#1142](https://github.com/betagouv/api-engagement/issues/1142) et [#1177](https://github.com/betagouv/api-engagement/issues/1177)
- Corrections de bugs mineurs sur l'interface utilisateur et l'API.
- Améliorations de l'accessibilité (RGAA) de l'interface utilisateur. [#1128](https://github.com/betagouv/api-engagement/issues/1128) et [#1155](https://github.com/betagouv/api-engagement/issues/1155)
- Suppression d'un endpoint obsolète. [#1213](https://github.com/betagouv/api-engagement/issues/1213)
- Ajout d'un script pour générer automatiquement le changelog. [#1202](https://github.com/betagouv/api-engagement/issues/1202)
