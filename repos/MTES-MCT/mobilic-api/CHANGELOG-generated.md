## Changelog : mobilic-api (30 derniers jours, au 9 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'optimisation des performances de l'API, notamment au niveau du tableau de bord d'administration, et sur la correction de plusieurs anomalies affectant l'affichage des données et le calcul des alertes réglementaires. Des améliorations ont également été apportées à l'interface d'administration pour une meilleure clarté et précision des informations.

### Évolutions fonctionnelles
- Amélioration du tableau de bord d'administration : les compteurs affichés sont désormais alignés avec les données des panneaux détaillés [#705](https://github.com/MTES-MCT/mobilic-api/issues/705).
- Affichage des jours multi-employeurs sur les alertes réglementaires dans l'interface d'administration [#703](https://github.com/MTES-MCT/mobilic-api/issues/703).
- Correction de l'affichage des alertes journalières/nocturnes dans le résumé mensuel [#4b93228](https://github.com/MTES-MCT/mobilic-api/commit/4b93228).
- Correction du calcul du dépassement de temps de travail avant la réinitialisation due à une pause prolongée [#9dd5ace](https://github.com/MTES-MCT/mobilic-api/commit/9dd5ace).
- Ajout d'un indicateur "hasAnyMissionThisWeek" sur le résumé du tableau de bord d'administration [#09c8ab3](https://github.com/MTES-MCT/mobilic-api/commit/09c8ab3).

### Évolutions techniques
- Optimisation des requêtes du tableau de bord d'administration pour améliorer les performances [#713](https://github.com/MTES-MCT/mobilic-api/issues/713).
- Augmentation du nombre de workers Gunicorn et ajustement des timeouts pour améliorer la capacité de l'API [#711](https://github.com/MTES-MCT/mobilic-api/issues/711) et [#709](https://github.com/MTES-MCT/mobilic-api/issues/709).
- Configuration de la concurrence Gunicorn via la variable d'environnement `WEB_CONCURRENCY` [#3739377](https://github.com/MTES-MCT/mobilic-api/commit/3739377).
- Suppression de code inutilisé lié à la durée des pauses prolongées [#aa8a710](https://github.com/MTES-MCT/mobilic-api/commit/aa8a710).

### Autres changements
- Correction de la sémantique et du fuseau horaire des compteurs du tableau de bord d'administration [#d567ff6](https://github.com/MTES-MCT/mobilic-api/commit/d567ff6).
- Correction de l'affichage du nombre d'invitations dans l'interface d'administration [#62da82f](https://github.com/MTES-MCT/mobilic-api/issues/705).
- Amélioration de la clarté des informations sur le tableau de bord en fonction des retours de Marie [#43801fb](https://github.com/MTES-MCT/mobilic-api/commit/43801fb).
