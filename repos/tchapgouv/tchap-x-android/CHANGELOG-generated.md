## Changelog : tchap-x-android (30 derniers jours, au 16/10/2026)

### Résumé
Cette période a été marquée par un renforcement de la sécurité des accès et une amélioration significative du confort d'utilisation. Les utilisateurs bénéficient désormais de nouvelles options de personnalisation (mode sombre), d'une meilleure gestion des notifications et de mécanismes de vérification d'identité plus robustes.

### Évolutions fonctionnelles
- **Sécurité et Authentification** : 
    - Renforcement de la vérification de l'adresse email lors de la connexion et de la création de compte.
    - Ajout d'une alerte de sécurité lors de la saisie d'une adresse email externe.
- **Expérience Utilisateur (UX) et Interface** :
    - Activation du thème sombre (Dark Mode).
    - Ajout du compteur de messages non lus et de la fonction "Aller au dernier message non lu".
    - Optimisation de l'affichage du texte des messages animés.
- **Notifications** : 
    - Nettoyage automatique des notifications pour les discussions déjà consultées.
- **Localisation** : 
    - Amélioration des traductions pour les badges d'information de l'historique des salons et pour les sondages à votes multiples.

### Évolutions techniques
- **Compatibilité et Sécurité** : 
    - Optimisation de la gestion des certificats pour assurer la compatibilité avec Android 13 et les versions antérieures.
    - Migration vers une gestion des certificats par le système Android.
- **CI/CD et Infrastructure** : 
    - Ajout de la génération de builds pour le dépôt F-Droid.
    - Configuration des URLs pour le suivi des erreurs via Sentry.
- **Optimisation logicielle** : 
    - Amélioration de la logique de lecture des notifications push (gestion des cas sans `eventId` ou `roomId`).

### Autres changements
- **Versions** : Publication des versions 26.09.1 et 26.09.2.
