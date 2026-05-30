## Changelog : dossierfacile-backend (30 derniers jours, au 28 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur dans le back-office (BO) avec de nouvelles fonctionnalités pour le traitement des documents, ainsi que sur des corrections et des optimisations de l'API et de l'intégration avec des services externes comme l'ADEME. Des améliorations ont également été apportées à la gestion des sessions utilisateurs et à l'analyse des commentaires.

### Évolutions fonctionnelles
- **Back-office :** Les opérateurs peuvent désormais retraiter les documents d'un locataire après un refus [#1242](https://github.com/MTES-MCT/dossierfacile-backend/issues/1242) et [#1241](https://github.com/MTES-MCT/dossierfacile-backend/issues/1241).
- **Back-office :** Ajout de Redis pour préserver la session utilisateur lors du redémarrage du BO [#1239](https://github.com/MTES-MCT/dossierfacile-backend/issues/1239).
- **PDF :** Correction d'un problème de dépassement de texte sur les PDF lors de l'utilisation de messages personnalisés longs [#1243](https://github.com/MTES-MCT/dossierfacile-backend/issues/1243).
- **Validation des justificatifs de salaire :** Restriction de la validation des fiches de paie aux cas de salaire de plus de 3 mois [#1235](https://github.com/MTES-MCT/dossierfacile-backend/issues/1235).
- **Classification de la résidence :** Ajout de règles de classification de la résidence [#1247](https://github.com/MTES-MCT/dossierfacile-backend/issues/1247).

### Évolutions techniques
- **Amélioration de l'IA :** Ajout d'une compétence SQL à l'IA pour améliorer ses capacités d'interrogation de la base de données [#1246](https://github.com/MTES-MCT/dossierfacile-backend/issues/1246).
- **Analyse des commentaires :** Refonte de la méthode d'analyse des commentaires [#1245](https://github.com/MTES-MCT/dossierfacile-backend/issues/1245).
- **Anonymisation :** Suppression de la colonne `json_profile` de la table `tenant_log` pour l'anonymisation [#1238](https://github.com/MTES-MCT/dossierfacile-backend/issues/1238).
- **API ADEME :** Correction du format de date retourné par l'API ADEME.
- **Suppression de documents :** Utilisation de l'ID du locataire impacté lors de la suppression d'un couple document [#1232](https://github.com/MTES-MCT/dossierfacile-backend/issues/1232).
- **Gestion des flags de fonctionnalités :** Correction de la gestion de la date de déploiement des flags de fonctionnalités [#1231](https://github.com/MTES-MCT/dossierfacile-backend/issues/1231).
- **Prévisualisation des fichiers :** Optimisation de l'appel à la prévisualisation des fichiers dans le back-office [#1236](https://github.com/MTES-MCT/dossierfacile-backend/issues/1236).
- **Correction IA Document :** Correction du type de retour de l'IA pour les documents 2DDoc inconnus [#1237](https://github.com/MTES-MCT/dossierfacile-backend/issues/1237).

### Autres changements
- Mises à jour de dépendances [#1233](https://github.com/MTES-MCT/dossierfacile-backend/issues/1233).
- Publication des versions 3.5.7, 3.5.8 et 3.5.10.
