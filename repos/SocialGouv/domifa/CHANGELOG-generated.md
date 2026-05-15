## Changelog : domifa (30 derniers jours, au 15 mai 2026)

### Résumé
Les dernières semaines ont été marquées par des améliorations significatives en matière de sécurité, avec l'ajout de l'authentification à deux facteurs (OTP) et de mécanismes de blocage des bots. L'interface d'administration a également été enrichie avec de nouvelles fonctionnalités de gestion des utilisateurs et de statistiques. Plusieurs corrections de bugs et améliorations de l'expérience utilisateur ont été apportées, notamment au niveau de l'interface et des tests.

### Évolutions fonctionnelles
- Ajout de l'authentification à deux facteurs (OTP) pour certaines actions sensibles, renforçant la sécurité des comptes utilisateurs.
- Implémentation d'un système de blocage des bots pour prévenir les abus et garantir la disponibilité du service.
- Ajout de statistiques dans l'interface d'administration pour un meilleur suivi de l'activité.
- Ajout d'une page de témoignages dans l'interface utilisateur.
- Possibilité de visualiser le détail du réseau associé à un compte.
- Ajout d'une liste d'utilisateurs dans l'interface d'administration.
- Ajout d'un statut (bloqué/débloqué) aux comptes utilisateurs.
- Amélioration de l'affichage des formulaires et de la page RGAA dans l'interface utilisateur.
- Ajout d'un bandeau d'information DSFR (Design System FR) dans l'interface utilisateur.
- Ajout d'un tooltip pour faciliter la compréhension des actions dans l'interface de gestion.

### Évolutions techniques
- Ajout de tests unitaires pour les nouvelles fonctionnalités et corrections de bugs.
- Refonte de la récupération des statistiques pour Metabase.
- Amélioration de la gestion des tests avec TypeORM.
- Mise à jour de la librairie `inlt-tel` et de ses tests unitaires.
- Ajout d'un fingerprint pour améliorer la sécurité des sessions.
- Limitation du nombre de sessions actives par utilisateur.
- Ajout de la gestion de l'agent utilisateur pour le blocage des bots.
- Correction de problèmes liés aux tests et aux migrations.
- Suppression de Bootstrap dans l'interface d'administration.
- Correction de problèmes liés aux filtres dans le backend.

### Autres changements
- Ajout d'un fichier CLA (Contributor License Agreement) pour les contributions externes.
- Correction de la configuration du CI/CD pour les releases.
- Amélioration du changelog et de la gestion des versions.
- Correction de problèmes de build et de tests frontend.
- Mise à jour de la documentation.
