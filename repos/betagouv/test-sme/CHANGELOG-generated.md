## Changelog : test-sme (30 derniers jours, au 26 mars 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur et la maintenance technique du projet. Des améliorations ont été apportées aux menus, aux cartes d'images et à la gestion des pages, ainsi que des corrections de bugs et des mises à jour de l'infrastructure CI/CD. La synchronisation avec Notion a été supprimée.

### Évolutions fonctionnelles
- **Menus :** Refonte complète des menus, améliorant l'ergonomie et la navigation. [#389](https://github.com/betagouv/test-sme/pulls/389)
- **Cartes d'images :** Correction d'une régression sur l'affichage des cartes horizontales en version 2.5.2. [#443](https://github.com/betagouv/test-sme/issues/443)
- **Pages de tags :** Amélioration de la pagination et suppression de l'image sur la page de tags pour optimiser l'affichage.
- **Exclusion du sitemap :** Ajout d'un champ permettant d'exclure une page du sitemap. [#466](https://github.com/betagouv/test-sme/pulls/466)
- **Composant UserbarPageAPILinkItem :** Mise à jour du composant pour améliorer sa fonctionnalité. [#462](https://github.com/betagouv/test-sme/pulls/462)
- **Correction d'un bug d'affichage des titres :** Correction d'un problème d'affichage des titres. [#459](https://github.com/betagouv/test-sme/pulls/459)

### Évolutions techniques
- **Mises à jour de versions :** Mise à jour des versions minimum requises de Python (12) et Django (6.0). [#449](https://github.com/betagouv/test-sme/pulls/449)
- **CI/CD :** Ajout de nouvelles actions CI pour la qualité du code et l'internationalisation. [#431](https://github.com/betagouv/test-sme/pulls/431)
- **Suppression de Notion Sync :** Suppression de la synchronisation avec Notion et de l'action GitHub associée. [#465](https://github.com/betagouv/test-sme/pulls/465), [#447](https://github.com/betagouv/test-sme/pulls/447)
- **Suppression du Makefile :** Suppression du Makefile. [#460](https://github.com/betagouv/test-sme/pulls/460)
- **Amélioration de la couverture de tests :** Augmentation de la couverture des tests unitaires.
- **Suppression des locales :** Suppression des fichiers de traductions inutiles.
- **Git blame :** Ajout de règles pour ignorer certaines révisions dans `git blame`. [#440](https://github.com/betagouv/test-sme/pulls/440)

### Autres changements
- **Documentation :** Correction de problèmes de formatage Markdown dans la documentation. [#448](https://github.com/betagouv/test-sme/pulls/448)
- **Nettoyage du code :** Suppression de code inutile et amélioration de la lisibilité.
- **Migrations :** Regeneration et ajout de migrations.
