## Changelog : domifa (30 derniers jours, au 17 mai 2026)

### Résumé
Ce mois-ci, les évolutions de DomiFa se concentrent sur la sécurité et l'amélioration de l'expérience utilisateur. L'ajout d'une authentification à deux facteurs (OTP) et de la détection d'empreinte digitale renforcent la protection des comptes. Des mises à jour de l'interface utilisateur et des corrections de bugs améliorent la fluidité et la fiabilité de la plateforme.

### Évolutions fonctionnelles
- Ajout de l'authentification à deux facteurs (OTP) pour certains endpoints et pour l'administration, avec envoi d'un email pour la récupération.
- Implémentation d'une détection d'empreinte digitale pour renforcer la sécurité des sessions utilisateurs.
- Ajout d'une fonctionnalité de blocage des utilisateurs suspects (bots) basée sur l'agent utilisateur et l'analyse du comportement.
- Ajout de statistiques dans l'interface d'administration.
- Ajout d'une page de témoignages pour les utilisateurs.
- Mise à jour de l'interface utilisateur avec la version 19, incluant des corrections liées à DSFR.
- Ajout d'une liste d'utilisateurs dans l'interface d'administration.
- Ajout d'un statut pour bloquer les comptes utilisateurs.
- Ajout de détails sur le réseau pour les utilisateurs.
- Ajout d'un bandeau DSFR.

### Évolutions techniques
- Mise à jour des tests Angular pour la compatibilité avec la version 19.
- Refactorisation du code pour l'intégration de statistiques Metabase.
- Correction de bugs et améliorations des tests unitaires backend et frontend.
- Amélioration des performances de la gestion des OTP.
- Correction de problèmes de typage dans les tests TypeORM.
- Ajout de tests unitaires pour la fonctionnalité de blocage.

### Autres changements
- Suppression de Bootstrap dans l'interface d'administration.
- Mise à jour des dépendances et des configurations CI/CD.
- Ajout de commentaires et documentation pour certaines fonctionnalités.
- Correction de problèmes de linting dans l'interface d'administration.
- Ajout de la possibilité de forcer une seule session par utilisateur.
- Correction de bugs mineurs dans l'interface utilisateur (étiquettes, champs de formulaire, etc.).
