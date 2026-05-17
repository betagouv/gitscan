## Changelog : cdata (30 derniers jours, au 15 mai 2026)

### Résumé
Ce mois-ci, l'application cdata a bénéficié d'une refonte importante de l'interface utilisateur, notamment pour les pages d'organisation et l'exploration des données tabulaires.  De nouvelles fonctionnalités de recherche et de filtrage ont été ajoutées, améliorant l'expérience utilisateur et la découverte de données.  Des améliorations de performance et des corrections de bugs ont également été implémentées.

### Évolutions fonctionnelles
- **Recherche :**
    - Ajout de filtres personnalisés et intelligents pour affiner les recherches [#1067](https://github.com/datagouv/cdata/issues/1067).
    - Possibilité de configurer le texte d'espace réservé dans la recherche [#1059](https://github.com/datagouv/cdata/issues/1059).
    - Exportation de types supplémentaires pour faciliter l'utilisation de la recherche [#1062](https://github.com/datagouv/cdata/issues/1062).
    - Correction du comportement des filtres personnalisés pour les effacer correctement [#1064](https://github.com/datagouv/cdata/issues/1064).
- **Exploration des données :**
    - Nouvelle interface pour l'exploration des données tabulaires, incluant une version responsive [#971](https://github.com/datagouv/cdata/issues/971) et [#1014](https://github.com/datagouv/cdata/issues/1014).
    - Amélioration de la présentation des pages d'organisation avec un nouveau layout [#1051](https://github.com/datagouv/cdata/issues/1051).
- **Guides :** Correction des URLs des guides [#1077](https://github.com/datagouv/cdata/issues/1077).
- **Callbacks :** Affichage des callbacks en attente et ajout du sujet utilisateur [#1073](https://github.com/datagouv/cdata/issues/1073).
- **Activité :** Affichage de l'activité pour les membres de l'organisation [#1052](https://github.com/datagouv/cdata/issues/1052).
- **Swagger :** Affichage de la documentation Swagger [#1055](https://github.com/datagouv/cdata/issues/1055).
- **SEO :** Améliorations du référencement naturel (SEO) [#1066](https://github.com/datagouv/cdata/issues/1066).
- **Segment Tabulaire :** Ajout d'un segment tabulaire [#1072](https://github.com/datagouv/cdata/issues/1072).

### Évolutions techniques
- **Nuxt :** Mise à jour vers Nuxt 4.4 et 4.3 [#1038](https://github.com/datagouv/cdata/issues/1038) et [#1037](https://github.com/datagouv/cdata/issues/1037).
- **Dépendances :** Mise à jour des dépendances du projet [#1060](https://github.com/datagouv/cdata/issues/1060).
- **Images SVG :** Utilisation d'images SVG simples et optimisation avec svgo [#1057](https://github.com/datagouv/cdata/issues/1057).
- **Nitro Server :** Correction d'un problème avec le serveur Nitro de Nuxt [#1053](https://github.com/datagouv/cdata/issues/1053).
- **README :** Alignement du README avec Nuxt 4 [#1068](https://github.com/datagouv/cdata/issues/1068).
- **Ignorer le store pnpm :** Ignorer le répertoire du store pnpm local pour éviter les problèmes de versionnement [#1071](https://github.com/datagouv/cdata/issues/1071).
- **No side effect :** Suppression des effets de bord dans le code [#1079](https://github.com/datagouv/cdata/issues/1079).

### Autres changements
- Correction de redirections cassées dans la configuration [#1065](https://github.com/datagouv/cdata/issues/1065).
- Correction d'un bug lié à la signature de `mobileVisibleFields` [#1058](https://github.com/datagouv/cdata/issues/1058).
- Tentative de correction d'un problème avec la nouvelle page /explore tabulaire [#1056](https://github.com/datagouv/cdata/issues/1056).
- Ajout d'un proof of concept pour la visualisation de données [#963](https://github.com/datagouv/cdata/issues/963).
- Lien vers le score de qualité dans les guides [#1061](https://github.com/datagouv/cdata/issues/1061).
