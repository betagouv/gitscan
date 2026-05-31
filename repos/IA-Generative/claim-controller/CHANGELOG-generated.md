## Changelog : claim-controller (30 derniers jours, au 12 mai 2026)

### Résumé
Ce mois-ci, claim-controller a bénéficié d'améliorations significatives en termes de gestion du cycle de vie des revendications, de flexibilité de configuration et de monitoring. Les nouvelles fonctionnalités permettent une gestion plus fine des ressources Kubernetes, notamment via des configurations spécifiques à l'environnement et un contrôle précis de la durée de vie des revendications.

### Évolutions fonctionnelles
- Ajout de la possibilité de définir des valeurs par défaut spécifiques à l'environnement via `extraValuesTemplate`, permettant une personnalisation accrue des déploiements. [#14](https://github.com/IA-Generative/claim-controller/issues/14)
- Implémentation de la fonctionnalité de libération des revendications et de nettoyage des revendications expirées.
- Ajout d'une métrique pour suivre la durée totale d'une revendication, de sa création à son expiration.
- Prise en charge de la pré-provisionnement des revendications.
- Ajout de sondes de readiness et de liveness pour une meilleure gestion des charges de travail.
- Support de `maxTTL` pour contrôler la durée de vie et le renouvellement des revendications.
- Amélioration des métriques pour le suivi du cycle de vie des revendications.
- Gestion des références de propriétaire (owner reference) dans les ConfigMap et les providers de fichiers.
- Mise à jour de l'endpoint de libération pour accepter l'ID de la revendication comme paramètre de chemin.

### Évolutions techniques
- Ajout d'une configuration GitLab CI pour la lecture des secrets et la construction de l'image Docker.
- Amélioration de la gestion des tags d'image dans le fichier `deployment.yaml` pour un versionnement plus précis. [#6](https://github.com/IA-Generative/claim-controller/issues/6)
- Correction de la récupération de la version dans l'étape de mise à jour du fichier `Chart.yaml`.
- Correction de l'ajout de labels pour l'instance et le nom dans les métadonnées du service.
- Mise à jour des fonctions `LoadResourceTemplate` pour inclure le paramètre `namespace`. [#10](https://github.com/IA-Generative/claim-controller/issues/10)

### Autres changements
- Publication des versions 0.4.1 et 0.5.0.
