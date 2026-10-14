## Changelog : transport-site (30 derniers jours, au 13 octobre 2026)

### Résumé
Cette période a été marquée par une modernisation majeure de l'infrastructure technique, notamment avec la mise à jour vers Elixir 1.20 et la préparation de la migration vers Phoenix 1.8. Parallèlement, l'expérience d'administration a été nettement améliorée grâce à une refonte de l'interface du Backoffice (recherche, menus et formulaires) et à une meilleure présentation des détails des jeux de données.

### Évolutions fonctionnelles
- **Amélioration du Backoffice** :
  - Mise en place d'une recherche de datasets plus intuitive [#5633](https://github.com/etalab/transport-site/issues/5633).
  - Ajout d'un menu contextuel pour faciliter les actions sur les datasets [#5631](https://github.com/etalab/transport-site/issues/5631).
  - Correction du rendu des boutons de validation et du comportement des menus [#5636](https://github.com/etalab/transport-site/issues/5636).
- **Optimisation de l'affichage des données** :
  - Refonte de la page de détails des datasets et amélioration du layout des ressources pour une meilleure lisibilité [#5629](https://github.com/etalab/transport-site/issues/5629) [#5625](https://github.com/etalab/transport-site/issues/5625).
  - Correction de la hiérarchie des titres HTML pour les réutilisations afin d'améliorer la structure de la page [#5624](https://github.com/etalab/transport-site/issues/5624).
  - Repositionnement du message invitant au partage des réutilisations [#5638](https://github.com/etalab/transport-site/issues/5638).

### Évolutions techniques
- **Modernisation de la stack et de l'architecture** :
  - Mise à jour vers Elixir v1.20.x et de nombreuses librairies associées [#5612](https://github.com/etalab/transport-site/issues/5612).
  - Convergence vers Phoenix 1.8 : mise à jour de `phoenix_html`, remplacement de `scrivener_html` par un composant de pagination et nettoyage des générateurs [#5651](https://github.com/etalab/transport-site/issues/5651) [#5646](https://github.com/etalab/transport-site/issues/5646) [#5644](https://github.com/etalab/transport-site/issues/5644).
  - Définition d'une ADR pour clarifier l'usage des clients HTTP [#5648](https://github.com/etalab/transport-site/issues/5648).
- **Refactoring et qualité du code** :
  - Migration des anciens helpers HTML vers des composants HEEx dans le Backoffice [#5653](https://github.com/etalab/transport-site/issues/5653) et modernisation de la gestion des formulaires [#5656](https://github.com/etalab/transport-site/issues/5656).
  - Amélioration de la robustesse du code : remplacement des tuples imbriqués par des structures (`struct`) dédiées [#5655](https://github.com/etalab/transport-site/issues/5655) et correction de bugs via Dialyzer [#5652](https://github.com/etalab/transport-site/issues/5652).
  - Remplacement de la librairie Earmark par MDEx [#5634](https://github.com/etalab/transport-site/issues/5634).
- **Données et Tests** :
  - Renforcement de la couverture de tests, notamment sur les rapports de validation et les niveaux de sévérité NeTEx [#5650](https://github.com/etalab/transport-site/issues/5650) [#5658](https://github.com/etalab/transport-site/issues/5658).
  - Mise à jour de la logique de détection des opérateurs GBFS [#5626](https://github.com/etalab/transport-site/issues/5626).
  - Optimisation de l'import quotidien des réutilisations depuis la base de données [#5639](https://github.com/etalab/transport-site/issues/5639).
- **Maintenance et Infrastructure** :
  - Désactivation du polling dynamique IRVE dans les environnements de staging, dev et sur certains workers de production [#5621](https://github.com/etalab/transport-site/issues/5621).
  - Nettoyage de code : suppression d'un client d'API orphelin [#5643](https://github.com/etalab/transport-site/issues/5643) et ajustement du nommage des fichiers GeoJSON [#5645](https://github.com/etalab/transport-site/issues/5645).
