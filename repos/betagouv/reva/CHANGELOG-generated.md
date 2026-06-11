## Changelog : reva (30 derniers jours, au 10 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur et de la gestion des candidatures, notamment au niveau de l'administration et de l'intégration FranceConnect. Des améliorations de sécurité ont également été apportées, avec l'introduction de l'authentification à deux facteurs (TOTP) et la sécurisation des cookies. Plusieurs corrections de bugs et optimisations ont été réalisées pour améliorer la stabilité et la performance de la plateforme.

### Évolutions fonctionnelles
- **Gestion des candidatures :**
    - Ajout de filtres pour les candidatures (accompagnement, archive, financement, jury, etc.) dans l'interface d'administration. [#1037](https://github.com/betagouv/reva/pull/1037)
    - Amélioration de la page de résumé des candidatures avec l'ajout d'une carte pour l'organisme certificateur et un lien vers sa page de détails.
    - Possibilité pour les administrateurs de créer des comptes collaborateurs pour les AAP directement depuis la liste des AAP.
    - Ajout d'un nouveau motif de fin d'accompagnement.
    - Amélioration de l'affichage des informations sur les résultats du jury.
    - Ajout d'une page de détails pour les organismes certificateurs.
- **FranceConnect :**
    - Amélioration de la gestion des comptes FranceConnect existants.
    - Correction de la gestion des codes pays lors de l'utilisation de FranceConnect.
- **Authentification :**
    - Implémentation de l'authentification à deux facteurs (TOTP) pour les utilisateurs.
    - Amélioration de la sécurité des cookies de session.
    - Possibilité d'activer/désactiver le tableau de bord AAP par utilisateur.
- **Interface utilisateur :**
    - Amélioration de l'interface de la page de gestion des lieux d'accueil (ajout d'un bouton de suppression, confirmation de suppression).
    - Amélioration de l'affichage des informations sur les cohortes VAE.
    - Correction de bugs d'affichage et de navigation dans l'interface d'administration.
- **Interopérabilité :**
    - Ajout de la possibilité d'ajouter un fichier de déclaration sur l'honneur à la réponse de création de décision de recevabilité PDF.

### Évolutions techniques
- **Keycloak :**
    - Mise à jour de la configuration de Keycloak pour activer les fonctionnalités token-exchange:v1 et admin-fine-grained-authz:v1.
    - Optimisation de la configuration de Keycloak pour l'authentification à deux facteurs.
- **Infrastructure :**
    - Mise à jour des dépendances (axios, @strapi/strapi, react-router, react-router-dom, tmp, ip-address, protobufjs/utf8).
    - Amélioration de la gestion des secrets et des variables d'environnement.
    - Amélioration de la gestion des logs.
- **Code :**
    - Refactorisation du code pour améliorer la lisibilité et la maintenabilité.
    - Optimisation des requêtes en base de données.
    - Ajout de tests unitaires et d'intégration.
    - Migration de tests Cypress vers Playwright.
    - Suppression de code obsolète.
- **CI/CD :**
    - Amélioration du pipeline CI/CD.

### Autres changements
- Mise à jour de la documentation.
- Correction de problèmes de typage.
- Amélioration des messages d'erreur.
- Correction de bugs mineurs.
- Ajout de scripts pour l'anonymisation des bases de données.
- Amélioration de la gestion des erreurs FranceConnect.
- Correction de la gestion des domaines Formacode.
- Amélioration de la gestion des filtres dans l'API.
- Correction de la gestion des codes INSEE des pays.
- Amélioration de la gestion des URL de redirection.
- Correction de problèmes de performance.
- Mise à jour de Next.js dans certains packages.
