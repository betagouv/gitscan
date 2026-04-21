## Changelog : sites-faciles (30 derniers jours, au 16 avril 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de l'internationalisation (i18n) du projet, notamment pour les formulaires et les menus, ainsi que sur l'optimisation des performances et la correction de bugs. Des améliorations ont également été apportées à l'administration et à la gestion des sitemaps.

### Évolutions fonctionnelles
- Ajout d'un sélecteur de langue dans l'interface d'administration pour faciliter la gestion du contenu multilingue. [#463](https://github.com/numerique-gouv/sites-faciles/issues/463)
- Internationalisation des champs de formulaire, permettant l'affichage des labels et des messages dans différentes langues. [#481](https://github.com/numerique-gouv/sites-faciles/issues/481)
- Possibilité d'exclure des pages du sitemap via un nouveau champ dans l'interface d'administration. [#466](https://github.com/numerique-gouv/sites-faciles/issues/466)
- Amélioration du menu utilisateur avec une présentation plus claire.
- Ajout de la possibilité d'obtenir l'image de prévisualisation d'une page via une requête.
- Correction de l'alignement des boutons.

### Évolutions techniques
- Optimisation des requêtes et ajout d'un cache avec un délai d'expiration pour améliorer les performances du tutoriel. [#473](https://github.com/numerique-gouv/sites-faciles/issues/473)
- Correction de la configuration de l'en-tête configurable. [#469](https://github.com/numerique-gouv/sites-faciles/issues/469)
- Suppression de la synchronisation avec Notion. [#465](https://github.com/numerique-gouv/sites-faciles/issues/465)
- Suppression des migrations inutiles et correction d'une migration existante.
- Mise à jour des dépendances Python. [#475](https://github.com/numerique-gouv/sites-faciles/issues/475)
- Amélioration de la couverture des tests.
- Suppression des traductions DjangoJS et des locales inutiles.

### Autres changements
- Ajout de commentaires pour améliorer la lisibilité du code.
- Correction de clés de langues.
- Correction de messages.
- Modification du nom d'une variable pour la constante de cache.
- Correction de l'URL de la page.
