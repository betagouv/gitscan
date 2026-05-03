## Changelog : euphrosyne (30 derniers jours, au 01 mai 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'implémentation d'une nouvelle fonctionnalité majeure de gestion du cycle de vie des données des projets, incluant des états "chaud" et "froid" pour optimiser le stockage et l'accès aux données.  De nombreuses améliorations ont également été apportées à l'infrastructure et aux dépendances du projet pour assurer sa stabilité et sa sécurité.

### Évolutions fonctionnelles
- **Gestion du cycle de vie des données :** Implémentation complète de la gestion du cycle de vie des données des projets, avec des états "chaud" et "froid" pour optimiser le stockage et l'accès. Cela inclut des API pour déclencher et suivre les opérations de cycle de vie, ainsi qu'une interface utilisateur pour les administrateurs. [#1700](https://github.com/betagouv/euphrosyne/pull/1700)
- **Gestion des images Joconde :** Activation du support pour les images provenant de Joconde.
- **Amélioration de l'interface utilisateur :** Ajout d'un panneau d'administration pour le cycle de vie des projets dans l'interface utilisateur, avec des notifications et des blocages de fonctionnalités en fonction de l'état du projet.
- **Commandes de gestion des données :** Ajout de commandes pour gérer le refroidissement des données des projets.
- **Intégration ORCID :** Amélioration de l'intégration avec ORCID.
- **Gestion des permissions :** Restriction de l'accès à certaines fonctionnalités en fonction des rôles et des permissions des utilisateurs.

### Évolutions techniques
- **Déploiement Scalingo :** Ajout d'un workflow pour le déploiement automatique sur Scalingo lors de la création d'une nouvelle release.
- **Mises à jour de dépendances :** Mises à jour de nombreuses dépendances, notamment Django (6.0.4), TypeScript, Vitest, Axios, et d'autres bibliothèques JavaScript, pour bénéficier des dernières corrections de bugs et améliorations de sécurité.
- **Refactoring :** Refactorisation du code pour améliorer sa lisibilité et sa maintenabilité, notamment dans la gestion du cycle de vie des données.
- **Tests :** Ajout de tests unitaires et d'intégration pour assurer la qualité du code et la stabilité des nouvelles fonctionnalités.
- **Amélioration de la sécurité :** Renforcement de la sécurité du projet grâce à la mise à jour des dépendances et à la correction de vulnérabilités potentielles.

### Autres changements
- **Documentation :** Mise à jour de la documentation pour refléter les nouvelles fonctionnalités et les changements apportés au projet.
- **Configuration :** Ajout de variables d'environnement pour configurer le comportement du projet.
- **Nettoyage de code :** Suppression de code obsolète et amélioration de la qualité générale du code.
- **Traduction :** Ajout de traductions manquantes.
