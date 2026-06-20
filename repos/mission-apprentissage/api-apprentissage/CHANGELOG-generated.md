## Changelog : api-apprentissage (30 derniers jours, au 19 juin 2026)

### Résumé
Cette version apporte des améliorations de stabilité et de performance, notamment en limitant le taux de requêtes vers le service LBA et en ajoutant des délais d'attente pour éviter les blocages. Des corrections de documentation et de configuration ont également été effectuées, ainsi que des migrations d'infrastructure pour les environnements de recette et de production.

### Évolutions fonctionnelles
- Correction de la description de l'API de recherche d'emploi [#490](https://github.com/mission-apprentissage/api-apprentissage/issues/490).
- Mise à jour de l'adresse email de contact [#491](https://github.com/mission-apprentissage/api-apprentissage/issues/491).
- Suppression du champ "origin" de la documentation, conformément à la demande LBA-3864 [#494](https://github.com/mission-apprentissage/api-apprentissage/issues/494).

### Évolutions techniques
- Implémentation d'une limitation du taux de requêtes (rate-limit) par consommateur sur les routes qui transmettent les requêtes au service LBA [#493](https://github.com/mission-apprentissage/api-apprentissage/issues/493).
- Ajout d'un délai d'attente (timeout) sur les requêtes forwardées vers LBA pour éviter les blocages [#485](https://github.com/mission-apprentissage/api-apprentissage/issues/485).
- Suppression des sous-modules `.infra/authorizations` et `.infra/inventories` [#488](https://github.com/mission-apprentissage/api-apprentissage/issues/488).
- Migrations des serveurs API pour les environnements de recette et de production [#486](https://github.com/mission-apprentissage/api-apprentissage/issues/486), [#487](https://github.com/mission-apprentissage/api-apprentissage/issues/487), [#495](https://github.com/mission-apprentissage/api-apprentissage/issues/495).
- Correction de quelques fautes de frappe [#489](https://github.com/mission-apprentissage/api-apprentissage/issues/489).
