## Changelog : api-subventions-asso (30 derniers jours, au 6 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'intégration et le traitement des données Helios, avec des améliorations de l'affichage des informations et des corrections liées à la migration Proconnect. Des ajustements ont également été apportés à l'automatisation du traitement des données Osiris.

### Évolutions fonctionnelles
- Intégration et parsing des données Helios, permettant de nouvelles informations sur les subventions. [#3865](https://github.com/betagouv/api-subventions-asso/issues/3865)
- Affichage du nom de l'allocataire dans l'interface pour les données Helios.
- Amélioration du titre d'information du tableau de bord des subventions.
- Correction d'un bug lié à la migration Proconnect. [#3898](https://github.com/betagouv/api-subventions-asso/issues/3898)

### Évolutions techniques
- Refactoring du code pour déplacer les DTO Helios vers les mappings d'entités dans les adaptateurs.
- Ajout de `paymentId` aux données Helios "application-flat".
- Ajout d'un objet manquant dans les données Helios "application-flat".
- Amélioration de l'automatisation du traitement des données Osiris.
- Mise à jour du test unitaire pour le parser Osiris afin de vérifier la date de mise à jour.

### Autres changements
- Rétractation temporaire du label "grant statistique total" dans l'API.
- Version bump uniquement pour le package api-subventions-asso (0.84.4 et 0.84.2).
