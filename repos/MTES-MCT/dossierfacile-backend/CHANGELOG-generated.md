## Changelog : dossierfacile-backend (30 derniers jours, au 15 juillet 2026)

### Résumé
Cette version apporte des améliorations à la gestion des locataires et des garants, notamment en rendant obligatoires certaines informations de contact. Des corrections ont également été apportées pour éviter la duplication de documents et améliorer l'analyse des avis de taxe foncière. Enfin, des optimisations de logs et de sécurité ont été implémentées.

### Évolutions fonctionnelles
- Rendre l'email du bénéficiaire obligatoire lors de la création d'un locataire. [#1277](https://github.com/MTES-MCT/dossierfacile-backend/issues/1277)
- Rendre l'email du couple co-locataire obligatoire. [#1274](https://github.com/MTES-MCT/dossierfacile-backend/issues/1274)
- Ajouter la possibilité de saisir l'email d'un garant personnel (garant naturel). [#1273](https://github.com/MTES-MCT/dossierfacile-backend/issues/1273)
- Ajouter un endpoint de vérification d'email, suppression d'utilisateur et test de l'opérateur dans le contrôleur de test. [#1260](https://github.com/MTES-MCT/dossierfacile-backend/issues/1260)
- Amélioration de l'analyse des avis de taxe foncière pour supporter plusieurs propriétaires et les catégories RESIDENCY/OWNER. [#1263](https://github.com/MTES-MCT/dossierfacile-backend/issues/1263) et [#1262](https://github.com/MTES-MCT/dossierfacile-backend/issues/1262)

### Évolutions techniques
- Ajout d'un index unique sur la table des documents pour éviter les doublons. [#1261](https://github.com/MTES-MCT/dossierfacile-backend/issues/1261)
- Mise à jour des dépendances. [#1272](https://github.com/MTES-MCT/dossierfacile-backend/issues/1272)
- Ajout de SSL aux logs envoyés à Logstash. [#1271](https://github.com/MTES-MCT/dossierfacile-backend/issues/1271)
- Modification de la règle de classification de la taxe foncière. [#1269](https://github.com/MTES-MCT/dossierfacile-backend/issues/1269)
- Bump vers la version V3.5.12. [#1261](https://github.com/MTES-MCT/dossierfacile-backend/issues/1261)

### Autres changements
- Ajout de logs lors de la suppression d'un fichier dans le back-office. [#1240](https://github.com/MTES-MCT/dossierfacile-backend/issues/1240)
