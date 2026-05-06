## Changelog : cdata (30 derniers jours, au 5 mai 2026)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur la migration vers Nuxt 4, apportant des améliorations de performance et de stabilité. De nouvelles fonctionnalités ont été ajoutées à la recherche, notamment la prise en charge de filtres personnalisés et des sujets, ainsi que des améliorations de l'interface utilisateur pour les pages d'organisation et l'exploration tabulaire des données. Des corrections de bugs et des améliorations de la documentation complètent ces évolutions.

### Évolutions fonctionnelles
- **Recherche :**
  - Ajout de filtres personnalisés et prise en charge des sujets dans la recherche globale [#1067](https://github.com/datagouv/cdata/issues/1067), [#1048](https://github.com/datagouv/cdata/issues/1048), [#1030](https://github.com/datagouv/cdata/issues/1030).
  - Possibilité de configurer le placeholder de la barre de recherche [#1059](https://github.com/datagouv/cdata/issues/1059).
  - Amélioration de la gestion des configurations pour les filtres de recherche [#1049](https://github.com/datagouv/cdata/issues/1049).
- **Pages d'organisation :** Nouvelle mise en page pour les pages d'organisation [#1051](https://github.com/datagouv/cdata/issues/1051).
- **Exploration tabulaire :** Nouvelle interface pour l'exploration tabulaire des données [#971](https://github.com/datagouv/cdata/issues/971).
- **Documentation :** Ajout d'informations sur l'obtention d'une clé API pour la démo [#1045](https://github.com/datagouv/cdata/issues/1045).
- **Swagger :** Affichage de l'interface Swagger [#1055](https://github.com/datagouv/cdata/issues/1055) et nouvelle implémentation personnalisée [#1012](https://github.com/datagouv/cdata/issues/1012).
- **SEO :** Améliorations du référencement naturel (SEO) [#1066](https://github.com/datagouv/cdata/issues/1066).
- **Visualisation :** Ajout d'une première preuve de concept pour les visualisations [#963](https://github.com/datagouv/cdata/issues/963).

### Évolutions techniques
- **Migration Nuxt :** Mise à jour vers Nuxt 4.4, 4.3, 4.2, 4.1 et 4.0 [#1038](https://github.com/datagouv/cdata/issues/1038), [#1037](https://github.com/datagouv/cdata/issues/1037), [#1047](https://github.com/datagouv/cdata/issues/1047), [#1035](https://github.com/datagouv/cdata/issues/1035), [#1023](https://github.com/datagouv/cdata/issues/1023).
- **Refactoring :** Suppression de duplication de code dans les previews [#1018](https://github.com/datagouv/cdata/issues/1018).
- **Corrections :** Correction de problèmes liés à l'initialisation des fonctionnalités du récolteur [#1043](https://github.com/datagouv/cdata/issues/1043).
- **Optimisations :** Utilisation d'images SVG statiques optimisées avec svgo [#1057](https://github.com/datagouv/cdata/issues/1057).
- **CI/CD :** Mise à jour des versions des actions utilisées dans le workflow CI/CD [#1013](https://github.com/datagouv/cdata/issues/1013).
- **Corrections Nuxt :** Patchs appliqués pour corriger des problèmes spécifiques à Nuxt [#1053](https://github.com/datagouv/cdata/issues/1053), [#1039](https://github.com/datagouv/cdata/issues/1039), [#1024](https://github.com/datagouv/cdata/issues/1024).

### Autres changements
- **Documentation :** Alignement du README avec Nuxt 4 [#1068](https://github.com/datagouv/cdata/issues/1068).
- **Corrections :** Correction de redirections cassées dans la configuration [#1065](https://github.com/datagouv/cdata/issues/1065).
- **Améliorations :** Ajout d'informations sur les previews manquantes [#1025](https://github.com/datagouv/cdata/issues/1025).
- **Dashboard de modération :** Améliorations de la page de modération, notamment l'ajout d'onglets pour filtrer les types de sujets [#1033](https://github.com/datagouv/cdata/issues/1033) et la correction de problèmes d'overflow dans les cellules [#1050](https://github.com/datagouv/cdata/issues/1050).
- **Feedback IA :** Affichage du lien vers le feedback IA uniquement après une suggestion [#1046](https://github.com/datagouv/cdata/issues/1046).
- **Corrections :** Correction d'un problème de valeur manquante pour les sujets [#1032](https://github.com/datagouv/cdata/issues/1032).
- **Revert :** Rétractation d'une modification concernant la liste des reviewers dans les pull requests [#1029](https://github.com/datagouv/cdata/issues/1029).
- **Ignore :** Ignorer le répertoire du cache pnpm local [#1071](https://github.com/datagouv/cdata/issues/1071).
