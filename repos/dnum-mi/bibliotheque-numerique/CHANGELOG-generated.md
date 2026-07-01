## Changelog : bibliotheque-numerique (30 derniers jours, au 8 juin 2026)

### Résumé
Cette version apporte des améliorations majeures concernant la gestion des conditions générales d'utilisation (CGU), avec l'ajout d'une page dédiée, d'un système d'acceptation et d'une validation côté serveur. Des corrections et améliorations techniques ont également été apportées à l'infrastructure et au processus de déploiement.

### Évolutions fonctionnelles
- Ajout d'une page publique pour consulter les conditions générales d'utilisation (CGU).
- Implémentation d'un flux d'acceptation des CGU pour les utilisateurs.
- Ajout d'un champ `termsAcceptedAt` au profil utilisateur pour enregistrer la date d'acceptation des CGU.
- Mise en place d'une validation de l'acceptation des CGU via un `TermsOfUseGuard`.
- Amélioration de la gestion des erreurs lors de l'acceptation des CGU.

### Évolutions techniques
- Mise à jour de l'image Docker pour utiliser une image "office" au lieu de "erc.aws".
- Correction de la commande utilisée pour démarrer le worker.
- Correction de la configuration du proxy local.
- Mise à jour du Dockerfile client.
- Correction du type manquant dans une vue.
- Modification de l'utilisateur utilisé pour le conteneur du serveur.
- Correction de la vérification du démarrage du serveur via le liveness probe dans le CI.
- Suppression d'un message d'erreur lié au nombre maximal de listeners Node.js.
- Correction de la variable d'environnement `VITE_APP_OPEN_SOURCE` pour garantir un comportement par défaut correct.

### Autres changements
- Mise à jour des tests E2E pour inclure la charte d'utilisation et les fixtures utilisateur.
- Suppression d'un dépôt Redis obsolète (bitnami/redis).
- Variabilisation des timeouts du health check.
