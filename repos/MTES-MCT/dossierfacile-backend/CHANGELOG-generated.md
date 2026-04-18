## Changelog : dossierfacile-backend (30 derniers jours, au 16 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'analyse des documents (notamment les fiches de paie et les avis d'imposition), la sécurité du back-end et l'expérience utilisateur du back-office. Des corrections de bugs et des optimisations de performance ont également été apportées.

### Évolutions fonctionnelles
- Amélioration de l'analyse des fiches de paie, notamment en introduisant une logique de correspondance d'identité et en gérant les cas de salaires faibles sans règle de continuité [#1202](https://github.com/MTES-MCT/dossierfacile-backend/issues/1202).
- Ajout d'une fonctionnalité pour relancer l'analyse des documents après modification de l'identité du locataire [#1207](https://github.com/MTES-MCT/dossierfacile-backend/issues/1207) et des documents du garant [#1205](https://github.com/MTES-MCT/dossierfacile-backend/issues/1205).
- Amélioration de la gestion des noms composés avec tiret dans l'analyse des avis d'imposition [#1195](https://github.com/MTES-MCT/dossierfacile-backend/issues/1195).
- Ajout d'un indicateur de statut d'analyse dans l'API locataire [#1187](https://github.com/MTES-MCT/dossierfacile-backend/issues/1187).
- Le back-office affiche désormais correctement l'absence de document et les messages personnalisés du locataire [#1196](https://github.com/MTES-MCT/dossierfacile-backend/issues/1196).
- Harmonisation de l'affichage dans le back-office en cas d'absence d'informations fiscales pour le locataire ou le garant [#1201](https://github.com/MTES-MCT/dossierfacile-backend/issues/1201).
- Possibilité d'assigner un opérateur à une demande dans le back-office [#1212](https://github.com/MTES-MCT/dossierfacile-backend/issues/1212).
- Ajout de l'historique des emails Brevo dans la page des messages du locataire dans le back-office [#1209](https://github.com/MTES-MCT/dossierfacile-backend/issues/1209).

### Évolutions techniques
- Renforcement de la sécurité du back-office avec des contrôles d'accès aux routes et des mesures de durcissement [#1214](https://github.com/MTES-MCT/dossierfacile-backend/issues/1214).
- Ajout de limites d'actions quotidiennes (recherche, consultation, traitement des demandes) dans le back-office [#1213](https://github.com/MTES-MCT/dossierfacile-backend/issues/1213).
- Implémentation de recommandations OWASP pour le téléchargement de fichiers [#1179](https://github.com/MTES-MCT/dossierfacile-backend/issues/1179).
- Refactorisation de la validation des fiches de paie et introduction d'une utilitaire de correspondance d'identité [#1202](https://github.com/MTES-MCT/dossierfacile-backend/issues/1202).
- Ajout d'un indicateur de performance dans le back-office pour suivre le temps de traitement des demandes et le nombre de demandes ayant échoué lors de l'analyse PDF [#1217](https://github.com/MTES-MCT/dossierfacile-backend/issues/1217).
- Ajout d'un flag de fonctionnalité pour l'analyse des fiches de paie [#1203](https://github.com/MTES-MCT/dossierfacile-backend/issues/1203).
- Amélioration de la gestion des PDFs encryptés [#1199](https://github.com/MTES-MCT/dossierfacile-backend/issues/1199).
- Ajout d'une règle pour améliorer la reconnaissance des noms sur les avis d'imposition [#1200](https://github.com/MTES-MCT/dossierfacile-backend/issues/1200).
- Ajout de l'algorithme de Levenshtein pour la comparaison des noms VISALE [#1206](https://github.com/MTES-MCT/dossierfacile-backend/issues/1206).
- Correction d'un bug empêchant l'analyse des documents sans `document_ia_analysis` [#1191](https://github.com/MTES-MCT/dossierfacile-backend/issues/1191).

### Autres changements
- Ajout d'un index sur `document_ia_file_analysis.file_id` pour améliorer les performances [#1210](https://github.com/MTES-MCT/dossierfacile-backend/issues/1210).
- Suppression des données brutes dans `raw_data` pour les documents 2DDoc [#1211](https://github.com/MTES-MCT/dossierfacile-backend/issues/1211).
- Correction d'un problème de limitation de débit pour le téléchargement de documents [#1189](https://github.com/MTES-MCT/dossierfacile-backend/issues/1189).
- Correction d'un bug lié à la régénération des dossiers après regroupement de locataires [#1204](https://github.com/MTES-MCT/dossierfacile-backend/issues/1204).
- Correction d'un bug empêchant la récupération des options refusées du garant [#1186](https://github.com/MTES-MCT/dossierfacile-backend/issues/1186).
- Correction d'un bug empêchant l'analyse des avis d'imposition étrangers [#1192](https://github.com/MTES-MCT/dossierfacile-backend/issues/1192).
- Plusieurs versions ont été publiées : v3.5.0, v3.5.1, v3.5.2, v3.5.3, v3.5.4 et v3.5.5.
