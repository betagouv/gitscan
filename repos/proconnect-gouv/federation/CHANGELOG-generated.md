## Changelog : federation (30 derniers jours)

### Résumé
Ce mois-ci, l'équipe a déployé une nouvelle interface utilisateur plus moderne et responsive, améliorant l'expérience utilisateur globale. Des corrections de sécurité et des mises à jour de dépendances ont également été effectuées pour assurer la stabilité et la sécurité de la plateforme. Plusieurs améliorations techniques ont été apportées, notamment au niveau de la configuration et des alertes.

### Évolutions fonctionnelles
- Nouvelle interface utilisateur avec une disposition en une seule colonne (#802, #851).
- Amélioration de la version responsive de la nouvelle interface utilisateur (#868).
- Ajout d'un bouton de contact pour signaler les erreurs internes (#829).
- Amélioration des messages d'erreur liés à la configuration de l'authentification OIDC (#853).

### Évolutions techniques
- Suppression d'un index TTL obsolète dans MongoDB (#849).
- Correction de la gestion des variables booléennes dans Ansible (#848).
- Passage au module ESNext pour une meilleure compatibilité et performance (#855).
- Mise à jour de plusieurs dépendances : Axios, pg, docker/build-push-action, otpauth, eslint-plugin-prettier, body-parser, prettier, @eslint-community/eslint-plugin-eslint-comments, type-fest, @nestjs/common, jquery (#833, #834, #836, #835, #837, #838, #839, #841, #846, #856, #857, #858, #860, #861, #863, #873, #874, #876, #877, #878).
- Mise à jour des tests Cypress pour l'environnement Kubernetes (#881).
- Révision de la politique de sécurité et ajout d'un mécanisme de signalement de vulnérabilités (#884).

### Autres changements
- Suppression d'un manifeste web misleading (#872).
- Suppression d'un avis concernant la nouvelle interface utilisateur (#867).
- Ajout d'une alerte d'avertissement pour l'environnement de test (#848).
- Suppression d'un revert de correction de crash (#869).
