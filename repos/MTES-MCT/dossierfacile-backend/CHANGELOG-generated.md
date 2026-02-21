## Changelog : dossierfacile-backend (30 derniers jours)

### Résumé
Ce changelog résume les évolutions du backend de DossierFacile au cours des 30 derniers jours. Les principales améliorations concernent la gestion du partage de dossiers, avec une refonte complète de la fonctionnalité et l'ajout de nouvelles options pour les utilisateurs et les opérateurs. Des corrections de bugs et des optimisations ont également été apportées pour améliorer la stabilité et la performance de l'application.

### Évolutions fonctionnelles
- Refonte complète de la fonctionnalité de partage de dossiers, incluant de nouvelles options pour les liens de partage (OWNER, PARTNER, MAIL) et une interface améliorée pour les opérateurs. (#1116, #1060, #1113)
- Possibilité de mettre à jour le titre et la date d'expiration des liens de partage.
- Ajout d'informations sur le créateur et l'URL des liens de partage.
- Amélioration de l'affichage des liens de partage dans l'interface opérateur, avec une meilleure gestion des liens inactifs et supprimés.
- Ajout d'une fonctionnalité permettant de ne pas compter les visites du tenant lorsqu'il accède à son propre lien. (#1119)
- Amélioration de la gestion des commentaires des opérateurs avec l'ajout du contexte utilisateur. (#1108)
- Possibilité de programmer la suppression des documents du tenant après 45 jours. (#1105)
- Correction d'un bug empêchant l'envoi de l'application au BO en cas d'avertissement concernant le compte. (#1130)
- Correction d'un bug empêchant l'application d'être renvoyée au traitement lorsque les noms ne sont pas mis à jour. (#1130)
- Correction d'un bug où l'API renvoyait une erreur 500 au lieu d'une erreur 404 lors de la récupération d'une propriété par son ID. (#1134)

### Évolutions techniques
- Mise à jour de plusieurs dépendances : Spring Boot 3.5, apache commons-lang3 3.18.0, openstack4j 3.12, brevo 1.1.0.
- Correction de vulnérabilités de sécurité en mettant à jour les dépendances crypto.
- Amélioration de la robustesse de la gestion des erreurs, notamment en évitant l'exposition des traces de pile dans les réponses de l'API. (#1138)
- Optimisation de la gestion des tâches planifiées pour permettre l'exécution en parallèle. (#1137)
- Refactorisation du code pour améliorer la lisibilité et la maintenabilité, notamment dans la gestion des liens de partage.
- Suppression de code inutilisé et de routes obsolètes dans les APIs owner et partner. (#1128, #1129)
- Amélioration de la journalisation pour faciliter le diagnostic des problèmes. (#1135, #1139)
- Normalisation de l'URI dans les logs. (#1140)
- Correction d'un problème lié à l'optimistic locking dans l'API tenant. (#1133)
- Suppression de la route de régénération de token. (#1128)

### Autres changements
- Configuration des IDs de templates Brevo directement dans le code. (#1102)
- Correction de tests suite aux refactorisations.
- Amélioration de la documentation et des tests unitaires.
- Correction de code smells.
