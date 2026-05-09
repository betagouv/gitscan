## Changelog : sites-conformes (30 derniers jours, au 7 mai 2026)

### Résumé
Ce changelog présente les améliorations apportées à Sites Conformes au cours du dernier mois. Les principales évolutions concernent l'internationalisation de l'interface d'administration, des corrections de bugs liés aux formulaires et à la gestion des URLs, ainsi que la mise en place d'un déploiement simplifié sur Scalingo.

### Évolutions fonctionnelles
- **Internationalisation:** Ajout de la gestion de l'internationalisation (i18n) pour les champs de formulaire dans l'administration, permettant d'afficher les formulaires dans différentes langues. [#481](https://github.com/numerique-gouv/sites-conformes/pull/481) et [#464](https://github.com/numerique-gouv/sites-conformes/pull/464)
- **Sélecteur de langue:** Intégration d'un sélecteur de langue dans l'interface d'administration. [#473](https://github.com/numerique-gouv/sites-conformes/pull/473)
- **Menu utilisateur:** Amélioration du menu utilisateur avec une implémentation plus appropriée. [#3b6f4d2](https://github.com/numerique-gouv/sites-conformes/commit/3b6f4d2)
- **Correction de bug:** Résolution d'un problème où le nom des champs de formulaire pouvait être vide, causant des erreurs. [#492](https://github.com/numerique-gouv/sites-conformes/issues/492)
- **Correction d'URL:** Correction d'un problème lié à l'URL des pages. [#3733200](https://github.com/numerique-gouv/sites-conformes/commit/3733200)

### Évolutions techniques
- **Déploiement Scalingo:** Mise en place d'un déploiement en un clic sur la plateforme Scalingo, simplifiant le processus de mise en production. [#484](https://github.com/numerique-gouv/sites-conformes/pull/484)
- **Optimisation tutoriel panel:** Optimisation du panel de tutoriel. [#473](https://github.com/numerique-gouv/sites-conformes/pull/473)
- **Correction header configurable:** Correction du header configurable. [#469](https://github.com/numerique-gouv/sites-conformes/pull/469)
- **Refactoring migrations:** Suppression et correction de migrations. [#f085b55](https://github.com/numerique-gouv/sites-conformes/commit/f085b55) et [#50e8757](https://github.com/numerique-gouv/sites-conformes/commit/50e8757)

### Autres changements
- Mise à jour du nom du dépôt. [#493](https://github.com/numerique-gouv/sites-conformes/pull/493)
- Mise à jour des dépendances. [#483](https://github.com/numerique-gouv/sites-conformes/pull/483) et [#1e7b552](https://github.com/numerique-gouv/sites-conformes/commit/1e7b552)
- Modification du nom d'une variable de cache pour plus de clarté. [#15bffb8](https://github.com/numerique-gouv/sites-conformes/commit/15bffb8)
- Ajout de commentaires pour améliorer la lisibilité du code. [#f58d720](https://github.com/numerique-gouv/sites-conformes/commit/f58d720)
- Ajout de gestion d'erreur lors de la validation. [#9fef8cc](https://github.com/numerique-gouv/sites-conformes/commit/9fef8cc)
- Ajout d'un script pour le sélecteur de langue dans l'administration. [#4f787cd](https://github.com/numerique-gouv/sites-conformes/commit/4f787cd)
- Ajout d'un script pour le sélecteur de langue dans l'administration. [#154bec6](https://github.com/numerique-gouv/sites-conformes/commit/154bec6)
