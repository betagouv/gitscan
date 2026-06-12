## Changelog : domifa (30 derniers jours, au 12 juin 2026)

### Résumé
Cette période a été marquée par une amélioration significative de la sécurité de la plateforme, notamment avec l'ajout de l'authentification à deux facteurs (OTP) et la surveillance des activités suspectes. Des corrections de bugs et des améliorations de la gestion des utilisateurs ont également été apportées, ainsi que des optimisations techniques et des mises à jour de l'interface utilisateur.

### Évolutions fonctionnelles
- Ajout de l'authentification à deux facteurs (OTP) pour la connexion et certaines actions sensibles.
- Implémentation d'un système de détection d'activités suspectes avec envoi d'OTP.
- Possibilité de supprimer des utilisateurs depuis le backend.
- Ajout de filtres dans l'interface d'administration pour faciliter la recherche et la gestion des données.
- Amélioration de la gestion des sessions utilisateurs, avec limitation du nombre de sessions actives.
- Ajout de la possibilité de renvoyer un OTP.
- Ajout de statistiques sur les sessions utilisateurs.
- Amélioration de l'affichage de l'agent utilisateur dans les logs.
- Ajout de la possibilité de débloquer des utilisateurs.

### Évolutions techniques
- Refonte des logs pour une meilleure traçabilité et un débogage facilité.
- Amélioration de la sécurité avec l'ajout de fingerprinting pour identifier les sessions.
- Mise à jour des dépendances Angular vers la version 19.
- Optimisation des performances de la gestion des utilisateurs.
- Ajout de tests unitaires et correction de tests existants.
- Amélioration de la gestion des erreurs avec l'ajout de filtres d'exception.
- Ajout d'un mécanisme de throttling pour limiter les tentatives de connexion.
- Intégration de Brevo pour l'envoi d'emails (OTP, alertes).
- Ajout de tests pour la gestion des OTP.

### Autres changements
- Correction de divers bugs mineurs dans l'interface utilisateur et le backend.
- Amélioration de la documentation et des messages d'erreur.
- Mise à jour des dépendances et des configurations.
- Ajout de templates d'emails pour les OTP.
- Correction de problèmes de typage dans le code.
- Ajout de logs pour faciliter le débogage.
- Correction de problèmes liés à l'importation de données.
- Amélioration de la structure des logs.
- Correction de problèmes liés à la gestion des utilisateurs bloqués.
- Ajout de titres et de pages dans l'interface d'administration.
- Correction de problèmes d'affichage de l'adresse email dans l'interface utilisateur.
- Suppression de composants Angular non utilisés.
- Correction de problèmes de linting.
