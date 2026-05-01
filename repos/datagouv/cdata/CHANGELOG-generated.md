## Changelog : cdata (30 derniers jours, au 30 avril 2026)

### Résumé
Ce mois-ci, l'application cdata a bénéficié d'une refonte majeure avec la migration vers Nuxt 4, apportant des améliorations de performance et de nouvelles fonctionnalités. L'expérience utilisateur a été améliorée grâce à une nouvelle présentation des pages d'organisation, une exploration tabulaire des données, et des optimisations de la recherche. Des corrections de bugs et des améliorations de la documentation complètent ces évolutions.

### Évolutions fonctionnelles
- **Recherche :**
    - Ajout de la prise en charge des sujets (Topics) dans la recherche globale [#1030](https://github.com/datagouv/cdata/issues/1030).
    - Possibilité de configurer le placeholder de la barre de recherche [#1059](https://github.com/datagouv/cdata/issues/1059).
    - Possibilité de définir plusieurs configurations pour la même classe de recherche [#1049](https://github.com/datagouv/cdata/issues/1049).
    - Suppression des filtres personnalisés après utilisation [#1064](https://github.com/datagouv/cdata/issues/1064).
- **Exploration des données :**
    - Nouvelle exploration tabulaire des données [#971](https://github.com/datagouv/cdata/issues/971).
    - Amélioration de la présentation responsive de l'explorateur de ressources [#1014](https://github.com/datagouv/cdata/issues/1014).
- **Pages d'organisation :** Nouvelle présentation des pages d'organisation [#1051](https://github.com/datagouv/cdata/issues/1051).
- **SEO :** Améliorations du référencement naturel (SEO) [#1066](https://github.com/datagouv/cdata/issues/1066).
- **Documentation :** Ajout de documentation sur l'obtention d'une clé API de démonstration [#1045](https://github.com/datagouv/cdata/issues/1045).
- **Formulaires :** Affichage du lien vers le feedback IA uniquement après une suggestion [#1046](https://github.com/datagouv/cdata/issues/1046).
- **Qualité des données :** Lien vers le score de qualité dans les guides [#1061](https://github.com/datagouv/cdata/issues/1061).

### Évolutions techniques
- **Migration Nuxt :** Mise à niveau vers Nuxt 4 (versions 4.0, 4.1, 4.2, 4.3 et 4.4) [#1023](https://github.com/datagouv/cdata/issues/1023), [#1035](https://github.com/datagouv/cdata/issues/1035), [#1047](https://github.com/datagouv/cdata/issues/1047), [#1037](https://github.com/datagouv/cdata/issues/1037), [#1038](https://github.com/datagouv/cdata/issues/1038).
- **Refactoring :** Suppression de la duplication entre les aperçus [#1018](https://github.com/datagouv/cdata/issues/1018).
- **Correction de bugs :** Correction de problèmes liés à l'initialisation des fonctionnalités du récolteur [#1043](https://github.com/datagouv/cdata/issues/1043).
- **Optimisations :** Utilisation d'images SVG optimisées avec svgo [#1057](https://github.com/datagouv/cdata/issues/1057).
- **CI/CD :** Mise à jour des versions des actions utilisées dans le workflow CI/CD [#1013](https://github.com/datagouv/cdata/issues/1013).
- **Correction de patch Nuxt :** Correction d'un patch Nuxt qui n'était plus appliqué [#1039](https://github.com/datagouv/cdata/issues/1039).
- **Correction de build assets URL :** Correction d'un problème lié à `__buildAssetsURL` dans Nuxt [#1024](https://github.com/datagouv/cdata/issues/1024).

### Autres changements
- Améliorations de la page de modération, notamment l'ajout d'onglets pour filtrer les types de sujets [#1033](https://github.com/datagouv/cdata/issues/1033) et l'amélioration de la présentation [#1021](https://github.com/datagouv/cdata/issues/1021).
- Correction de redirections cassées dans la configuration [#1065](https://github.com/datagouv/cdata/issues/1065).
- Correction d'un problème de débordement de cellule dans le tableau de bord de modération [#1050](https://github.com/datagouv/cdata/issues/1050).
- Correction d'un problème lié aux valeurs manquantes pour les sujets [#1032](https://github.com/datagouv/cdata/issues/1032).
- Suppression d'une réversion précédente [#1029](https://github.com/datagouv/cdata/issues/1029).
- Correction de liens oEmbed [#1026](https://github.com/datagouv/cdata/issues/1026).
- Ajout d'informations supplémentaires sur les aperçus manquants [#1025](https://github.com/datagouv/cdata/issues/1025).
- Correction de problèmes de fluidité des tests [#1028](https://github.com/datagouv/cdata/issues/1028).
