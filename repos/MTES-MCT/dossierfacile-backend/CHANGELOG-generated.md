## Changelog : dossierfacile-backend (30 derniers jours, au 22 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur dans l'interface opérateur (back-office) avec de nouvelles fonctionnalités de relecture et de retraitement des documents, ainsi que sur des corrections et des optimisations de l'API et de la logique métier. Des améliorations ont également été apportées à la gestion des documents et à l'intégration avec des services externes.

### Évolutions fonctionnelles
- L'opérateur peut désormais retraiter les documents d'un locataire après un refus [#1242](https://github.com/MTES-MCT/dossierfacile-backend/issues/1242) et [#1241](https://github.com/MTES-MCT/dossierfacile-backend/issues/1241).
- Ajout du nom préféré du garant [#1227](https://github.com/MTES-MCT/dossierfacile-backend/issues/1227).
- Restriction de la validation des fiches de paie aux cas de salaire de plus de 3 mois [#1235](https://github.com/MTES-MCT/dossierfacile-backend/issues/1235).
- Amélioration de la logique `honorDeclaration` pour les couples [#1229](https://github.com/MTES-MCT/dossierfacile-backend/issues/1229).
- Correction d'un problème de débordement PDF pour les messages personnalisés longs [#1243](https://github.com/MTES-MCT/dossierfacile-backend/issues/1243).

### Évolutions techniques
- Ajout de règles de classification de la résidence [#1247](https://github.com/MTES-MCT/dossierfacile-backend/issues/1247).
- Ajout de compétences SQL pour améliorer les capacités SQL du LLM [#1246](https://github.com/MTES-MCT/dossierfacile-backend/issues/1246).
- Refonte de la méthode d'analyse des commentaires [#1245](https://github.com/MTES-MCT/dossierfacile-backend/issues/1245).
- Ajout de Redis pour préserver la session utilisateur lors du redémarrage du back-office [#1239](https://github.com/MTES-MCT/dossierfacile-backend/issues/1239).
- Suppression de la colonne `json_profile` de la table `tenant_log` pour l'anonymisation [#1238](https://github.com/MTES-MCT/dossierfacile-backend/issues/1238).
- Correction du type de retour de l'IA de document 2DDoc inconnu [#1237](https://github.com/MTES-MCT/dossierfacile-backend/issues/1237).
- Optimisation de l'appel à la prévisualisation des fichiers dans le back-office, pour ne l'appeler que lorsque nécessaire [#1236](https://github.com/MTES-MCT/dossierfacile-backend/issues/1236).
- Correction de l'utilisation de l'ID du locataire impacté lors de la suppression d'un document de couple [#1232](https://github.com/MTES-MCT/dossierfacile-backend/issues/1232).
- Gestion correcte de la date de déploiement des *feature flags* [#1231](https://github.com/MTES-MCT/dossierfacile-backend/issues/1231).
- Correction du format de date retourné par l'API ADEME [#1233](https://github.com/MTES-MCT/dossierfacile-backend/issues/1233).

### Autres changements
- Bump de version à 3.5.8 et 3.5.7.
- Mise à jour des dépendances.
