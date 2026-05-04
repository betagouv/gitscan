## Changelog : api-subventions-asso (30 derniers jours, au 23 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'intégration et l'amélioration du traitement des données Helios, une nouvelle source de subventions. Des corrections de bugs et des améliorations de l'interface utilisateur ont également été apportées, ainsi qu'une flexibilité accrue dans le parsing des données.

### Évolutions fonctionnelles
- L'application affiche désormais le nom de l'allocataire dans l'instructeur pour les données Helios.
- Le titre de la page du tableau de bord des subventions a été amélioré.
- L'API peut désormais parser les données Helios, permettant d'intégrer de nouvelles subventions. [#3865](https://github.com/betagouv/api-subventions-asso/issues/3865)
- Possibilité de restreindre le parsing des données à des exercices spécifiques. [#3873](https://github.com/betagouv/api-subventions-asso/issues/3873)
- Correction d'un bug concernant la notification de renouvellement de dépôt. [#3822](https://github.com/betagouv/api-subventions-asso/issues/3822)
- L'instance Matomo a été modifiée. [#3825](https://github.com/betagouv/api-subventions-asso/issues/3825)

### Évolutions techniques
- Refactoring du code pour déplacer les DTO Helios vers le mapping des entités dans les adaptateurs.
- Amélioration de l'outil d'automatisation Osiris.
- Initialisation du cron Scdl.
- Corrections d'erreurs ESLint et TypeScript.

### Autres changements
- Mise à jour de la documentation et de la configuration.
