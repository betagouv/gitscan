## Changelog : dossierfacile-backend (30 derniers jours)

### Résumé
Les dernières semaines ont été marquées par d'importantes améliorations concernant le partage de dossiers, avec une refonte complète de la fonctionnalité et l'ajout de nouvelles options pour les utilisateurs et les opérateurs. Des corrections de bugs et des améliorations de la robustesse ont également été apportées, ainsi que des mises à jour de sécurité et de dépendances.

### Évolutions fonctionnelles
- **Partage de dossiers (v2) :** Refonte complète de la fonctionnalité de partage de dossiers, incluant de nouvelles options pour les utilisateurs et les opérateurs. Cela comprend la gestion des liens de partage (création, modification, suppression), l'affichage des liens actifs et inactifs, et l'ajout d'informations sur les créateurs et les dates de création. (#1116, #1060, #1113)
- **Commentaires opérateur :** Amélioration de la fonctionnalité de commentaires des opérateurs avec l'ajout du contexte utilisateur. (#1108)
- **Génération de liens par défaut :** Ajout d'un endpoint pour générer un lien de partage par défaut.
- **Expiration des liens :** Possibilité de modifier la date d'expiration des liens de partage.
- **Amélioration de la gestion des liens :**  Correction de bugs liés à la suppression et à la gestion des liens de partage, notamment pour éviter la duplication et assurer la cohérence entre l'interface utilisateur et le backend.
- **Normalisation des URI dans les logs :** Amélioration de la logique de normalisation des URI pour une meilleure lisibilité et analyse des logs. (#1140)
- **Gestion des erreurs :** Amélioration de la gestion des erreurs, notamment en renvoyant des codes d'erreur 404 au lieu de 500 dans certains cas. (#1134)
- **Suppression automatique des documents :** Planification de la suppression des documents des locataires après 45 jours. (#1105)

### Évolutions techniques
- **Refactoring API Tenant :** Suppression des endpoints liés à FranceConnect et à la configuration des partenaires par email. (#1144, #1143)
- **Refactoring API Partner :** Suppression des routes API partenaires inutilisées, ne conservant que les 3 endpoints de lecture. (#1129)
- **Refactoring BO :** Suppression de la route de régénération de token et du code associé. (#1128)
- **Optimisation de la planification des tâches :** Activation de l'exécution parallèle des tâches pour améliorer les performances. (#1137)
- **Amélioration de la gestion des logs :** Ajout de logs de diagnostic pour les échecs de verrouillage optimiste. (#1139)
- **Gestion des exceptions :**  Empêche l'exposition de la trace de la pile dans les réponses de l'API. (#1138)
- **Mises à jour de dépendances :** Mises à jour de plusieurs dépendances pour améliorer la sécurité et la stabilité (Spring Boot, Apache Commons Lang3, Brevo, Openstack4j, crypto).
- **Refactor code :** Refactor de code pour améliorer la lisibilité et la maintenabilité.

### Autres changements
- **Documentation :** Ajout de documentation pour les nouveaux endpoints et fonctionnalités.
- **Configuration :** Définition des identifiants de modèles Brevo par défaut dans le code. (#1102)
- **Tests :** Ajout et mise à jour de tests unitaires et d'intégration.
- **Nettoyage de code :** Suppression de code obsolète et amélioration de la qualité du code.
