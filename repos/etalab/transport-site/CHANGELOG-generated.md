## Changelog : transport-site (30 derniers jours, au 15 octobre 2026)

### Résumé
Ce mois-ci, le projet a bénéficié d'une mise à jour majeure de ses technologies de base et d'un renforcement de la fiabilité du traitement des données de transport. L'interface d'administration a été modernisée pour plus de robustesse, tandis que l'expérience utilisateur a été affinée sur les pages de détails des jeux de données.

### Évolutions fonctionnelles
- Amélioration de la mise en page des ressources dans les pages de détails des jeux de données [#5625](https://github.com/etalab/transport-site/issues/5625).
- Ajustement de l'interface pour repositionner le message incitant au partage des réutilisations [#5638](https://github.com/etalab/transport-site/issues/5638).

### Évolutions techniques
- **Modernisation du framework** : Migration vers Phoenix 1.8 (incluant la mise à jour de `phoenix_html` et l'intégration de nouveaux composants de pagination) [#5651](https://github.com/etalab/transport-site/issues/5651), [#5646](https://github.com/etalab/transport-site/issues/5646), [#5644](https://github.com/etalab/transport-site/issues/5644) et passage à Elixir v1.20.x [#5612](https://github.com/etalab/transport-site/issues/5612).
- **Fiabilisation du traitement NeTEx** : Centralisation du parsing des fichiers Parquet [#5659](https://github.com/etalab/transport-site/issues/5659) et renforcement significatif de la couverture de tests (cartes de ressources, niveaux de sévérité et rapports de validation) [#5662](https://github.com/etalab/transport-site/issues/5662), [#5658](https://github.com/etalab/transport-site/issues/5658), [#5650](https://github.com/etalab/transport-site/issues/5650).
- **Refonte du Backoffice** : Modernisation de l'interface d'administration via l'utilisation de composants HEEx et une meilleure gestion des formulaires [#5653](https://github.com/etalab/transport-site/issues/5653), [#5656](https://github.com/etalab/transport-site/issues/5656).
- **Qualité logicielle et architecture** :
    - Correction de bugs et d'alertes de typage via Dialyzer [#5652](https://github.com/etalab/transport-site/issues/5652).
    - Refactoring des structures de données pour utiliser des `structs` plutôt que des tuples imbriqués [#5655](https://github.com/etalab/transport-site/issues/5655).
    - Clarification de l'usage des clients HTTP via une nouvelle ADR [#5648](https://github.com/etalab/transport-site/issues/5648).
    - Remplacement de la bibliothèque Earmark par MDEx [#5634](https://github.com/etalab/transport-site/issues/5634).
- **Gestion des données** : Optimisation de l'import quotidien des réutilisations depuis la base de données [#5639](https://github.com/etalab/transport-site/issues/5639) et ajustement du nommage des fichiers GeoJSON convertis [#5645](https://github.com/etalab/transport-site/issues/5645).

### Autres changements
- Nettoyage du code avec la suppression d'un client d'API obsolète [#5643](https://github.com/etalab/transport-site/issues/5643).
