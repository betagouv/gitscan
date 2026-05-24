## Changelog : domifa (30 derniers jours, au 22 mai 2026)

### Résumé
Cette période a été marquée par une amélioration significative de la sécurité de la plateforme, notamment avec l'ajout de l'authentification à deux facteurs (OTP) pour la connexion et certaines actions sensibles. Des corrections de bugs et des améliorations de la journalisation ont également été apportées, ainsi que des mises à jour de l'interface utilisateur et des dépendances.

### Évolutions fonctionnelles
- Ajout de la possibilité de renvoyer le code OTP (One-Time Password) pour la connexion.
- Implémentation de l'authentification à deux facteurs (OTP) pour la connexion des utilisateurs.
- Ajout de la possibilité de bloquer des comptes utilisateurs pour des raisons de sécurité.
- Ajout d'une page de témoignages.
- Amélioration de la recherche et des filtres dans l'interface d'administration.
- Ajout d'une liste d'utilisateurs dans l'interface d'administration.
- Ajout d'un statut (bloqué/débloqué) pour les comptes utilisateurs.
- Amélioration de l'affichage des listes et des formulaires dans l'interface utilisateur.
- Ajout d'un indicateur visuel (tooltip) dans l'interface de gestion.

### Évolutions techniques
- Renforcement de la sécurité de l'authentification avec l'ajout de limitations de débit (throttling) et de la vérification de l'empreinte du navigateur.
- Ajout de la journalisation (logs) plus détaillée, incluant le type d'utilisateur et des informations supplémentaires pour le débogage.
- Mise à jour de la structure des logs pour une meilleure lisibilité.
- Amélioration des tests unitaires et de bout en bout.
- Mise à niveau des dépendances frontend vers la version 19.
- Refactorisation du code pour l'intégration des statistiques Metabase.
- Suppression de Bootstrap et migration vers DSFR (Design System for French administration).

### Autres changements
- Correction de divers bugs mineurs dans l'interface utilisateur et le backend.
- Amélioration de la documentation et des tests.
- Correction de problèmes liés aux tests OTP.
- Ajustement des limites de throttling.
- Correction de l'envoi des emails d'alerte.
- Correction de problèmes liés au chargement des utilisateurs.
- Suppression de code obsolète.
- Correction de problèmes de linting et de configuration des composants autonomes.
