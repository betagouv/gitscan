## Changelog : csplab (30 derniers jours, au 17 juillet 2026)

### Résumé
Ce mois-ci, les évolutions de csplab se concentrent sur l'amélioration de l'interface utilisateur pour les recruteurs, notamment avec l'ajout de fonctionnalités de gestion des recrutements et des organismes. Des améliorations ont également été apportées à l'ingestion des offres d'emploi et à l'infrastructure du projet.

### Évolutions fonctionnelles
- **Recrutement :**
    - Ajout d'une interface pour la gestion des recrutements ("Mes recrutements") avec des fonctionnalités de recherche et de filtrage [#946](https://github.com/betagouv/csplab/issues/946).
    - Implémentation des étapes de recrutement et de la gestion des organismes [#819](https://github.com/betagouv/csplab/issues/819), [#835](https://github.com/betagouv/csplab/issues/835).
    - Ajout d'un kanban et d'un switch de vue liste pour la gestion des recrutements [#947](https://github.com/betagouv/csplab/issues/947).
    - Intégration du pipeline de recrutement avec des étapes guidées pour l'utilisateur [#915](https://github.com/betagouv/csplab/issues/915).
- **Ingestion des offres :**
    - Transmission des coordonnées GPS des offres vers l'API web [#969](https://github.com/betagouv/csplab/issues/969).
    - Ajout des champs `fin_candidature` et `debut_vacance_poste` aux données des offres importées [#970](https://github.com/betagouv/csplab/issues/970).
    - Amélioration de la configuration des identifiants TalentSoft pour une plus grande flexibilité [#892](https://github.com/betagouv/csplab/issues/892).
- **Autres :**
    - Ajout d'une page pour afficher les détails d'une offre [#898](https://github.com/betagouv/csplab/issues/898).
    - Ajout de notifications (toasts) pour améliorer l'expérience utilisateur [#815](https://github.com/betagouv/csplab/issues/815).

### Évolutions techniques
- **Infrastructure :**
    - Refactorisation du queryset avec des mappers pour améliorer la performance [#976](https://github.com/betagouv/csplab/issues/976).
    - Amélioration de la gestion des review apps pour faciliter les tests et les déploiements [#975](https://github.com/betagouv/csplab/issues/975).
    - Mise en place de sauvegardes régulières de la base de données sur Scaleway [#833](https://github.com/betagouv/csplab/issues/833).
    - Ajout de releases Sentry lors des déploiements pour une meilleure traçabilité des erreurs [#850](https://github.com/betagouv/csplab/issues/850).
- **Architecture :**
    - Séparation de l'interface d'offre en deux parties : base et ingestion [#887](https://github.com/betagouv/csplab/issues/887).
    - Refactorisation de l'architecture pour améliorer la lisibilité et la maintenabilité du code.
- **Divers :**
    - Mise à jour des dépendances de plusieurs modules (web, ocr, ingestion) [#951](https://github.com/betagouv/csplab/issues/951), [#950](https://github.com/betagouv/csplab/issues/950), [#952](https://github.com/betagouv/csplab/issues/952).
    - Amélioration de la gestion des erreurs et ajout de logs plus précis.

### Autres changements
- Ajout d'une documentation pour l'API web [#820](https://github.com/betagouv/csplab/issues/820).
- Ajout d'un script pour faciliter la mise à jour des dépendances [#832](https://github.com/betagouv/csplab/issues/832).
- Amélioration de la documentation interne et des commentaires dans le code.
- Ajout de tests unitaires pour améliorer la couverture du code.
- Correction de bugs mineurs et améliorations de la qualité du code.
- Ajout d'un modèle admin pour les snapshots de statistiques [#894](https://github.com/betagouv/csplab/issues/894).
- Ajout d'un composant pour séparer les appels CSP [#956](https://github.com/betagouv/csplab/issues/956).
- Ajout d'un composant pour afficher des messages d'alerte (CspCallout) [#910](https://github.com/betagouv/csplab/issues/910).
- Amélioration de la lisibilité des tests avec l'utilisation du décorateur `@patch` [#849](https://github.com/betagouv/csplab/issues/849).
- Traduction des messages d'erreur de domaine en français [#807](https://github.com/betagouv/csplab/issues/807).
