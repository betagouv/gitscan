## Changelog : mobilic-api (30 derniers jours, au 8 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la performance de l'API et la correction de quelques anomalies dans l'interface d'administration. Des ajustements ont été apportés aux indicateurs affichés dans le tableau de bord administrateur pour une meilleure précision et clarté. Une correction a également été apportée concernant le téléchargement des CGU et des données personnelles.

### Évolutions fonctionnelles
- Correction de l'affichage des compteurs du tableau de bord administrateur pour qu'ils correspondent aux données des panneaux détaillés [#705](https://github.com/MTES-MCT/mobilic-api/pull/705).
- Amélioration de la sémantique et du fuseau horaire des compteurs du tableau de bord administrateur [#703](https://github.com/MTES-MCT/mobilic-api/pull/703).
- Ajout d'un indicateur pour signaler les jours avec plusieurs employeurs sur les alertes réglementaires dans l'interface administrateur [#703](https://github.com/MTES-MCT/mobilic-api/pull/703).
- Ajout d'une information indiquant si un utilisateur a des missions cette semaine sur le résumé du tableau de bord administrateur [#703](https://github.com/MTES-MCT/mobilic-api/pull/703).
- Correction d'un problème lors du téléchargement des CGU et des données personnelles [#702](https://github.com/MTES-MCT/mobilic-api/pull/702).

### Évolutions techniques
- Augmentation du nombre de workers Gunicorn et réduction des timeouts pour améliorer la performance de l'API [#709](https://github.com/MTES-MCT/mobilic-api/pull/709), [#711](https://github.com/MTES-MCT/mobilic-api/pull/711).
- Configuration du nombre de workers Gunicorn via la variable d'environnement `WEB_CONCURRENCY` pour une meilleure flexibilité [#711](https://github.com/MTES-MCT/mobilic-api/pull/711).
- Correction d'une erreur de transaction imbriquée dans l'export des données, en déplaçant l'appel à `set_transferred_data_date` en dehors de la transaction principale [#702](https://github.com/MTES-MCT/mobilic-api/pull/702).

### Autres changements
- Aucun changement significatif à signaler.
