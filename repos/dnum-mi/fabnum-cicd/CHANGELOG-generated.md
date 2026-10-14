## Changelog : fabnum-cicd (30 derniers jours, au 13/10/2026)

### Résumé
Ce mois-ci, le projet a franchi une étape importante avec la synchronisation des workflows réutilisables vers la version 0.40.0 de la référence (upstream). Ces évolutions renforcent la fiabilité des processus de publication et de construction d'images Docker, tout en optimisant la structure de validation de la chaîne CI/CD.

### Évolutions fonctionnelles
- **build-docker** : Ajout de labels et d'annotations conformes aux standards OCI, avec la possibilité pour les utilisateurs de désactiver ce jeu de métadonnées.
- **release-app** : Amélioration de la logique de publication pour éviter la création de branches de pré-version redondantes.

### Évolutions techniques
- **Synchronisation majeure** : Mise à jour des workflows réutilisables avec la version upstream 0.40.0 et intégration des correctifs associés.
- **Optimisation de la CI** : Centralisation de la validation des pipelines derrière un contrôle unique obligatoire pour simplifier le suivi des échecs.
- **Amélioration de `sync-prerelease-branch`** : 
    - Intégration de correctifs de revue issus de l'upstream.
    - Gestion automatisée des conflits de fichiers de release lors des opérations de rebase.
    - Support de l'authentification via un token GitHub App pour les opérations de push.
- **Qualité et Tests** : 
    - Extension de la couverture de tests pour couvrir les nouveaux workflows synchronisés.
    - Correction de la configuration CI pour assurer la compatibilité avec les labels Ubuntu 26.04.
    - Correction des tests d'exécution de blocs de code dans le shell du runner.

### Autres changements
- Mise à jour de la documentation technique en français suite à la synchronisation des workflows.
