## Changelog : dossierfacile-backend (30 derniers jours, au 20 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur pour les opérateurs du back-office, avec de nouvelles fonctionnalités pour le re-traitement des documents, la gestion des sessions et la suppression de fichiers. Des corrections et des améliorations ont également été apportées à l'API et à la logique métier, notamment concernant la validation des fiches de paie et le traitement des documents ADEME.

### Évolutions fonctionnelles
- Les opérateurs du back-office peuvent désormais retravailler les documents d'un locataire après un refus. [#1241](https://github.com/MTES-MCT/dossierfacile-backend/issues/1241) et [#1242](https://github.com/MTES-MCT/dossierfacile-backend/issues/1242)
- Ajout d'un nom préféré pour le garant. [#1227](https://github.com/MTES-MCT/dossierfacile-backend/issues/1227)
- Les opérateurs peuvent supprimer un fichier individuel directement depuis la page de l'application. [#1222](https://github.com/MTES-MCT/dossierfacile-backend/issues/1222)
- Amélioration de la recherche dans le back-office avec une augmentation de la limite d'actions. [#1228](https://github.com/MTES-MCT/dossierfacile-backend/issues/1228)
- Ajout d'une table des temps d'attente pour le rôle de gestionnaire dans le back-office. [#1224](https://github.com/MTES-MCT/dossierfacile-backend/issues/1224)
- Le commentaire de l'opérateur est désormais conservé lors du traitement d'un fichier. [#1223](https://github.com/MTES-MCT/dossierfacile-backend/issues/1223)
- Restriction de la validation des fiches de paie aux cas de salaire de plus de 3 mois. [#1235](https://github.com/MTES-MCT/dossierfacile-backend/issues/1235)
- Correction de la logique `honorDeclaration` pour les couples. [#1229](https://github.com/MTES-MCT/dossierfacile-backend/issues/1229)
- Correction d'un problème de débordement PDF pour les messages personnalisés longs. [#1243](https://github.com/MTES-MCT/dossierfacile-backend/issues/1243)

### Évolutions techniques
- Ajout de Redis pour préserver la session utilisateur lorsque le back-office est redémarré. [#1239](https://github.com/MTES-MCT/dossierfacile-backend/issues/1239)
- Suppression de la colonne `json_profile` de `tenant_log` pour l'anonymisation. [#1238](https://github.com/MTES-MCT/dossierfacile-backend/issues/1238)
- Correction du type de retour de l'IA Document pour les documents 2DDoc inconnus. [#1237](https://github.com/MTES-MCT/dossierfacile-backend/issues/1237)
- Correction pour n'appeler la prévisualisation de fichier que lorsque nécessaire. [#1236](https://github.com/MTES-MCT/dossierfacile-backend/issues/1236)
- Mise à jour des dépendances. [#1233](https://github.com/MTES-MCT/dossierfacile-backend/issues/1233)
- Correction du format de date retourné par l'API ADEME.
- Correction de l'utilisation de l'ID du locataire impacté lors de la suppression d'un couple de documents. [#1232](https://github.com/MTES-MCT/dossierfacile-backend/issues/1232)
- Gestion correcte de la date de déploiement des feature flags. [#1231](https://github.com/MTES-MCT/dossierfacile-backend/issues/1231)
- Mise à jour de la date de dernière modification du locataire. [#1219](https://github.com/MTES-MCT/dossierfacile-backend/issues/1219)
- Ajout d'une nouvelle règle d'analyse pour le numéro de page de la déclaration de revenus. [#1225](https://github.com/MTES-MCT/dossierfacile-backend/issues/1225)

### Autres changements
- Publication des versions 3.5.6, 3.5.7 et 3.5.8.
