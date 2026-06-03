## Changelog : catalogi (30 derniers jours, au 01 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'administration du catalogue, l'importation automatique de données et la gestion des sources d'informations. Des corrections ont également été apportées pour améliorer la stabilité des tests et la gestion des données Wikidata.

### Évolutions fonctionnelles
- Ajout d'une fonctionnalité permettant de récupérer tous les identifiants lors de l'utilisation de HAL. [#515](https://github.com/codegouvfr/catalogi/issues/515)
- Introduction d'une page d'administration `/admin` avec un rôle dédié pour gérer les attributs personnalisés.
- Restriction des attributs personnalisés à l'administration uniquement.
- Amélioration de l'interface d'administration pour mieux gérer les larges étiquettes d'attributs et limiter la largeur de la page.
- L'importation automatique ne crée plus d'entrée utilisateur. [#528](https://github.com/codegouvfr/catalogi/issues/528)

### Évolutions techniques
- Amélioration du suivi de la déréférenciation des auteurs via l'API, avec stockage de l'heure au format ISO.
- Correction de la sélection de la dernière version dans les données Wikidata.
- Refactorisation de l'entrée d'objet pour l'importation et renommage des références de variables. [#528](https://github.com/codegouvfr/catalogi/issues/528)
- Mise en cache des navigateurs Playwright pour accélérer l'exécution des tests en CI.
- Correction de l'installation et de l'exécution des tests Playwright en CI.
- Le nom du logiciel peut maintenant retomber sur les sources si nécessaire.
- Ajout d'un script `db up` pour la base de données racine.
- Préservation des remplacements d'entrée utilisateur.
- Encodage des valeurs de repli d'entrée utilisateur avec `null`.

### Autres changements
- Mise à jour des attentes du test de rafraîchissement Wikidata.
- Plusieurs mises à jour de version (build bumps) ont été effectuées.
