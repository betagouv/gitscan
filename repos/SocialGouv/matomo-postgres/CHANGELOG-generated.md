## Changelog : matomo-postgres (30 derniers jours, au 21 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'enrichissement des données synchronisées depuis Matomo vers PostgreSQL. Une nouvelle fonctionnalité permet désormais d'importer les données relatives aux tests A/B, offrant ainsi une vue plus complète des performances web. Une documentation a également été ajoutée concernant une limitation de l'API Matomo.

### Évolutions fonctionnelles
- Ajout de l'import des données d'A/B Testing (expériences) [#94](https://github.com/SocialGouv/matomo-postgres/issues/94)
- Ajout d'une documentation concernant la limitation de l'API `Live.getLastVisitsDetails` de Matomo [#93](https://github.com/SocialGouv/matomo-postgres/issues/93)

### Évolutions techniques
- Publication de la version 2.4.0.

### Autres changements
- Correction d'une fuite de mémoire [#91](https://github.com/SocialGouv/matomo-postgres/issues/91)
- Correction de problèmes liés à la publication de la version (plusieurs commits npm release)
- Correction de l'import dans les tables non partitionnées [#0912909](https://github.com/SocialGouv/matomo-postgres/commit/091290933a8cf13df532b61b19d56b89dfddd710)
- Correction de problèmes liés au binaire (bin)
- Correction de problèmes liés aux migrations pnpm
