## Changelog : reva (30 derniers jours, au 28 avril 2026)

### Résumé
Ce mois-ci, les évolutions de reva se concentrent sur l'amélioration de l'authentification avec FranceConnect, la gestion des rôles et des permissions, ainsi que l'ajout de nouvelles fonctionnalités pour l'administration des jurys et la gestion des candidatures. Des corrections et optimisations ont également été apportées pour améliorer la performance et la sécurité de la plateforme.

### Évolutions fonctionnelles
- Intégration améliorée de FranceConnect : simplification du processus de connexion et de gestion des informations utilisateur, notamment pour la gestion des lieux de naissance. [#9233d20](https://github.com/betagouv/reva/issues/9233d20)
- Gestion des rôles et permissions : ajout de pages d'administration pour la gestion des accès et des rôles des utilisateurs.
- Gestion des jurys :
    - Ajout de la possibilité de visualiser et de gérer les résultats des jurys par blocs de compétences. [#851b337](https://github.com/betagouv/reva/issues/851b337)
    - Amélioration de l'interface de saisie des résultats de jury, avec une meilleure gestion des validations et des incohérences.
    - Ajout d'une page dédiée à la planification des dates de jury.
- Amélioration de l'expérience utilisateur :
    - Ajout de titres et de slogans de service dans les en-têtes des différentes applications (candidat, collectif, admin). [#f724232](https://github.com/betagouv/reva/issues/f724232)
    - Amélioration de la gestion des erreurs d'authentification avec des messages plus clairs et des liens d'aide.
- Ajout d'une page pour la gestion des comptes FranceConnect en sandbox.
- Possibilité de supprimer une candidature (en mode projet). [#1d1c02e](https://github.com/betagouv/reva/issues/1d1c02e)

### Évolutions techniques
- Refonte de l'authentification : refactorisation du code d'authentification avec Keycloak, amélioration de la sécurité et de la gestion des tokens.
- Amélioration des performances : optimisation des requêtes SQL et ajout d'index pour accélérer l'accès aux données.
- Mise à jour des dépendances : mise à jour de nombreuses dépendances pour bénéficier des dernières corrections de sécurité et améliorations de performance.
- Refactorisation du code : amélioration de la structure du code et suppression de code obsolète.
- Amélioration des tests : ajout de nouveaux tests unitaires et d'intégration pour garantir la qualité du code.
- Utilisation de feature flags pour activer/désactiver de nouvelles fonctionnalités de manière progressive.
- Suppression de code lié à des fonctionnalités obsolètes (inscription candidat, etc.).
- Amélioration de la gestion des erreurs et des logs.

### Autres changements
- Mise à jour de la documentation.
- Corrections de bugs mineurs et améliorations de l'interface utilisateur.
- Suppression de tables inutilisées dans la base de données. [#67872a3](https://github.com/betagouv/reva/issues/67872a3)
- Ajustements de la configuration pour améliorer la sécurité et la performance.
- Amélioration de la gestion des cookies.
- Correction de problèmes de compatibilité avec différentes versions de navigateurs.
