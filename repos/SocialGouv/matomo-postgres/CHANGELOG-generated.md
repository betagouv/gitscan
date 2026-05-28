## Changelog : matomo-postgres (30 derniers jours, au 26 mai 2026)

### Résumé
Ce changelog couvre les dernières améliorations apportées à l'outil de synchronisation des données Matomo vers PostgreSQL. Les mises à jour se concentrent sur la correction de bugs liés à la migration de schéma, à la gestion des partitions et à la compatibilité avec les versions de Node.js, ainsi que sur la sérialisation correcte des champs JSON.

### Évolutions fonctionnelles
*   Correction d'un bug qui empêchait la réplication correcte du schéma de la table Matomo vers une table de destination personnalisée après les migrations. [#fe7413b](https://github.com/SocialGouv/matomo-postgres/commit/fe7413bd9c2be580944113c4f8826d838373d503)
*   Correction d'un problème de condition de concurrence lors de la création de partitions, améliorant la robustesse du processus de partitionnement. [#910ded4](https://github.com/SocialGouv/matomo-postgres/commit/910ded49feae6e992eb986fb362c34afbe07c739)
*   Correction d'un bug de sérialisation des champs JSON, qui provoquait des erreurs de syntaxe JSON. [#3ae9f7e](https://github.com/SocialGouv/matomo-postgres/commit/3ae9f7e1bb828035e224d6c82a292294ee412f87)

### Évolutions techniques
*   Mise à jour de la déclaration de compatibilité Node.js pour exiger une version 18 ou supérieure, afin d'éviter les erreurs avec les versions obsolètes. [#ccc9f5c](https://github.com/SocialGouv/matomo-postgres/commit/ccc9f5c405647409ee6895c28facf6f92d8e80e8)

### Autres changements
*   Publication des versions 2.4.4, 2.4.3 et 2.4.2.
*   Publication des versions 2.4.1.
