## Changelog : nosgestesclimat (30 derniers jours, au 15 octobre 2026)

### Résumé
Les récentes évolutions se concentrent sur l'amélioration de la précision des simulations grâce à l'intégration de l'âge dans les profils utilisateurs. Le projet a également bénéficié de nombreuses corrections de règles métier, notamment pour affiner les calculs concernant les mineurs et certains statuts sociaux, ainsi que d'une adaptation spécifique pour le contexte suisse.

### Évolutions fonctionnelles
- Intégration de l'âge dans les profils utilisateurs pour une simulation plus précise.
- Correction de nombreuses règles de calcul concernant les mineurs (énergie, chauffage, isolation, conduite, etc.).
- Ajustement des conditions pour certains statuts (parents, salariés) afin de mieux refléter les situations réelles des utilisateurs.
- Adaptation du contenu pour le contexte suisse en supprimant les informations spécifiques à la France [#2832](https://github.com/incubateur-ademe/nosgestesclimat/pull/2832).
- Corrections de conditions liées à l'aviation et à la mobilité [#2834](https://github.com/incubateur-ademe/nosgestesclimat/pull/2834).

### Évolutions techniques
- Refactorisation du moteur de règles : les conditions liées au logement, à l'alimentation et aux services sociétaux sont désormais directement rattachées au profil utilisateur.
- Introduction d'un mécanisme de variation pour optimiser le fonctionnement des actions.
- Réorganisation de la structure des données pour regrouper l'âge dans une catégorie "profil" dédiée [#2826](https://github.com/incubateur-ademe/nosgestesclimat/pull/2826) [#2827](https://github.com/incubateur-ademe/nosgestesclimat/pull/2827).
- Correction du workflow DLUO.

### Autres changements
- Corrections de fautes de frappe (typos).
