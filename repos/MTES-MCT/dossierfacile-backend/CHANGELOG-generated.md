## Changelog : dossierfacile-backend (30 derniers jours, au 8 juillet 2026)

### Résumé
Les dernières évolutions de dossierfacile-backend se concentrent sur l'amélioration de l'analyse des documents (notamment les avis de taxe foncière) et l'ajout de fonctionnalités pour la gestion des garants. Une correction a également été apportée pour éviter la duplication de documents.

### Évolutions fonctionnelles
- Amélioration de l'analyse des avis de taxe foncière pour supporter plusieurs propriétaires et de nouvelles règles de classification. ([#1263](https://github.com/MTES-MCT/dossierfacile-backend/issues/1263), [#1269](https://github.com/MTES-MCT/dossierfacile-backend/issues/1269), [#1262](https://github.com/MTES-MCT/dossierfacile-backend/issues/1262))
- Ajout de la possibilité de spécifier une adresse email pour le garant naturel. ([#1273](https://github.com/MTES-MCT/dossierfacile-backend/issues/1273))
- Ajout d'un endpoint de vérification d'email, suppression d'utilisateur et test d'opérateur dans le contrôleur de test. ([#1260](https://github.com/MTES-MCT/dossierfacile-backend/issues/1260))
- Ajout de logs lors de la suppression de fichiers dans l'interface administrateur. ([#1240](https://github.com/MTES-MCT/dossierfacile-backend/issues/1240))

### Évolutions techniques
- Ajout d'un index unique sur la table des documents pour éviter les doublons. ([#1261](https://github.com/MTES-MCT/dossierfacile-backend/issues/1261))
- Configuration de SSL pour Logstash. ([#1271](https://github.com/MTES-MCT/dossierfacile-backend/issues/1271))
- Mise à jour des dépendances. ([#1272](https://github.com/MTES-MCT/dossierfacile-backend/issues/1272))

### Autres changements
- Publication de la version V3.5.12.
