## Changelog : kube-image-keeper (30 derniers jours, au 18 mai 2026)

### Résumé
Cette version apporte des améliorations significatives à la flexibilité du mirroring d'images, notamment la possibilité de spécifier des plateformes cibles. La documentation a été largement revue et améliorée, avec des guides d'installation plus clairs et des informations actualisées. Plusieurs corrections de bugs ont été implémentées pour améliorer la stabilité et la fiabilité du système, en particulier concernant le routage et le mirroring.

### Évolutions fonctionnelles
- Possibilité de configurer une liste de plateformes cibles lors du mirroring d'images [#586](https://github.com/SocialGouv/kube-image-keeper/issues/586).
- Amélioration de la gestion des variables d'environnement complexes en utilisant `toYaml`.
- Amélioration de la documentation concernant l'installation et la configuration, notamment pour ISM (Image Stream Manager).
- Ajout d'informations sur la migration depuis la version v1.
- Ajout d'une table des matières à la documentation des CRD (Custom Resource Definitions).

### Évolutions techniques
- Mise à jour de la version de Go vers 1.26.2 et des dépendances.
- Validation des expressions régulières utilisées dans les CRD `include/exclude`.
- Ajout d'une option `routing.HonorPrioritiesOnAlwaysImagePullPolicy` pour contrôler le comportement du routage.
- Limitation du nombre de goroutines et ajout d'un timeout dans `clearStaleMirrorStatus` pour améliorer la performance et la stabilité.
- Amélioration de la gestion des conflits lors des opérations de finalisation ISM.
- Correction de l'analyse des images conteneur dans le webhook.
- Suppression du bloc de configuration par défaut dans le Helm chart, privilégiant les valeurs par défaut de l'opérateur.
- Amélioration des tests, ajout de tests de non-régression.
- Utilisation d'un parser `conventionalcommits` pour la validation des messages de commit.
- Suppression de la génération du README dans le Helm chart, car il est généré par le CI.
- Correction de l'utilisation de l'image originale dans ISM lors de la réécriture des pods.
- Suppression des secrets `NotFound` de la liste des secrets de pull.
- Ancrage des motifs d'expressions régulières pour une sémantique de correspondance complète correcte.

### Autres changements
- Amélioration de la documentation, correction des erreurs de linting et normalisation des termes.
- Suppression d'instructions d'installation obsolètes.
- Correction de problèmes de linting Markdown.
- Silence de l'outil `gocyclo` sur certaines fonctions complexes.
- Ajout de tests unitaires et d'intégration.
- Amélioration du workflow CI/CD.
