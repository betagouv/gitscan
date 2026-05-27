## Changelog : cdata (30 derniers jours, au 26 mai 2026)

### Résumé
Ce mois-ci, l'application data.gouv.fr a bénéficié d'améliorations significatives en termes de recherche, d'administration et d'expérience utilisateur. Des fonctionnalités ont été ajoutées pour faciliter la gestion des organisations, des utilisateurs et des mots de passe, tout en optimisant la recherche et l'affichage des données. La migration vers Nuxt 4 continue d'apporter des améliorations de performance et de stabilité.

### Évolutions fonctionnelles
- **Recherche :**
    - Annonce du nombre de résultats de recherche et possibilité de focaliser le curseur directement sur le champ de recherche [#1096](https://github.com/datagouv/cdata/issues/1096).
    - Correction d'un bug empêchant la réinitialisation du champ de recherche après une recherche vide [#1083](https://github.com/datagouv/cdata/issues/1083).
    - Amélioration des filtres personnalisés dans la recherche, avec configuration du placeholder [#1062](https://github.com/datagouv/cdata/issues/1062), [#1059](https://github.com/datagouv/cdata/issues/1059), [#1067](https://github.com/datagouv/cdata/issues/1067).
- **Administration :**
    - Réintroduction du lien entre les jeux de données et les sujets (topics) [#1082](https://github.com/datagouv/cdata/issues/1082).
    - Possibilité de faire pivoter le mot de passe des utilisateurs en administration [#1078](https://github.com/datagouv/cdata/issues/1078).
    - Correction d'un bug où la recherche "q" dans l'administration ne réinitialisait pas la pagination [#1089](https://github.com/datagouv/cdata/issues/1089).
- **Utilisateurs et Notifications :**
    - Ajout de nouvelles notifications [#1076](https://github.com/datagouv/cdata/issues/1076).
    - Affichage des callbacks en attente et ajout d'un sujet utilisateur [#1073](https://github.com/datagouv/cdata/issues/1073).
    - Affichage des activités pour les membres d'une organisation [#1052](https://github.com/datagouv/cdata/issues/1052).
- **Affichage des données :**
    - Amélioration de l'affichage des contacts [#1075](https://github.com/datagouv/cdata/issues/1075).
    - Ajout d'un segment tabulaire pour l'affichage des données [#1072](https://github.com/datagouv/cdata/issues/1072).
    - Ajout d'une preuve de concept de visualisation (viz poc) [#963](https://github.com/datagouv/cdata/issues/963).
    - Ajout de données sénatoriales aux élections [#1091](https://github.com/datagouv/cdata/issues/1091).
- **Guides :**
    - Correction des URLs des guides [#1077](https://github.com/datagouv/cdata/issues/1077).
    - Ajout d'un lien vers le score de qualité dans les guides [#1061](https://github.com/datagouv/cdata/issues/1061).

### Évolutions techniques
- **Nuxt :** Mise à jour vers Nuxt 4.3 et 4.4 [#1037](https://github.com/datagouv/cdata/issues/1037), [#1038](https://github.com/datagouv/cdata/issues/1038).
- **Dépendances :** Mise à jour de `geopf-extensions-openlayers` vers la version 1.0.0-beta.10 [#1085](https://github.com/datagouv/cdata/issues/1085).
- **Optimisations :** Ajout de dépendances optimisées [#1086](https://github.com/datagouv/cdata/issues/1086).
- **Documentation :** Alignement du README avec Nuxt 4 [#1068](https://github.com/datagouv/cdata/issues/1068).
- **SEO :** Améliorations du référencement (SEO) [#1066](https://github.com/datagouv/cdata/issues/1066).

### Autres changements
- Correction de redirections cassées dans la configuration [#1065](https://github.com/datagouv/cdata/issues/1065).
- Ignorer le répertoire du cache pnpm local [#1071](https://github.com/datagouv/cdata/issues/1071).
- Correction d'un effet de bord dans le code [#1080](https://github.com/datagouv/cdata/issues/1080), [#1079](https://github.com/datagouv/cdata/issues/1079).
- Correction de la signature `mobileVisibleFields` [#1058](https://github.com/datagouv/cdata/issues/1058).
- Nouvelle disposition pour les pages d'organisation [#1051](https://github.com/datagouv/cdata/issues/1051).
