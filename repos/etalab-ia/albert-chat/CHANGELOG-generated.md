## Changelog : albert-chat (30 derniers jours, au 10 novembre 2026)

### Résumé
Le projet a franchi une étape majeure avec son rebranding complet de `chat-widget` vers `albert-chat`. Les dernières semaines ont été marquées par une amélioration significative de l'expérience utilisateur (intégration via Web Component, interface de chat plus fluide et citations intégrées) et un renforcement majeur de la sécurité et de la robustesse de l'infrastructure (durcissement des iframes, déploiement automatisé et scans de vulnérabilités).

### Évolutions fonctionnelles
- **Nouvelles méthodes d'intégration** : Ajout du support via Web Component en complément de l'intégration par iframe ([#24](https://github.com/etalab-ia/albert-chat/pull/24)).
- **Amélioration de l'interface utilisateur** :
  - Optimisation du bouton de lancement (launcher) : positionnement fixe dans un coin et signal visuel de l'état ouvert ([#61](https://github.com/etalab-ia/albert-chat/pull/61)).
  - Affichage des réponses : les citations sont désormais intégrées directement dans le texte et les blocs de code bénéficient d'un meilleur formatage ([#73ba3dd](https://github.com/etalab-ia/albert-chat/commit/73ba3dd), [#a36d2d2](https://github.com/etalab-ia/albert-chat/commit/a36d2d2)).
  - Corrections de mise en page : ajustements des en-têtes, pieds de page et comportements de défilement ([#5b05aa1](https://github.com/etalab-ia/albert-chat/commit/5b05aa1), [#e0bbb3c](https://github.com/etalab-ia/albert-chat/commit/e0bbb3c)).
- **Nouvelles capacités** :
  - Support des collections de documents provisionnées de manière externe ([#43](https://github.com/etalab-ia/albert-chat/pull/43)).
  - Gestion configurable des limites d'utilisation pour prévenir les abus ([#e93a407](https://github.com/etalab-ia/albert-chat/commit/e93a407)).
  - Synchronisation incrémentale des guides ANSSI français ([#28](https://github.com/etalab-ia/albert-chat/pull/28)).

### Évolutions techniques
- **Sécurité et robustesse** :
  - Renforcement de la sécurité des iframes et de la liste d'autorisation (allowlist) pour l'intégration ([#7](https://github.com/etalab-ia/albert-chat/pull/7)).
  - Mise en place de scans de vulnérabilités (CVE Lite) en pré-commit ([#26c218f](https://github.com/etalab-ia/albert-chat/commit/26c218f)).
  - Durcissement de l'ingestion des données et du décodage des flux pour une meilleure fiabilité ([#4e6ac2c](https://github.com/etalab-ia/albert-chat/commit/4e6ac2c)).
- **Infrastructure et CI/CD** :
  - Automatisation du déploiement via Scaleway CLI avec intégration de barrières de qualité (quality gates) ([#9](https://github.com/etalab-ia/albert-chat/pull/9)).
  - Sécurisation et configuration des workflows GitHub Actions pour les forks ([#48](https://github.com/etalab-ia/albert-chat/pull/48)).
  - Migration de l'environnement vers Node 26 ([#9adf33e](https://github.com/etalab-ia/albert-chat/commit/9adf33e)).
  - Création d'une image conteneur autonome pour faciliter le déploiement ([#47f0e20](https://github.com/etalab-ia/albert-chat/commit/47f0e20)).
- **Refactoring** :
  - Rebranding complet du dépôt et de l'élément personnalisé vers `albert-chat` ([#58](https://github.com/etalab-ia/albert-chat/pull/58)).

### Autres changements
- **Documentation** :
  - Restructuration de la documentation : séparation du README principal et d'un dossier `docs/` dédié ([#56](https://github.com/etalab-ia/albert-chat/pull/56)).
  - Ajout d'un guide d'onboarding pour les FDE ([#45](https://github.com/etalab-ia/albert-chat/pull/45)).
  - Mise à jour des informations relatives aux ressources Scaleway et aux limites de débit ([#535c7fb](https://github.com/etalab-ia/albert-chat/commit/535c7fb), [#c87c9cd](https://github.com/etalab-ia/albert-chat/commit/c87c9cd)).
