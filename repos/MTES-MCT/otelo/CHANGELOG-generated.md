## Changelog : otelo (30 derniers jours)

### Résumé
Le projet Otelo a connu un mois de février et début mars riche en améliorations et nouvelles fonctionnalités. Les efforts se sont concentrés sur l'amélioration de la gestion des données (versioning, import), l'expérience utilisateur (gestion des utilisateurs, simulations, affichage des résultats) et la correction de bugs pour une application plus stable et performante. Une page de feedback utilisateur a également été ajoutée.

### Évolutions fonctionnelles
- Ajout d'une page de feedback utilisateur pour recueillir les retours des utilisateurs. [#16](https://github.com/MTES-MCT/otelo/pull/16)
- Possibilité de supprimer un groupe d'EPCI. [#15](https://github.com/MTES-MCT/otelo/pull/15)
- Amélioration de l'affichage des résultats des simulations avec un bouton d'export. [#10](https://github.com/MTES-MCT/otelo/pull/10)
- Ajout d'un historique des résultats des simulations, permettant de suivre l'évolution des données. [#10](https://github.com/MTES-MCT/otelo/pull/10)
- Amélioration de la gestion des utilisateurs avec un refonte de l'interface et du tri.
- Correction de l'affichage des logements secondaires.
- Correction de l'affichage des données cumulées pour les logements vacants et secondaires.
- Correction de l'export Excel pour les décimales.
- Correction de l'affichage des données dans les graphiques récapitulatifs.
- Correction d'un bug lié à la projection du scroll dans la liste des ménages.
- Correction d'un bug lié au gel de la taille de page.

### Évolutions techniques
- Implémentation du versioning des datapacks. [#23](https://github.com/MTES-MCT/otelo/pull/23)
- Ajout d'un CLI pour importer des données. [#25](https://github.com/MTES-MCT/otelo/pull/25)
- Gestion des clés API et des consommateurs. [#20](https://github.com/MTES-MCT/otelo/pull/20)
- Refactorisation de la gestion des mises à jour de la base de données pour éviter les erreurs.
- Suppression du module d'authentification de l'API.
- Amélioration de la gestion des énumérations dans Swagger.
- Ajout de tests et de linting pour améliorer la qualité du code.

### Autres changements
- Ajout d'une page changelog. [#6](https://github.com/MTES-MCT/otelo/pull/6)
- Correction de divers typos et améliorations de la documentation.
- Correction de l'année du millésime dans différentes parties de l'application.
- Correction de la gestion du millésime dans le provider de taux.
- Correction de la restructuration liée à la disparition des données.
- Amélioration de la gestion des injections de modules CLI.
- Ajout d'un fichier README et configuration du mode "dry run" par défaut pour le CLI.
