## Changelog : domifa (30 derniers jours, au 22 mai 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de la sécurité, notamment l'ajout de l'authentification à deux facteurs (OTP) pour la connexion et pour certaines actions sensibles. Des corrections de bugs et des améliorations de la stabilité ont également été apportées, ainsi que des mises à jour de l'interface utilisateur et des dépendances.

### Évolutions fonctionnelles
- Ajout de l'authentification à deux facteurs (OTP) pour la connexion des utilisateurs.
- Ajout de l'OTP pour certaines actions sensibles, renforçant la sécurité.
- Amélioration de la recherche avec ajout de filtres et débogage.
- Ajout d'une page de témoignages.
- Amélioration de l'interface utilisateur pour la gestion des structures, avec affichage de l'UUID et amélioration des menus déroulants.
- Ajout d'une liste d'utilisateurs dans l'espace administrateur.
- Ajout d'un statut pour bloquer/débloquer les comptes utilisateurs.
- Ajout d'informations sur le réseau (network) dans les détails d'une structure.
- Correction de l'email des alertes.
- Correction du chargement des utilisateurs.
- Correction du modal de premier login.
- Ajout d'un indicateur de statut pour les comptes bloqués.
- Ajout de tooltips dans la gestion des structures.
- Ajout d'un bandeau d'information (DSFR).

### Évolutions techniques
- Mise à jour des dépendances Angular vers la version 19.
- Amélioration de la journalisation (logs) avec ajout du type d'utilisateur et d'autres informations contextuelles.
- Refactorisation du code pour améliorer la performance et la maintenabilité.
- Ajout de tests unitaires pour les nouvelles fonctionnalités et corrections de bugs.
- Amélioration de la sécurité en durcissant l'implémentation de l'OTP (limitation du nombre de tentatives, accès aux structures).
- Ajout de fingerprinting pour améliorer la sécurité des sessions.
- Limitation du nombre de sessions actives par utilisateur.
- Ajout de blocage basé sur l'agent utilisateur (user-agent).
- Amélioration des tests pour l'OTP.
- Ajout de statistiques dans l'interface administrateur.

### Autres changements
- Correction de divers bugs mineurs et améliorations de la qualité du code.
- Mise à jour de la documentation.
- Suppression de Bootstrap dans l'interface administrateur.
- Correction de problèmes liés à l'intégration avec DSFR.
- Ajustement des limites de throttling.
- Amélioration des tests unitaires.
- Correction de problèmes de build.
- Correction de labels de boutons.
