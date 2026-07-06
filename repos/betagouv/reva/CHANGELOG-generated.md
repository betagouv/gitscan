## Changelog : reva (30 derniers jours, au 03 juillet 2026)

### Résumé
Les dernières mises à jour de reva se concentrent sur l'amélioration de l'expérience utilisateur dans l'interface d'administration, notamment pour la gestion des organismes de certification et des candidatures. Des améliorations ont également été apportées à l'interopérabilité avec des systèmes externes, ainsi qu'à la sécurité avec l'ajout de l'authentification par email. Des corrections de bugs et des optimisations de performance ont également été réalisées.

### Évolutions fonctionnelles
- Ajout de la possibilité de mettre à jour l'autorité de certification dans la page récapitulative d'une candidature ([#1057](https://github.com/betagouv/reva/issues/1057)).
- Amélioration de l'interface utilisateur des pages "expériences du candidat", "pièces jointes", "prérequis", "compétences-blocs" et "certification" dans l'administration.
- Ajout d'une page de sélection de l'autorité de certification avec une liste et une action de mise à jour directe.
- Possibilité de voir les domaines de certification au lieu des sous-domaines dans l'administration.
- Ajout d'un bouton pour impersonner un utilisateur dans la nouvelle liste des comptes AAP.
- Ajout d'un message de confirmation lors de la mise à jour de l'autorité de certification.
- Ajout de la possibilité d'ajouter des commentaires et des décisions à l'historique de faisabilité dans l'interopérabilité.
- Ajout de la possibilité d'accepter des résultats par compétence lors de la mise à jour des résultats du jury dans l'interopérabilité.
- Ajout d'une alerte dans l'administration pour les candidatures sans financement.
- Ajout de la possibilité de supprimer le financement dans la page récapitulative de la candidature.
- Ajout d'une nouvelle page pour la gestion des comptes collaborateurs AAP.
- Ajout de la possibilité d'ajouter de nouveaux comptes collaborateurs AAP depuis la liste.
- Ajout de la possibilité de s'inscrire avec un mot de passe (contrôlé par un flag de fonctionnalité).
- Ajout de la vérification par email (OTP) pour l'authentification.
- Ajout d'un lien vers un formulaire de pré-qualification dans le pied de page du site web.

### Évolutions techniques
- Mise à jour de la version de Keycloak (26.6.1 -> 26.6.4).
- Amélioration de la gestion des sessions SSO.
- Ajout d'un index sur la colonne `create_at` de la table `account_email_otp` pour optimiser les performances.
- Refactoring du code pour améliorer la lisibilité et la maintenabilité.
- Ajout de tests unitaires et d'intégration pour valider les nouvelles fonctionnalités et les corrections de bugs.
- Amélioration de la gestion des erreurs et des logs.
- Ajout de tests Cypress et Playwright.
- Ajout d'un service ClamAV pour l'analyse antivirus des fichiers téléchargés par les utilisateurs.
- Optimisation des requêtes SQL.
- Amélioration de la gestion des transactions.
- Ajout de tests pour la vérification de la signature des fichiers.

### Autres changements
- Mise à jour des dépendances (js-yaml, @microsoft/kiota-http-fetchlibrary, vite, shell-quote, form-data, undici, dompurify).
- Correction de bugs mineurs et améliorations de la documentation.
- Nettoyage du code et suppression de code obsolète.
- Amélioration des messages d'erreur et des validations.
- Correction de tests cassés.
- Suppression de code dupliqué.
- Amélioration de la structure du projet.
- Ajout de commentaires au code.
- Correction de problèmes de typage.
- Amélioration de la sécurité.
- Ajout de logs pour le débogage.
- Correction de problèmes de performance.
- Amélioration de l'accessibilité.
- Correction de problèmes de compatibilité.
- Amélioration de la configuration.
- Mise à jour des fichiers de documentation.
- Correction de problèmes de build.
- Amélioration de la gestion des erreurs de build.
