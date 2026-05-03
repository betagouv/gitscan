## Changelog : cdata (30 derniers jours, au 30 avril 2026)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur l'amélioration de la recherche, la modernisation de la stack technologique avec une migration vers Nuxt 4, et l'amélioration de l'expérience utilisateur, notamment sur les pages d'organisation et l'explorateur tabulaire. Des corrections de bugs et des améliorations de la documentation ont également été apportées.

### Évolutions fonctionnelles
- **Recherche :**
    - Ajout de la prise en charge des sujets (Topics) dans la recherche globale [#1030](https://github.com/datagouv/cdata/issues/1030).
    - Possibilité de configurer le placeholder de la barre de recherche [#1059](https://github.com/datagouv/cdata/issues/1059).
    - Possibilité de définir plusieurs configurations pour une même classe de recherche [#1049](https://github.com/datagouv/cdata/issues/1049).
    - Ajout de filtres personnalisés à la recherche [#1048](https://github.com/datagouv/cdata/issues/1048).
    - Correction d'un bug qui empêchait le bon fonctionnement des filtres personnalisés [#1064](https://github.com/datagouv/cdata/issues/1064).
- **Pages d'organisation :** Nouvelle mise en page pour les pages d'organisation [#1051](https://github.com/datagouv/cdata/issues/1051).
- **Explorateur tabulaire :** Nouvelle fonctionnalité d'exploration tabulaire des données [#971](https://github.com/datagouv/cdata/issues/971) et amélioration de la réactivité [#1014](https://github.com/datagouv/cdata/issues/1014). Correction d'un bug lié à cette fonctionnalité [#1056](https://github.com/datagouv/cdata/issues/1056).
- **Documentation :** Ajout de documentation sur l'obtention d'une clé API pour la démo [#1045](https://github.com/datagouv/cdata/issues/1045).
- **Formulaires :** Le lien vers le feedback IA n'est affiché qu'après une suggestion [#1046](https://github.com/datagouv/cdata/issues/1046).
- **SEO :** Améliorations du référencement naturel (SEO) [#1066](https://github.com/datagouv/cdata/issues/1066).
- **Qualité des données :** Ajout d'un lien vers le score de qualité dans les guides [#1061](https://github.com/datagouv/cdata/issues/1061).

### Évolutions techniques
- **Migration Nuxt :** Mise à jour vers Nuxt 4.0, 4.1, 4.2, 4.3 et 4.4 [#1023](https://github.com/datagouv/cdata/issues/1023), [#1035](https://github.com/datagouv/cdata/issues/1035), [#1047](https://github.com/datagouv/cdata/issues/1047), [#1037](https://github.com/datagouv/cdata/issues/1037), [#1038](https://github.com/datagouv/cdata/issues/1038).
- **Refactoring :** Suppression de la duplication entre les previews [#1018](https://github.com/datagouv/cdata/issues/1018).
- **Correction de bugs :** Correction de problèmes liés à l'initialisation des fonctionnalités du récolteur [#1043](https://github.com/datagouv/cdata/issues/1043) et à l'application des patches Nuxt [#1039](https://github.com/datagouv/cdata/issues/1039), [#1053](https://github.com/datagouv/cdata/issues/1053).
- **Optimisation :** Utilisation d'images SVG optimisées avec svgo [#1057](https://github.com/datagouv/cdata/issues/1057).
- **CI/CD :** Mise à jour des versions des actions utilisées dans le workflow CI/CD [#1013](https://github.com/datagouv/cdata/issues/1013).
- **Modération :** Améliorations de la page de modération, notamment avec l'ajout d'onglets pour filtrer les types de sujets [#1033](https://github.com/datagouv/cdata/issues/1033) et la correction de problèmes d'overflow dans le tableau de bord [#1050](https://github.com/datagouv/cdata/issues/1050).

### Autres changements
- Correction de redirections cassées dans la configuration [#1065](https://github.com/datagouv/cdata/issues/1065).
- Correction d'un problème de signature `mobileVisibleFields` [#1058](https://github.com/datagouv/cdata/issues/1058).
- Correction d'un problème lié aux valeurs manquantes pour les sujets [#1032](https://github.com/datagouv/cdata/issues/1032).
- Suppression d'une réversion d'un changement précédent [#1029](https://github.com/datagouv/cdata/issues/1029).
- Correction de liens oEmbed [#1026](https://github.com/datagouv/cdata/issues/1026).
- Amélioration de l'affichage des blocs dans les publications [#1027](https://github.com/datagouv/cdata/issues/1027).
- Ajout d'informations sur les previews manquantes [#1025](https://github.com/datagouv/cdata/issues/1025).
- Correction de problèmes de flakiness dans les tests [#1028](https://github.com/datagouv/cdata/issues/1028).
