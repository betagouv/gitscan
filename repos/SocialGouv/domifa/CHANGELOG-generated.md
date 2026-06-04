## Changelog : domifa (30 derniers jours, au 3 juin 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de la sécurité, notamment l'ajout de l'authentification à deux facteurs (OTP) et des mesures anti-bot. Des corrections de bugs et des optimisations ont également été apportées pour améliorer la stabilité et l'expérience utilisateur, en particulier dans l'interface d'administration.

### Évolutions fonctionnelles
- Ajout de l'authentification à deux facteurs (OTP) pour la connexion des utilisateurs.
- Implémentation d'un système de blocage des bots basé sur l'analyse de l'agent utilisateur et d'autres critères.
- Possibilité de réinitialiser l'OTP.
- Ajout d'une page de témoignages.
- Ajout de détails réseau dans l'interface d'administration.
- Ajout d'une liste d'utilisateurs dans l'interface d'administration.
- Ajout d'un statut de blocage pour les comptes utilisateurs.
- Amélioration de l'interface d'administration avec des tooltips et des titres plus clairs.
- Ajout de statistiques dans l'interface d'administration.

### Évolutions techniques
- Refactorisation des logs pour améliorer la sécurité et le débogage.
- Durcissement de la sécurité de l'OTP avec limitation du nombre de tentatives et restriction d'accès.
- Mise à jour des dépendances Angular vers la version 19 dans l'interface d'administration.
- Amélioration des tests unitaires.
- Ajout de fingerprinting pour améliorer la sécurité des sessions.
- Implémentation d'une politique de session unique (une seule session active par utilisateur).
- Ajout de logs pour le suivi des activités et la détection des anomalies.

### Autres changements
- Correction de divers bugs et améliorations de la stabilité.
- Mise à jour de la documentation et des tests.
- Amélioration des messages d'erreur et des informations affichées aux utilisateurs.
- Correction de problèmes liés à l'affichage des adresses e-mail.
- Suppression de Bootstrap de l'interface d'administration.
- Correction de problèmes de chargement des utilisateurs dans l'interface d'administration.
- Correction de problèmes de typage dans le code backend.
- Ajout d'un testeur d'envoi d'emails générique.
- Correction de problèmes liés à la gestion des utilisateurs bloqués.
- Ajout d'un mécanisme de déblocage des utilisateurs.
- Amélioration de la gestion des erreurs 401.
- Ajout de labels d'action pour une meilleure traçabilité.
- Ajout d'une structure de logs plus claire.
- Correction de problèmes liés aux tests de bout en bout.
- Correction de problèmes liés à l'UUID.
- Amélioration des limites de throttling.
- Correction de bugs dans les tests unitaires.
- Ajout de la possibilité de se déconnecter de Brevo.
- Correction de problèmes de construction de l'application frontend.
