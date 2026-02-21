## Changelog : apilos (30 derniers jours)

### Résumé
Les dernières mises à jour d'apilos se concentrent sur l'amélioration de la gestion des conventions APL, notamment en corrigeant des bugs liés à la manipulation des annexes, des financements et des logements. Des adaptations ont également été apportées pour mieux supporter les conventions spécifiques à l'outre-mer.

### Évolutions fonctionnelles
- Permet de récupérer toutes les annexes dans le contexte d'une convention. (#2132)
- Le champ "nb_logement" est désormais modifiable après l'upload d'un document. (#2127)
- Correction d'un bug empêchant la suppression des stationnements. (#2119)
- Correction d'un blocage de l'interface utilisateur pour les utilisateurs "lecteurs" concernant le groupage/dégroupage. (#2123)
- Correction du problème de mise à jour du champ "nb-logement". (#2126)
- Correction d'une erreur Sentry liée à un attribut manquant dans l'objet 'Annexe'. (#2122)
- Adaptation des templates de convention pour l'outre-mer. (#2121)
- Correction de l'affichage des financements (taille minuscule). (#2120)
- Modifications des templates HLM, SEM et type 2. (#2118)

### Évolutions techniques
- Ajout de `setuptools` aux dépendances et compilation avec l'option `--allow-unsafe` pour améliorer la gestion des packages. (#2129)

### Autres changements
Aucun autre changement significatif à signaler.
