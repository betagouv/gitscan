## Changelog : signalement-api (30 derniers jours)

### Résumé
Les récentes évolutions de l'API SignalConso se concentrent sur l'amélioration de la gestion de la mémoire et des ressources, ainsi que sur la correction de bugs liés à l'export de fichiers et à la taille des requêtes. Ces améliorations visent à rendre l'API plus robuste et performante, notamment en production.

### Évolutions fonctionnelles
- Correction d'un bug concernant la taille limite du parser du corps des requêtes, permettant de traiter des requêtes plus importantes. [#3175](https://github.com/betagouv/signalement-api/issues/3175)
- Correction du nom des fichiers exportés. [#3179](https://github.com/betagouv/signalement-api/issues/3179)

### Évolutions techniques
- Limitation de la taille de la mémoire directe (direct memory) pour éviter des problèmes de performance. [#3152](https://github.com/betagouv/signalement-api/issues/3152)
- Ajout de la possibilité de définir des options de mémoire personnalisées (Xmx et Xms) en production. [#3152](https://github.com/betagouv/signalement-api/issues/3152)
- Suppression des fichiers temporaires après leur téléchargement depuis S3 pour libérer de l'espace disque. [#2027](https://github.com/betagouv/signalement-api/issues/2027)
- Limitation des "arenas" directes pour optimiser l'utilisation des ressources. [#3152](https://github.com/betagouv/signalement-api/issues/3152)
- Correction de problèmes de linting. [#3179](https://github.com/betagouv/signalement-api/issues/3179)
