## Changelog : dossierfacile-backend (30 derniers jours, au 30 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la sécurité et de la gestion des accès au back-office, ainsi que sur l'enrichissement des fonctionnalités d'analyse de documents et de gestion des applications locatives. Plusieurs corrections et optimisations ont également été apportées pour améliorer la stabilité et la performance de la plateforme.

### Évolutions fonctionnelles
- **Back-office :**
    - Ajout de la possibilité de supprimer un fichier individuel dans la page d'application locative. [#1222](https://github.com/MTES-MCT/dossierfacile-backend/issues/1222)
    - Affichage des métadonnées des fichiers dans la page d'application locative. [#1221](https://github.com/MTES-MCT/dossierfacile-backend/issues/1221)
    - Possibilité d'assigner un opérateur à une application locative. [#1212](https://github.com/MTES-MCT/dossierfacile-backend/issues/1212)
    - Ajout de l'historique des emails Brevo (Sendinblue) dans la page des messages du locataire. [#1209](https://github.com/MTES-MCT/dossierfacile-backend/issues/1209)
    - Ajout de limites d'actions quotidiennes (recherche, consultation, traitement des dossiers) pour les opérateurs. [#1213](https://github.com/MTES-MCT/dossierfacile-backend/issues/1213)
    - Ajout d'un tableau de bord avec des métriques sur les dossiers les plus anciens en traitement et le nombre de dossiers avec des PDF ayant échoué. [#1217](https://github.com/MTES-MCT/dossierfacile-backend/issues/1217)
    - Le commentaire de l'opérateur est désormais persistant lors du traitement d'un fichier. [#1223](https://github.com/MTES-MCT/dossierfacile-backend/issues/1223)
    - Ajout d'un tableau des temps d'attente pour le rôle de gestionnaire. [#1224](https://github.com/MTES-MCT/dossierfacile-backend/issues/1224)
- **Garantie :** Ajout de la possibilité de renseigner le nom préféré du garant. [#1227](https://github.com/MTES-MCT/dossierfacile-backend/issues/1227)
- **Analyse de documents :** Amélioration de la règle d'analyse des fiches de paie. [#1216](https://github.com/MTES-MCT/dossierfacile-backend/issues/1216) et [#1215](https://github.com/MTES-MCT/dossierfacile-backend/issues/1215)

### Évolutions techniques
- **Sécurité :** Renforcement de la sécurité du back-office avec application des accès aux routes et durcissement général. [#1214](https://github.com/MTES-MCT/dossierfacile-backend/issues/1214)
- **Analyse de documents :** Refactorisation de la validation des fiches de paie et introduction d'une classe utilitaire `IdentityMatchUtil`. [#1202](https://github.com/MTES-MCT/dossierfacile-backend/issues/1202)
- **API :** Utilisation de l'ID du locataire impacté lors de la suppression d'un document en couple. [#1232](https://github.com/MTES-MCT/dossierfacile-backend/issues/1232)
- **Gestion des versions :** Publication des versions V3.5.5 et V3.5.6. [#1231](https://github.com/MTES-MCT/dossierfacile-backend/issues/1231) et [#1225](https://github.com/MTES-MCT/dossierfacile-backend/issues/1225)
- **Base de données :** Ajout d'un index sur `document_ia_file_analysis.file_id` pour améliorer les performances. [#1210](https://github.com/MTES-MCT/dossierfacile-backend/issues/1210)
- **Logique métier :** Correction de la logique `honorDeclaration` pour les couples. [#1229](https://github.com/MTES-MCT/dossierfacile-backend/issues/1229)
- **Mise à jour du tenant :** Mise à jour de la date de dernière mise à jour du locataire. [#1219](https://github.com/MTES-MCT/dossierfacile-backend/issues/1219)

### Autres changements
- Correction d'un bug où les données brutes étaient conservées dans `raw_data` pour les analyses de documents. [#1211](https://github.com/MTES-MCT/dossierfacile-backend/issues/1211)
- Correction d'un bug qui empêchait de relancer l'analyse lors d'un changement d'identité. [#1207](https://github.com/MTES-MCT/dossierfacile-backend/issues/1207)
- Augmentation de la limite d'actions de recherche dans le back-office. [#1228](https://github.com/MTES-MCT/dossierfacile-backend/issues/1228)
