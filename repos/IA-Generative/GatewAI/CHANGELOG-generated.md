## Changelog : GatewAI (30 derniers jours, au 09/11/2026)

### Résumé
Ce mois a été marqué par des avancées majeures, notamment l'introduction du support du streaming en temps réel via WebSocket et l'amélioration significative des mécanismes de limitation de débit (rate limiting) pour une meilleure compatibilité avec les standards OpenAI. Le projet a également bénéficié d'optimisations de performance importantes sur le suivi de l'utilisation et a finalisé sa transition vers l'organisation IA-Generative.

### Évolutions fonctionnelles
- **Support du temps réel (WebSocket) :**
    - Introduction d'un proxy de streaming WebSocket avec contrôle d'accès lors du handshake.
    - Mise en place de limites de concurrence par session et de la mesure de consommation (audio-seconds metering).
    - Ajout de garde-fous (guardrails) sur le texte des transcriptions.
- **Limitation de débit (Rate Limiting) :**
    - Introduction de la fonctionnalité `budget_group` permettant de mutualiser le budget de tokens par modèle.
    - Support des en-têtes de limitation de débit compatibles avec OpenAI.
    - Amélioration de la gestion des quotas avec la possibilité de réinitialiser les quotas par modèle.
- **Configuration Kubernetes :**
    - Ajout de la prise en charge des propriétés `envFrom` et `volumes` pour faciliter le déploiement.

### Évolutions techniques
- **Optimisation des performances :**
    - Refonte du pipeline de reporting de l'utilisation : passage de centaines de requêtes Redis sérielles à seulement deux requêtes via du pipelining, réduisant drastiquement la charge sur Redis [#223](https://github.com/IA-Generative/GatewAI/pull/223).
    - Optimisation des uploads synchrones : passage d'un mode bufferisé à un mode streaming pour éviter les fuites de stockage éphémère et une meilleure gestion des slots de modèles.
- **Infrastructure et Sécurité :**
    - Migration de la chaîne de build vers Go 1.27 et utilisation d'images de base Debian 13 (distroless) pour renforcer la sécurité.
    - Correction du chemin d'exportation OTLP pour assurer le bon fonctionnement de la télémétrie.
- **Helm :**
    - Correction d'alertes obsolètes et mise à jour de la documentation des métriques.

### Autres changements
- **Identité et Branding :** Migration complète des références de l'organisation `Qatr-io` vers `IA-Generative` (licence, copyright et URLs).
- **Documentation :**
    - Mise à jour majeure de la documentation pour garantir l'exactitude des informations (architecture, endpoints, métriques).
    - Traduction des cartes de fonctionnalités de la page d'accueil en anglais.
    - Documentation des nouveaux en-têtes de rate-limiting et des pools de backends.
- **Divers :** Ajout de labels OCI sur les images Docker pour lier les packages GHCR au dépôt.
