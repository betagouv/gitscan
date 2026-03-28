## Changelog : sante-mentale-etudiant (30 derniers jours, au 26 mars 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur et la maintenance technique du projet. On note une refonte des menus, des corrections de bugs sur l'affichage des cartes et des images, ainsi que des mises à jour des versions de Python et Django pour assurer la pérennité du site. La synchronisation avec Notion a été supprimée.

### Évolutions fonctionnelles
- **Menus :** Refonte complète des menus pour une meilleure navigation et expérience utilisateur. [#389](https://github.com/betagouv/sante-mentale-etudiant/pulls/389)
- **Cartes Horizontales :** Correction d'une régression affectant l'affichage des cartes horizontales en version 2.5.2. [#443](https://github.com/betagouv/sante-mentale-etudiant/issues/443)
- **Images et Tags :** Amélioration de l'affichage des images et de la pagination sur les pages de tags. [#432](https://github.com/betagouv/sante-mentale-etudiant/pulls/432)
- **UserbarPageAPILinkItem :** Mise à jour du composant `UserbarPageAPILinkItem`. [#462](https://github.com/betagouv/sante-mentale-etudiant/pulls/462)
- **Exclusion du Sitemap :** Ajout d'un champ permettant d'exclure des pages du sitemap. [#466](https://github.com/betagouv/sante-mentale-etudiant/pulls/466)

### Évolutions techniques
- **Versions Python et Django :** Mise à jour des versions minimum requises à Python 12 et Django 6.0 pour bénéficier des dernières améliorations et correctifs de sécurité. [#449](https://github.com/betagouv/sante-mentale-etudiant/pulls/449)
- **CI/CD :** Ajout de nouvelles actions dans la CI pour améliorer la qualité du code et la gestion de l'internationalisation. [#431](https://github.com/betagouv/sante-mentale-etudiant/pulls/431)
- **Suppression Notion Sync :** Suppression de la synchronisation avec Notion et de l'action GitHub associée. [#465](https://github.com/betagouv/sante-mentale-etudiant/pulls/465) et [#466](https://github.com/betagouv/sante-mentale-etudiant/pulls/466)
- **Makefile :** Suppression du Makefile. [#460](https://github.com/betagouv/sante-mentale-etudiant/pulls/460)
- **Git Blame :** Ajout d'une configuration pour ignorer certaines révisions dans `git blame`. [#440](https://github.com/betagouv/sante-mentale-etudiant/pulls/440)
- **Suppression Locales :** Suppression des fichiers de locales inutiles.

### Autres changements
- **Documentation :** Correction de problèmes de formatage Markdown dans la documentation. [#448](https://github.com/betagouv/sante-mentale-etudiant/pulls/448)
- **Mise à jour des dépendances :** Mise à jour des numéros de version des dépendances du projet. [#447](https://github.com/betagouv/sante-mentale-etudiant/pulls/447)
- **Corrections de clés de langues :** Mise à jour des clés de langues pour assurer la cohérence des traductions.
- **Amélioration de la couverture de tests :** Augmentation de la couverture de tests pour garantir la qualité du code.
