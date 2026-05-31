## Changelog : catalogi (30 derniers jours, au 29 mai 2026)

### Résumé
Ce mois-ci, les améliorations de catalogi se concentrent sur l'administration du catalogue, l'importation automatique de données et la gestion des sources d'informations. Des corrections ont également été apportées pour améliorer la fiabilité des tests et la gestion des données Wikidata.

### Évolutions fonctionnelles
- Ajout d'une page d'administration accessible avec un rôle dédié pour gérer les attributs personnalisés du catalogue. [#528](https://github.com/codegouvfr/catalogi/issues/528)
- Restriction des attributs personnalisés à l'administration uniquement.
- Amélioration de l'affichage de l'interface d'administration : largeur de page contrainte et troncature des étiquettes d'attributs trop longues.
- Possibilité de récupérer tous les identifiants (IDs) lors d'une requête HAL. [#515](https://github.com/codegouvfr/catalogi/issues/515)
- Amélioration de l'importation automatique de données : ne crée plus d'entrées utilisateur. [#528](https://github.com/codegouvfr/catalogi/issues/528)

### Évolutions techniques
- Amélioration de la gestion des données Wikidata : correction de la sélection de la dernière version et mise à jour du test associé.
- Suivi du déréférencement de l'auteur via l'API et stockage de l'heure au format ISO.
- Correction de l'encodage des valeurs par défaut issues des entrées utilisateur.
- Mise en cache des navigateurs Playwright pour accélérer l'exécution des tests en CI.
- Correction de l'installation et de l'exécution des tests Playwright en CI.
- Refactorisation de l'entrée d'objet et renommage des références de variables. [#528](https://github.com/codegouvfr/catalogi/issues/528)

### Autres changements
- Ajout d'un script pour initialiser la base de données racine.
- Le nom du logiciel peut maintenant retomber sur les sources si nécessaire.
- Mises à jour de version (build bumps).
