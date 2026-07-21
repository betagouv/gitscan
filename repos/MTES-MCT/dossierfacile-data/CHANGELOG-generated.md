## Changelog : dossierfacile-data (30 derniers jours, au 15 juillet 2026)

### Résumé
Cette mise à jour apporte des corrections et améliorations concernant le suivi des opérations et la gestion des données, notamment pour l'analyse des validations et la recherche d'applications. Ces changements visent à améliorer la qualité des données et la fiabilité des analyses.

### Évolutions fonctionnelles
- Correction d'une erreur DBT sur la date de validation des OCPT, maintenant correctement identifiée comme `validated_at` [#75](https://github.com/MTES-MCT/dossierfacile-data/issues/75).
- Ajout d'un nouveau type d'action (`APPLICATION_SEARCHED`) pour les opérations, permettant un suivi plus précis des recherches d'applications [#71](https://github.com/MTES-MCT/dossierfacile-data/issues/71).
- Correction du label `log_type` dans les statistiques hebdomadaires des opérations par validation [#73](https://github.com/MTES-MCT/dossierfacile-data/issues/73).
- Autorisation des valeurs nulles pour `tenant_id` lorsque le type d'action est `APPLICATION_SEARCHED` [#72](https://github.com/MTES-MCT/dossierfacile-data/issues/72).
- Correction du label dans le fichier `analytics_yml` [#77](https://github.com/MTES-MCT/dossierfacile-data/issues/77).

### Évolutions techniques
- Aucune évolution technique majeure à signaler durant cette période.

### Autres changements
- Aucune autre modification significative.
