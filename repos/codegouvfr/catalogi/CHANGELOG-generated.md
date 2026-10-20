## Changelog : catalogi (30 derniers jours, au 16 octobre 2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur la fiabilité de l'importation des données et l'amélioration de l'expérience utilisateur via de nouveaux outils en ligne de commande. Des correctifs de sécurité importants et de nouvelles capacités d'exportation de données (Codemeta) ont également été intégrés pour renforcer la robustesse et l'interopérabilité de la plateforme.

### Évolutions fonctionnelles
- **Nouveaux outils en ligne de commande** : ajout de fonctionnalités permettant d'importer et de mettre à jour des références directement via le terminal ([#577](https://github.com/codegouvfr/catalogi/issues/577)).
- **Fiabilisation de l'importation de données** : 
    - Amélioration de la résolution des identifiants GitLab ([#575](https://github.com/codegouvfr/catalogi/issues/575)).
    - Meilleure gestion des identifiants Zenodo et des sources de données (CNLL, gestion des doublons et des liens externes).
- **Améliorations de l'interface utilisateur** : affichage plus clair de la page d'accueil lorsqu'aucun cas d'usage n'est défini et correction du logo.

### Évolutions techniques
- **Gestion des données (Codemeta)** : ajout d'une fonctionnalité d'exportation de la base de données au format Codemeta et amélioration de la gestion des types et des versions.
- **Sécurité** : correction d'une vulnérabilité liée au processus de connexion OIDC pour mieux lier les transactions au navigateur initiateur.
- **Qualité et tests** : 
    - Affinement de la détection des licences de logiciels libres via Wikidata.
    - Amélioration de la couverture de tests (ex: détection de la licence pour Apache HTTP Server).
- **Infrastructure de développement** : mise en place d'un environnement local dédié aux tests d'intrusion (pentest).

### Autres changements
- **Documentation** : mise à jour et correction de la documentation relative au déploiement.
- **Configuration** : suppression de l'importation des anciennes configurations d'interface utilisateur lors des nouvelles installations pour garantir un état propre.
