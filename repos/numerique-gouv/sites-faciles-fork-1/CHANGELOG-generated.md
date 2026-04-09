## Changelog : sites-faciles-fork-1 (30 derniers jours, au 02 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'internationalisation, la gestion des sitemaps, la correction de bugs liés aux images et aux tags, ainsi que la suppression de fonctionnalités obsolètes comme la synchronisation Notion et le Makefile. Ces changements visent à améliorer l'expérience utilisateur et la maintenabilité du projet.

### Évolutions fonctionnelles
- **Internationalisation des menus:** Les menus sont désormais internationalisables, permettant d'afficher le contenu dans différentes langues. ([#463](https://github.com/numerique-gouv/sites-faciles-fork-1/issues/463))
- **Exclusion de pages du sitemap:** Possibilité d'exclure des pages spécifiques du sitemap, offrant un contrôle plus fin sur l'indexation par les moteurs de recherche. ([#466](https://github.com/numerique-gouv/sites-faciles-fork-1/issues/466))
- **Correction des images dans le catalogue de tags:** Amélioration de l'affichage des images dans le catalogue de tags, notamment en supprimant l'image des cartes et en simplifiant les blocs d'images et de texte. ([#432](https://github.com/numerique-gouv/sites-faciles-fork-1/issues/432))
- **Correction de la pagination sur la page des tags:** La pagination sur la page des tags a été corrigée pour une meilleure navigation.
- **Mise à jour du composant UserbarPageAPILinkItem:** Amélioration du composant UserbarPageAPILinkItem. ([#462](https://github.com/numerique-gouv/sites-faciles-fork-1/issues/462))

### Évolutions techniques
- **Suppression de la synchronisation Notion:** La synchronisation avec Notion a été supprimée, simplifiant ainsi l'infrastructure du projet. ([#465](https://github.com/numerique-gouv/sites-faciles-fork-1/issues/465))
- **Suppression du Makefile:** Le Makefile a été supprimé. ([#460](https://github.com/numerique-gouv/sites-faciles-fork-1/issues/460))
- **Suppression des locales et des traductions DjangoJS:** Suppression des fichiers de locales et des traductions DjangoJS pour alléger le projet.
- **Amélioration de la couverture de tests:** Augmentation de la couverture de tests pour garantir la qualité du code.
- **Refonte des menus:** Refonte complète de la gestion des menus. ([#389](https://github.com/numerique-gouv/sites-faciles-fork-1/issues/389))
- **Regénération des migrations:** Regénération des migrations pour assurer la cohérence de la base de données.

### Autres changements
- Mise à jour des clés de langues.
- Correction de messages.
- Correction d'un bug lié à l'affichage des tags sur les pages en preview.
