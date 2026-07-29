## Changelog : cdtn-admin (30 derniers jours, au 27 juillet 2026)

### Résumé
Cette mise à jour apporte des améliorations significatives à l'ingestion des données (accords d'entreprise, NPS, contributions) et au sitemap du site, notamment pour les URLs liées aux congés et aux conventions collectives. Des corrections de bugs ont également été apportées pour assurer la stabilité et la fiabilité de l'application. L'infrastructure de build a été modernisée.

### Évolutions fonctionnelles
- Ajout de l'ingestion des accords d'entreprise. [#1702](https://github.com/SocialGouv/cdtn-admin/issues/1702)
- Ajout d'une table pour le calcul du NPS (Net Promoter Score). [#1705](https://github.com/SocialGouv/cdtn-admin/issues/1705)
- Amélioration de l'analyse des contributions suite aux changements SEO. [#1698](https://github.com/SocialGouv/cdtn-admin/issues/1698)
- Ajout du suivi des contributions par vues mensuelles. [#1697](https://github.com/SocialGouv/cdtn-admin/issues/1697)
- Correction des URLs sur la contribution congés pour évènement familiaux. [#1699](https://github.com/SocialGouv/cdtn-admin/issues/1699) et [3b28a51](https://github.com/SocialGouv/cdtn-admin/commit/3b28a51e2bb8ac1ff8c8b6876c9b30c37c6a71d9)
- Ajout du slug de la convention collective dans l'URL du sitemap. [#1701](https://github.com/SocialGouv/cdtn-admin/issues/1701)

### Évolutions techniques
- Mise à jour de la version de Node dans le CI. [2a1a180](https://github.com/SocialGouv/cdtn-admin/commit/2a1a180bf151bc688567a31c527e606676d8d2fc)
- Migration des builds d'images de buildkit-service vers buildkit-operator. [#1695](https://github.com/SocialGouv/cdtn-admin/issues/1695)
- Ajout du job d'analyse dans le docker-compose et documentation associée. [#1704](https://github.com/SocialGouv/cdtn-admin/issues/1704)

### Autres changements
- Correction d'une erreur lors de l'ingestion des contributions. [#1706](https://github.com/SocialGouv/cdtn-admin/issues/1706)
- Exclusion des accords et statuts des alertes de suppression. [#1696](https://github.com/SocialGouv/cdtn-admin/issues/1696)
- Correction du parsing du document des IDCC. [#1694](https://github.com/SocialGouv/cdtn-admin/issues/1694)
- Filtrage des documents de type contribution dans le sitemap. [6deb18c](https://github.com/SocialGouv/cdtn-admin/commit/6deb18c5a66ffd05a25d6fe85d99638bebdd99a4)
