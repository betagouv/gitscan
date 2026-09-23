## Changelog : sites-conformes (30 derniers jours, au 22 septembre 2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur le renforcement de la sécurité, notamment via le déploiement de l'authentification à deux facteurs (2FA), et sur l'amélioration de l'expérience de recherche. La navigation a été simplifiée et la documentation a bénéficié d'une restructuration majeure pour être plus claire et centralisée.

### Évolutions fonctionnelles
- **Sécurité** : Mise en place et amélioration de l'authentification à deux facteurs (2FA) [#516](https://github.com/numerique-gouv/sites-conformes/pull/516) [#592](https://github.com/numerique-gouv/sites-conformes/pull/592), incluant l'ajout de notifications dans l'interface d'administration pour inciter les utilisateurs à l'activer.
- **Recherche** : Amélioration de la pertinence des résultats grâce à l'indexation de la section "Hero" et ajout de nouveaux mécanismes pour personnaliser les résultats de recherche [#561](https://github.com/numerique-gouv/sites-conformes/pull/561).
- **Navigation et Interface** :
    - Mise en avant de la FAQ dans la navigation principale.
    - Correction d'un bug sur les filtres des pages de catalogue [#578](https://github.com/numerique-gouv/sites-conformes/pull/578).
    - Possibilité de personnaliser le texte des boutons et les liens de redirection dans les blocs "Articles récents" (Blog/Événements) [#542](https://github.com/numerique-gouv/sites-conformes/pull/542).
    - Ajustements cosmétiques sur les formulaires et les textes.

### Évolutions techniques
- **Sécurité et CI/CD** :
    - Renforcement de la sécurité de la chaîne de production (CI) avec l'ajout de contrôles automatiques de vulnérabilités (CVE) et de détection de malwares.
    - Durcissement des droits d'accès pour les processus de CI [#584](https://github.com/numerique-gouv/sites-conformes/pull/584).
    - Intégration de nouveaux outils d'analyse de code et de dépendances (Bandit [#583](https://github.com/numerique-gouv/sites-conformes/pull/583) et deptry [#582](https://github.com/numerique-gouv/sites-conformes/pull/582)).
    - Mise en place d'une période de latence (*cooldown*) pour la mise à jour des dépendances Python et NPM [#588](https://github.com/numerique-gouv/sites-conformes/pull/588).
- **Tests et Performance** :
    - Optimisation de la vitesse d'exécution des tests [#574](https://github.com/numerique-gouv/sites-conformes/pull/574).
    - Amélioration de la couverture de tests, notamment sur les filtres d'URL [#546](https://github.com/numerique-gouv/sites-conformes/pull/546).

### Autres changements
- **Documentation** : Réorganisation complète et centralisation de la documentation technique via l'outil Sphinx [#558](https://github.com/numerique-gouv/sites-conformes/pull/558).
