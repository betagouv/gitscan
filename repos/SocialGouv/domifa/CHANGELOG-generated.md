## Changelog : domifa (30 derniers jours, au 29 mai 2026)

### Résumé
Ce changelog présente les améliorations apportées à domifa au cours des 30 derniers jours. Les principales évolutions concernent la sécurité avec l'ajout de l'authentification à deux facteurs (OTP) et des mesures anti-bot, ainsi que des corrections de bugs et des améliorations de la gestion des utilisateurs et des journaux d'événements. L'interface d'administration a également été améliorée.

### Évolutions fonctionnelles
- Ajout de la possibilité de renvoyer un code OTP (One-Time Password) pour la connexion.
- Implémentation de l'authentification à deux facteurs (OTP) pour la connexion et certaines actions sensibles.
- Ajout d'une liste d'utilisateurs dans l'interface d'administration.
- Ajout d'un statut (bloqué/débloqué) pour les comptes utilisateurs dans l'interface d'administration.
- Amélioration de l'interface d'administration pour la gestion des utilisateurs, avec des filtres et des corrections d'affichage.
- Ajout d'une page de témoignages.
- Amélioration de l'affichage des informations réseau.
- Correction de l'affichage de l'agent utilisateur.
- Correction de l'affichage des modals de première connexion.
- Correction du chargement des utilisateurs dans l'interface d'administration.
- Ajout de tooltips dans l'interface de gestion.
- Ajout d'actualités dans l'interface.

### Évolutions techniques
- Refactorisation des journaux d'événements pour améliorer la sécurité et la traçabilité.
- Ajout de la gestion de Brevo (Sendinblue) pour l'envoi d'emails, incluant la possibilité de se désinscrire.
- Amélioration de la sécurité avec l'ajout de mesures anti-bot (blocage basé sur l'agent utilisateur et l'ajout de fingerprinting).
- Mise en place de limitations de débit (throttling) pour certaines actions afin de prévenir les abus.
- Ajout de tests unitaires et d'intégration pour les nouvelles fonctionnalités et corrections de bugs.
- Mise à jour des dépendances Angular vers la version 19.
- Amélioration de la gestion des sessions.
- Ajout de logs pour le monitoring et le débogage.
- Correction de problèmes liés à TypeORM dans les tests.
- Suppression de Bootstrap de l'interface d'administration.

### Autres changements
- Correction de bugs mineurs dans l'interface utilisateur et les tests.
- Amélioration de la configuration et de la documentation.
- Correction de problèmes de linting et de structure de code.
- Correction de problèmes liés aux tests unitaires.
- Ajout de statistiques pour l'administration.
- Correction de l'envoi d'emails d'alerte.
- Correction de problèmes liés aux tests de bout en bout.
- Ajout de structure aux logs.
- Ajout de labels pour les actions.
- Ajout de secrets.
- Correction de l'affichage des champs de formulaire.
- Correction des fiches pratiques.
- Amélioration de la conformité RGAA.
- Correction de problèmes de build.
- Correction de problèmes d'affichage.
- Ajout de tests pour le blocage des utilisateurs.
- Correction de l'annulation du blocage des utilisateurs.
- Ajout de la gestion des UUID dans l'interface d'administration.
- Durcissement de la sécurité de l'OTP.
- Ajout de whitelist.
- Ajout de logs pour le type d'utilisateur.
- Ajout d'éléments aux logs.
- Ajout de monitoring.
- Suppression de l'obligation de réinitialiser l'OTP.
- Ajustement des limites de throttling.
- Correction de bugs dans les tests unitaires.
- Correction de problèmes de build.
- Correction de problèmes d'affichage.
- Correction de problèmes liés à DSFR.
- Ajout de champs requis.
- Correction des tests unitaires.
- Correction des labels des boutons.
- Correction des tests de build.
- Ajout de template d'email pour l'OTP.
- Correction de l'affichage des statistiques.
- Correction de l'upload des fichiers.
