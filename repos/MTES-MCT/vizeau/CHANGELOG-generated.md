## Changelog : vizeau (30 derniers jours, au 27 août 2026)

### Résumé
Ce mois a été marqué par une modernisation importante de l'infrastructure technique et une amélioration de l'expérience utilisateur. Les utilisateurs bénéficient désormais de nouvelles capacités d'exportation de données (calendrier, projets) et d'une interface plus stable et accueillante. En coulisses, la migration vers Inertia 3 et la refonte de la gestion cartographique assurent une base plus performante et évolutive pour la plateforme.

### Évolutions fonctionnelles
- **Nouvelles capacités d'exportation** :
    - Export des tâches au format calendrier (ICS) [#494](https://github.com/MTES-MCT/vizeau/pull/494).
    - Export des données liées aux projets [#495](https://github.com/MTES-MCT/vizeau/pull/495).
    - Export des entrées de journal pour une meilleure gestion du calendrier.
- **Amélioration de l'interface et de l'expérience utilisateur** :
    - Refonte de la page d'accueil et ajout d'une page de bienvenue [#482](https://github.com/MTES-MCT/vizeau/pull/482).
    - Amélioration de la page publique.
    - Mise en place de projets partagés [#481](https://github.com/MTES-MCT/vizeau/pull/481).
    - Correction de fautes de frappe dans les descriptions des Aires d’Alimentation de Captage (AAC).
- **Stabilité** :
    - Amélioration de la gestion des erreurs : les plantages lors de l'affichage de la carte ne bloquent plus l'utilisation du reste de l'application.

### Évolutions techniques
- **Modernisation du framework** : Migration vers Inertia 3 pour améliorer la réactivité de l'application [#491](https://github.com/MTES-MCT/vizeau/pull/491).
- **Optimisation cartographique et SIG** :
    - Refonte de la gestion des fichiers PMTiles pour une meilleure performance [#498](https://github.com/MTES-MCT/vizeau/pull/498).
    - Refactorisation des effets de réconciliation sur la carte principale [#487](https://github.com/MTES-MCT/vizeau/pull/487).
- **Refactorisation du backend et des services** :
    - Simplification et optimisation du service AAC, incluant l'externalisation de la gestion DuckDB [#488](https://github.com/MTES-MCT/vizeau/pull/488).
    - Optimisation de l'API du réconciliateur et de ses mécanismes de synchronisation.
- **Architecture Frontend** :
    - Refonte de la structure de navigation du header et amélioration de la gestion du contexte sur les pages territoires/AAC et exploitations [#493](https://github.com/MTES-MCT/vizeau/pull/493).
    - Mise à jour et nettoyage des composants UI (`SectionCard`, `CheckboxCard`).

### Autres changements
- **Gestion du projet** : Déplacement du générateur de PMTiles dans un dépôt dédié.
- **Configuration et CI/CD** :
    - Mise à jour de la compatibilité `package-lock.json` pour Node 24.
    - Ajout de l'étape de linting (`npm run lint`) au hook de pre-commit pour garantir la qualité du code.
