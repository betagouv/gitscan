## Changelog : dora (30 derniers jours, au 29 octobre 2026)

### Résumé
Ce mois-ci, la plateforme dora a bénéficié d'une refonte de son interface utilisateur (nouvelle page d'accueil et formulaires simplifiés) et d'une amélioration de l'expérience de recherche. Parallèlement, des mesures de sécurité importantes ont été déployées pour protéger les accès et les données, tout en fiabilisant la gestion des documents et des fichiers.

### Évolutions fonctionnelles
- **Interface et Navigation** : 
    - Refonte de la page d'accueil avec l'introduction d'onglets par type de public [#1449](https://github.com/gip-inclusion/dora/issues/1449).
    - Simplification de l'affichage des structures (suppression des colonnes de résumé et de détails horaires) [#1385](https://github.com/gip-inclusion/dora/issues/1385).
    - Nettoyage du menu de navigation (suppression de « Mon portail ») [#1416](https://github.com/gip-inclusion/dora/issues/1416).
- **Services et Formulaires** : 
    - Refonte du formulaire d'édition des services pour une meilleure ergonomie [#1331](https://github.com/gip-inclusion/dora/issues/1331).
    - Amélioration de la saisie avec la présélection automatique du formulaire Dora pour les services [#1462](https://github.com/gip-inclusion/dora/issues/1462) et une meilleure synchronisation des données lors du rendu [#1455](https://github.com/gip-inclusion/dora/issues/1455).
- **Recherche** : 
    - Remplacement de la recherche Google par une recherche interne par mots-clés plus performante [#1464](https://github.com/gip-inclusion/dora/issues/1464).
    - Amélioration de la cohérence de recherche en partageant le dernier lieu sélectionné entre la recherche thématique et la recherche par mots-clés [#1476](https://github.com/gip-inclusion/dora/issues/1476).
- **Gestion des documents et fichiers** : 
    - Support étendu des formats de fichiers `.doc` et `.xls` lors des téléchargements [#1415](https://github.com/gip-inclusion/dora/issues/1415).
    - Correction d'un problème entraînant la perte de documents lors des nettoyages automifères [#1483](https://github.com/gip-inclusion/dora/issues/1483), [#1489](https://github.com/gip-inclusion/dora/issues/1489).
    - Amélioration de l'affichage des notifications lors du chargement des documents [#1482](https://github.com/gip-inclusion/dora/issues/1482).
- **Orientations et Utilisateurs** : 
    - Redirection des demandes d'orientation vers la plateforme de l'inclusion [#1463](https://github.com/gip-inclusion/dora/issues/1463).
    - Sécurisation du téléchargement des exports via les liens envoyés par e-mail [#1405](https://github.com/gip-inclusion/dora/issues/1405).
    - Amélioration de la gestion des utilisateurs (prévention des comptes sans nom [#1471](https://github.com/gip-inclusion/dora/issues/1471) et gestion des dates de suspension [#1461](https://github.com/gip-inclusion/dora/issues/1461)).

### Évolutions techniques
- **Sécurité et Accès** : 
    - Renforcement de la protection contre les accès non autorisés en supprimant plusieurs endpoints de diagnostic et d'upload vulnérables [#1477](https://github.com/gip-inclusion/dora/issues/1477), [#1478](https://github.com/gip-inclusion/dora/issues/1478), [#1480](https://github.com/gip-inclusion/dora/issues/1480).
    - Amélioration de la gestion du *rate limiting* pour protéger l'API et le front-end [#1440](https://github.com/gip-inclusion/dora/issues/1440), [#1501](https://github.com/gip-inclusion/dora/issues/1501).
    - Uniformisation et limitation des demandes de liens de connexion pour renforcer l'authentification [#1479](https://github.com/gip-inclusion/dora/issues/1479).
- **Infrastructure et CI/CD** : 
    - Automatisation de la relecture des Pull Requests via un nouveau workflow de relecteur [#1497](https://github.com/gip-inclusion/dora/issues/1497).
    - Optimisation des environnements de test (*review apps*) avec une migration vers le projet `dora-staging` [#1430](https://github.com/gip-inclusion/dora/issues/1430) et une meilleure gestion des noms d'applications [#1434](https://github.com/gip-inclusion/dora/issues/1434).
    - Amélioration du processus de déploiement et de gestion des tâches cron en CI [#1414](https://github.com/gip-inclusion/dora/issues/1414), [#1419](https://github.com/gip-inclusion/dora/issues/1419).
- **Architecture et API** : 
    - Refactorisation des gestionnaires de services pour une meilleure maintenance du code [#1496](https://github.com/gip-inclusion/dora/issues/1496).
    - Nettoyage de l'API avec la suppression d'endpoints obsolètes (notamment pour le module Emplois) et l'exposition de nouveaux champs (description des structures) [#1421](https://github.com/gip-inclusion/dora/issues/1421).
    - Sécurisation du stockage S3 en ajoutant des chaînes aléatoires aux chemins des documents [#1481](https://github.com/gip-inclusion/dora/issues/1481).

### Autres changements
- Ajout d'une indication de la date de mise à jour des données dans l'interface [#1500](https://github.com/gip-inclusion/dora/issues/1500).
- Mise à jour du fichier de politique de sécurité `security.txt` [#1493](https://github.com/gip-inclusion/dora/issues/1493).
