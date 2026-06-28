## Changelog : api-engagement (30 derniers jours, au 26 juin 2026)

### Résumé
Ce mois-ci, l'API Engagement a bénéficié d'améliorations significatives en termes de fonctionnalités et de performances. Les principales évolutions concernent l'ajout de filtres pour les missions selon le dispositif, l'intégration avec Demarches Simplifiées, l'amélioration de la recherche de missions, et des corrections de bugs pour une meilleure stabilité et expérience utilisateur. Des optimisations ont également été apportées à l'infrastructure et aux processus de déploiement.

### Évolutions fonctionnelles
- Ajout d'un filtre pour les missions par dispositif sur la plateforme [#1211](https://github.com/betagouv/api-engagement/issues/1211).
- Intégration avec Demarches Simplifiées pour l'enrichissement des missions [#1154](https://github.com/betagouv/api-engagement/issues/1154).
- Amélioration de la correspondance des résultats sur la carte avec la liste des missions [#1207](https://github.com/betagouv/api-engagement/issues/1207).
- Ajout d'un lien vers les résultats de la recherche dans les emails [#1208](https://github.com/betagouv/api-engagement/issues/1208).
- Amélioration de l'affichage des images des témoignages et de la mise en page tablette [#1210](https://github.com/betagouv/api-engagement/issues/1210).
- Ajout d'un script pour générer automatiquement le changelog [#1202](https://github.com/betagouv/api-engagement/issues/1202).
- Ajout de badges de compensation sur la plateforme [#1173](https://github.com/betagouv/api-engagement/issues/1173).
- Amélioration de la gestion des règles de diffusion des missions, avec la possibilité de filtrer par valeurs de champs [#1111](https://github.com/betagouv/api-engagement/issues/1111).
- Amélioration de la compatibilité de l'endpoint v2/activity pour les diffuseurs [#1091](https://github.com/betagouv/api-engagement/issues/1091).
- Ajout de la possibilité de gérer plusieurs adresses sur la liste des missions [#1114](https://github.com/betagouv/api-engagement/issues/1114).
- Amélioration de l'interface utilisateur du quiz et de la page d'accueil de la plateforme [#1084](https://github.com/betagouv/api-engagement/issues/1084).

### Évolutions techniques
- Suppression de l'endpoint `stats-mean` de l'API [#1213](https://github.com/betagouv/api-engagement/issues/1213).
- Suppression des tables `publisher_diffusion` de l'API [#1206](https://github.com/betagouv/api-engagement/issues/1206).
- Refactorisation de l'utilisation de Typesense pour la recherche de missions, passant à la méthode `multi-search` [#1200](https://github.com/betagouv/api-engagement/issues/1200).
- Mise en place d'une file d'attente pour l'enrichissement des missions, avec une priorité ajustée [#1203](https://github.com/betagouv/api-engagement/issues/1203).
- Amélioration de la gestion des règles de diffusion des missions, avec stockage sur `publisherOrganizationId` [#1183](https://github.com/betagouv/api-engagement/issues/1183).
- Refactorisation de la résolution des règles de diffusion des missions [#1188](https://github.com/betagouv/api-engagement/issues/1188) et [#1150](https://github.com/betagouv/api-engagement/issues/1150).
- Suppression de l'utilisation des tables `publisher_diffusion` [#1135](https://github.com/betagouv/api-engagement/issues/1135).
- Ajout d'une porte `openToMinor` pour contrôler les mises à jour mineures [#1185](https://github.com/betagouv/api-engagement/issues/1185).
- Ajout d'une limitation du nombre d'opérations Typesense [#1201](https://github.com/betagouv/api-engagement/issues/1201).
- Mise en place d'une file d'attente pour les emails [#1145](https://github.com/betagouv/api-engagement/issues/1145).
- Ajout d'une limite de débit (rate limit) sur les routes de l'API de la plateforme [#1075](https://github.com/betagouv/api-engagement/issues/1075).

### Autres changements
- Correction d'une erreur "mission not found" lors de la redirection [#1214](https://github.com/betagouv/api-engagement/issues/1214).
- Correction d'un bug concernant l'image de repli pour les missions dans les emails [#1190](https://github.com/betagouv/api-engagement/issues/1190).
- Correction d'un problème d'IDOR sur les missions [#1195](https://github.com/betagouv/api-engagement/issues/1195).
- Correction d'un problème de typographie dans le modèle `publisher_diffusion_rule` [#1199](https://github.com/betagouv/api-engagement/issues/1199).
- Amélioration du suivi des documents (tracking) [#1204](https://github.com/betagouv/api-engagement/issues/1204).
- Amélioration de l'accessibilité RGAA de l'application et de la plateforme [#1175](https://github.com/betagouv/api-engagement/issues/1175) et [#1128](https://github.com/betagouv/api-engagement/issues/1128).
- Mise à jour de la documentation des règles de diffusion [#1177](https://github.com/betagouv/api-engagement/issues/1177) et [#1142](https://github.com/betagouv/api-engagement/issues/1142).
- Correction de problèmes de merge conflict et restauration de changements perdus liés aux règles de diffusion [#1140](https://github.com/betagouv/api-engagement/issues/1140) et [#1131](https://github.com/betagouv/api-engagement/issues/1131).
