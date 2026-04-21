## Changelog : drive (30 derniers jours, au 20 avril 2026)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur l'amélioration de l'expérience de prévisualisation des fichiers, en particulier pour les PDF et les images. De nouvelles fonctionnalités comme la duplication d'éléments et la personnalisation des colonnes dans l'explorateur de fichiers ont également été ajoutées, ainsi que des corrections de bugs pour améliorer la stabilité et la fiabilité de la plateforme. Des optimisations de performance et des améliorations de l'infrastructure ont également été réalisées.

### Évolutions fonctionnelles
- Ajout de la possibilité de prévisualiser les fichiers PDF avec navigation par pages et zoom. [#3030f71](https://github.com/suitenumerique/drive/commit/3030f7189f177782025d9622603054654f46187a)
- Amélioration de la prévisualisation des images avec possibilité d'impression via le navigateur. [#49c0821](https://github.com/suitenumerique/drive/commit/49c082163686792053678a94b560369737651698)
- Implémentation de la duplication d'éléments (fichiers et dossiers). [#e817417](https://github.com/suitenumerique/drive/commit/e81741787b180956449967710f306512b559257e)
- Ajout de la possibilité de personnaliser les colonnes affichées dans l'explorateur de fichiers. [#a4569a3](https://github.com/suitenumerique/drive/commit/a4569a33179646624900841705f616656859913f)
- Amélioration de l'expérience d'upload avec affichage de la progression, gestion des erreurs et possibilité d'annulation. [#399c1a7](https://github.com/suitenumerique/drive/commit/399c1a768d89881455357884a2a9614235335f89)
- Ajout d'un menu d'actions sur mobile pour faciliter l'accès aux fonctionnalités. [#0cc97d6](https://github.com/suitenumerique/drive/commit/0cc97d6180497852793648444646725851054949)

### Évolutions techniques
- Refonte de la prévisualisation des fichiers pour une meilleure performance et maintenabilité. [#511ca27](https://github.com/suitenumerique/drive/commit/511ca2760636662002556691385553386409260d)
- Mise en place d'un système de cache pour les navigateurs Playwright dans les tests E2E. [#d194b51](https://github.com/suitenumerique/drive/commit/d194b5166355819634496697317654614933092a)
- Amélioration de l'infrastructure CI/CD pour un déploiement plus rapide et fiable. [#768f616](https://github.com/suitenumerique/drive/commit/768f6162b7391298361f89b34671c4b342645766) et [#bdfade5](https://github.com/suitenumerique/drive/commit/bdfade56683928008f99990261c9752c39114298)
- Mise à jour de plusieurs dépendances pour bénéficier des dernières corrections de sécurité et améliorations. [#8029d4f](https://github.com/suitenumerique/drive/commit/8029d4f85517939403571679394471571f299413) et [#d4a83b6](https://github.com/suitenumerique/drive/commit/d4a83b679311032644267864415c7179161b7a3e)
- Optimisation de la configuration Nginx pour servir les fichiers statiques de manière plus efficace. [#aca3adf](https://github.com/suitenumerique/drive/commit/aca3adf2793385207664f43917918290f1824947)

### Autres changements
- Mise à jour de la documentation pour refléter les nouvelles fonctionnalités et améliorations. [#30cfcc7](https://github.com/suitenumerique/drive/commit/30cfcc7466a21f953128045972b6a79025325181)
- Ajout de tests E2E pour assurer la qualité et la stabilité des nouvelles fonctionnalités.
- Corrections de bugs mineurs et améliorations de l'interface utilisateur.
- Ajout d'une commande pour purger les éléments supprimés. [#ea811ca](https://github.com/suitenumerique/drive/commit/ea811ca541f111792489498624913663491c037a)
