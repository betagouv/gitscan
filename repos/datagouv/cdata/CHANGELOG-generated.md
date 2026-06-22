## Changelog : cdata (30 derniers jours, au 19 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur, notamment dans l'explorateur tabulaire, la recherche et la visualisation des données. Des corrections de bugs et des optimisations de performance ont également été apportées pour améliorer la stabilité et la réactivité de la plateforme. Plusieurs améliorations techniques ont été implémentées, notamment concernant l'API Harvest et la configuration de Sentry.

### Évolutions fonctionnelles
- Amélioration de l'explorateur tabulaire avec des corrections et des améliorations de l'expérience utilisateur. [#1070](https://github.com/datagouv/cdata/issues/1070) et [#1127](https://github.com/datagouv/cdata/issues/1127)
- Amélioration de la visualisation des graphiques. [#1088](https://github.com/datagouv/cdata/issues/1088)
- Amélioration de la page des jeux de données réutilisés, affichant maintenant les champs "x-fields". [#1102](https://github.com/datagouv/cdata/issues/1102)
- Ajout d'une page dédiée aux sujets (topics). [#1110](https://github.com/datagouv/cdata/issues/1110)
- Possibilité de personnaliser les icônes des types de recherche. [#1109](https://github.com/datagouv/cdata/issues/1109)
- Possibilité de personnaliser le titre des cartes (TitleTag). [#1092](https://github.com/datagouv/cdata/issues/1092) et [#1119](https://github.com/datagouv/cdata/issues/1119)
- Amélioration de l'affichage de l'ID de la ressource impactée dans les activités. [#1123](https://github.com/datagouv/cdata/issues/1123)
- Ajout de la possibilité de marquer les notifications comme lues. [#1103](https://github.com/datagouv/cdata/issues/1103)
- Clarification de l'accès à l'API Tabular. [#1108](https://github.com/datagouv/cdata/issues/1108)
- Amélioration de l'affichage de l'image de réutilisation à l'étape 3 de la création. [#1134](https://github.com/datagouv/cdata/issues/1134)
- Amélioration de l'affichage de l'OpenAPI response viewer pour les dataservices. [#1100](https://github.com/datagouv/cdata/issues/1100)

### Évolutions techniques
- Utilisation de la nouvelle API Harvest. [#1074](https://github.com/datagouv/cdata/issues/1074)
- Mise à jour des dépendances. [#1105](https://github.com/datagouv/cdata/issues/1105)
- Configuration de Sentry pour la surveillance des erreurs. [#1126](https://github.com/datagouv/cdata/issues/1126) et [#1122](https://github.com/datagouv/cdata/issues/1122)
- Optimisation des performances en supprimant les appels d'API dupliqués. [#1129](https://github.com/datagouv/cdata/issues/1129)
- Amélioration de la gestion des erreurs CORS. [#1098](https://github.com/datagouv/cdata/issues/1098) et [#1116](https://github.com/datagouv/cdata/issues/1116)
- Utilisation de `NODE_ENV production` dans le Dockerfile. [#1104](https://github.com/datagouv/cdata/issues/1104)
- Remplacement de "owner" par "organization" pour l'appel d'API harvest. [#1133](https://github.com/datagouv/cdata/issues/1133)
- Possibilité de désactiver Echarts. [#1095](https://github.com/datagouv/cdata/issues/1095)
- Correction de la configuration des runs CI pour la branche udata. [#1131](https://github.com/datagouv/cdata/issues/1131)
- Suppression des layers dans le type de métadonnées WFS. [#1140](https://github.com/datagouv/cdata/issues/1140)

### Autres changements
- Correction de bugs divers liés à l'interface utilisateur et à la navigation. [#1142](https://github.com/datagouv/cdata/issues/1142), [#1143](https://github.com/datagouv/cdata/issues/1143), [#1144](https://github.com/datagouv/cdata/issues/1144), [#1146](https://github.com/datagouv/cdata/issues/1146), [#1147](https://github.com/datagouv/cdata/issues/1147), [#1148](https://github.com/datagouv/cdata/issues/1148), [#1135](https://github.com/datagouv/cdata/issues/1135), [#1138](https://github.com/datagouv/cdata/issues/1138)
- Ajout de timestamps dans les logs. [#1084](https://github.com/datagouv/cdata/issues/1084)
- Correction de la gestion des credentials avec la nouvelle politique CORS. [#1098](https://github.com/datagouv/cdata/issues/1098)
- Activation des pull request runs pour les contributions externes. [#1042](https://github.com/datagouv/cdata/issues/1042)
- Correction des pages 404. [#1094](https://github.com/datagouv/cdata/issues/1094)
- Masquage des statistiques de téléchargement sans jeux de données. [#1113](https://github.com/datagouv/cdata/issues/1113)
- Ajout d'une URI QR code pour l'authentification à deux facteurs. [#1090](https://github.com/datagouv/cdata/issues/1090)
- Amélioration de l'accessibilité de la recherche avec l'annonce du nombre de résultats et l'autofocus optionnel. [#1096](https://github.com/datagouv/cdata/issues/1096)
