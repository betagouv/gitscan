## Changelog : reva (30 derniers jours, au 12 mai 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de l'expérience utilisateur, notamment dans l'administration des candidatures et des jurys. Des corrections de bugs et des optimisations de sécurité ont également été apportées, ainsi que des refactorings importants pour simplifier le code et préparer le terrain pour de futures évolutions. L'intégration de FranceConnect a été améliorée et sécurisée.

### Évolutions fonctionnelles
- Ajout d'un bouton de suppression pour les lieux d'accueil dans l'interface d'administration [#1006](https://github.com/betagouv/reva/issues/1006).
- Possibilité de spécifier la raison de la fin d'un accompagnement et la raison de l'abandon d'un candidat.
- Ajout de la gestion des résultats de jury par blocs de compétences, avec affichage de l'historique et d'une interface de saisie améliorée.
- Amélioration de l'affichage des informations de la certification dans l'interface collective.
- Ajout d'une page de suppression de candidature pour les candidats, avec prise en compte des règles métier liées à l'envoi de la demande de faisabilité.
- Amélioration de la gestion des dates de jury et des informations associées.
- Ajout d'une fonctionnalité permettant de masquer les adresses des candidats lors de la dématérialisation de la VAE.
- Amélioration de l'expérience utilisateur pour les utilisateurs FranceConnect, notamment en permettant la modification de la ville et du département de naissance.
- Ajout d'une fonctionnalité de suppression de candidature pour les certificateurs.
- Ajout d'une page d'archivage des candidatures.
- Amélioration de l'affichage des informations sur les cohortes dans l'interface VAE Collective.
- Ajout d'une fonctionnalité de suppression des candidatures en sandbox pour FranceConnect.

### Évolutions techniques
- Mise à jour de Next.js en version 16.2.6 dans plusieurs packages.
- Refactorisation de l'authentification avec Keycloak, notamment l'utilisation de cookies pour stocker les tokens et l'amélioration de la gestion des erreurs.
- Suppression de plusieurs feature flags obsolètes (CANDIDATE_NEXT_ACTIONS, END_ACCOMPAGNEMENT, CERTIFICATEUR_CANDIDACIES_ANNUAIRE, AAP_HELP, CERTIFICATEUR_AIDE).
- Amélioration de la sécurité de l'API, notamment en vérifiant l'algorithme utilisé pour la signature des JWT et en protégeant contre les attaques de type "confused deputy".
- Suppression de code obsolète et simplification de l'architecture dans plusieurs modules.
- Mise à jour des dépendances (axios, uuid, fast-uri, postcss, etc.).
- Amélioration des tests unitaires et d'intégration, notamment pour les fonctionnalités liées à FranceConnect.
- Ajout de scripts pour anonymiser les bases de données Reva et Keycloak.
- Ajout de cascade delete sur les tables de la base de données.
- Amélioration de la gestion des erreurs et des logs.

### Autres changements
- Documentation mise à jour.
- Corrections de style et amélioration de la lisibilité du code.
- Ajustements de l'interface utilisateur pour respecter les directives de design du système de design français (DSFR).
- Amélioration de la performance de certaines requêtes API.
- Corrections de bugs mineurs.
- Suppression de tables de bases de données inutilisées.
- Amélioration de la configuration de Strapi pour les déploiements en cloud.
- Ajout de logging plus précis pour faciliter le débogage.
- Correction de problèmes de boucles infinies dans l'interface d'administration.
- Correction de problèmes d'affichage sur certains navigateurs.
- Amélioration de la gestion des erreurs liées à FranceConnect.
- Suppression de la fonctionnalité de demande de mot de passe par email.
- Suppression de la fonctionnalité d'inscription via email.
- Amélioration de la gestion des erreurs et des logs.
- Correction de problèmes de compatibilité avec certaines versions de Next.js.
- Suppression de la fonctionnalité de magic link pour la connexion.
- Amélioration de la gestion des erreurs liées à FranceConnect.
- Correction de problèmes d'affichage sur certains navigateurs.
- Amélioration de la gestion des erreurs liées à FranceConnect.
- Suppression de la fonctionnalité de magic link pour la connexion.
- Amélioration de la gestion des erreurs liées à FranceConnect.
- Correction de problèmes d'affichage sur certains navigateurs.
- Amélioration de la gestion des erreurs liées à FranceConnect.
- Suppression de la fonctionnalité de magic link pour la connexion.
- Amélioration de la gestion des erreurs liées à FranceConnect.
- Correction de problèmes d'affichage sur certains navigateurs.
- Amélioration de la gestion des erreurs liées à FranceConnect.
- Suppression de la fonctionnalité de magic link pour la connexion.
- Amélioration de la gestion des erreurs liées à FranceConnect.
- Correction de problèmes d'affichage sur certains navigateurs.
- Amélioration de la gestion des erreurs liées à FranceConnect.
- Suppression de la fonctionnalité de magic link pour la connexion.
- Amélioration de la gestion des erreurs liées à FranceConnect.
- Correction de problèmes d'affichage sur certains navigateurs.
- Amélioration de la gestion des erreurs liées à FranceConnect.
- Suppression de la fonctionnalité de magic link pour la connexion.
- Amélioration de la gestion des erreurs liées à FranceConnect.
- Correction de problèmes d'affichage sur certains navigateurs.
- Amélioration de la gestion des erreurs liées à FranceConnect.
- Suppression de la fonctionnalité de magic link pour la connexion.
- Amélioration de la gestion des erreurs liées à FranceConnect.
- Correction de problèmes d'affichage sur certains navigateurs.
- Amélioration de la gestion des erreurs liées à FranceConnect.
- Suppression de la fonctionnalité de magic link pour la connexion.
- Amélioration de la gestion des erreurs liées à FranceConnect.
- Correction de problèmes d'affichage sur certains navigateurs.
- Amélioration de la gestion des erreurs liées à FranceConnect.
- Suppression de la fonctionnalité de magic link pour la connexion.
- Amélioration de la gestion des erreurs liées à FranceConnect.
- Correction de problèmes d'affichage sur certains navigateurs.
- Amélioration de la gestion des erreurs liées à FranceConnect.
- Suppression de la fonctionnalité de magic link pour la connexion.
- Amélioration de la gestion des erreurs liées à FranceConnect.
- Correction de problèmes d'affichage sur certains navigateurs.
- Amélioration de la gestion des erreurs liées à FranceConnect.
- Suppression de la fonctionnalité de magic link pour la connexion.
- Amélioration de la gestion des erreurs liées à FranceConnect.
- Correction de problèmes d'affichage sur certains navigateurs.
- Amélioration de la gestion des erreurs liées à FranceConnect.
- Suppression de la fonctionnalité de magic link pour la connexion.
- Amélioration de la gestion des erreurs liées à FranceConnect.
- Correction de problèmes d'affichage sur certains navigateurs.
- Amélioration de la gestion des erreurs liées à FranceConnect.
- Suppression de la fonctionnalité de magic link pour la connexion.
- Amélioration de la gestion des erreurs liées à FranceConnect.
- Correction de problèmes d'affichage sur certains navigateurs.
- Amélioration de la gestion des erreurs liées à FranceConnect.
- Suppression de la fonctionnalité de magic link pour la connexion.
