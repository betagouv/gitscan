## Changelog : dossierfacile-backend (30 derniers jours, au 8 juillet 2026)

### Résumé
Les dernières mises à jour de dossierfacile-backend améliorent la gestion des garants, l'analyse des documents (notamment les taxes foncières), la robustesse de la création de locataires et la gestion des utilisateurs dans l'interface d'administration. Des corrections de bugs ont également été apportées pour éviter la duplication de documents et permettre la déconnexion de l'interface d'administration.

### Évolutions fonctionnelles
- Ajout de l'email pour le garant personnel lors de la création d'un locataire. [#1273](https://github.com/MTES-MCT/dossierfacile-backend/issues/1273)
- Amélioration de la reconnaissance des noms de propriétaires sur les avis de taxe foncière, supportant désormais plusieurs propriétaires. [#1263](https://github.com/MTES-MCT/dossierfacile-backend/issues/1263)
- Ajout d'un endpoint pour vérifier l'email, supprimer un utilisateur et tester l'opérateur dans le contrôleur de test. [#1260](https://github.com/MTES-MCT/dossierfacile-backend/issues/1260)
- Ajout de règles Docia pour la taxe foncière concernant les catégories RESIDENCY / OWNER. [#1262](https://github.com/MTES-MCT/dossierfacile-backend/issues/1262)
- Ajout d'un endpoint E2E pour simuler un rejet par un opérateur. [#1258](https://github.com/MTES-MCT/dossierfacile-backend/issues/1258)
- Amélioration de la classification de la taxe foncière. [#1269](https://github.com/MTES-MCT/dossierfacile-backend/issues/1269)

### Évolutions techniques
- Ajout d'un index unique sur la table des documents pour éviter les doublons. [#1261](https://github.com/MTES-MCT/dossierfacile-backend/issues/1261)
- Optimisation de la requête pour la récupération paginée des locataires à archiver.
- Correction d'une course conditionnelle pouvant entraîner la création de plusieurs locataires simultanément. [#1257](https://github.com/MTES-MCT/dossierfacile-backend/issues/1257)
- Correction d'un problème empêchant la déconnexion de l'interface d'administration. [#1256](https://github.com/MTES-MCT/dossierfacile-backend/issues/1256)
- Refonte de la transaction sur la tâche d'archivage des locataires. [#1255](https://github.com/MTES-MCT/dossierfacile-backend/issues/1255)
- Ajout de SSL pour Logstash. [#1271](https://github.com/MTES-MCT/dossierfacile-backend/issues/1271)

### Autres changements
- Mise à jour des dépendances. [#1272](https://github.com/MTES-MCT/dossierfacile-backend/issues/1272)
- Ajout de logs lors de la suppression d'un fichier dans l'interface d'administration. [#1240](https://github.com/MTES-MCT/dossierfacile-backend/issues/1240)
- Publication des versions V3.5.11 et V3.5.12.
