## Changelog : GatewAI (30 derniers jours, au 23 octobre 2026)

### Résumé
Ce mois a été marqué par des avancées majeures, notamment l'introduction du support du streaming WebSocket pour les applications en temps réel et une gestion plus intelligente des quotas de consommation via des groupes de budget partagés. Le projet a également entamé sa migration vers l'organisation IA-Generative et a bénéficié d'une montée en version de son infrastructure pour garantir une sécurité et des performances accrues.

### Évolutions fonctionnelles
- **Streaming Temps Réel** : Introduction d'un proxy WebSocket permettant le streaming, incluant le contrôle d'accès lors du handshake, la limitation de la concurrence des sessions et le suivi de la consommation audio.
- **Gestion avancée des quotas (Rate-limiting)** :
    - Mise en place de `budget_group` permettant de mutualiser le budget de jetons entre plusieurs alias de modèles (ex: partager un quota entre `code-v1` et `code-v2`).
    - Support des headers de limitation de débit compatibles avec la spécification OpenAI.
    - Possibilité de réinitialiser les quotas de manière ciblée par modèle.

### Évolutions techniques
- **Optimisation des flux de données** : Refactorisation des uploads multipart pour utiliser le streaming au lieu du buffering, ce qui élimine les fuites de stockage éphémère et améliore la stabilité du système.
- **Infrastructure & Sécurité** :
    - Migration de la chaîne de compilation vers Go 1.27 et passage aux images de base Debian 13 (distroless) pour renforcer la sécurité.
    - Migration complète du dépôt, des images et de la documentation vers l'organisation `IA-Generative` [#203](https://github.com/IA-Generative/GatewAI/pull/203).
    - Amélioration des charts Helm avec l'ajout du support pour les propriétés `envFrom` et `volumes`.
- **Observabilité** : Correction du routage des exports OTLP pour assurer le bon fonctionnement de la télémétrie (traces, métriques, logs) [#204](https://github.com/IA-Generative/GatewAI/pull/204).

### Autres changements
- **Documentation** : Mise à jour majeure pour améliorer la précision des informations, incluant un nouveau guide de mise à niveau, la documentation des headers de rate-limiting et des pools de backends [#206](https://github.com/IA-Generative/GatewAI/pull/206).
- **Internationalisation** : Traduction des cartes de fonctionnalités de la page d'accueil en anglais.
- **Maintenance** : Mise à jour des licences/copyrights et ajout de labels OCI pour lier les packages GHCR au dépôt [#205](https://github.com/IA-Generative/GatewAI/pull/205).
