## Changelog : catalogi (30 derniers jours, au 9 juin 2026)

### Résumé
Ce changelog présente les améliorations apportées à catalogi au cours du dernier mois. Les principales évolutions concernent l'intégration de sources de données externes (Wikidata, HAL), des améliorations de l'interface d'administration et des corrections de bugs pour stabiliser les tests et l'import automatique de logiciels.

### Évolutions fonctionnelles
- Ajout de la récupération et de la recherche d'organisations sur Wikidata.  [#505](https://github.com/codegouvfr/catalogi/issues/505)
- Ajout de la récupération de tous les identifiants sur HAL. [#515](https://github.com/codegouvfr/catalogi/issues/515)
- Amélioration de l'interface d'administration :
    - Contrainte de la largeur de la page et troncature des labels d'attributs longs.
    - Restriction des attributs personnalisés à un rôle administrateur.
    - Ajout d'un rôle administrateur et d'une page `/admin` pour la gestion des attributs personnalisés.
- Le nom du logiciel peut maintenant retomber sur les sources si non renseigné.
- Amélioration de la sélection de la dernière version sur Wikidata.

### Évolutions techniques
- Refactorisation de l'entrée d'objet et renommage des variables pour l'import automatique. [#528](https://github.com/codegouvfr/catalogi/issues/528)
- L'import automatique ne crée plus d'entrée utilisateur. [#528](https://github.com/codegouvfr/catalogi/issues/528)
- Utilisation de la configuration source pour résoudre l'identifiant du dépôt.
- Amélioration de la stabilité des tests Playwright, notamment en corrigeant l'installation et l'exécution en CI.
- Mise en cache des navigateurs Playwright pour accélérer les tests CI.
- Ajout d'un script `db up` pour initialiser la base de données.

### Autres changements
- Clarification de la documentation concernant le routage de l'API Helm.
- Correction de l'ordre des tests. [#505](https://github.com/codegouvfr/catalogi/issues/505)
- Plusieurs mises à jour de version (build bumps).
