## Changelog : dora (30 derniers jours, au 22 octobre 2026)

### Résumé
Ce mois-ci, la plateforme a bénéficié d'une refonte importante de ses interfaces, notamment avec une nouvelle organisation de la page d'accueil et des tableaux de bord pour faciliter la navigation. Les outils de gestion des structures et des services ont été simplifiés et enrichis, tandis que la sécurité des accès et la fiabilité de la gestion des données ont été renforcées.

### Évolutions fonctionnelles
- **Interface et expérience utilisateur**
    - Refonte de la page d'accueil avec des onglets par public cible [#1449] et création d'une nouvelle page d'accueil dédiée aux gestionnaires de territoires [#1339].
    - Refonte du tableau de bord des gestionnaires de territoires [#1349].
    - Simplification des formulaires d'édition des services [#1331] et des structures [#1383].
    - Amélioration de l'affichage des fiches structures (fusion des descriptions et suppression de colonnes superflues) [#1384, #1385].
    - Mise à jour du bandeau d'avertissement pour supporter le format Markdown [#1404].
    - Suppression du menu « Mon portail » dans Nexus [#1416].
- **Recherche et données**
    - Remplacement de la recherche Google par une recherche par mots-clés interne à Dora [#1464].
    - Amélioration de l'export des orientations pour inclure les données liées aux emplois [#1361].
    - Exposition du champ description des structures via l'API [#1421].
- **Corrections et fonctionnalités métier**
    - Possibilité de rattacher des structures à un réseau porteur [#1382].
    - Sécurisation du téléchargement des exports via des liens envoyés par e-mail [#1405].
    - Support des fichiers `.doc` et `.xls` lors des téléchargements [#1415].
    - Correction de la création d'utilisateurs sans nom (via ProConnect ou import CSV) [#1471].
    - Sécurisation des orientations (interdiction de création pour les utilisateurs non connectés) [#1453].
    - Diverses corrections sur la synchronisation des services, la gestion des pièces jointes et l'affichage des formulaires [#1452, #1370, #1455, #1392].

### Évolutions techniques
- **Infrastructure et CI/CD**
    - Migration du stockage S3 local de MinIO vers SeaweedFS [#1376].
    - Migration des applications de test (review apps) vers le projet `dora-staging` sur Scalingo [#1430].
    - Optimisations de la CI/CD (alignement des noms d'apps, suppression des tâches cron sur les review apps, ciblage de la prod par défaut dans les scripts de livraison) [#1434, #1414, #1419].
- **Architecture et API**
    - Suppression des endpoints obsolètes de l'API Emplois et des pages d'administration des services [#1cd9cee, #1377].
    - Amélioration de la sécurité du rate limiting via la stabilisation de l'IP client utilisée [#1440].
    - Correction de l'authentification ProConnect pour la création de tokens DRF [#1363].
    - Migration vers le SDK Sentry v11 [#1397].

### Autres changements
- Nettoyage des statuts de modération pour les structures et les services [#1380, #1378].
- Suppression de la fonctionnalité de synchronisation immédiate [#1425].
- Nettoyage de la commande de remplissage de la base de statistiques Nexus [#1389].
