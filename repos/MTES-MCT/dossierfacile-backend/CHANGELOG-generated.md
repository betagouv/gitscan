## Changelog : dossierfacile-backend (30 derniers jours, au 24 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur dans l'interface administrateur (BO), avec de nouvelles fonctionnalités pour la gestion des applications locataires, des statistiques et des actions sur les documents. Des améliorations significatives ont également été apportées à l'analyse des documents, notamment des fiches de paie, et à la sécurité de la plateforme.

### Évolutions fonctionnelles
- Ajout de la possibilité de supprimer un fichier individuel dans la page d'application locataire. [#1222](https://github.com/MTES-MCT/dossierfacile-backend/issues/1222)
- Amélioration de la recherche dans le BO avec une augmentation de la limite d'actions. [#1228](https://github.com/MTES-MCT/dossierfacile-backend/issues/1228)
- Ajout d'une table de temps d'attente pour le rôle de gestionnaire dans le BO. [#1224](https://github.com/MTES-MCT/dossierfacile-backend/issues/1224)
- Possibilité de rendre le commentaire de l'opérateur persistant lors du traitement d'un dossier. [#1223](https://github.com/MTES-MCT/dossierfacile-backend/issues/1223)
- Affichage des métadonnées des fichiers dans la page d'application locataire. [#1221](https://github.com/MTES-MCT/dossierfacile-backend/issues/1221)
- Ajout de l'historique des emails Brevo (envoi d'emails) dans la page des messages du locataire. [#1209](https://github.com/MTES-MCT/dossierfacile-backend/issues/1209)
- Affectation d'un opérateur à une demande de dossier. [#1212](https://github.com/MTES-MCT/dossierfacile-backend/issues/1212)
- Correction d'un bug où le regroupement de locataires ne réinitialisait pas le PDF du dossier, assurant ainsi la régénération d'une version à jour. [#1204](https://github.com/MTES-MCT/dossierfacile-backend/issues/1204)
- Harmonisation de l'affichage dans le BO lorsque le locataire ou le garant n'ont pas d'impôts à afficher. [#1201](https://github.com/MTES-MCT/dossierfacile-backend/issues/1201)
- Ajout d'une logique pour relancer l'analyse des documents après une modification de l'identité du locataire. [#1205](https://github.com/MTES-MCT/dossierfacile-backend/issues/1205)
- Amélioration de la comparaison des noms pour la vérification VISALE avec l'ajout de l'algorithme de Levenshtein. [#1206](https://github.com/MTES-MCT/dossierfacile-backend/issues/1206)
- Ajout d'un indicateur de fonctionnalité (feature flag) pour l'analyse des fiches de paie. [#1203](https://github.com/MTES-MCT/dossierfacile-backend/issues/1203)
- Ajout d'une nouvelle règle pour la page des impôts dans l'analyse documentaire. [#1225](https://github.com/MTES-MCT/dossierfacile-backend/issues/1225)
- Logique améliorée pour la déclaration conjointe (honorDeclaration) pour les couples. [#1229](https://github.com/MTES-MCT/dossierfacile-backend/issues/1229)

### Évolutions techniques
- Refactorisation de la validation des fiches de paie et introduction de `IdentityMatchUtil`. [#1202](https://github.com/MTES-MCT/dossierfacile-backend/issues/1202)
- Amélioration de la sécurité du BO avec l'application de restrictions d'accès basées sur le locataire et un renforcement général de la sécurité. [#1214](https://github.com/MTES-MCT/dossierfacile-backend/issues/1214)
- Ajout de limites d'actions quotidiennes (recherche, consultation, traitement des demandes) dans le BO. [#1213](https://github.com/MTES-MCT/dossierfacile-backend/issues/1213)
- Ajout d'un index sur `document_ia_file_analysis.file_id` pour améliorer les performances. [#1210](https://github.com/MTES-MCT/dossierfacile-backend/issues/1210)
- Suppression des données brutes (raw_data) dans les analyses de documents pour optimiser le stockage. [#1211](https://github.com/MTES-MCT/dossierfacile-backend/issues/1211)
- Ajout de métriques au BO : locataire le plus ancien en cours de traitement et nombre de locataires avec des PDF ayant échoué. [#1217](https://github.com/MTES-MCT/dossierfacile-backend/issues/1217)

### Autres changements
- Mises à jour de version : V3.5.5, V3.5.6 et V3.5.4.
- Correction de bugs mineurs et améliorations de la stabilité.
