## Changelog : OTP-DS-to-Grist (30 derniers jours, au 9 avril 2026)

### Résumé
Ce changelog présente les améliorations apportées à OTP-DS-to-Grist au cours des 30 derniers jours. Les principales évolutions concernent l'amélioration de la performance et de la robustesse de l'application, notamment au niveau du chargement des données et de la gestion des erreurs. Des corrections ont également été apportées pour améliorer l'expérience utilisateur et la fiabilité de la synchronisation des données. La mise en place de Docker et Codespaces facilite le développement et le déploiement.

### Évolutions fonctionnelles
- Ajout de l'affichage de l'environnement d'exécution de l'application. [#254](https://github.com/betagouv/OTP-DS-to-Grist/issues/254)
- Amélioration de la création de tables "avis" dans Grist. [#265](https://github.com/betagouv/OTP-DS-to-Grist/issues/265)
- Ajout de la récupération et de la création de la table "expert". [#247](https://github.com/betagouv/OTP-DS-to-Grist/issues/247)
- Amélioration du loader pour une meilleure précision. [#249](https://github.com/betagouv/OTP-DS-to-Grist/issues/249)
- Suppression des détails unitaires des temps d'appels dans l'affichage de la progression. [#273](https://github.com/betagouv/OTP-DS-to-Grist/issues/273)
- Amélioration du loader pour atteindre 98% de complétion. [#270](https://github.com/betagouv/OTP-DS-to-Grist/issues/270)

### Évolutions techniques
- Mise en place de Docker et de Codespaces pour faciliter le développement et le déploiement. [#220](https://github.com/betagouv/OTP-DS-to-Grist/issues/220)
- Optimisation des performances : mise en cache global, utilisation d'instructeurs uniques, traitement par lots des champs, ajout de champs de requêtes d'extraction. [#224](https://github.com/betagouv/OTP-DS-to-Grist/issues/224)
- Amélioration de la gestion des logs : affichage des temps de requête vers l'API DN. [#217](https://github.com/betagouv/OTP-DS-to-Grist/issues/217)
- Suppression de code mort et ajout de fallbacks pour une meilleure robustesse. [#257](https://github.com/betagouv/OTP-DS-to-Grist/issues/257)
- Suppression des crochets et guillemets dans les données JSON pour éviter les erreurs de parsing. [#256](https://github.com/betagouv/OTP-DS-to-Grist/issues/256)

### Autres changements
- Publication de la version 0.7.0. [#189](https://github.com/betagouv/OTP-DS-to-Grist/issues/189)
- Mise à jour des dépendances de développement : `ruff`, `pytest-cov`, `poethepoet`, `eslint`, `baseline-browser-mapping`, `jest`, `jest-environment-jsdom`.
- Mise à jour des dépendances : `requests`, `cryptography`, `python-socketio`.
