## Changelog : api-subventions-asso (30 derniers jours, au 16 mars 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur des améliorations de la robustesse de l'API, notamment dans la gestion des erreurs et des données, ainsi que sur des corrections d'affichage et de formulation dans l'interface utilisateur. Des refactorings importants ont été entrepris pour améliorer la structure interne de l'API et préparer de futures évolutions.

### Évolutions fonctionnelles
- Correction d'un bug d'affichage des en-têtes de modales de paiement sur l'interface utilisateur. [#3852](https://github.com/betagouv/api-subventions-asso/issues/3852)
- Correction de la formulation concernant le processus de dépôt sur l'interface utilisateur. [#3836](https://github.com/betagouv/api-subventions-asso/issues/3836) et [#3843](https://github.com/betagouv/api-subventions-asso/issues/3843)
- Ajout de la possibilité d'activer les notifications pour les dépôts partiels.
- Implémentation du support des paiements européens Chorus. [#3839](https://github.com/betagouv/api-subventions-asso/issues/3839)
- Amélioration de la gestion des statistiques détaillées des consommateurs. [#3826](https://github.com/betagouv/api-subventions-asso/issues/3826)

### Évolutions techniques
- Refactoring majeur de l'architecture de l'API avec introduction de patterns Mapper, Port et Adapter. [#3803](https://github.com/betagouv/api-subventions-asso/issues/3803) et [#3828](https://github.com/betagouv/api-subventions-asso/issues/3828)
- Mise à jour de la configuration TypeScript. [#3799](https://github.com/betagouv/api-subventions-asso/issues/3799)
- Homogénéisation des services "plats" dans l'API. [#3815](https://github.com/betagouv/api-subventions-asso/issues/3815)
- Correction d'une erreur d'importation du module "core".
- Suppression de l'alias "dev.local" pour une meilleure cohérence de l'environnement. [#3851](https://github.com/betagouv/api-subventions-asso/issues/3851)
- Correction d'un problème d'accès à une propriété sur un DTO non défini.
- Correction d'un bug où une erreur `NotAssociationError` était levée incorrectement en l'absence de numéro RNA.

### Autres changements
- Correction de noms d'imports dans les tests.
- Renommage du "port" en "adapter" dans le cadre du refactoring. [#3861](https://github.com/betagouv/api-subventions-asso/issues/3861)
- Ajout d'une configuration d'environnement pour filtrer les notifications. [#3820](https://github.com/betagouv/api-subventions-asso/issues/3820)
