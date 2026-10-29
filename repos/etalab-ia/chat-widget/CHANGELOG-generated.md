## Changelog : chat-widget (30 derniers jours, au 28 octobre 2026)

### Résumé
Ce mois-ci, le projet a franchi une étape importante avec la sortie de la version 0.2.0. Les évolutions majeures incluent une nouvelle méthode d'intégration via Web Component, une synchronisation plus intelligente des guides de l'ANSSI et une interface de chat nettement améliorée, notamment pour la gestion des citations. La robustesse et la sécurité de l'infrastructure ont également été renforcées pour garantir un service stable et protégé.

### Évolutions fonctionnelles
- **Nouvelles méthodes d'intégration** : Ajout d'une intégration directe via Web Component en complément de l'iframe, ainsi qu'un chargeur d'intégration autonome (standalone embed loader) pour faciliter l'usage sur des sites tiers [#24](https://github.com/etalab-ia/chat-widget/pull/24).
- **Amélioration de l'interface de chat** : 
    - Les citations sont désormais intégrées directement dans le texte des réponses pour une meilleure lisibilité.
    - Amélioration de l'affichage des blocs de code et du défilement automatique vers la question.
    - Correction de l'affichage des sources et du header du widget.
- **Gestion de l'usage** : Mise en place de limites d'utilisation (abuse caps) configurables sur l'endpoint public pour prévenir les abus.
- **Refonte visuelle** : Mise à jour de la page d'accueil (landing page) et de la page de démonstration.

### Évolutions techniques
- **Optimisation de l'IA (RAG)** : Mise en place d'une synchronisation incrémentale des guides ANSSI français pour une mise à jour plus efficace et rapide des connaissances [#28](https://github.com/etalab-ia/chat-widget/pull/28).
- **Sécurisation de l'intégration** : 
    - Durcissement de la sécurité de l'iframe (allowlist et gestion du redimensionnement) [#7](https://github.com/etalab-ia/chat-widget/pull/7).
    - Isolation du widget par rapport au Design System Français (DSFR) pour garantir le respect de sa charte graphique [#26](https://github.com/etalab-ia/chat-widget/pull/26).
- **Infrastructure et CI/CD** :
    - Migration vers Node 26 et déploiement optimisé via la CLI Scaleway [#9](https://github.com/etalab-ia/chat-widget/pull/9).
    - Introduction de portes de qualité (quality gates) et de scans de sécurité automatisés (Gitleaks, CVE Lite) dans le pipeline CI.
- **Robustesse du flux** : Amélioration de la gestion du streaming de données et de la résilience face aux déconnexions clients.

### Autres changements
- **Documentation** : Mise à jour des informations relatives aux limites de débit (rate limits) et au périmètre de déploiement.
- **Maintenance** : Nettoyage de la configuration (suppression de Cloudflare) et optimisation des workflows de release.
