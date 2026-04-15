## Changelog : cdata (30 derniers jours, au 15 avril 2026)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur l'amélioration de l'expérience de modération, la mise à jour des dépendances et l'amélioration de la stabilité et des performances de l'application. Plusieurs améliorations ont été apportées à l'interface utilisateur, notamment pour la gestion des ressources et la recherche, ainsi que des corrections de bugs pour assurer une meilleure expérience utilisateur. Une migration vers Nuxt 4 est en cours.

### Évolutions fonctionnelles
- Ajout du support des "Topics" dans la recherche globale [#1030](https://github.com/datagouv/cdata/issues/1030).
- Amélioration de la page de modération avec des onglets pour filtrer les types de sujets [#1033](https://github.com/datagouv/cdata/issues/1033).
- Affichage d'informations supplémentaires sur les previews manquantes [#1025](https://github.com/datagouv/cdata/issues/1025).
- Amélioration de l'affichage des liens OEmbed [#1026](https://github.com/datagouv/cdata/issues/1026).
- Ajout d'une indication de la définition des catégories restreintes [#1017](https://github.com/datagouv/cdata/issues/1017).
- Amélioration de l'affichage des statistiques de téléchargement du catalogue [#998](https://github.com/datagouv/cdata/issues/998).
- Affichage du lien vers le feedback IA uniquement après une suggestion [#1046](https://github.com/datagouv/cdata/issues/1046).
- Correction de l'affichage des posts avec des blocs [#1027](https://github.com/datagouv/cdata/issues/1027).
- Amélioration de l'affichage des cartes avec un affichage par défaut de l'attribution [#992](https://github.com/datagouv/cdata/issues/992).
- Amélioration de la gestion des CORS pour l'affichage des previews des ressources [#954](https://github.com/datagouv/cdata/issues/954).

### Évolutions techniques
- Mise à jour vers Nuxt 4.0 et 4.1 [#1035](https://github.com/datagouv/cdata/issues/1035), [#1023](https://github.com/datagouv/cdata/issues/1023), [#1009](https://github.com/datagouv/cdata/issues/1009), [#1008](https://github.com/datagouv/cdata/issues/1008).
- Refactorisation pour supprimer les duplications entre les previews [#1018](https://github.com/datagouv/cdata/issues/1018).
- Suppression de code mort lié à ProducerSelect [#1003](https://github.com/datagouv/cdata/issues/1003).
- Mise à jour de Node vers la version 24 [#1011](https://github.com/datagouv/cdata/issues/1011).
- Mise à jour des dépendances [#1002](https://github.com/datagouv/cdata/issues/1002), [#975](https://github.com/datagouv/cdata/issues/975).
- Correction d'un problème de chargement des fonctionnalités du harvester [#1043](https://github.com/datagouv/cdata/issues/1043).
- Correction d'un patch Nuxt qui n'était plus appliqué [#1039](https://github.com/datagouv/cdata/issues/1039).
- Correction d'un crash lors du changement de layout en développement [#1004](https://github.com/datagouv/cdata/issues/1004).
- Ajout de la configuration pour les nouvelles clés API [#1006](https://github.com/datagouv/cdata/issues/1006).
- Ajout de l'URL de rate limiting aux dataservices [#1005](https://github.com/datagouv/cdata/issues/1005).
- Mise à jour des versions des actions CI/CD [#1013](https://github.com/datagouv/cdata/issues/1013).
- Tentative de correction des tests instables [#1028](https://github.com/datagouv/cdata/issues/1028).

### Autres changements
- Ajout de documentation sur l'obtention d'une clé API depuis la démo [#1045](https://github.com/datagouv/cdata/issues/1045).
- Amélioration de la formulation pour les datasets liés aux schémas [#1019](https://github.com/datagouv/cdata/issues/1019).
- Suppression d'une tentative d'amélioration de la liste des reviewers dans les pull requests [#1029](https://github.com/datagouv/cdata/issues/1029).
- Suppression de l'index pour la page de design [#991](https://github.com/datagouv/cdata/issues/991).
- Encodage de l'URI pour les OEmbed [#994](https://github.com/datagouv/cdata/issues/994).
- Renommage de la vue tf-validate pour la 2FA [#999](https://github.com/datagouv/cdata/issues/999).
