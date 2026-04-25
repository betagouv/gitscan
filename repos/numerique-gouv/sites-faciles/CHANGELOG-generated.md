## Changelog : sites-faciles (30 derniers jours, au 23 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'internationalisation de la plateforme, avec l'ajout de la gestion de plusieurs langues pour les formulaires et les menus. Des optimisations de performance ont également été apportées au panneau de tutoriel et à la récupération des images de prévisualisation. Enfin, un déploiement en un clic sur Scalingo a été mis en place pour faciliter le déploiement des sites.

### Évolutions fonctionnelles
- Ajout d'un sélecteur de langue pour l'administration et les formulaires, permettant la gestion de contenu multilingue. [#481](https://github.com/numerique-gouv/sites-faciles/pull/481)
- Possibilité d'exclure des pages du sitemap via un nouveau champ. [#466](https://github.com/numerique-gouv/sites-faciles/pull/466)
- Amélioration du menu utilisateur avec une présentation plus claire.
- Ajout de la possibilité d'obtenir l'image de prévisualisation d'une page via une requête. [#463](https://github.com/numerique-gouv/sites-faciles/pull/463)
- Optimisation de la récupération des images de prévisualisation avec ajout d'un cache et d'un timeout.

### Évolutions techniques
- Mise en place d'un déploiement en un clic sur la plateforme Scalingo. [#484](https://github.com/numerique-gouv/sites-faciles/pull/484)
- Internationalisation des champs de formulaire. [#481](https://github.com/numerique-gouv/sites-faciles/pull/481)
- Optimisation du panneau de tutoriel pour améliorer les performances. [#473](https://github.com/numerique-gouv/sites-faciles/pull/473)
- Correction d'un bug lié à l'URL des pages.
- Correction d'un bug lié à l'en-tête configurable. [#469](https://github.com/numerique-gouv/sites-faciles/pull/469)
- Mise à jour des dépendances Python. [#475](https://github.com/numerique-gouv/sites-faciles/pull/475)
- Suppression de la synchronisation avec Notion. [#465](https://github.com/numerique-gouv/sites-faciles/pull/465)

### Autres changements
- Amélioration de l'alignement des boutons.
- Ajout de commentaires dans le code pour une meilleure lisibilité.
- Correction de la migration.
- Modification du nom d'une variable pour la constante de cache.
- Ajout d'une gestion d'erreur lors de la validation.
