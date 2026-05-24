## Changelog : partaj (30 derniers jours, au 22 mai 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de l'expérience utilisateur, notamment en permettant aux demandeurs de voir la relation de parrainage et en corrigeant des blocages dans la validation des sous-saisines. Des mises à jour techniques importantes ont également été apportées, avec la modernisation des librairies React et React Router, ainsi que la synchronisation des versions de PostgreSQL, Elasticsearch et Django.

### Évolutions fonctionnelles
- Les demandeurs peuvent désormais voir la relation de parrainage.
- Correction d'un blocage lors de la validation d'une sous-saisine [#15](https://github.com/MTES-MCT/partaj/issues/15).
- Ajout d'une image manquante dans la politique de sécurité du contenu pour "jedonnemonavis".

### Évolutions techniques
- Mise à jour de React vers la version 18.
- Mise à jour de React Router.
- Migration de la librairie `react-query` vers `tanstack`.
- Synchronisation des versions de PostgreSQL, Elasticsearch et Django.
- Mise à niveau de Jest.
- Ajout du tag GCP sur l'ensemble des jobs CI pour une meilleure identification de l'environnement.

### Autres changements
- Ajout de tests pour les relations de parrainage.
- Ajout d'un délai pour les tests front-end afin d'améliorer leur stabilité.
- Correction d'un problème de test dans l'environnement de test.
