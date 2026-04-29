## Changelog : sites-faciles (30 derniers jours, au 23 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'internationalisation de la plateforme, avec l'ajout de la gestion de plusieurs langues pour les formulaires, les menus et le sélecteur de langue. Des optimisations de performance ont également été apportées, notamment au niveau de la récupération des images de prévisualisation. Enfin, un déploiement en un clic sur Scalingo a été mis en place pour faciliter le déploiement de l'application.

### Évolutions fonctionnelles
- Ajout d'un sélecteur de langue dans l'interface d'administration pour faciliter la gestion des traductions. [#464](https://github.com/numerique-gouv/sites-faciles/issues/464)
- Internationalisation des champs de formulaire, permettant d'afficher les formulaires dans différentes langues. [#481](https://github.com/numerique-gouv/sites-faciles/issues/481)
- Internationalisation des menus, permettant d'afficher les menus dans différentes langues. [#463](https://github.com/numerique-gouv/sites-faciles/issues/463)
- Ajout d'un menu utilisateur plus approprié.
- Possibilité d'obtenir l'image de prévisualisation d'une page via une requête. [#469](https://github.com/numerique-gouv/sites-faciles/issues/469)
- Optimisation de la récupération des images de prévisualisation avec ajout d'un cache et d'un timeout. [#473](https://github.com/numerique-gouv/sites-faciles/issues/473)

### Évolutions techniques
- Mise en place d'un déploiement en un clic sur la plateforme Scalingo. [#484](https://github.com/numerique-gouv/sites-faciles/issues/484)
- Correction d'une migration. [#483](https://github.com/numerique-gouv/sites-faciles/issues/483)
- Correction de l'URL de la page.
- Mise à jour des dépendances Python. [#475](https://github.com/numerique-gouv/sites-faciles/issues/475)

### Autres changements
- Ajout de commentaires dans le code.
- Suppression d'une migration inutile.
- Correction d'une erreur de validation.
- Modification du nom d'une variable de cache pour plus de clarté.
