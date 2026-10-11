## Changelog : transport-site (30 derniers jours, au 09/10/2026)

### Résumé
Cette période a été marquée par une modernisation importante de l'infrastructure technique du site et une amélioration notable de l'interface d'administration (Backoffice). Les utilisateurs bénéficieront d'une navigation plus fluide dans les jeux de données et de rapports de validation NeTEx plus lisibles et structurés.

### Évolutions fonctionnelles
- **Amélioration de l'interface d'administration (Backoffice) :**
    - Recherche de jeux de données plus intuitive [#5633](https://github.com/etalab/transport-site/issues/5633).
    - Ajout d'un menu contextuel pour les actions sur les datasets [#5631](https://github.com/etalab/transport-site/issues/5631).
    - Corrections sur le rendu des boutons de validation et le comportement des menus [#5636](https://github.com/etalab/transport-site/issues/5636).
- **Optimisation de la validation NeTEx :**
    - Affichage de la version XSD dans les rapports [#5607](https://github.com/etalab/transport-site/issues/5607).
    - Tri des erreurs par criticité décroissante pour faciliter le diagnostic [#5604](https://github.com/etalab/transport-site/issues/5604).
- **Amélioration de l'expérience utilisateur (UI/UX) :**
    - Refonte du layout pour les détails des jeux de données [#5625](https://github.com/etalab/transport-site/issues/5625) [#5629](https://github.com/etalab/transport-site/issues/5629) et les réutilisations [#5623](https://github.com/etalab/transport-site/issues/5623).
    - Correction de la hiérarchie des titres HTML pour les réutilisations [#5624](https://github.com/etalab/transport-site/issues/5624).
    - Repositionnement du message invitant au partage des réutilisations [#5638](https://github.com/etalab/transport-site/issues/5638).
- **Données :** Mise à jour de la détection des opérateurs GBFS [#5626](https://github.com/etalab/transport-site/issues/5626).

### Évolutions techniques
- **Modernisation du framework :**
    - Mise à jour majeure vers Elixir v1.20.x [#5612](https://github.com/etalab/transport-site/issues/5612).
    - Travaux de convergence vers Phoenix 1.8, incluant la mise à jour de `phoenix_html` [#5651](https://github.com/etalab/transport-site/issues/5651) et le remplacement de `scrivener_html` par un composant de pagination [#5646](https://github.com/etalab/transport-site/issues/5646).
- **Qualité du code et architecture :**
    - Refactoring des structures de données (remplacement des tuples imbriqués par des structs dédiés) [#5655](https://github.com/etalab/transport-site/issues/5655).
    - Correction d'alertes Dialyzer, incluant la résolution de bugs réels [#5652](https://github.com/etalab/transport-site/issues/5652).
    - Clarification de l'usage des clients HTTP via une nouvelle ADR [#5648](https://github.com/etalab/transport-site/issues/5648).
    - Remplacement de la librairie Earmark par MDEx [#5634](https://github.com/etalab/transport-site/issues/5634).
- **Tests et performance :**
    - Augmentation de la couverture de tests pour les rapports de validation NeTEx [#5650](https://github.com/etalab/transport-site/issues/5650).
    - Désactivation du polling IRVE dynamique dans les environnements de staging et de développement [#5621](https://github.com/etalab/transport-site/issues/5621).
    - Optimisation de l'import quotidien des réutilisations depuis la base de données [#5639](https://github.com/etalab/transport-site/issues/5639).

### Autres changements
- **Nettoyage :** Suppression d'un client d'API obsolète [#5643](https://github.com/etalab/transport-site/issues/5643).
- **Données :** Ajustement du nommage des fichiers GeoJSON issus des données statiques [#5645](https://github.com/etalab/transport-site/issues/5645).
