## Changelog : drive (30 derniers jours, au 11 septembre 2026)

### Résumé
Cette période a été marquée par l'introduction d'un système de restrictions d'accès plus puissant et flexible, ainsi que par une refonte majeure de la gestion des permissions en arrière-plan. La plateforme bénéficie également de nouveaux outils de monitoring et de tests de charge pour garantir une meilleure stabilité et performance.

### Évolutions fonctionnelles
- **Nouveau système de restrictions** : gestion granulaire de l'accès aux dossiers, permettant d'activer ou désactiver des restrictions, d'isoler certains contenus des recherches et de mieux contrôler la visibilité dans les listes de premier niveau.
- **Amélioration de la prévisualisation** : correction et amélioration du rendu des documents PDF.
- **Interface utilisateur** : la vue "Récents" se rafraîchit désormais correctement après la modification d'un élément.
- **Administration** : ajout de la possibilité d'abandonner une analyse de logiciel malveillant en cours.
- **Sécurité** : renforcement des règles de suppression pour empêcher un créateur de supprimer un élément s'il n'en a plus l'accès.

### Évolutions techniques
- **Refonte de l'architecture des permissions** : migration de la logique de calcul des droits et de résolution des rôles vers un composant backend dédié pour une meilleure modularité.
- **Monitoring et performance** : intégration du suivi des performances via Sentry et ajout de scénarios de tests de charge (JMeter) pour simuler des sessions utilisateurs et des lectures intensives.
- **Frontend** : migration vers la bibliothèque de composants unifiée `@gouvfr-lasuite/ui-components`.
- **Tests** : amélioration de l'environnement de tests de bout en bout (E2E) et optimisation des tests unitaires sur les exceptions.
- **Infrastructure et DevOps** : optimisation des scripts de base de données (psql), du Makefile et de la planification des tâches de détection de malwares via Helm.

### Autres changements
- **Documentation** : ajout de la documentation concernant les paramètres de configuration du backend des permissions.
- **Nettoyage** : suppression de variables d'environnement inutilisées.
