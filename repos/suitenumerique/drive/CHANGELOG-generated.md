## Changelog : drive (30 derniers jours, au 15 septembre 2026)

### Résumé
Cette période a été marquée par l'introduction d'un système de restriction d'accès avancé, permettant de sécuriser et d'isoler des dossiers ou fichiers de manière granulaire. Le projet a également bénéficié d'une refonte majeure de son moteur de permissions et de l'ajout de tests de charge pour garantir la stabilité et la performance de la plateforme.

### Évolutions fonctionnelles
- **Nouveau système de restriction d'accès** : gestion granulaire permettant d'activer ou désactiver des restrictions sur des dossiers, d'isoler certains éléments de la recherche et de l'indexation, et de gérer l'accès via le déplacement de dossiers dans l'arborescence.
- **Sécurité renforcée** : blocage de la suppression de fichiers par un créateur dont les droits ont été révoqués et contrôle strict des droits de création à la racine du drive.
- **Améliorations de l'expérience utilisateur** : correction de l'affichage de la vue "Récents", meilleure gestion des langues de navigateur et optimisation du rendu des documents PDF.
- **Administration** : ajout de la possibilité d'abandonner manuellement les analyses de malwares en cours.

### Évolutions techniques
- **Refonte du moteur de permissions** : restructuration du backend pour séparer les capacités (*abilities*) en méthodes distinctes et déportation du calcul des permissions vers un composant dédié.
- **Tests et performance** : intégration d'une suite de tests de charge avec JMeter (scénarios de session utilisateur et de lecture intensive) et amélioration de l'environnement de tests de bout en bout (E2E).
- **Frontend** : migration vers la bibliothèque de composants `@gouvfr-lasuite/ui-components`.
- **Infrastructure et DevOps** : optimisation des processus de build (Makefile, Docker), mise à jour des sources d'images (Minio) et planification des tâches de détection de malwares via Helm.
- **Observabilité** : intégration du suivi de performance via Sentry.

### Autres changements
- **Documentation** : ajout de la documentation sur les paramètres de permissions backend et mise à jour du changelog.
- **Projet** : ajout du badge DPG dans le README.
