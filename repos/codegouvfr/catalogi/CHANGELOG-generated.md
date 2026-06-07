## Changelog : catalogi (30 derniers jours, au 5 juin 2026)

### Résumé
Cette version apporte des améliorations significatives à l'administration des attributs personnalisés, avec l'ajout d'un rôle administrateur et d'une interface dédiée.  Des corrections et optimisations ont également été apportées aux tests d'intégration et à la gestion des sources de données, notamment pour l'importation automatique et la résolution d'identifiants de référentiels.

### Évolutions fonctionnelles
- Ajout d'une page d'administration accessible avec un rôle dédié pour la gestion des attributs personnalisés. [#528](https://github.com/codegouvfr/catalogi/issues/528)
- Restriction des attributs personnalisés à l'administration uniquement.
- Amélioration de l'interface d'administration : contrainte de la largeur de la page et troncature des étiquettes d'attributs trop longues.
- Possibilité de récupérer tous les identifiants via l'API HAL. [#515](https://github.com/codegouvfr/catalogi/issues/515)
- Le nom du logiciel peut maintenant retomber sur les sources si nécessaire.

### Évolutions techniques
- Amélioration de la résolution d'identifiants de référentiels en utilisant la configuration source.
- Refactorisation de l'entrée d'objet pour l'importation automatique. [#528](https://github.com/codegouvfr/catalogi/issues/528)
- Stabilisation des assertions pour les logiciels similaires dans les tests.
- Mise en cache des navigateurs Playwright dans le CI pour accélérer les tests.
- Correction de l'installation des navigateurs Playwright dans le CI.
- Correction de l'exécution des tests Playwright dans le CI.
- Ajout d'un script `db up` pour la base de données racine.
- Sélection de la dernière version Wikidata corrigée.

### Autres changements
- Clarification de la configuration du routage de l'API Helm dans la documentation.
- Augmentation de la version du build.
