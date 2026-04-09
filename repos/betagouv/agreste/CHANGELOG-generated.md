## Changelog : agreste (30 derniers jours, au 2 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'internationalisation du site, la simplification de la gestion des menus, et des corrections concernant l'affichage des images et la pagination sur les pages de tags. La synchronisation avec Notion a été supprimée, ainsi que certains fichiers de locales et de traductions inutilisés.

### Évolutions fonctionnelles
- Possibilité d'internationaliser les menus du site. [#463](https://github.com/betagouv/agreste/issues/463)
- Amélioration de l'affichage des images sur les pages de tags : suppression de l'image sur les cartes et simplification des blocs d'images et de citations. [#432](https://github.com/betagouv/agreste/issues/432)
- Correction de la pagination sur la vue des tags.
- Ajout d'un champ pour exclure des pages du sitemap. [#466](https://github.com/betagouv/agreste/issues/466)
- Mise à jour du composant `UserbarPageAPILinkItem`. [#462](https://github.com/betagouv/agreste/issues/462)
- Correction de l'affichage des titres. [#459](https://github.com/betagouv/agreste/issues/459)

### Évolutions techniques
- Suppression de la synchronisation avec Notion et de l'action GitHub associée. [#475](https://github.com/betagouv/agreste/issues/475)
- Suppression du Makefile. [#460](https://github.com/betagouv/agreste/issues/460)
- Refonte des menus, améliorant leur structure et leur maintenabilité. [#389](https://github.com/betagouv/agreste/issues/389)
- Suppression des fichiers de locales et des traductions DjangoJS inutilisés.
- Amélioration de la couverture des tests.
- Génération et ajout de migrations pour les changements de structure de données.

### Autres changements
- Initialisation d'une application Wagtail de base gérée par `uv`.
- Mise à jour des dépendances Python.
- Correction de messages.
- Mise à jour des clés de langues.
