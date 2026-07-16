## Changelog : keycloak-buildpack (30 derniers jours, au 13 juillet 2026)

### Résumé
Ce buildpack a été mis à jour pour corriger un problème empêchant la montée de version de Keycloak suite à une modification de la variable `KEYCLOAK_VERSION`. Cette correction assure le bon fonctionnement des mises à jour de Keycloak sur Scalingo.

### Évolutions fonctionnelles
- Correction d'un bug empêchant la mise à jour de Keycloak [#21](https://github.com/MTES-MCT/keycloak-buildpack/issues/21).

### Évolutions techniques
- Modification de la valeur de la variable `KEYCLOAK_VERSION` pour permettre les mises à jour.
