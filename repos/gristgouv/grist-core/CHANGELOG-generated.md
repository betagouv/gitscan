## Changelog : grist-core (30 derniers jours, au 2026-05-22)

### Résumé
Les dernières semaines ont été marquées par des améliorations de la stabilité et de la correction de tests automatisés, ainsi que par des avancées significatives dans l'importation de données depuis Airtable et la gestion des automatisations. Des améliorations d'accessibilité ont également été apportées aux formulaires, et des traductions ont été mises à jour.

### Évolutions fonctionnelles
- **Import Airtable :** Amélioration de l'importation depuis Airtable avec la prise en charge des couleurs des choix et la mise à jour des lignes existantes. [#2199](https://github.com/gristgouv/grist-core/issues/2199), [#2216](https://github.com/gristgouv/grist-core/issues/2216)
- **Automatisation :** Nouvelle interface utilisateur pour les déclencheurs de documents dans la version SaaS.
- **Formulaires :** Amélioration de l'accessibilité des champs "select" pour les lecteurs d'écran. [#2164](https://github.com/gristgouv/grist-core/issues/2164)
- **Abonnements (SaaS) :** Ajout de bannières d'abonnement et passage en mode lecture seule en cas de problème avec l'abonnement.
- **Page de configuration :** Ajout d'une page de configuration initiale.
- **Connexion :** Ajout d'une connexion via clé de démarrage.

### Évolutions techniques
- **Tests :** Correction de plusieurs tests automatisés instables (DocTutorial, PageWidgetPicker, AccessRules2, Search2, GranularAccess, UserManager). [#2244](https://github.com/gristgouv/grist-core/issues/2244), [#2247](https://github.com/gristgouv/grist-core/issues/2247), [#2248](https://github.com/gristgouv/grist-core/issues/2248), [#2232](https://github.com/gristgouv/grist-core/issues/2232)
- **Docker :** Mise à jour de la configuration pour les tests Docker.
- **gvisor :** Utilisation de `gristlabs/gvisor-unprivileged` dans `gristlabs/grist-base`.
- **Email :** Modification de la gestion des groupes d'emails pour une meilleure performance et flexibilité.
- **Liens :** Mise à jour des liens vers le site et la documentation.
- **Architecture :** Refactorisation pour séparer les tests spécifiques à l'édition Enterprise (grist-ee) du cœur du projet.

### Autres changements
- **Traductions :** Mise à jour des traductions en français, allemand, portugais (Brésil), catalan, suédois.
- **Dépendances :** Mise à jour de la dépendance `handlebars` (4.7.7 -> 4.7.9) et `mocha-webdriver` (0.3.3 -> 0.3.5).
- **Documentation :** Mise à jour du fichier README.md.
- **CLA :** Signature du CLA par plusieurs contributeurs.
- **Automatisation des traductions :** Mise en place d'une automatisation pour les clés de traduction.
