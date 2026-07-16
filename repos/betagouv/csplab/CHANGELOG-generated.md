## Changelog : csplab (30 derniers jours, au 15 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'ingestion des offres d'emploi, le développement de l'interface "Mes Recrutements" et l'ajout de fonctionnalités pour le module recruteur. Des optimisations techniques et des corrections de bugs ont également été apportées pour améliorer la stabilité et la performance de la plateforme.

### Évolutions fonctionnelles
- **Ingestion des offres :**
    - Prise en charge de la configuration dynamique des identifiants Talentsoft [#892](https://github.com/betagouv/csplab/issues/892).
    - Ajout de la gestion des offres archivées de Talentsoft [#868](https://github.com/betagouv/csplab/issues/868).
    - Amélioration de la gestion des erreurs et des retries lors de la récupération des offres [#873](https://github.com/betagouv/csplab/issues/873).
    - Enrichissement des offres avec de nouveaux champs provenant de Talentsoft [#794](https://github.com/betagouv/csplab/issues/794).
    - Mapping du type de contrat depuis Talentsoft [#968](https://github.com/betagouv/csplab/issues/968).
- **"Mes Recrutements" :**
    - Développement de l'interface "Mes Recrutements" avec pagination, filtres et affichage des offres [#897](https://github.com/betagouv/csplab/issues/897), [#898](https://github.com/betagouv/csplab/issues/898), [#899](https://github.com/betagouv/csplab/issues/900), [#946](https://github.com/betagouv/csplab/issues/946).
    - Ajout de la fonctionnalité de recherche d'offres dans "Mes Recrutements" [#900](https://github.com/betagouv/csplab/issues/900).
- **Module Recruteur :**
    - Implémentation des étapes de recrutement et de leur gestion [#819](https://github.com/betagouv/csplab/issues/819), [#835](https://github.com/betagouv/csplab/issues/835), [#882](https://github.com/betagouv/csplab/issues/882), [#883](https://github.com/betagouv/csplab/issues/883), [#886](https://github.com/betagouv/csplab/issues/886).
    - Ajout de la gestion des notes associées aux recrutements [#878](https://github.com/betagouv/csplab/issues/878), [#879](https://github.com/betagouv/csplab/issues/879).
    - Création de l'interface pour la gestion des détails de recrutement [#856](https://github.com/betagouv/csplab/issues/856).
- **Autres améliorations UI/UX :**
    - Ajout d'un composant de séparation de CSP [#956](https://github.com/betagouv/csplab/issues/956).
    - Ajout de composants d'interface utilisateur génériques (table, pagination, tabs, breadcrumb) pour faciliter le développement futur [#790](https://github.com/betagouv/csplab/issues/790), [#812](https://github.com/betagouv/csplab/issues/812), [#817](https://github.com/betagouv/csplab/issues/817), [#852](https://github.com/betagouv/csplab/issues/852).
    - Ajout de notifications Toast [#815](https://github.com/betagouv/csplab/issues/815).
    - Ajout d'un guide utilisateur pour les étapes du processus de recrutement [#915](https://github.com/betagouv/csplab/issues/915).

### Évolutions techniques
- **Architecture & Infrastructure :**
    - Séparation de l'interface utilisateur et du backend pour une meilleure maintenabilité [#944](https://github.com/betagouv/csplab/issues/944).
    - Utilisation de Celery pour le traitement asynchrone des webhooks [#737](https://github.com/betagouv/csplab/issues/737).
    - Amélioration de la configuration et du déploiement avec Scalingo (sauvegarde de la base de données, gestion des secrets) [#833](https://github.com/betagouv/csplab/issues/833).
    - Ajout de releases Sentry pour faciliter le suivi des erreurs en production [#850](https://github.com/betagouv/csplab/issues/850).
- **Base de données :**
    - Ajout d'index pour améliorer les performances des requêtes [#786](https://github.com/betagouv/csplab/issues/786), [#789](https://github.com/betagouv/csplab/issues/789).
    - Mise à jour des modèles de données pour le module recruteur [#943](https://github.com/betagouv/csplab/issues/943).
- **Tests & CI/CD :**
    - Amélioration des tests et de la couverture de code.
    - Automatisation de la création de releases et de la mise à jour du changelog [#799](https://github.com/betagouv/csplab/issues/799).
    - Amélioration de la configuration de Storybook et de ses workflows de déploiement [#871](https://github.com/betagouv/csplab/issues/871), [#872](https://github.com/betagouv/csplab/issues/872).

### Autres changements
- Documentation de l'API et des modèles de données [#804](https://github.com/betagouv/csplab/issues/804), [#863](https://github.com/betagouv/csplab/issues/863).
- Refactoring et nettoyage du code pour améliorer la lisibilité et la maintenabilité.
- Mise à jour des dépendances (hors mises à jour automatiques) [#950](https://github.com/betagouv/csplab/issues/950), [#951](https://github.com/betagouv/csplab/issues/951).
- Ajout d'une ADR concernant la localisation du read model [#958](https://github.com/betagouv/csplab/issues/958).
- Ajout d'un script pour faciliter la mise à jour des dépendances [#954](https://github.com/betagouv/csplab/issues/954).
