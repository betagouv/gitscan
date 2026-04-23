## Changelog : mobilic-api (30 derniers jours, au 21 avril 2026)

### Résumé
Ce changelog couvre une période d'amélioration continue de l'API Mobilic, avec un focus sur la correction de bugs liés aux fuseaux horaires dans les exports, la sécurité (désactivation de GraphiQL en production, limitation de la complexité des requêtes GraphQL), et l'amélioration de la robustesse de l'application (validation automatique des missions, gestion des poids des véhicules). Une mise à jour majeure de Flask a également été intégrée.

### Évolutions fonctionnelles
- Correction de l'application des fuseaux horaires dans les exports et les PDF, résolvant ainsi des erreurs liées à l'heure. [#671](https://github.com/MTES-MCT/mobilic-api/pull/671)
- Amélioration de la validation automatique des missions, notamment en corrigeant un problème lié aux activités en cours. [#689](https://github.com/MTES-MCT/mobilic-api/pull/689)
- Correction du format d'affichage du poids des véhicules dans les bulletins de contrôle BDC (utilisation d'une virgule décimale). [#691](https://github.com/MTES-MCT/mobilic-api/pull/691)
- Mise à jour du label de vérification de la réglementation "pas de licence". [#684](https://github.com/MTES-MCT/mobilic-api/pull/684)
- Correction d'un problème lié à l'auto-validation des missions, évitant une erreur de type `NoneType` lors de la récupération des identifiants des entreprises. [#692](https://github.com/MTES-MCT/mobilic-api/pull/692)

### Évolutions techniques
- Mise à jour de Flask, une des principales dépendances du projet. [#686](https://github.com/MTES-MCT/mobilic-api/pull/686)
- Sécurité : Désactivation de l'interface GraphiQL en production pour réduire les risques d'exposition.
- Sécurité : Ajout d'une limite de complexité pour les requêtes GraphQL afin de prévenir les attaques par déni de service (DoS). [#694](https://github.com/MTES-MCT/mobilic-api/pull/694)
- Suppression du contexte des accès aux données d'activité pour améliorer la sécurité et la clarté du code. [#693](https://github.com/MTES-MCT/mobilic-api/pull/693)
- Amélioration de la gestion des erreurs et ajout de logs pour le processus d'authentification Agent Connect.
- Refactoring du code pour améliorer la qualité et la conformité aux bonnes pratiques (renommage de variables en snake_case, nettoyage de code pour la conformité SonarCloud).

### Autres changements
- Corrections mineures et ajustements de configuration pour améliorer la stabilité et la performance de l'application.
- Mise à jour de la documentation et des tests pour refléter les changements apportés.
- Mises à jour de la configuration de CircleCI pour utiliser une version plus récente de `pipenv`.
