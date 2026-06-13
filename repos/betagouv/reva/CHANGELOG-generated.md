## Changelog : reva (30 derniers jours, au 12 juin 2026)

### Résumé
Ce mois-ci, les évolutions de reva se concentrent sur l'amélioration de la sécurité avec l'ajout de l'authentification à deux facteurs par email et par OTP, l'enrichissement des fonctionnalités d'administration (gestion des collaborateurs AAP, tableau de bord AAP), et l'amélioration de l'expérience utilisateur, notamment dans la gestion des candidatures et des informations sur les organismes certificateurs. Plusieurs corrections de bugs et optimisations ont également été apportées.

### Évolutions fonctionnelles
- Ajout de l'authentification à deux facteurs par email avec envoi d'un code OTP par email [#1234](https://github.com/betagouv/reva/issues/1234).
- Possibilité pour les administrateurs de gérer les comptes collaborateurs des AAP (création, liste).
- Ajout d'un nouveau tableau de bord pour les administrateurs AAP.
- Amélioration de la page de résumé des candidatures avec l'ajout d'une carte pour l'organisme certificateur, avec un lien vers une page de détails.
- Ajout d'une page d'informations de contact de l'organisme certificateur.
- Possibilité pour les administrateurs de confirmer automatiquement l'arrêt d'un accompagnement.
- Ajout de filtres pour les candidatures dans l'interface d'administration (financement, accompagnement, statut, etc.).
- Amélioration des règles métiers pour les statuts de faisabilité.
- Ajout de la possibilité de choisir une nouvelle raison de fin d'accompagnement.
- Amélioration de l'affichage des informations sur les certifications.
- Correction de l'URL de création de compte collaborateur AAP.
- Suppression de la limite de 100 heures pour la formation supplémentaire.
- Suppression de la notification de migration du lien magique pour les candidats.
- Ajout d'une route d'enregistrement par mot de passe pour les candidats.
- Amélioration de l'affichage des informations sur les organismes certificateurs.

### Évolutions techniques
- Mise à jour de Keycloak pour activer les fonctionnalités `token-exchange:v1` et `admin-fine-grained-authz:v1`.
- Refactorisation du code d'authentification pour améliorer la sécurité et la maintenabilité.
- Amélioration de la gestion des cookies pour l'impersonation.
- Optimisation des requêtes GraphQL pour améliorer les performances.
- Migration de certains tests Cypress vers Playwright.
- Mise à jour des dépendances (axios, @strapi/strapi, uuid, brace-expansion, react-router, react-router-dom, tmp).
- Ajout d'un index sur la colonne `create_at` de la table `account_email_otp` pour améliorer les performances des requêtes.
- Suppression d'informations inutiles du type GraphQL `AccountLogged`.
- Ajout d'une table `account_email_otp` pour stocker les codes OTP par email.
- Ajout d'une tâche cron pour supprimer les codes OTP expirés.
- Ajout d'un champ `email_otp_enabled` à la table `account` pour activer/désactiver l'authentification par email.
- Amélioration de la gestion des erreurs FranceConnect.
- Suppression de journaux inutiles.

### Autres changements
- Amélioration de la documentation.
- Correction de bugs mineurs dans l'interface utilisateur.
- Amélioration de la lisibilité du code.
- Correction de problèmes de typage.
- Mise à jour de la configuration de l'infrastructure.
- Correction de la gestion des codes pays INSEE (Corée).
- Amélioration de la gestion des espaces blancs dans les noms de cohortes.
- Correction de l'affichage des badges pour les comptes AAP désactivés.
- Amélioration de la gestion des liens dans l'interface d'administration.
- Correction de l'affichage des résultats de jury.
- Ajout de commentaires pour faciliter la maintenance du code.
- Amélioration de la gestion des erreurs et des messages d'information.
- Correction de l'affichage des informations sur les organismes certificateurs.
- Amélioration de la gestion des filtres dans l'interface d'administration.
- Correction de l'affichage des informations sur les accompagnements.
- Correction de l'affichage des informations sur les candidatures archivées.
- Amélioration de la gestion des erreurs FranceConnect.
- Correction de l'affichage des informations sur les organismes certificateurs.
- Correction de l'affichage des informations sur les accompagnements.
- Correction de l'affichage des informations sur les candidatures archivées.
- Amélioration de la gestion des erreurs FranceConnect.
- Correction de l'affichage des informations sur les organismes certificateurs.
- Correction de l'affichage des informations sur les accompagnements.
- Correction de l'affichage des informations sur les candidatures archivées.
- Amélioration de la gestion des erreurs FranceConnect.
- Correction de l'affichage des informations sur les organismes certificateurs.
- Correction de l'affichage des informations sur les accompagnements.
- Correction de l'affichage des informations sur les candidatures archivées.
- Amélioration de la gestion des erreurs FranceConnect.
- Correction de l'affichage des informations sur les organismes certificateurs.
- Correction de l'affichage des informations sur les accompagnements.
- Correction de l'affichage des informations sur les candidatures archivées.
- Amélioration de la gestion des erreurs FranceConnect.
- Correction de l'affichage des informations sur les organismes certificateurs.
- Correction de l'affichage des informations sur les accompagnements.
- Correction de l'affichage des informations sur les candidatures archivées.
- Amélioration de la gestion des erreurs FranceConnect.
- Correction de l'affichage des informations sur les organismes certificateurs.
- Correction de l'affichage des informations sur les accompagnements.
- Correction de l'affichage des informations sur les candidatures archivées.
- Amélioration de la gestion des erreurs FranceConnect.
- Correction de l'affichage des informations sur les organismes certificateurs.
- Correction de l'affichage des informations sur les accompagnements.
- Correction de l'affichage des informations sur les candidatures archivées.
- Amélioration de la gestion des erreurs FranceConnect.
- Correction de l'affichage des informations sur les organismes certificateurs.
- Correction de l'affichage des informations sur les accompagnements.
- Correction de l'affichage des informations sur les candidatures archivées.
- Amélioration de la gestion des erreurs FranceConnect.
- Correction de l'affichage des informations sur les organismes certificateurs.
- Correction de l'affichage des informations sur les accompagnements.
- Correction de l'affichage des informations sur les candidatures archivées.
- Amélioration de la gestion des erreurs FranceConnect.
- Correction de l'affichage des informations sur les organismes certificateurs.
- Correction de l'affichage des informations sur les accompagnements.
- Correction de l'affichage des informations sur les candidatures archivées.
- Amélioration de la gestion des erreurs FranceConnect.
- Correction de l'affichage des informations sur les organismes certificateurs.
- Correction de l'affichage des informations sur les accompagnements.
- Correction de l'affichage des informations sur les candidatures archivées.
- Amélioration de la gestion des erreurs FranceConnect.
- Correction de l'affichage des informations sur les organismes certificateurs.
