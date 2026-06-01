## Changelog : reva (30 derniers jours, au 29 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur pour les administrateurs et les candidats, notamment avec l'ajout de nouvelles fonctionnalités de gestion des candidatures, d'informations sur les certifications et de sécurité (authentification à deux facteurs). Des optimisations ont également été apportées à l'interface et aux performances de l'application.

### Évolutions fonctionnelles
- Ajout d'une page "Candidatures pour un AAP" avec des filtres pour faciliter la recherche et la gestion des candidatures ([#1034](https://github.com/betagouv/reva/issues/1034)).
- Amélioration de l'affichage des informations sur les certifications, avec l'ajout d'une nouvelle carte "Autorité de certification" dans le résumé de la candidature et un lien direct pour consulter les informations de l'autorité de certification.
- Ajout d'une page dédiée aux comptes collaborateurs AAP, permettant de gérer les accès et les permissions.
- Possibilité pour les administrateurs de confirmer l'abandon d'une candidature par un candidat.
- Ajout de raisons pour l'arrêt de l'accompagnement et de la raison de l'abandon de la candidature.
- Amélioration de l'interface pour la gestion des lieux d'accueil, avec l'ajout d'un bouton de suppression et une confirmation avant suppression.
- Ajout d'une page de détails pour les résultats du jury.
- Ajout d'un badge indiquant si un compte AAP est désactivé.
- Amélioration de l'affichage des informations sur les résultats du jury dans l'interface administrateur.
- Ajout de la possibilité pour les administrateurs de filtrer les candidatures par accompagnement, financement, résultats du jury, statut du dossier et type d'accompagnement.
- Ajout d'une page pour la gestion des collaborateurs AAP.
- Ajout d'un nouveau champ pour la raison de la fin de l'accompagnement.
- Amélioration de l'affichage des informations sur les certifications dans l'interface candidat.
- Ajout d'une fonctionnalité d'authentification à deux facteurs (TOTP) pour les utilisateurs de vae-collective et l'administration.
- Amélioration de la gestion des cookies pour une meilleure sécurité.
- Ajout d'un système de redirection amélioré après l'authentification.
- Amélioration de la gestion des erreurs et des messages d'information.

### Évolutions techniques
- Mise à jour de plusieurs dépendances (Next.js, Strapi, Axios, etc.).
- Refactorisation du code pour améliorer la lisibilité et la maintenabilité.
- Amélioration de la gestion des erreurs et des logs.
- Optimisation des performances de l'application.
- Amélioration de la sécurité de l'application (gestion des cookies, authentification).
- Mise à jour du buildpack Scalingo pour Keycloak.
- Amélioration de la gestion des tokens et des sessions.
- Suppression de code obsolète.
- Amélioration de la gestion des tests.
- Mise en place de nouvelles métriques de monitoring.

### Autres changements
- Amélioration de la documentation.
- Corrections de bugs mineurs.
- Amélioration de la traduction et de la terminologie.
- Mise à jour des configurations.
- Ajout de tests unitaires et d'intégration.
- Amélioration de la gestion des logs.
- Correction de problèmes d'affichage et de mise en page.
- Amélioration de l'accessibilité de l'application.
- Correction de problèmes de compatibilité avec différents navigateurs.
- Amélioration de la gestion des erreurs et des exceptions.
- Ajout de commentaires et de documentation au code.
- Mise à jour des fichiers de configuration.
- Correction de problèmes de sécurité.
- Amélioration de la gestion des dépendances.
- Ajout de nouvelles fonctionnalités de monitoring et de logging.
- Amélioration de la gestion des environnements de développement, de test et de production.
