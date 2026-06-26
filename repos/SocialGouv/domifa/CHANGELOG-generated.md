## Changelog : domifa (30 derniers jours, au 24 juin 2026)

### Résumé
Cette période a été marquée par de nombreuses corrections de bugs et améliorations de la sécurité, notamment concernant la gestion des organismes, des utilisateurs et des accès. Des améliorations ont également été apportées à la gestion des journaux et des alertes de sécurité. Enfin, des corrections ont été apportées à l'interface utilisateur et aux tests.

### Évolutions fonctionnelles
- Ajout de la possibilité de gérer les organismes sans raison spécifique ("autre").
- Amélioration de la gestion des utilisateurs bloqués, avec suppression de la possibilité de les éditer.
- Ajout de la suppression des utilisateurs (via [#4152](https://github.com/SocialGouv/domifa/issues/4152)).
- Ajout de statistiques sur les sessions utilisateurs.

### Évolutions techniques
- Mise en place de règles de pare-feu IP pour une meilleure sécurité.
- Ajout de filtres pour la gestion des données supprimées.
- Refonte des journaux pour une meilleure traçabilité des événements de sécurité.
- Ajout d'un délai de 30 minutes pour les OTP (One-Time Password) afin d'améliorer la sécurité.
- Amélioration de la gestion des erreurs et ajout de filtres d'exception.
- Correction d'une potentielle vulnérabilité de type "Type confusion through parameter tampering".
- Amélioration de la gestion des tests unitaires.
- Mise à jour des dépendances de sécurité et correction des alertes associées.

### Autres changements
- Amélioration des tests pour le portail usagers.
- Ajout de tests pour les emails.
- Correction de problèmes de build de l'application frontend.
- Amélioration de la gestion des erreurs de typage.
- Ajout de logs pour les tentatives de connexion inconnues.
- Suppression de la possibilité de modifier le mot de passe pour les utilisateurs bloqués.
- Ajout d'un testeur d'envoi d'emails génériques.
- Suppression de la fabrique sociale.
- Correction de problèmes de linting.
