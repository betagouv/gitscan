## Changelog : apilos (30 derniers jours)

### Résumé
Les dernières mises à jour d'apilos se concentrent sur l'amélioration de la gestion des conventions APL, notamment en permettant la récupération de toutes les annexes, la correction de bugs liés à la saisie et à la mise à jour des informations sur les logements, ainsi que des adaptations spécifiques pour les conventions outre-mer. Des corrections de bugs et des améliorations de l'interface ont également été apportées pour une meilleure expérience utilisateur.

### Évolutions fonctionnelles
- Possibilité de récupérer toutes les annexes dans le contexte d'une convention. [#2132](https://github.com/MTES-MCT/apilos/issues/2132)
- Le champ "nb_logement" est maintenant saisissable après l'upload d'un document. [#2127](https://github.com/MTES-MCT/apilos/issues/2127)
- Correction d'un bug empêchant la suppression des stationnements. [#2119](https://github.com/MTES-MCT/apilos/issues/2119)
- Correction d'un blocage de l'interface pour les utilisateurs lecteurs concernant le groupage/dégroupage. [#2123](https://github.com/MTES-MCT/apilos/issues/2123)
- Correction du problème de mise à jour du champ "nb-logement". [#2126](https://github.com/MTES-MCT/apilos/issues/2126)
- Adaptation des templates de convention pour l'outre-mer. [#2121](https://github.com/MTES-MCT/apilos/issues/2121)
- Correction de l'affichage des financements (taille minuscule). [#2120](https://github.com/MTES-MCT/apilos/issues/2120)
- Modifications des templates HLM, SEM et type 2. [#2118](https://github.com/MTES-MCT/apilos/issues/2118)

### Évolutions techniques
- Ajout de `setuptools` aux dépendances et compilation avec l'option `--allow-unsafe` pour améliorer la gestion des packages. [#2129](https://github.com/MTES-MCT/apilos/issues/2129)
- Correction d'une erreur Sentry liée à l'attribut 'financement' manquant dans l'objet 'Annexe'. [#2122](https://github.com/MTES-MCT/apilos/issues/2122)
