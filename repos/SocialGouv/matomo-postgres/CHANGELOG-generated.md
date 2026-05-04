## Changelog : matomo-postgres (30 derniers jours, au 30 avril 2026)

### Résumé
Cette version apporte l'intégration des données d'A/B testing (expériences) depuis Matomo vers la base de données PostgreSQL, permettant une analyse plus fine des performances des différentes versions de vos pages web. Une correction de bug a également été implémentée pour assurer la sérialisation correcte des champs JSON, évitant ainsi des erreurs d'importation. Enfin, une documentation a été ajoutée concernant une limitation de l'API Matomo utilisée.

### Évolutions fonctionnelles
- Ajout de la synchronisation des données d'A/B testing (expériences) depuis Matomo vers PostgreSQL. [#94](https://github.com/SocialGouv/matomo-postgres/issues/94)
- Documentation ajoutée concernant la limitation de l'API `Live.getLastVisitsDetails` de Matomo. [#93](https://github.com/SocialGouv/matomo-postgres/issues/93)

### Évolutions techniques
- Correction de la sérialisation des champs JSON avec `JSON.stringify` pour éviter les erreurs de syntaxe JSON lors de l'importation. [3ae9f7e](https://github.com/SocialGouv/matomo-postgres/commit/3ae9f7e1bb828035e224d6c82a292294ee412f87)

### Autres changements
- Publication des versions 2.4.1 et 2.4.0.
