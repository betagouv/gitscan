## Changelog : euphrosyne (30 derniers jours, au 17 avril 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'implémentation d'une gestion du cycle de vie des données de projet (refroidissement et archivage), avec des améliorations significatives pour la gestion des données "froides" et "chaudes". Des correctifs ont également été apportés pour améliorer la stabilité et la sécurité de la plateforme, ainsi que des mises à jour de dépendances pour assurer la compatibilité et la sécurité.

### Évolutions fonctionnelles
- **Gestion du cycle de vie des données :** Implémentation complète d'un système de gestion du cycle de vie des données de projet, incluant la possibilité de "refroidir" les données après une période définie, avec des règles d'éligibilité et des actions associées. [#1697](https://github.com/betagouv/euphrosyne/pull/1697)
- **Interface administrateur :** Ajout d'un panneau d'administration pour gérer le cycle de vie des projets, avec des notifications et des contrôles d'accès.
- **API de gestion du cycle de vie :** Développement d'APIs pour déclencher et surveiller les opérations de cycle de vie des données.
- **Exemption du plan de prévention :** Ajout d'un interrupteur dans l'interface d'administration pour exempter un projet du plan de prévention. [#1807](https://github.com/betagouv/euphrosyne/pull/1807)
- **Correction de bug :** Correction d'un problème empêchant le rendu correct du sélecteur de définition d'image de projet pour les utilisateurs non administrateurs. [#1848](https://github.com/betagouv/euphrosyne/pull/1848)
- **Correction de bug :** Correction d'un problème lié à la collision de noms dans les tests de l'usine de projets. [#1822](https://github.com/betagouv/euphrosyne/pull/1822)
- **Correction de bug :** Correction d'un problème avec l'attribution du statut "staff" lors de la vérification ORCID. [#1808](https://github.com/betagouv/euphrosyne/pull/1808)
- **Images Joconde :** Activation du support pour les images Joconde. [#1826](https://github.com/betagouv/euphrosyne/pull/1826)

### Évolutions techniques
- **Refactoring :** Refactorisation de l'interface utilisateur du "virtual office" en TypeScript.
- **Amélioration de la sécurité :** Renforcement de la sécurité des endpoints liés au cycle de vie des données.
- **Gestion des erreurs :** Amélioration de la gestion des erreurs lors du démarrage des opérations de gestion des données.
- **Architecture :** Passage de la gestion du cycle de vie des données au niveau "run" vers le niveau "projet".
- **Intégrations :** Mise à jour des intégrations avec les outils Euphrosyne (euphro-tools) pour prendre en charge les nouveaux identifiants de projet.
- **Tests :** Ajout de tests pour la récupération du cycle de vie des projets.
- **Documentation :** Ajout de documentation pour les nouvelles fonctionnalités de gestion des données.

### Autres changements
- Mise à jour des dépendances : plusieurs dépendances ont été mises à jour vers leurs dernières versions stables (Django, Pillow, pytest, sentry-sdk, webpack, etc.). Ces mises à jour incluent des correctifs de sécurité et des améliorations de performance.
- Nettoyage de code et refactoring mineur.
- Amélioration des messages d'erreur et de la journalisation.
- Mise à jour de la documentation interne.
- Correction de problèmes d'audit npm.
