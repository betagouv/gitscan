## Changelog : sites-faciles (30 derniers jours, au 9 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'internationalisation, la gestion des menus, et la correction de bugs liés à l'affichage des images et des pages de tags. Des optimisations ont également été apportées pour simplifier la maintenance du projet en supprimant des éléments obsolètes comme la synchronisation Notion et le Makefile.

### Évolutions fonctionnelles
- **Internationalisation des menus :** Possibilité d'internationaliser les menus du site. [#463](https://github.com/numerique-gouv/sites-faciles/issues/463)
- **Exclusion de pages du sitemap :** Ajout d'un champ permettant d'exclure des pages du sitemap. [#466](https://github.com/numerique-gouv/sites-faciles/issues/466)
- **Amélioration de l'affichage des images :** Correction de bugs liés à l'affichage des images dans les vues par tags et dans le catalogue d'images. [#432](https://github.com/numerique-gouv/sites-faciles/issues/432)
- **Correction de l'affichage des titres :** Correction d'un bug lié à l'affichage des titres. [#459](https://github.com/numerique-gouv/sites-faciles/issues/459)
- **Composant UserbarPageAPILinkItem mis à jour :** Amélioration du composant UserbarPageAPILinkItem. [#462](https://github.com/numerique-gouv/sites-faciles/issues/462)

### Évolutions techniques
- **Suppression de la synchronisation Notion :** Suppression de l'action GitHub et du code associé à la synchronisation avec Notion. [#465](https://github.com/numerique-gouv/sites-faciles/issues/465)
- **Suppression du Makefile :** Suppression du Makefile pour simplifier la gestion du projet. [#460](https://github.com/numerique-gouv/sites-faciles/issues/460)
- **Refonte des menus :** Refonte complète de la gestion des menus. [#389](https://github.com/numerique-gouv/sites-faciles/issues/389)
- **Suppression des locales inutiles :** Suppression des fichiers de traduction DjangoJS et des locales non utilisées.
- **Amélioration de la couverture de tests :** Augmentation de la couverture de tests pour garantir la qualité du code.
- **Regénération des migrations :** Regénération des migrations pour assurer la cohérence de la base de données.

### Autres changements
- Mise à jour des dépendances Python. [#475](https://github.com/numerique-gouv/sites-faciles/issues/475)
- Mise à jour des clés de langues.
