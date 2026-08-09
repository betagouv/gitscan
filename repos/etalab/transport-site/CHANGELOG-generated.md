## Changelog : transport-site (30 derniers jours, au 7 août 2026)

### Résumé
Les récentes évolutions se concentrent sur l'amélioration de la fiabilité des données de transport (GTFS-RT, IRVE) et le renforcement de la sécurité de la plateforme. Des optimisations ont également été apportées au système de notification pour mieux informer les utilisateurs de l'état de fraîcheur des données.

### Évolutions fonctionnelles
- Mise à jour du système de notification concernant l'expiration des données [#5586](https://github.com/etalab/transport-site/issues/5586).

### Évolutions techniques
- **Gestion des données de mobilité** : Mise à jour du protocole GTFS-RT [#5569](https://github.com/etalab/transport-site/issues/5569) et ajustement des règles pour MobilityData [#5574](https://github.com/etalab/transport-site/issues/5574).
- **Optimisation IRVE** : Refactorisation du processus de consolidation des données de recharge pour véhicules électriques afin d'optimiser le passage des fichiers vers les dataframes et la validation [#5559](https://github.com/etalab/transport-site/issues/5559).
- **Sécurité** : Mise en place d'un scanner de vulnérabilités pour renforcer la surveillance des dépendances [#5566](https://github.com/etalab/transport-site/issues/5566).

### Autres changements
- **Maintenance et documentation** : Corrections diverses dans la documentation [#5547](https://github.com/etalab/transport-site/issues/5547) et ajustement de la configuration du linter pour les liens markdown [#5589](https://github.com/etalab/transport-site/issues/5589).
- **Nettoyage** : Suppression de l'outil de test `exvcr` [#5564](https://github.com/etalab/transport-site/issues/5564).
