## Changelog : tchap-x-android (30 derniers jours, au 20 octobre 2026)

### Résumé
La version 26.10.0 renforce la sécurité des accès et optimise la gestion des notifications pour offrir une expérience utilisateur plus fluide et mieux sécurisée.

### Évolutions fonctionnelles
- **Sécurité** : Renforcement de l'authentification via la vérification de l'adresse email lors de la connexion et de la création de compte, et ajout d'une alerte de sécurité lors de la saisie d'une adresse email externe.
- **Notifications** : Amélioration de la gestion des notifications globales du compte et mise en place d'un nettoyage automatique des notifications pour les discussions déjà lues.
- **Interface** : Optimisation de l'affichage du texte pour les messages provenant du Web.

### Évolutions techniques
- **Notifications** : Amélioration de la robustesse de la lecture des notifications push (gestion des cas sans `eventId` ou `roomId`).
- **Observabilité** : Configuration des URLs Sentry pour le suivi et le rapport d'erreurs.
