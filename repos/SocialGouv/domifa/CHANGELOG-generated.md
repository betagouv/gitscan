## Changelog : domifa (30 derniers jours, au 9 juin 2026)

### Résumé
Cette version apporte des améliorations significatives à la sécurité, notamment avec l'ajout de l'authentification à deux facteurs (OTP) et la protection contre les bots.  Des corrections de bugs et des améliorations de l'interface utilisateur ont également été implémentées, ainsi que des optimisations pour la gestion des utilisateurs et des journaux d'événements.

### Évolutions fonctionnelles
- Ajout de la suppression de comptes utilisateurs.
- Implémentation de l'authentification à deux facteurs (OTP) pour la connexion et certaines actions sensibles.
- Ajout de la possibilité de renvoyer un OTP.
- Ajout d'une liste d'utilisateurs dans l'interface d'administration.
- Ajout d'un statut pour bloquer/débloquer les comptes utilisateurs.
- Amélioration de l'interface d'administration avec des tooltips et des informations supplémentaires.
- Ajout d'une fonctionnalité de blocage des bots basée sur l'agent utilisateur et l'empreinte digitale.
- Ajout de statistiques de session.

### Évolutions techniques
- Renforcement de la sécurité avec l'ajout de limitations de tentatives de connexion (throttling).
- Amélioration de la journalisation (logs) pour faciliter le débogage et la surveillance de la sécurité.
- Mise à jour de la version d'Angular en v19 dans l'interface d'administration.
- Refactorisation des logs pour améliorer la sécurité et la lisibilité.
- Ajout de tests unitaires pour les nouvelles fonctionnalités et corrections de bugs.
- Amélioration de la gestion des sessions et de la sécurité.
- Ajout d'un mécanisme de détection d'activité suspecte et d'envoi d'alertes.
- Ajout d'une whitelist.

### Autres changements
- Correction de divers bugs liés à l'interface utilisateur et au backend.
- Amélioration des tests unitaires.
- Mise à jour des dépendances et de la configuration.
- Ajout de modèles d'emails pour l'authentification à deux facteurs.
- Correction de problèmes de construction de l'application frontend.
- Correction de problèmes d'affichage de l'adresse email.
- Ajout de tests pour la détection de type confusion.
