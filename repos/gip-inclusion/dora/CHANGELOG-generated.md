## Changelog : dora (30 derniers jours, au 02/10/2026)

### Résumé
Ce mois-ci, Dora a bénéficié d'une simplification importante de la gestion des structures et des services, avec des formulaires plus intuitifs et une meilleure organisation des données. Les gestionnaires de territoires disposent désormais d'outils de pilotage plus performants grâce à une refonte de leur tableau de bord. Parallèlement, l'infrastructure a été modernisée pour améliorer la fiabilité du stockage et le suivi des erreurs.

### Évolutions fonctionnelles
- **Gestion des structures et services**
    - Simplification de la fiche et du formulaire d'édition des structures [#1383](https://github.com/gip-inclusion/dora/issues/1383).
    - Fusion de la présentation et du résumé en une description unique pour les structures [#1384](https://github.com/gip-inclusion/dora/issues/1384).
    - Possibilité de rattacher des structures à un réseau porteur [#1382](https://github.com/gip-inclusion/dora/issues/1382).
    - Amélioration de la gestion des services : correction de la synchronisation avec les modèles [#1370](https://github.com/gip-inclusion/dora/issues/1370), ajout des horaires d'accueil et correction des doublons de formulaires [#1354](https://github.com/gip-inclusion/dora/issues/1354).
    - Suppression des processus de modération devenus obsolètes pour les structures [#1380](https://github.com/gip-inclusion/dora/issues/1380) et les services [#1378](https://github.com/gip-inclusion/dora/issues/1378).
    - Ajout d'une option vide pour le champ typologie des structures dans l'administration [#1398](https://github.com/gip-inclusion/dora/issues/1398).
- **Expérience utilisateur et interface**
    - Refonte complète du tableau de bord et de la page d'accueil pour les gestionnaires de territoires [#1349](https://github.com/gip-inclusion/dora/issues/1349), [#1339](https://github.com/gip-inclusion/dora/issues/1339).
    - Support du format Markdown pour les bandeaux d'avertissement [#1404](https://github.com/gip-inclusion/dora/issues/1404) et amélioration du rendu des descriptions [#1364](https://github.com/gip-inclusion/dora/issues/1364).
    - Ajout de fonctionnalités de recherche par communes et EPCI [#1340](https://github.com/gip-inclusion/dora/issues/1340).
    - Optimisation de l'export des orientations pour inclure les données des emplois [#1361](https://github.com/gip-inclusion/dora/issues/1361) et ajout de champs pour l'export vers data.inclusion [#1345](https://github.com/gip-inclusion/dora/issues/1345).
    - Amélioration de la gestion des erreurs de formulaire pour l'utilisateur [#1392](https://github.com/gip-inclusion/dora/issues/1392).
    - Sécurisation des données en empêchant la publication de liens de mobilisation internes [#1360](https://github.com/gip-inclusion/dora/issues/1360).

### Évolutions techniques
- **Infrastructure et stockage**
    - Migration du stockage S3 local de MinIO vers SeaweedFS [#1376](https://github.com/gip-inclusion/dora/issues/1376).
- **Authentification et sécurité**
    - Correction de la génération du token DRF lors de l'authentification via ProConnect [#1363](https://github.com/gip-inclusion/dora/issues/1363).
- **Performance et outils de développement**
    - Optimisation du chargement des structures pour le personnel afin d'éviter les surcharges de données [#1353](https://github.com/gip-inclusion/dora/issues/1353).
    - Migration vers la version 11 du SDK Sentry pour un meilleur suivi des erreurs [#1397](https://github.com/gip-inclusion/dora/issues/1397).
    - Ajout d'une commande pour l'anonymisation des données [#1321](https://github.com/gip-inclusion/dora/issues/1321).
    - Amélioration de la compatibilité de la pagination avec les navigateurs plus anciens [#1391](https://github.com/gip-inclusion/dora/issues/1391).

### Autres changements
- **Maintenance et configuration**
    - Nettoyage du code : suppression des pages et endpoints d'administration obsolètes pour les services [#1377](https://github.com/gip-inclusion/dora/issues/1377) et nettoyage de la commande de statistiques Nexus [#1389](https://github.com/gip-inclusion/dora/issues/1389).
    - Mise à jour de la politique de sécurité de contenu (CSP) pour intégrer Matomo [#1409](https://github.com/gip-inclusion/dora/issues/1409).
    - Actualisation des configurations de staging et de la CI (URL Dora et image MinIO) [#1357](https://github.com/gip-inclusion/dora/issues/1357), [#1355](https://github.com/gip-inclusion/dora/issues/1355).
