## Changelog : api-subventions-asso (30 derniers jours, au 21 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'intégration et le traitement des données Helios, avec des améliorations de l'API pour parser ces données et afficher des informations pertinentes dans l'interface utilisateur. Des corrections de bugs et des refactorings techniques ont également été réalisés pour améliorer la stabilité et la maintenabilité du code.

### Évolutions fonctionnelles
- L'interface utilisateur affiche désormais le nom de l'allocataire dans l'instructeur pour les données Helios.
- Le tableau de bord des subventions a été amélioré avec des informations supplémentaires.
- L'instance Matomo utilisée pour le suivi analytique a été modifiée.
- Intégration initiale du parsing des données Helios, permettant de traiter les informations relatives aux subventions.
- Amélioration du processus de dépôt avec l'application des changements de la version 4.

### Évolutions techniques
- Refactoring de l'API pour déplacer les DTO Helios vers le mapping des entités dans les adaptateurs.
- Renommage des dossiers et fichiers de l'API pour respecter les conventions de nommage.
- Création de ports vers les adaptateurs dans l'API pour une meilleure modularité.
- Correction d'une erreur de chemin d'accès dans la configuration ESLint.
- Amélioration de la documentation Swagger de l'API.
- Correction d'un problème d'encodage des noms de fichiers multipart.
- Correction d'une erreur liée à l'utilisation de `__dirname` dans les modules ES6.
- Amélioration de la configuration ESLint pour spécifier les fichiers `tsconfig`.
- Refactoring du code Chorus pour une meilleure structure et maintenabilité.

### Autres changements
- Correction d'un bug lié à la notification de dépôt de renouvellement.
- Ajout de l'ID de paiement aux données Helios.
- Possibilité de restreindre le parsing des données Helios à des exercices spécifiques.
- Correction d'un test dans le front-end.
- Mise à jour de la description de FSE.
- Correction d'un import dans le front-end.
- Mise à jour du code et de la description du programme Chorus FSE.
