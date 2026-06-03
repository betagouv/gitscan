## Changelog : service-national-universel (30 derniers jours, au 26 mai 2024)

### Résumé
Ce changelog présente les récentes évolutions du Service National Universel. Les mises à jour incluent des améliorations de la logique de validation et de soumission des dates de mission pour les administrateurs, ainsi qu'une simplification de la gestion des représentants légaux. Une correction de configuration a également été apportée pour la gestion des secrets JWT en environnement de développement.

### Évolutions fonctionnelles
- **Admin / API :** Amélioration de la logique de validation et de soumission des dates de mission, notamment pour la date limite de candidature. [#5268](https://github.com/betagouv/service-national-universel/issues/5268)
- **Configuration :** Mise à jour de la variable `JWT_SECRET` pour utiliser une valeur spécifique en environnement de développement et s'assurer qu'elle est définie en production. [#5271](https://github.com/betagouv/service-national-universel/issues/5271)

### Évolutions techniques
- **API / Lib :** Suppression de l'archivage des représentants légaux, simplifiant ainsi le code et la maintenance. [#5269](https://github.com/betagouv/service-national-universel/issues/5269)

### Autres changements
- Aucun changement significatif à signaler.
