## Changelog : kube-image-keeper (30 derniers jours, au 7 mai 2026)

### Résumé
Ce mois-ci, kube-image-keeper a bénéficié d'améliorations significatives en termes de documentation, de stabilité et de flexibilité. Les changements incluent une documentation plus complète des CRD, des corrections de bugs pour améliorer la fiabilité du mirroring et du routing des images, et la possibilité de configurer des plateformes cibles spécifiques lors du mirroring. Des améliorations de la CI/CD et des outils de linting ont également été apportées pour garantir la qualité du code.

### Évolutions fonctionnelles
- Possibilité de configurer une liste de plateformes cibles lors du mirroring d'images. [#586](https://github.com/SocialGouv/kube-image-keeper/issues/586)
- Amélioration de la gestion des variables d'environnement complexes en utilisant `toYaml`.
- Amélioration de la gestion des images alternatives, notamment en clarifiant la documentation et en corrigeant des limitations antérieures.
- Correction du comportement de routing pour toujours privilégier l'image originale lorsque la politique de pull est définie sur `Always`, indépendamment des priorités.
- Ajout de la possibilité de configurer l'ordre de priorité des routes.
- Amélioration de la gestion des secrets utilisés pour l'authentification.

### Évolutions techniques
- Mise à jour de la version de Go à 1.26.2 et des dépendances.
- Refonte de la documentation des CRD (Custom Resource Definitions) avec une table des matières et des informations détaillées sur chaque champ.
- Amélioration de la CI/CD : ajout de tests, de vérifications de linting et de conformité aux conventions de commit.
- Correction de problèmes de complexité cyclomatique dans le code.
- Optimisation des goroutines et ajout de délais d'attente pour éviter les blocages.
- Suppression de la génération du README du helm chart, désormais géré par la CI.
- Amélioration de la gestion des conflits lors des opérations de finalisation dans l'ISM (Image Status Manager).
- Suppression de la configuration par défaut dans le Helm chart, privilégiant la configuration via l'opérateur.
- Validation des expressions régulières utilisées dans les CRD `include/exclude`.

### Autres changements
- Amélioration de la documentation générale, incluant des instructions d'installation et des exemples d'utilisation.
- Correction de problèmes de linting dans la documentation.
- Normalisation de la terminologie utilisée dans la documentation.
- Ajout d'informations sur la migration depuis la version v1.
- Ajout d'informations sur l'installation avec ISM (Image Security Manager).
- Suppression d'instructions d'installation obsolètes.
- Ajout de tests de non-régression pour certaines corrections.
- Backfill du champ `original` dans le statut des images pour améliorer le monitoring.
- Suppression des images inutilisées du statut du CISA (Container Image Status Aggregator).
