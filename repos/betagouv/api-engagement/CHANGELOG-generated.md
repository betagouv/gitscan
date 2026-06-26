## Changelog : api-engagement (30 derniers jours, au 25 juin 2026)

### Résumé
Ce mois-ci, l'API Engagement a bénéficié d'améliorations significatives en termes de diffusion des missions, d'intégration avec des services tiers comme Démareches Simplifiées, et d'optimisations des performances et de la sécurité. Des corrections de bugs et des améliorations de l'expérience utilisateur sur la plateforme et le back-office ont également été apportées.

### Évolutions fonctionnelles
- Ajout de l'intégration avec Démareches Simplifiées pour la diffusion des missions [#1154](https://github.com/betagouv/api-engagement/issues/1154).
- Amélioration du suivi de la diffusion des missions avec l'implémentation de JSTag [#1194](https://github.com/betagouv/api-engagement/issues/1194).
- Ajout d'une extension Chrome pour faciliter l'utilisation de l'API [#1178](https://github.com/betagouv/api-engagement/issues/1178).
- Amélioration de l'affichage des badges de compensation sur la plateforme [#1173](https://github.com/betagouv/api-engagement/issues/1173).
- Amélioration de la compatibilité de l'API avec les diffuseurs pour l'endpoint `/v2/activity` [#1155](https://github.com/betagouv/api-engagement/issues/1155).
- Refonte de la page de résultats et des missions sur la plateforme, notamment pour l'accessibilité et l'expérience mobile [#1060](https://github.com/betagouv/api-engagement/issues/1060), [#1074](https://github.com/betagouv/api-engagement/issues/1074).
- Amélioration des libellés et de l'accessibilité (RGAA) sur l'application et la plateforme [#1175](https://github.com/betagouv/api-engagement/issues/1175), [#1128](https://github.com/betagouv/api-engagement/issues/1128).
- Ajout de la possibilité de filtrer les diffuseurs par valeur de champ dans les règles de diffusion [#1111](https://github.com/betagouv/api-engagement/issues/1111).

### Évolutions techniques
- Refactorisation de la gestion des règles de diffusion des missions pour une meilleure flexibilité et maintenabilité [#1187](https://github.com/betagouv/api-engagement/issues/1187), [#1183](https://github.com/betagouv/api-engagement/issues/1183), [#1151](https://github.com/betagouv/api-engagement/issues/1151), [#1135](https://github.com/betagouv/api-engagement/issues/1135).
- Optimisation de la recherche Typesense en utilisant la fonction multi-search [#1200](https://github.com/betagouv/api-engagement/issues/1200).
- Mise en place d'une file d'attente de lettres mortes pour améliorer la robustesse du traitement des missions [#1113](https://github.com/betagouv/api-engagement/issues/1113).
- Amélioration de la sécurité en ajoutant une limite de débit IP sur les routes de l'API de la plateforme [#1075](https://github.com/betagouv/api-engagement/issues/1075).
- Suppression de l'utilisation des tables `publisher_diffusion` obsolètes [#1135](https://github.com/betagouv/api-engagement/issues/1135).
- Mise à jour de la version de l'invite d'enrichissement à v3 [#1182](https://github.com/betagouv/api-engagement/issues/1182).
- Ajout d'un script pour générer automatiquement le changelog [#1202](https://github.com/betagouv/api-engagement/issues/1202).
- Amélioration de la gestion des erreurs et de la résilience de l'enrichissement des missions [#1108](https://github.com/betagouv/api-engagement/issues/1108).

### Autres changements
- Correction de typos et amélioration de la documentation [#1204](https://github.com/betagouv/api-engagement/issues/1204), [#1177](https://github.com/betagouv/api-engagement/issues/1177).
- Correction de problèmes d'affichage et de wording sur la plateforme [#1205](https://github.com/betagouv/api-engagement/issues/1205).
- Correction de bugs liés à l'IDOR (Insecure Direct Object Reference) sur les missions [#1195](https://github.com/betagouv/api-engagement/issues/1195).
- Correction de problèmes liés aux règles de diffusion et à l'affichage des données analytiques [#1199](https://github.com/betagouv/api-engagement/issues/1199), [#1193](https://github.com/betagouv/api-engagement/issues/1193).
- Correction de problèmes liés à l'image de repli pour les missions envoyées par e-mail [#1190](https://github.com/betagouv/api-engagement/issues/1190).
- Correction de problèmes liés à la configuration de Typesense [#1201](https://github.com/betagouv/api-engagement/issues/1201).
- Mise à jour des dépendances.
