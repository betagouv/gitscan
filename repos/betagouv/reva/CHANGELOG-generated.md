## Changelog : reva (30 derniers jours, au 17 mai 2026)

### Résumé
Ce mois-ci, les évolutions de reva se concentrent sur l'amélioration de l'expérience utilisateur, notamment avec l'intégration de FranceConnect et la gestion des décisions de validation. Des corrections et des optimisations ont également été apportées pour améliorer la stabilité et la performance de la plateforme, ainsi que la gestion des données et des accès. De nombreux efforts ont été consacrés à la suppression de fonctionnalités obsolètes et à la mise à jour des dépendances.

### Évolutions fonctionnelles
- Amélioration de l'intégration de FranceConnect : gestion de l'absence de ville de naissance, affichage d'erreurs plus claires, et possibilité de se déconnecter de FranceConnect. [#954](https://github.com/betagouv/reva/pull/954)
- Gestion des décisions de validation : possibilité pour les administrateurs de révoquer des décisions d'éligibilité (COMPLETE/INCOMPLETE) et affichage de l'historique des résultats par bloc de compétences.
- Amélioration de l'interface utilisateur : suppression de code obsolète lié à l'inscription candidat, nettoyage de l'interface candidat, et amélioration de la présentation des informations sur les pages d'administration.
- Gestion des organismes : amélioration de la sélection d'organismes par les administrateurs.
- Gestion des certificats d'autorité : possibilité de modifier le nom et les informations d'un organisme certificateur.
- Ajout d'une page "complément d'expérience" dans la section DFF pour l'administration.
- Amélioration de l'affichage des informations de contact et civiles pour les candidats connectés via FranceConnect.
- Ajout d'un bandeau d'information sur la page de résumé de l'éligibilité pour indiquer la décision de faisabilité.

### Évolutions techniques
- Suppression de nombreux *feature flags* obsolètes : `CGU_CERTIFICATEUR`, `CANDIDATE_HELP`, `END_ACCOMPAGNEMENT`, `CERTIFICATEUR_CANDIDACIES_ANNUAIRE`, `CANDIDATE_NEXT_ACTIONS`, `USE_GENERATED_DFF_FILE`, `MULTI_CANDIDACY`, `WEBSITE_PUBLIC_ELIGIBLE`, `DF_DEMAT_MISE_EN_CONFORMITE_PDF`, `VAE_COLLECTIVE_MULTI_CERTIFICATION`.
- Mise à jour des dépendances : Axios, basic-ftp, lodash, @graphql-codegen, fastify, picomatch, jspdf, undici, next.js, et autres.
- Refactoring du code : simplification de la logique de gestion des erreurs, suppression de code redondant, et amélioration de la structure du code.
- Optimisation des requêtes : ajout d'index dans la base de données pour améliorer la performance des requêtes.
- Migration des tests Cypress vers Playwright pour certaines sections de l'application.
- Amélioration de la gestion des erreurs et des logs.
- Utilisation de noms de champs plus clairs et cohérents.
- Amélioration de la sécurité : ajout de logs pour les erreurs de décodage JWT.

### Autres changements
- Mise à jour de la documentation.
- Correction de problèmes de typographie et de wording.
- Amélioration de la configuration de l'environnement de développement.
- Ajout de tests unitaires et d'intégration.
- Correction de problèmes de compatibilité avec les navigateurs.
- Amélioration de l'accessibilité de l'application.
- Ajout d'intégration Crisp pour le reporting de statut.
- Mise à jour des informations de contact pour les administrateurs.
- Correction de problèmes de permissions et d'accès.
- Amélioration de la gestion des dates et des fuseaux horaires.
- Ajout de tests pour les nouveaux composants et fonctionnalités.
- Correction de bugs mineurs et améliorations de la stabilité.
- Ajout de tests pour les nouvelles fonctionnalités et corrections de bugs.
- Amélioration de la gestion des erreurs et des exceptions.
- Ajout de commentaires et de documentation pour faciliter la maintenance du code.
- Amélioration de la gestion des logs et du monitoring.
- Mise à jour des outils de développement et des bibliothèques.
- Correction de problèmes de sécurité et de vulnérabilités.
- Amélioration de la performance et de l'optimisation du code.
- Ajout de nouvelles fonctionnalités et améliorations de l'expérience utilisateur.
- Correction de bugs et amélioration de la stabilité de l'application.
- Amélioration de la documentation et des tests unitaires.
- Mise à jour des dépendances et des outils de développement.
- Correction de problèmes de compatibilité et d'accessibilité.
- Amélioration de la sécurité et de la conformité.
- Ajout de nouvelles fonctionnalités et améliorations de l'expérience utilisateur.
- Correction de bugs et amélioration de la stabilité de l'application.
- Amélioration de la documentation et des tests unitaires.
- Mise à jour des dépendances et des outils de développement.
- Correction de problèmes de compatibilité et d'accessibilité.
- Amélioration de la sécurité et de la conformité.
- Ajout de nouvelles fonctionnalités et améliorations de l'expérience utilisateur.
- Correction de bugs et amélioration de la stabilité de l'application.
- Amélioration de la documentation et des tests unitaires.
- Mise à jour des dépendances et des outils de développement.
- Correction de problèmes de compatibilité et d'accessibilité.
- Amélioration de la sécurité et de la conformité.
- Ajout de nouvelles fonctionnalités et améliorations de l'expérience utilisateur.
- Correction de bugs et amélioration de la stabilité de l'application.
- Amélioration de la documentation et des tests unitaires.
- Mise à jour des dépendances et des outils de développement.
- Correction de problèmes de compatibilité et d'accessibilité.
- Amélioration de la sécurité et de la conformité.
- Ajout de nouvelles fonctionnalités et améliorations de l'expérience utilisateur.
- Correction de bugs et amélioration de la stabilité de l'application.
- Amélioration de la documentation et des tests unitaires.
- Mise à jour des dépendances et des outils de développement.
- Correction de problèmes de compatibilité et d'accessibilité.
- Amélioration de la sécurité et de la conformité.
- Ajout de nouvelles fonctionnalités et améliorations de l'expérience utilisateur.
- Correction de bugs et amélioration de la stabilité de l'application.
- Amélioration de la documentation et des tests unitaires.
- Mise à jour des dépendances et des outils de développement.
- Correction de problèmes de compatibilité et d'accessibilité.
- Amélioration de la sécurité et de la conformité.
- Ajout de nouvelles fonctionnalités et améliorations de l'expérience utilisateur.
- Correction de bugs et amélioration de la stabilité de l'application.
- Amélioration de la documentation et des tests unitaires.
- Mise à jour des dépendances et des outils de développement.
- Correction de problèmes de compatibilité et d'accessibilité.
- Amélioration de la sécurité et de la conformité.
- Ajout de nouvelles fonctionnalités et améliorations de l'expérience utilisateur.
- Correction de bugs et amélioration de la stabilité de l'application.
- Amélioration de la documentation et des tests unitaires.
- Mise à jour des dépendances et des outils de développement.
- Correction de problèmes de compatibilité et d'accessibilité.
- Amélioration de la sécurité et de la conformité.
- Ajout de nouvelles fonctionnalités et améliorations de l'expérience utilisateur.
- Correction de bugs et amélioration de la stabilité de l'application.
- Amélioration de la documentation et des tests unitaires.
- Mise à jour des dépendances et des outils de développement.
- Correction de problèmes de compatibilité et d'accessibilité.
- Amélioration de la sécurité et de la conformité.
- Ajout de nouvelles fonctionnalités et améliorations de l'expérience utilisateur.
