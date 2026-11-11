## Changelog : cdtn-admin (30 derniers jours, au 09 novembre 2026)

### Résumé
Ce mois-ci, l'outil d'administration a franchi une étape importante dans ses capacités d'analyse grâce à l'intégration de nouveaux indicateurs statistiques et d'outils de reporting. L'expérience de gestion des contenus a été fluidifiée, notamment pour la création de contributions et la publication d'actualités, tout en renforçant la fiabilité des données exportées et la sécurité de l'infrastructure.

### Évolutions fonctionnelles

**Contributions**
- Amélioration globale du processus de création d'une contribution ([#1727](https://github.com/SocialGouv/cdtn-admin/issues/1727)).
- Automatisation de la date de mise à jour lors de la publication ([#1726](https://github.com/SocialGouv/cdtn-admin/issues/1726)).
- Correction d'un bug permettant d'éviter les doubles créations, sauvegardes ou publications de contenus ([#1736](https://github.com/SocialGouv/cdtn-admin/issues/1736)).
- Correction du contrôle du surlignage, désormais limité au type « Afficher la réponse » ([#1737](https://github.com/SocialGouv/cdtn-admin/issues/1737)).

**Actualités (News)**
- Enrichissement des contenus avec l'ajout de sections « Pour aller plus loin », « Références » et la possibilité d'insérer des textes d'introduction ([#1722](https://github.com/SocialGouv/cdtn-admin/issues/1722)).
- Flexibilité accrue sur les médias : les images sont désormais facultatives ([#1735](https://github.com/SocialGouv/cdtn-admin/issues/1735)).
- Amélioration de la gestion temporelle : gestion des fuseaux horaires (Paris), tolérance des dates et conservation de la date de première publication lors des modifications ([#1730](https://github.com/SocialGouv/cdtn-admin/issues/1730), [#1731](https://github.com/SocialGouv/cdtn-admin/issues/1731)).

**Analyse et Statistiques**
- Ajout de nouveaux indicateurs de performance : taux de complétion des pages modèles ([#1724](https://github.com/SocialGouv/cdtn-admin/issues/1724)) et suivi des données relatives aux actualités ([#1728](https://github.com/SocialGouv/cdtn-admin/issues/1728)).
- Intégration du suivi des parcours après contribution et des fiches Service-Public ([#7562](https://github.com/SocialGouv/cdtn-admin/issues/7562), [#1738](https://github.com/SocialGouv/cdtn-admin/issues/1738)).

**Export**
- Inclusion des liens recommandés issus des fiches Service-Public dans les exports (pipeline L2) ([#1719](https://github.com/SocialGouv/cdtn-admin/issues/1719)).

### Évolutions techniques

**Données et Reporting**
- Mise en place de capacités Metabase pour la création de tableaux de bord personnalisés.
- Nettoyage et optimisation des scripts d'agrégation de données pour l'analyse.

**Sécurité et Infrastructure**
- Mise à jour de Node.js vers la version 24.22.1 pour répondre aux correctifs de sécurité d'octobre 2026 ([#1732](https://github.com/SocialGouv/cdtn-admin/issues/1732)).
