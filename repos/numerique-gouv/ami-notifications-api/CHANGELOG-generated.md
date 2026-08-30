## Changelog : ami-notifications-api (30 derniers jours, au 28 août 2026)

### Résumé
Ce mois-ci, le projet a franchi des étapes majeures concernant la sécurité et l'expérience utilisateur. L'authentification a été modernisée avec l'intégration des Passkeys et un renforcement des processus FranceConnect. L'interface a également été enrichie par une refonte de l'affichage des notifications (suivis), une meilleure présentation des services (SOS, étapes) et une gestion plus fluide des consentements pour les partenaires.

### Évolutions fonctionnelles
- **Authentification et accès** : 
    - Support des Passkeys pour Android et iOS avec une gestion améliorée des erreurs et des redirections lors du processus d'authentification [#1088](https://github.com/numerique-gouv/ami-notifications-api/issues/1088), [#1185](https://github.com/numerique-gouv/ami-notifications-api/issues/1185), [#1179](https://github.com/numerique-gouv/ami-notifications-api/issues/1179).
    - Amélioration du parcours de connexion avec une redirection automatique vers la page de login si l'utilisateur n'est pas connecté [#1152](https://github.com/numerique-gouv/ami-notifications-api/issues/1152).
- **Interface utilisateur (UI/UX)** :
    - Refonte complète de l'écran de démarrage pour améliorer la clarté et l'ergonomie [#1098](https://github.com/numerique-gouv/ami-notifications-api/issues/1098).
    - Amélioration de l'affichage des notifications (suivis) avec une gestion de hiérarchie complexe (sous-éléments) [#825](https://github.com/numerique-gouv/ami-notifications-api/issues/825).
    - Intégration de nouveaux services (SOS et étapes) avec des icônes et des catégories dédiées [#1048](https://github.com/numerique-gouv/ami-notifications-api/issues/1048).
    - Ajout de fonctionnalités de promotion automatique pour les vacances scolaires sur la page d'accueil [#1001](https://github.com/numerique-gouv/ami-notifications-api/issues/1001).
    - Ajout de bannières informatives sur les pages d'édition [#769](https://github.com/numerique-gouv/ami-notifications-api/issues/769).

### Évolutions techniques
- **Sécurité et API** :
    - Renforcement de la sécurité FranceConnect via la vérification des signatures des tokens et l'utilisation de l'algorithme ES256 [#1219](https://github.com/numerique-gouv/ami-notifications-api/issues/1219), [#1172](https://github.com/numerique-gouv/ami-notifications-api/issues/1172).
    - Mise en place d'une limitation de débit (rate limiting) sur les endpoints de gestion des clés d'accès [#1096](https://github.com/numerique-gouv/ami-notifications-api/issues/1096).
    - Création de nouveaux endpoints permettant aux partenaires de gérer et de consulter le consentement des utilisateurs [#1192](https://github.com/numerique-gouv/ami-notifications-api/issues/1192), [#1159](https://github.com/numerique-gouv/ami-notifications-api/issues/1159).
    - Finalisation de la migration des champs de l'API de notification vers la version 2 [#1005](https://github.com/numerique-gouv/ami-notifications-api/issues/1005).
- **Architecture et Infrastructure** :
    - Transition vers Vite pour le proxying des URLs Django afin d'optimiser le développement frontend [#1138](https://github.com/numerique-gouv/ami-notifications-api/issues/1138).
    - Publication des fichiers de configuration nécessaires au lien d'application mobile (Android/iOS) via les dossiers `.well-known` [#1088](https://github.com/numerique-gouv/ami-notifications-api/issues/1088).
    - Ajout de logs d'audit pour suivre les modifications effectuées sur les services dans l'interface d'administration [#1054](https://github.com/numerique-gouv/ami-notifications-api/issues/1054).
    - Intégration des tests système dans les workflows GitHub Actions [#10](https://github.com/numerique-gouv/ami-notifications-api/issues/10).

### Autres changements
- **Configuration** : Ajout d'un template pour les variables d'environnement (`.env.local.template`) [#1095](https://github.com/numerique-gouv/ami-notifications-api/issues/1095).
- **Maintenance** : Nettoyage du code (suppression d'icônes inutilisées, correction de fautes de frappe et de typographie) et ajout de hooks de pré-commit pour la validation des messages de commit [#157](https://github.com/numerique-gouv/ami-notifications-api/issues/157).
