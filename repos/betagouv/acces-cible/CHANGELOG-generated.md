## Changelog : acces-cible (30 derniers jours, au 2026-08-06)

### Résumé
Les récentes évolutions renforcent la sécurité de l'application (gestion des sessions, protection contre les abus et restrictions de modification) et améliorent la fiabilité de la gestion des données, notamment grâce à l'introduction de captures d'écran de pages (snapshots) et une meilleure organisation des traitements par lots.

### Évolutions fonctionnelles
- **Sécurité et permissions** : restriction de la possibilité de modifier ou de supprimer des sites, des audits ou des tags directement depuis l'interface ([#643](https://github.com/betagouv/acces-cible/issues/643), [#637](https://github.com/betagouv/acces-cible/issues/637)).
- **Gestion des sessions** : ajout d'une durée de vie maximale pour les sessions et réduction du délai d'inactivité pour plus de sécurité ([#674](https://github.com/betagouv/acces-cible/issues/674)).
- **Gestion des équipes** : utilisation des labels d'organisation ProConnect pour la gestion des équipes ([#668](https://github.com/betagouv/acces-cible/issues/668)).
- **Interface utilisateur** : correction de l'affichage du nom de l'utilisateur sur la page de profil ([#646](https://github.com/betagouv/acces-cible/issues/646)).

### Évolutions techniques
- **Sécurité et infrastructure** : mise en place de `rack-attack` pour limiter le débit des requêtes et prévenir les abus ([#659](https://github.com/betagouv/acces-cible/issues/659)).
- **Refonte de la gestion des données et des pages** :
  - Introduction du modèle `PageSnapshot` pour améliorer la gestion des captures de pages ([#669](https://github.com/betagouv/acces-cible/issues/669)).
  - Ajout de nouveaux attributs aux contrôles et audits avec mise à jour des données existantes ([#672](https://github.com/betagouv/acces-cible/issues/672)).
  - Refonte du traitement par lots avec l'introduction d' `AuditBatch` ([#679](https://github.com/betagouv/acces-cible/issues/679)).
  - Ajout d'une gestion de privilèges pour les modèles `Team` et `User` ([#639](https://github.com/betagouv/acces-cible/issues/639)).
  - Nettoyage de la base de données (suppression de la colonne `name` sur les sites) ([#641](https://github.com/betagouv/acces-cible/issues/641)).
- **Corrections et optimisations** :
  - Optimisation des délais d'attente réseau (network idling/timeout) ([#627](https://github.com/betagouv/acces-cible/issues/627)).
  - Correction d'erreurs liées au parsing de liens et aux types de contenu ([#636](https://github.com/betagouv/acces-cible/issues/636), [#614](https://github.com/betagouv/acces-cible/issues/614)).
  - Amélioration et stabilisation des tâches de fond (backfill) pour les snapshots de pages ([#675](https://github.com/betagouv/acces-cible/issues/675), [#676](https://github.com/betagouv/acces-cible/issues/676)).
