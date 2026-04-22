## Changelog : reva (30 derniers jours, au 2026-04-21)

### Résumé
Ce mois-ci, les évolutions de reva se concentrent sur l'amélioration de l'expérience utilisateur, notamment dans la gestion des candidatures FranceConnect, la gestion des jurys et la correction de bugs. Des optimisations de performance ont également été apportées, ainsi que des mises à jour de sécurité et de dépendances.

### Évolutions fonctionnelles
- **FranceConnect :**
    - Amélioration de la gestion des erreurs et des informations lors de la connexion via FranceConnect, notamment en cas de données manquantes ou incohérentes.
    - Possibilité de modifier la ville et le département de naissance pour les candidats connectés via FranceConnect (si le pays n'est pas la France).
    - Ajout d'une fonctionnalité de nettoyage des données FranceConnect en sandbox pour l'administration.
    - Enregistrement de la date de dernière connexion via FranceConnect.
- **Gestion des jurys :**
    - Refonte de l'interface de gestion des résultats de jury, avec affichage des blocs de compétences validés et non validés.
    - Possibilité de sauvegarder les résultats du jury par blocs de compétences.
    - Ajout d'une page dédiée à la gestion de la date de jury.
    - Possibilité de révoquer une décision de jury.
- **Administration :**
    - Ajout d'une page pour gérer les informations générales des organismes certificateurs, incluant la possibilité de modifier le label.
    - Amélioration de l'interface pour la gestion des fichiers de dématérialisation (DFF), avec ajout de la gestion du "complément d'expérience parcours Vise".
- **VAE Collective :**
    - Amélioration de la gestion des jetons de session pour éviter les erreurs liées à la taille des cookies.
- **Candidatures :**
    - Suppression des fonctionnalités liées à l'inscription manuelle et à la demande de mot de passe, privilégiant FranceConnect.
    - Amélioration de l'affichage des informations de contact et de la civilité pour les candidats connectés via FranceConnect.

### Évolutions techniques
- **API :**
    - Optimisation des requêtes GraphQL pour améliorer les performances, notamment lors de la récupération des expériences et des objectifs d'une candidature.
    - Ajout d'index sur les tables de la base de données pour accélérer les requêtes.
    - Suppression de code obsolète.
    - Mise à jour des dépendances (Fastify, Strapi, Brevo).
    - Amélioration de la gestion des erreurs et des logs.
- **Infrastructure :**
    - Mise à jour des dépendances des différents packages.
    - Refactorisation du code pour améliorer la maintenabilité et la lisibilité.
- **Tests :**
    - Ajout de tests unitaires et d'intégration pour valider les nouvelles fonctionnalités et les corrections de bugs.
    - Amélioration de la couverture de tests.
    - Migration de certains tests vers Playwright.

### Autres changements
- Documentation mise à jour.
- Corrections de bugs mineurs et améliorations de l'interface utilisateur.
- Suppression de fonctionnalités obsolètes.
- Amélioration de la sécurité (gestion des jetons, validation des données).
- Uniformisation du style de code.
- Suppression de certains feature flags.
