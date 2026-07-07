## Changelog : cdata (30 derniers jours, au 3 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à l'exploration des données, notamment avec l'introduction d'une nouvelle page de suivi de publication et des améliorations de l'explorateur tabulaire. Des corrections de bugs et des optimisations de performance ont également été implémentées pour une meilleure expérience utilisateur. De nouvelles fonctionnalités ont été ajoutées pour la visualisation et la gestion des données, ainsi que des améliorations de l'API et de l'infrastructure.

### Évolutions fonctionnelles
- Ajout d'une page d'édition pour les organisations [#1132](https://github.com/datagouv/cdata/issues/1132).
- Nouvelle page de suivi de publication [#1137](https://github.com/datagouv/cdata/issues/1137).
- Amélioration de la visualisation des graphiques [#1088](https://github.com/datagouv/cdata/issues/1088).
- Possibilité de sauvegarder une image lors de la sauvegarde d'une visualisation [#1111](https://github.com/datagouv/cdata/issues/1111).
- Amélioration de l'explorateur tabulaire avec des corrections et ajustements [#1127](https://github.com/datagouv/cdata/issues/1127) et [#1157](https://github.com/datagouv/cdata/issues/1157).
- Amélioration de la vue de l'API Dataservice avec suppression de la date de création et ajout de l'URL de base [#1117](https://github.com/datagouv/cdata/issues/1117).
- Possibilité de personnaliser le tri par défaut dans la recherche [#1114](https://github.com/datagouv/cdata/issues/1114).
- Clarification de l'accès à l'API Tabular [#1108](https://github.com/datagouv/cdata/issues/1108).
- Amélioration de l'affichage des images "reuse" à l'étape 3 de la création de "reuse" [#1134](https://github.com/datagouv/cdata/issues/1134).

### Évolutions techniques
- Utilisation de la nouvelle API Harvest [#1074](https://github.com/datagouv/cdata/issues/1074).
- Utilisation de la nouvelle API Reuse v2 [#1155](https://github.com/datagouv/cdata/issues/1155).
- Suppression du filtrage heuristique du titre pour l'endpoint OpenAPI bouquet de fiches [#1151](https://github.com/datagouv/cdata/issues/1151).
- Correction de l'appel d'API en double dans l'explorateur avec `new_explorer=1` [#1129](https://github.com/datagouv/cdata/issues/1129).
- Correction d'une condition de course dans la recherche [#1146](https://github.com/datagouv/cdata/issues/1146).
- Correction d'un problème de réhydratation dans les métriques [#1135](https://github.com/datagouv/cdata/issues/1135).
- Ajout de mocks pour les tests [#1154](https://github.com/datagouv/cdata/issues/1154).
- Sharding des tests E2E pour améliorer la performance [#1152](https://github.com/datagouv/cdata/issues/1152).
- Mise à jour des dépendances [#1105](https://github.com/datagouv/cdata/issues/1105).
- Configuration de Sentry pour le serveur [#1126](https://github.com/datagouv/cdata/issues/1126).
- Correction pour ne pas envoyer d'en-tête indésirable avec la clé API de développement [#1122](https://github.com/datagouv/cdata/issues/1122).
- Activation des exécutions de pull request pour les contributions externes [#1042](https://github.com/datagouv/cdata/issues/1042).

### Autres changements
- Correction de la tabulation de l'API pour l'accordéon des ressources [#1138](https://github.com/datagouv/cdata/issues/1138).
- Correction du remplacement de "owner" par "organization" pour l'appel d'API [#1133](https://github.com/datagouv/cdata/issues/1133).
- Correction d'un problème de 404 sur les pages [#1094](https://github.com/datagouv/cdata/issues/1094).
- Suppression des layers dans le type de métadonnées WFS [#1140](https://github.com/datagouv/cdata/issues/1140).
- Correction d'une faute de frappe dans le tableau de bord [#1143](https://github.com/datagouv/cdata/issues/1143).
- Correction du réinitialisation de l'état du dataset créé lors du nouveau flux de publication [#1142](https://github.com/datagouv/cdata/issues/1142).
- Ajout de tests unitaires [#1136](https://github.com/datagouv/cdata/issues/1136) et tests E2E [#1139](https://github.com/datagouv/cdata/issues/1139).
- Suppression du fichier lockfile des composants [#1156](https://github.com/datagouv/cdata/issues/1156).
- Mise à jour de shell quote et autres [#1158](https://github.com/datagouv/cdata/issues/1158).
- Correction de la gestion des réponses non-JSON de l'API [#1159](https://github.com/datagouv/cdata/issues/1159).
- Ajout de la gestion de `localMarkAsRead` et du rafraîchissement multi-page pour les notifications [#1121](https://github.com/datagouv/cdata/issues/1121).
- Correction de l'affichage de la page d'actualités avec la conception des blocs [#1147](https://github.com/datagouv/cdata/issues/1147).
- Correction du problème de réinitialisation de la page lors du changement de type de recherche [#1148](https://github.com/datagouv/cdata/issues/1148).
- Rendre echarts optionnel [#1095](https://github.com/datagouv/cdata/issues/1095).
- Autoriser 'p' dans TitleTag [#1119](https://github.com/datagouv/cdata/issues/1119).
