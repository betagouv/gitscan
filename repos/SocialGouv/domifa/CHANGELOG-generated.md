## Changelog : domifa (30 derniers jours, au 31 mai 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur la sécurité et la robustesse de la plateforme DomiFa.  Des améliorations significatives ont été apportées à la gestion des sessions, à la protection contre les attaques (OTP, fingerprinting, blocage de bots) et à la journalisation des événements pour faciliter le diagnostic et la surveillance. Des corrections de bugs et des améliorations de l'interface utilisateur ont également été implémentées.

### Évolutions fonctionnelles
- Ajout de la possibilité de renvoyer un OTP (One-Time Password) pour la connexion.
- Implémentation de l'authentification à deux facteurs (OTP) pour certaines fonctionnalités et pour l'administration.
- Ajout d'une page de témoignages.
- Amélioration de la liste des utilisateurs dans l'interface d'administration.
- Ajout d'un détail réseau dans l'interface d'administration.
- Ajout d'un affichage du statut de blocage des comptes utilisateurs.
- Ajout d'un tooltip dans l'interface de gestion.
- Ajout d'une page d'actualités.

### Évolutions techniques
- Renforcement de la sécurité des sessions utilisateurs avec l'ajout de fingerprinting et la limitation du nombre de sessions simultanées.
- Amélioration de la journalisation (logs) pour faciliter le débogage et la surveillance de la plateforme.
- Refactorisation des logs pour améliorer la sécurité.
- Mise en place d'un système de blocage des bots et des attaques automatisées.
- Mise à jour des dépendances Angular vers la version 19.
- Amélioration de la gestion des tests unitaires et d'intégration.
- Ajout de tests pour la gestion des comptes bloqués.
- Ajout de la gestion des rôles et des migrations de base de données.

### Autres changements
- Correction de divers bugs et améliorations de la stabilité de la plateforme.
- Correction de l'affichage de l'agent utilisateur.
- Suppression de Bootstrap dans l'interface d'administration.
- Ajout de titres et d'une page pour améliorer l'accessibilité.
- Correction de problèmes liés aux tests unitaires.
- Amélioration des statistiques Metabase.
- Correction de problèmes de chargement des utilisateurs.
- Correction de problèmes d'affichage des alertes.
- Correction de problèmes liés à l'envoi d'emails.
- Correction de problèmes de configuration et de déploiement.
- Ajout de la possibilité de délier un compte Brevo.
- Ajout d'une whitelist pour Brevo.
- Ajustement des limites de throttling.
- Ajout de labels d'action.
- Ajout de secrets.
- Ajout de structure aux logs.
- Correction de tests end-to-end.
- Correction de filtres.
- Correction de l'affichage de l'email des alertes.
- Correction de la gestion des OTP.
- Correction de la réinitialisation des OTP.
- Correction de la performance de la gestion des utilisateurs.
- Correction de la gestion des sessions.
- Correction de la vue de sécurité.
