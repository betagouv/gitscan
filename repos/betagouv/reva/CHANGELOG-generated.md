## Changelog : reva (30 derniers jours, au 26 juin 2026)

### Résumé
Ce mois-ci, les évolutions de reva se concentrent sur l'amélioration de l'administration des candidatures VAE, notamment avec l'ajout de fonctionnalités de gestion des organismes certificateurs et des cohortes VAE collectives. Des améliorations significatives ont également été apportées à l'interface utilisateur de l'application admin pour faciliter la navigation et la gestion des données. Des corrections et optimisations ont été apportées à l'API, notamment en matière de sécurité et de gestion des fichiers.

### Évolutions fonctionnelles
- Ajout d'une page de sélection d'un organisme certificateur dans l'administration. [#1037](https://github.com/betagouv/reva)
- Amélioration de l'interface utilisateur des pages "expériences du candidat", "pièces jointes", "prérequis" et "compétences" dans l'administration.
- Ajout d'une page de détails de l'organisme certificateur accessible depuis le résumé de la candidature.
- Ajout d'un lien "Consulter" sur la carte de l'organisme certificateur dans le résumé de la candidature.
- Amélioration de la gestion des filtres de statut des candidatures pour les AAP (Accompagnement à la VAE).
- Possibilité de filtrer les candidatures par organisme certificateur et par cohortes VAE collectives.
- Ajout de la possibilité de créer un compte collaborateur pour un AAP directement depuis la liste des AAP.
- Amélioration de l'affichage des organismes certificateurs dans le résumé de la candidature.
- Ajout de la possibilité de signaler un DVA (Décision de Validation des Acquis) comme invalide depuis l'interop.
- Amélioration de l'affichage de l'historique des décisions pour la dématérialisation.
- Suppression de la limite de 100 heures pour la formation complémentaire.
- Ajout de la possibilité d'enregistrer un mot de passe pour les candidats (fonctionnalité gérée par un flag).
- Suppression de la notification de migration du lien magique.
- Amélioration de l'interface utilisateur de la page de profil du candidat.
- Amélioration de l'interface utilisateur de la page d'éligibilité.

### Évolutions techniques
- Mise à jour de plusieurs dépendances (Fastify, Next.js, GraphQL, Prisma, React, Keycloak, Outscale, Traefik, Vitest, Cypress, Playwright, Datadog, Metabase, Strapi, URQL, graphql-request).
- Refactorisation de la logique de détection des feature flags pour les tableaux de bord AAP.
- Simplification de la logique de vérification de l'accès aux données.
- Ajout d'une vue PostgreSQL pour récupérer les AAP avec ou sans candidatures VAECo.
- Amélioration de la gestion des sessions SSO.
- Correction du temps de vie des cookies OTP (One-Time Password).
- Correction du TTL (Time To Live) des tokens de challenge OTP.
- Ajout d'un antivirus (ClamAV) pour analyser les fichiers téléchargés par les utilisateurs.
- Amélioration de la gestion des erreurs et des logs.
- Ajout de tests unitaires et d'intégration.
- Migration de certains tests Cypress vers Playwright.
- Correction de plusieurs bugs et améliorations de la performance.
- Amélioration de la gestion des images dans l'application candidat.
- Mise à jour des packages Strapi.

### Autres changements
- Ajout d'un lien vers le nouveau formulaire de pré-qualification sur le site web.
- Correction de la cartographie du code INSEE pour la Corée.
- Amélioration de la documentation.
- Nettoyage du code.
- Ajout de commentaires et de documentation pour faciliter la maintenance.
- Correction de la gestion des codes de pays pour les lieux de naissance.
- Ajout de tests pour la vérification de l'OTP par email.
- Ajout d'un flag pour activer la vérification par email OTP.
- Ajout d'une table `account_email_otp` pour stocker les codes OTP par email.
- Ajout d'une tâche cron pour supprimer les OTP expirés.
- Amélioration de la gestion des erreurs lors de l'utilisation de l'API.
- Correction de bugs mineurs dans l'interface utilisateur.
- Ajout de la possibilité de définir un lien externe supplémentaire sur la page de statut.
- Correction de l'affichage des noms de cohortes trop longs dans l'administration.
- Amélioration de la gestion des filtres dans l'administration.
