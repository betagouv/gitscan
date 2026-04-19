## Changelog : calendars (30 derniers jours, au 18 avril 2026)

### Résumé
Ce mois-ci, l'application Calendars a bénéficié d'améliorations significatives en termes de gestion des boîtes aux lettres et des calendriers, ainsi que de corrections de bugs et d'optimisations diverses. L'intégration avec Messages a été ajoutée, offrant de nouvelles possibilités aux utilisateurs. Plusieurs améliorations ont été apportées à la sécurité et à la fiabilité de l'application.

### Évolutions fonctionnelles
- **Partage :** Ajout de différents niveaux de partage avec des corrections d'interface utilisateur associées. [#41](https://github.com/suitenumerique/calendars/issues/41)
- **Intégration Messages :** Intégration avec l'application Messages pour une meilleure expérience utilisateur. [#46](https://github.com/suitenumerique/calendars/issues/46)
- **Boîtes aux lettres :** Possibilité de mettre à niveau des calendriers individuels en boîtes aux lettres. [#49](https://github.com/suitenumerique/calendars/issues/49)
- **URL de rappel :** Simplification de la logique des URL de rappel (callbacks). [#47](https://github.com/suitenumerique/calendars/issues/47)
- **Disponibilités :** Masquage de la case à cocher "disponibilités" dans le modal d'édition en fonction d'un indicateur de fonctionnalité.
- **Invitations :** Correction d'un bug empêchant l'envoi d'invitations depuis la boîte aux lettres sélectionnée.
- **Audit :** Ajout de champs d'audit pour suivre le canal et l'utilisateur. [#42](https://github.com/suitenumerique/calendars/issues/42)

### Évolutions techniques
- **SabreDAV :** Séparation de la boîte aux lettres et des principaux utilisateurs dans SabreDAV. [#49](https://github.com/suitenumerique/calendars/issues/49)
- **Favicon :** Chargement du favicon à partir d'un fichier d'asset au lieu d'un SVG en ligne. [#39](https://github.com/suitenumerique/calendars/issues/39)
- **CI/CD :** Nettoyage des anciens fichiers et correction de la CI.
- **Makefile :** Démarrage du backend et de Keycloak avec la commande `make start`.

### Autres changements
- Correction de plusieurs petits problèmes avant la première version.
- Correction d'une boucle infinie après la connexion en production.
- Correction d'erreurs d'affichage et de verbosité des logs.
- Correction de tests instables.
- Correction de problèmes de linting.
- Affichage d'une erreur lorsque aucune URL de base n'est présente.
