## Changelog : reva (30 derniers jours, au 05 juin 2026)

### Résumé
Ce mois-ci, les évolutions de reva se concentrent sur l'amélioration de l'expérience utilisateur dans l'administration des candidatures VAE, notamment avec l'ajout de nouvelles informations et filtres pour les administrateurs, ainsi que sur la sécurité avec l'implémentation de l'authentification à deux facteurs. Des corrections et optimisations ont également été apportées pour améliorer la stabilité et la performance de la plateforme.

### Évolutions fonctionnelles
- Ajout d'une page de détails de l'organisme de certification, accessible depuis le résumé de la candidature [#1234](https://github.com/betagouv/reva/issues/1234).
- Implémentation de filtres pour les candidatures par accompagnement (VAE collective), financement, résultats du jury, statut de faisabilité, et archive.
- Amélioration de la page de résumé des candidatures pour les AAP, avec l'ajout d'un indicateur pour les comptes AAP désactivés.
- Ajout d'une nouvelle page pour lister les comptes collaborateurs AAP.
- Ajout d'une page pour gérer les dates de jury et les résultats par blocs pour les AAP.
- Amélioration de l'affichage des informations sur les organismes de formation.
- Ajout d'un champ pour la raison de fin d'accompagnement.
- Correction de l'affichage des images de pièces justificatives pour préserver les proportions.
- Amélioration de la gestion des codes pays INSEE, notamment pour la Corée.
- Ajout d'un avertissement lors de la suppression d'un lieu d'accueil ayant des candidatures associées.
- Ajout d'une page de détails pour les informations de contact de l'organisme de certification.
- Ajout d'un badge indiquant si les résultats du jury sont définis par l'organisme de certification.
- Amélioration de la gestion des statuts de candidature dans l'API.
- Ajout de la possibilité de confirmer automatiquement l'abandon d'une candidature par un administrateur.
- Amélioration de la navigation sur les pages de filtres AAP et organisme certificateur.
- Ajout d'une nouvelle bannière pour les résultats du jury par blocs.

### Évolutions techniques
- Mise à jour de Keycloak pour activer les fonctionnalités `token-exchange:v1` et `admin-fine-grained-authz:v1`.
- Refactorisation du code pour améliorer la gestion des cookies et de l'authentification, notamment avec l'implémentation de l'authentification à deux facteurs (TOTP).
- Migration de certains tests Cypress vers Playwright pour améliorer la performance et la fiabilité des tests.
- Amélioration de la gestion des erreurs et des exceptions dans l'API.
- Mise à jour des dépendances (axios, @strapi/strapi, react-router, react-router-dom, uuid, cypress, brace-expansion, fast-uri, basic-ftp, next).
- Optimisation des requêtes Prisma pour améliorer les performances.
- Amélioration de la gestion des erreurs FranceConnect.
- Ajout de scripts pour anonymiser les bases de données reva et Keycloak.
- Mise à jour de Next.js dans les différents packages.
- Amélioration de la gestion des jetons d'authentification pour éviter les boucles de rafraîchissement.

### Autres changements
- Amélioration de la documentation et des commentaires dans le code.
- Correction de bugs mineurs et amélioration de la qualité du code.
- Mise à jour de la configuration de Traefik.
- Amélioration de la gestion des logs.
- Correction de problèmes de typage.
- Amélioration de la gestion des erreurs dans l'API.
- Correction de la gestion des domaines Formacode.
- Amélioration de la gestion des emails d'activation de Keycloak.
- Correction de problèmes de rendu et d'affichage dans l'interface utilisateur.
- Correction de problèmes de compatibilité avec les navigateurs.
- Amélioration de la gestion des erreurs dans l'API.
- Ajout de tests unitaires et d'intégration pour les nouvelles fonctionnalités.
- Correction de problèmes de performance.
- Amélioration de la sécurité de l'application.
