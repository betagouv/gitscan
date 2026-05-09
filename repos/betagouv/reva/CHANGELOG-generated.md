## Changelog : reva (30 derniers jours, au 07 mai 2026)

### Résumé
Ce mois-ci, les évolutions de reva se concentrent sur l'amélioration de la sécurité et de l'expérience utilisateur, notamment avec l'intégration de l'authentification à deux facteurs (2FA) pour l'administration, l'optimisation du parcours FranceConnect, et l'ajout de fonctionnalités pour la gestion des jurys et des résultats de VAE. Des corrections et des améliorations de performance ont également été apportées.

### Évolutions fonctionnelles
- Ajout de l'authentification à deux facteurs (2FA) pour l'administration, avec une page de connexion dédiée et une gestion des cookies chiffrés.
- Amélioration de l'intégration FranceConnect : gestion des erreurs et des informations manquantes, notamment la date de naissance.
- Possibilité de supprimer une candidature en cours, avec des règles spécifiques selon l'état d'avancement (notamment après l'envoi d'un dossier de faisabilité).
- Ajout de la possibilité pour un administrateur d'annuler un abandon de candidature confirmé par le candidat.
- Amélioration de la gestion des résultats de jury, avec la possibilité de saisir les résultats par blocs de compétences et de consulter l'historique.
- Ajout d'une page dédiée à la gestion des dates de jury.
- Amélioration de l'affichage des informations de certification dans l'interface d'administration.
- Ajout d'une fonctionnalité permettant de verrouiller la modification des expériences professionnelles une fois le dossier de faisabilité soumis.
- Ajout d'une page de suppression de candidature pour les certificateurs.
- Amélioration de l'affichage des informations de l'organisme de formation dans l'interface d'administration.
- Ajout d'un avertissement avant le renvoi d'une formation confirmée.
- Amélioration de l'expérience utilisateur sur la page d'inscription et de connexion.
- Ajout d'une fonctionnalité de nettoyage des données FranceConnect en sandbox pour l'administration.
- Amélioration de la gestion des erreurs et des logs pour FranceConnect.

### Évolutions techniques
- Mise à jour de plusieurs dépendances (Next.js, uuid, fastify, postcss, etc.).
- Refactorisation du code de l'administration pour améliorer la structure et la maintenabilité.
- Amélioration de la gestion des erreurs et des logs.
- Optimisation des requêtes SQL pour améliorer les performances.
- Mise à jour de Strapi vers la dernière version.
- Amélioration de la sécurité de l'application, notamment en corrigeant des vulnérabilités potentielles liées à l'authentification et à la gestion des secrets.
- Refactorisation de la gestion des tokens d'authentification dans l'administration.
- Utilisation de URQL pour la gestion du cache et des requêtes dans l'administration.
- Suppression de code obsolète et de fonctionnalités non utilisées.
- Amélioration de la couverture des tests unitaires et d'intégration.
- Mise à jour de la configuration de l'infrastructure (Scalingo, Keycloak, Docker).

### Autres changements
- Mise à jour de la documentation.
- Correction de bugs mineurs et améliorations de l'interface utilisateur.
- Amélioration de la gestion des erreurs et des messages d'alerte.
- Suppression de certaines fonctionnalités liées à l'inscription et à la gestion des comptes candidats.
- Ajout d'index sur les tables de la base de données pour améliorer les performances des requêtes.
- Correction de problèmes de compatibilité avec différents navigateurs.
- Amélioration de la gestion des cookies.
- Suppression de certaines dépendances inutiles.
- Correction de problèmes de performance liés à l'affichage des données.
