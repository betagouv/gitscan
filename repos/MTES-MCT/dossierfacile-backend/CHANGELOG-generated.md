## Changelog : dossierfacile-backend (30 derniers jours, au 28 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la sécurité et de la gestion des applications, notamment au niveau du back-office. Des améliorations ont également été apportées à l'analyse de documents (fiches de paie) et à la gestion des garanties. Enfin, des corrections de bugs et des optimisations de performance ont été réalisées.

### Évolutions fonctionnelles
- **Back-office :**
    - Ajout de la possibilité de supprimer un fichier individuel dans la page d'application [#1222](https://github.com/MTES-MCT/dossierfacile-backend/issues/1222).
    - Ajout d'une table des temps d'attente pour le rôle de gestionnaire [#1224](https://github.com/MTES-MCT/dossierfacile-backend/issues/1224).
    - Le commentaire de l'opérateur est maintenant conservé lors du traitement d'un dossier [#1223](https://github.com/MTES-MCT/dossierfacile-backend/issues/1223).
    - Affichage des métadonnées des fichiers dans la page d'application [#1221](https://github.com/MTES-MCT/dossierfacile-backend/issues/1221).
    - Ajout de l'historique des emails Brevo dans la page des messages du locataire [#1209](https://github.com/MTES-MCT/dossierfacile-backend/issues/1209).
    - Possibilité d'assigner un opérateur à une demande [#1212](https://github.com/MTES-MCT/dossierfacile-backend/issues/1212).
    - Ajout de limites d'actions quotidiennes (recherche, consultation, traitement) pour les opérateurs [#1213](https://github.com/MTES-MCT/dossierfacile-backend/issues/1213).
- **Analyse de documents :**
    - Amélioration de la règle d'analyse des fiches de paie, notamment pour les salaires faibles [#1215](https://github.com/MTES-MCT/dossierfacile-backend/issues/1215) et [#1216](https://github.com/MTES-MCT/dossierfacile-backend/issues/1216).
    - Refonte de la validation des fiches de paie et introduction d'un utilitaire de comparaison d'identité [#1202](https://github.com/MTES-MCT/dossierfacile-backend/issues/1202).
    - Ajout d'un indicateur de similarité de Levenshtein pour la comparaison des noms VISALE [#1206](https://github.com/MTES-MCT/dossierfacile-backend/issues/1206).
    - Ajout d'un *feature flag* pour l'analyse des fiches de paie [#1203](https://github.com/MTES-MCT/dossierfacile-backend/issues/1203).
- **Garantie :**
    - Ajout du nom préféré du garant [#1227](https://github.com/MTES-MCT/dossierfacile-backend/issues/1227).
- **Logique métier :**
    - Correction de la logique de la déclaration d'honoraires pour les couples [#1229](https://github.com/MTES-MCT/dossierfacile-backend/issues/1229).
    - Relance de l'analyse lors d'un changement d'identité du locataire [#1205](https://github.com/MTES-MCT/dossierfacile-backend/issues/1205) et [#1207](https://github.com/MTES-MCT/dossierfacile-backend/issues/1207).
- **Autres :**
    - Correction d'un bug qui empêchait la régénération d'une version mise à jour du dossier après un regroupement de demandes [#1204](https://github.com/MTES-MCT/dossierfacile-backend/issues/1204).

### Évolutions techniques
- Amélioration de la sécurité du back-office avec un renforcement de l'accès aux routes et des contrôles d'accès [#1214](https://github.com/MTES-MCT/dossierfacile-backend/issues/1214).
- Ajout d'un index sur la colonne `file_id` de la table `document_ia_file_analysis` pour optimiser les performances [#1210](https://github.com/MTES-MCT/dossierfacile-backend/issues/1210).
- Mise à jour de la date de dernière mise à jour du locataire [#1219](https://github.com/MTES-MCT/dossierfacile-backend/issues/1219).
- Ajout de métriques au back-office (locataires les plus anciens en traitement, nombre de locataires avec des PDF échoués) [#1217](https://github.com/MTES-MCT/dossierfacile-backend/issues/1217).

### Autres changements
- Suppression des données brutes dans `raw_data` pour les documents d'analyse [#1211](https://github.com/MTES-MCT/dossierfacile-backend/issues/1211).
- Publication des versions V3.5.3, V3.5.4 et V3.5.6.
