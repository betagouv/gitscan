## Changelog : graal (30 derniers jours)

### Résumé
Les dernières mises à jour de Graal se concentrent sur l'amélioration de la gestion des configurations, notamment l'ajout de la prise en charge des fichiers Excel stockés dans S3. Des corrections de bugs ont également été apportées pour améliorer la stabilité du pipeline de traitement et la gestion des manifestes. Enfin, des améliorations de l'interface utilisateur et de l'authentification ont été implémentées.

### Évolutions fonctionnelles
- Ajout d'une interface utilisateur pour la configuration des fichiers Excel ([54a38ea](https://github.com/SocialGouv/graal/commit/54a38ea9a98d24df57838af3abc58db9a3265f6e)).
- Possibilité de supprimer les configurations Excel via le backend ([41a67dd](https://github.com/SocialGouv/graal/commit/41a67dd4a68d291227e4ade8a17cc6dd405606f7)).
- Ajout d'un titre à l'onglet GRAAL dans l'interface utilisateur ([da392c7](https://github.com/SocialGouv/graal/commit/da392c71f9889492048c8668f5c02476a51b480c)).
- Les requêtes OAuth sont maintenant stockées dans la base de données PostgreSQL ([81dbcd0](https://github.com/SocialGouv/graal/commit/81dbcd0b3ab37c32b655d7788b0f444bd63dac03)).

### Évolutions techniques
- Implémentation d'un mécanisme de nouvelle tentative pour la génération de nouveaux types d'API ([506b526](https://github.com/SocialGouv/graal/commit/506b526e52a58e370c310d941d36ba4a29a86b46)).
- Refactorisation du backend pour la gestion des fichiers de configuration Excel, utilisant les IDs ([bd61f6d](https://github.com/SocialGouv/graal/commit/bd61f6d163922528697395b97760360a1020769d)).
- Ajout de routes API pour la gestion des fichiers de configuration Excel ([088b79d](https://github.com/SocialGouv/graal/commit/088b79d477b985266de8e14010a5f40fdc369b5e)).
- Ajout du backend pour la gestion des fichiers de configuration Excel dans S3 ([01077ec](https://github.com/SocialGouv/graal/commit/01077ec874874654577983976831162d428ed9dd)).
- Correction d'un crash du pipeline lié à la recherche de similarités et à des problèmes asynchrones avec S3 ([7a7bd4e](https://github.com/SocialGouv/graal/commit/7a7bd4eb6082aeeb66fec33a047f3659ac5759df)).
- Correction d'un problème empêchant la suppression des manifestes de la base de données si le fichier S3 n'existait pas ([d4a18ee](https://github.com/SocialGouv/graal/commit/d4a18ee24d5ab982714fea11f6289835b89a36ac)).
- Utilisation de variables d'environnement pour les uploads S3 ([d23c618](https://github.com/SocialGouv/graal/commit/d23c61825149923590666452f8f3399186844241)).
- Amélioration des appels à `require_db_role` en fournissant l'utilisateur ([2f0fb71](https://github.com/SocialGouv/graal/commit/2f0fb71f8368f482277f183097f877d94b67928f)).

### Autres changements
- Corrections mineures diverses ([e396dc1](https://github.com/SocialGouv/graal/commit/e396dc1626472589480074467365435547230623)).
- Correction de l'utilisation de `config_file_id` ([24cb206](https://github.com/SocialGouv/graal/commit/24cb206c6c8d82d3ee54b645891f0b662f19dcdd)).
