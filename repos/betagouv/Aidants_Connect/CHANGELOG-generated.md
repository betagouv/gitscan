## Changelog : Aidants_Connect (30 derniers jours, au 27 juillet 2026)

### Résumé
Les récentes évolutions se concentrent sur l'amélioration de la gestion des organisations et des numéros SIRET, notamment en préparation d'exports de données plus complets et fiables. Des corrections ont également été apportées aux tests liés à l'authentification FranceConnect.

### Évolutions fonctionnelles
- Amélioration de la gestion des numéros SIRET :
  - Ajout de champs pour le nettoyage des SIRET lors de l'export global de données. [#1802](https://github.com/betagouv/Aidants_Connect/issues/1802)
  - Ajout d'un champ pour sauvegarder les SIRET invalides. [#1799](https://github.com/betagouv/Aidants_Connect/issues/1799)
  - Ajout d'un champ pour sauvegarder les SIRET en doublon. [#1800](https://github.com/betagouv/Aidants_Connect/issues/1800)
  - Modification de l'API FNE pour intégrer ces améliorations. [#1801](https://github.com/betagouv/Aidants_Connect/issues/1801)

### Évolutions techniques
- Correction des tests liés à l'authentification FranceConnect. [#1783](https://github.com/betagouv/Aidants_Connect/issues/1783) et [911d3f9](https://github.com/betagouv/Aidants_Connect/commit/911d3f9)
