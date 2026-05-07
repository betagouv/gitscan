## Changelog : sites-faciles (30 derniers jours, au 6 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'internationalisation de la plateforme, notamment l'ajout d'un sélecteur de langue et la traduction des champs de formulaire.  Des corrections de bugs et des optimisations ont également été apportées, ainsi qu'une simplification du déploiement sur Scalingo.

### Évolutions fonctionnelles
- Ajout d'un sélecteur de langue dans l'interface d'administration pour faciliter la gestion du contenu multilingue. [#464](https://github.com/numerique-gouv/sites-faciles/pull/464)
- Internationalisation des champs de formulaire, permettant leur traduction et améliorant l'expérience utilisateur pour les différentes langues. [#481](https://github.com/numerique-gouv/sites-faciles/pull/481) et [#420](https://github.com/numerique-gouv/sites-faciles/pull/420)
- Correction d'un bug empêchant le bon fonctionnement du nettoyage des noms de champs de formulaire. [#492](https://github.com/numerique-gouv/sites-faciles/issues/492)
- Ajout d'un menu utilisateur plus clair et fonctionnel. [#3b6f4d2](https://github.com/numerique-gouv/sites-faciles/commit/3b6f4d2)
- Correction de l'URL des pages. [#3733200](https://github.com/numerique-gouv/sites-faciles/commit/3733200)

### Évolutions techniques
- Mise en place d'un déploiement en un clic sur la plateforme Scalingo, simplifiant le processus de mise en production. [#484](https://github.com/numerique-gouv/sites-faciles/pull/484)
- Optimisation du panneau tutoriel. [#473](https://github.com/numerique-gouv/sites-faciles/pull/473)
- Correction d'un problème lié à l'en-tête configurable. [#469](https://github.com/numerique-gouv/sites-faciles/pull/469)
- Correction de la migration. [#f085b55](https://github.com/numerique-gouv/sites-faciles/commit/f085b55)
- Suppression d'une migration inutile. [#50e8757](https://github.com/numerique-gouv/sites-faciles/commit/50e8757)

### Autres changements
- Mise à jour des dépendances du projet.
- Modifications diverses pour améliorer la lisibilité et la maintenabilité du code.
- Ajout de commentaires pour faciliter la compréhension du code. [#f58d720](https://github.com/numerique-gouv/sites-faciles/commit/f58d720)
- Ajout d'un script pour le sélecteur de langue dans l'administration. [#4f787cd](https://github.com/numerique-gouv/sites-faciles/commit/4f787cd)
- Ajout d'une gestion des erreurs lors de la validation. [#9fef8cc](https://github.com/numerique-gouv/sites-faciles/commit/9fef8cc)
- Changement de nom de variable pour une constante de cache. [#15bffb8](https://github.com/numerique-gouv/sites-faciles/commit/15bffb8)
- Ajout de la gestion de l'internationalisation (i18n). [#154bec6](https://github.com/numerique-gouv/sites-faciles/commit/154bec6)
