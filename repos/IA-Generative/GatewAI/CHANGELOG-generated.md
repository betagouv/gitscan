## Changelog : GatewAI (30 derniers jours, au 23 octobre 2026)

### Résumé
Ce mois a été marqué par des avancées majeures, notamment l'introduction du support pour le streaming en temps réel via WebSocket et une gestion plus intelligente des quotas de consommation. Le projet a également entamé sa transition officielle vers l'organisation IA-Generative et a bénéficié d'optimisations de performance pour le transfert de fichiers volumineux.

### Évolutions fonctionnelles
- **Streaming Temps Réel (WebSocket) :** Introduction d'un proxy de streaming WebSocket incluant le contrôle d'accès lors du handshake, la limitation de la concurrence des sessions, le comptage de la consommation audio (audio-seconds metering) et des garde-fous sur les transcriptions. [#192](https://github.com/IA-Generative/GatewAI/pull/192)
- **Gestion avancée des quotas (Rate Limiting) :**
    - Mise en place de `budget_group` permettant de mutualiser le budget de tokens entre plusieurs alias de modèles partageant un même backend.
    - Support des headers de limitation de débit compatibles avec l'API OpenAI.
    - Amélioration de la gestion administrative permettant la réinitialisation des quotas pour un modèle spécifique. [#194](https://github.com/IA-Generative/GatewAI/pull/194)

### Évolutions techniques
- **Optimisation des transferts de données :** Refactorisation du mode synchrone pour utiliser le streaming des uploads multipart au lieu du buffering, ce qui évite les fuites de stockage éphémère et améliore l'efficacité du système.
- **Infrastructure & Kubernetes :** Ajout de la prise en charge des propriétés `envFrom` et `volumes` dans les charts Helm pour une configuration plus flexible.
- **Observabilité :** Correction du chemin de l'exportateur OTLP pour garantir le bon acheminement des traces et métriques vers les collecteurs. [#204](https://github.com/IA-Generative/GatewAI/pull/204)
- **Mise à jour de la stack :** Migration vers Go 1.27 et passage à des images de base Debian 13 (distroless) pour renforcer la sécurité et la stabilité.

### Autres changements
- **Migration d'organisation :** Transfert complet des références, de la licence et des images de l'organisation `Qatr-io` vers `IA-Generative`.
- **Documentation :** 
    - Mise à jour majeure de la précision documentaire (guide de mise à niveau des pools de backends, documentation des headers de rate-limiting).
    - Traduction des cartes de fonctionnalités de la page d'accueil en anglais.
- **Docker :** Ajout de labels OCI pour lier explicitement les packages GHCR au dépôt source.
