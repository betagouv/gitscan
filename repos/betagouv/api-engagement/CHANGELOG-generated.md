## Changelog : api-engagement (30 derniers jours, au 31 juillet 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de l'expérience utilisateur, notamment une refonte de l'affichage des missions sur la carte, des corrections d'accessibilité importantes pour répondre aux normes RGAA, et des optimisations de performance pour l'API et le back-office. Des nouvelles fonctionnalités ont également été ajoutées, comme l'intégration de nouvelles taxonomies de compétences et le suivi des clics sur les missions pour l'analyse des données.

### Évolutions fonctionnelles
- Refonte de l'affichage des missions sur la carte avec des icônes DSFR. [#1357](https://github.com/betagouv/api-engagement/issues/1357)
- Ajout de nouvelles taxonomies de compétences avec une configuration évolutive. [#1350](https://github.com/betagouv/api-engagement/issues/1350)
- Possibilité pour les diffuseurs de gérer la modération de leurs propres missions. [#1330](https://github.com/betagouv/api-engagement/issues/1330)
- Ajout d'indicateurs clés de performance (KPI) pour le suivi des recommandations et des clics sur les missions. [#1352](https://github.com/betagouv/api-engagement/issues/1352)
- Ajout d'un bandeau de consentement aux cookies. [#1329](https://github.com/betagouv/api-engagement/issues/1329)
- Ajout de pages légales et de liens dans le pied de page. [#1246](https://github.com/betagouv/api-engagement/issues/1246)
- Ajout de la possibilité de s'inscrire à une newsletter. [#1209](https://github.com/betagouv/api-engagement/issues/1209)
- Amélioration de l'affichage des statistiques publiques. [#1348](https://github.com/betagouv/api-engagement/issues/1348)
- Ajout d'onglets pour la diffusion des missions et les documents Typesense. [#1340](https://github.com/betagouv/api-engagement/issues/1340)

### Évolutions techniques
- Indexation de plus de champs de missions dans Typesense pour améliorer la recherche. [#1337](https://github.com/betagouv/api-engagement/issues/1337)
- Refactorisation de l'option de scaling pour le container worker. [#1359](https://github.com/betagouv/api-engagement/issues/1359)
- Modification du scaling CPU en fonction de la concurrence des requêtes. [#1361](https://github.com/betagouv/api-engagement/issues/1361)
- Amélioration de la performance de la requête de matching des missions. [#1268](https://github.com/betagouv/api-engagement/issues/1268) et [#1248](https://github.com/betagouv/api-engagement/issues/1248)
- Utilisation de materialized mission diffusion pour améliorer les performances. [#1302](https://github.com/betagouv/api-engagement/issues/1302)
- Ajout de la gestion des secrets pour l'API. [#1307](https://github.com/betagouv/api-engagement/issues/1307)
- Correction d'une vulnérabilité potentielle de type SSRF lors de l'importation de fichiers XML. [#1303](https://github.com/betagouv/api-engagement/issues/1303)
- Amélioration de la gestion des jobs et des tâches asynchrones. [#1339](https://github.com/betagouv/api-engagement/issues/1339)
- Ajout de tests d'évaluation pour l'enrichissement des missions. [#1363](https://github.com/betagouv/api-engagement/issues/1363)

### Autres changements
- Corrections d'accessibilité (RGAA) importantes sur l'application (plateforme et widget) pour améliorer l'expérience utilisateur pour les personnes handicapées. [#1277](https://github.com/betagouv/api-engagement/issues/1277), [#1273](https://github.com/betagouv/api-engagement/issues/1273), [#1317](https://github.com/betagouv/api-engagement/issues/1317), [#1316](https://github.com/betagouv/api-engagement/issues/1316), [#1315](https://github.com/betagouv/api-engagement/issues/1315), [#1314](https://github.com/betagouv/api-engagement/issues/1314), [#1313](https://github.com/betagouv/api-engagement/issues/1313), [#1312](https://github.com/betagouv/api-engagement/issues/1312), [#1311](https://github.com/betagouv/api-engagement/issues/1311), [#1310](https://github.com/betagouv/api-engagement/issues/1310), [#1309](https://github.com/betagouv/api-engagement/issues/1309), [#1308](https://github.com/betagouv/api-engagement/issues/1308), [#1296](https://github.com/betagouv/api-engagement/issues/1296)
- Corrections de bugs et améliorations diverses de l'interface utilisateur.
- Mise à jour des dépendances.
- Nettoyage du code et refactorisation.
- Ajout de scripts pour l'intégration des compétences de la gendarmerie et de la police. [#1270](https://github.com/betagouv/api-engagement/issues/1270)
- Correction d'un problème de sur-comptage des événements mensuels dans les analytics. [#1332](https://github.com/betagouv/api-engagement/issues/1332)
- Correction d'un problème de duplication des en-têtes sur la page de description des missions. [#1331](https://github.com/betagouv/api-engagement/issues/1331)
