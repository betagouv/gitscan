## Changelog : cdata (30 derniers jours, au 26 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'explorateur tabulaire, l'API Dataservice, la recherche et les notifications. Des corrections de bugs et des optimisations de performance ont également été apportées pour améliorer l'expérience utilisateur et la stabilité de la plateforme. Plusieurs améliorations techniques ont été réalisées, notamment des mises à jour de l'infrastructure et des tests.

### Évolutions fonctionnelles
- **Explorateur tabulaire :** Améliorations et corrections de bugs pour une meilleure expérience utilisateur. [#1127](https://github.com/datagouv/cdata/issues/1127), [#1070](https://github.com/datagouv/cdata/issues/1070)
- **API Dataservice :** Amélioration de l'affichage de la réponse OpenAPI. [#1100](https://github.com/datagouv/cdata/issues/1100)
- **Recherche :**
    - Possibilité de personnaliser l'ordre de tri par défaut. [#1114](https://github.com/datagouv/cdata/issues/1114)
    - Correction d'un problème de concurrence pouvant affecter la recherche. [#1146](https://github.com/datagouv/cdata/issues/1146)
    - Correction du réinitialisation de la page lors du changement de type de recherche. [#1148](https://github.com/datagouv/cdata/issues/1148)
- **Notifications :**
    - Ajout de la possibilité de marquer les notifications comme lues individuellement et en masse. [#1121](https://github.com/datagouv/cdata/issues/1121), [#1103](https://github.com/datagouv/cdata/issues/1103)
- **Visualisations :** Correction d'un problème de CORS. [#1116](https://github.com/datagouv/cdata/issues/1116)
- **Pages :** Correction des erreurs 404 sur certaines pages. [#1094](https://github.com/datagouv/cdata/issues/1094)
- **Sujets :** Ajout d'une page dédiée aux sujets. [#1110](https://github.com/datagouv/cdata/issues/1110)
- **Activités :** Affichage de l'ID de la ressource impactée dans les activités. [#1123](https://github.com/datagouv/cdata/issues/1123)

### Évolutions techniques
- **Tests :**
    - Ajout de mocks pour les tests. [#1154](https://github.com/datagouv/cdata/issues/1154)
    - Ajout de tests unitaires et E2E. [#1136](https://github.com/datagouv/cdata/issues/1136), [#1139](https://github.com/datagouv/cdata/issues/1139)
    - Sharding des tests E2E pour améliorer la performance. [#1152](https://github.com/datagouv/cdata/issues/1152)
- **Infrastructure :** Utilisation de `NODE_ENV=production` dans le Dockerfile. [#1104](https://github.com/datagouv/cdata/issues/1104)
- **CI/CD :**
    - Activation des exécutions de pull request pour les contributions externes. [#1042](https://github.com/datagouv/cdata/issues/1042)
    - Correction des exécutions dupliquées dans le CI. [#1128](https://github.com/datagouv/cdata/issues/1128)
    - Mise à jour de la branche udata dans le CI. [#1131](https://github.com/datagouv/cdata/issues/1131)
- **Composants :** Mise à jour des composants en version 1.1.2 et 1.3. [#1101](https://github.com/datagouv/cdata/issues/1101), [#1150](https://github.com/datagouv/cdata/issues/1150)
- **Harvest :** Utilisation de la nouvelle API Harvest. [#1074](https://github.com/datagouv/cdata/issues/1074)
- **Performances :** Suppression d'appels API dupliqués dans l'explorateur. [#1129](https://github.com/datagouv/cdata/issues/1129)

### Autres changements
- Amélioration des charts. [#1088](https://github.com/datagouv/cdata/issues/1088)
- Clarification de l'accès à l'API tabulaire. [#1108](https://github.com/datagouv/cdata/issues/1108)
- Suppression des layers dans le type de métadonnées WFS. [#1140](https://github.com/datagouv/cdata/issues/1140)
- Correction d'un typo dans le dashboard. [#1143](https://github.com/datagouv/cdata/issues/1143)
- Correction d'un problème d'hydratation dans les métriques. [#1135](https://github.com/datagouv/cdata/issues/1135)
- Correction de l'affichage de l'image de réutilisation. [#1134](https://github.com/datagouv/cdata/issues/1134)
- Remplacement de "owner" par "organization" pour l'appel API harvest. [#1133](https://github.com/datagouv/cdata/issues/1133)
- Ajout de configuration Sentry. [#1126](https://github.com/datagouv/cdata/issues/1126)
- Correction de l'envoi d'un header non souhaité avec la clé API de développement. [#1122](https://github.com/datagouv/cdata/issues/1122)
- Ajout de la possibilité d'utiliser `<p>` dans le TitleTag. [#1119](https://github.com/datagouv/cdata/issues/1119)
- Rendre echarts optionnel. [#1095](https://github.com/datagouv/cdata/issues/1095)
- Suppression du date de création et ajout de l'URL de base dans la sidebar dataservice. [#1117](https://github.com/datagouv/cdata/issues/1117)
- Correction du design des blocs dans les news. [#1147](https://github.com/datagouv/cdata/issues/1147)
- Suppression du lockfile des composants. [#1156](https://github.com/datagouv/cdata/issues/1156)
- Mise à jour des dépendances. [#1105](https://github.com/datagouv/cdata/issues/1105)
- Amélioration de la gestion de l'état du dataset créé. [#1142](https://github.com/datagouv/cdata/issues/1142)
- Correction de l'affichage de l'icône de type de recherche personnalisée. [#1109](https://github.com/datagouv/cdata/issues/1109)
