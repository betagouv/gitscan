## Changelog : GatewAI (30 derniers jours, au 23 octobre 2026)

### Résumé
Ce mois a été marqué par l'introduction de fonctionnalités majeures de streaming en temps réel via WebSocket et par une refonte importante du système de limitation de débit (rate-limiting). Le projet a également franchi une étape clé avec sa migration complète vers l'organisation IA-Generative et une optimisation de la gestion des ressources pour garantir une meilleure stabilité et sécurité.

### Évolutions fonctionnelles
- **Streaming en temps réel** : Introduction du support WebSocket pour le streaming, incluant le contrôle d'accès lors du handshake, la limitation de la concurrence des sessions et la mesure de la consommation audio [#192](https://github.com/IA-Generative/GatewAI/pull/192).
- **Amélioration du Rate Limiting** : 
    - Introduction de `budget_group` pour mutualiser les budgets de tokens entre plusieurs alias de modèles.
    - Support des headers de limitation de débit compatibles avec l'API OpenAI.
    - Possibilité de réinitialiser les quotas de manière granulaire pour un modèle spécifique [#194](https://github.com/IA-Generative/GatewAI/pull/194).
- **Configuration** : Ajout du support des propriétés `envFrom` et `volumes` pour faciliter le déploiement.

### Évolutions techniques
- **Optimisation de la gestion des flux** : Refonte de l'upload des fichiers multipart pour utiliser le streaming vers le backend au lieu du buffering, évitant ainsi les fuites de stockage éphémère et les pics de consommation mémoire.
- **Mise à jour de l'infrastructure** : Migration de la stack de base vers Go 1.27 et l'image Debian 13 (distroless) pour renforcer la sécurité et la pérennité du runtime.
- **Correction de la télémétrie** : Résolution du problème de routage des endpoints pour l'exportateur OTLP, assurant le bon acheminement des traces et métriques [#204](https://github.com/IA-Generative/GatewAI/pull/204).

### Autres changements
- **Migration organisationnelle** : Transfert complet de l'ensemble des références (images Docker, documentation, licence) de l'organisation `Qatr-io` vers `IA-Generative`.
- **Documentation** : 
    - Mise à jour majeure pour inclure les guides de mise à niveau et la documentation des nouveaux headers de rate-limiting.
    - Traduction des cartes de fonctionnalités de la page d'accueil en anglais.
- **Nettoyage** : Suppression des fichiers de documentation obsolètes et correction des liens vers les runbooks d'alerte.
