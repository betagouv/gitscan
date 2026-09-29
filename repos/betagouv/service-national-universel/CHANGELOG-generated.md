## Changelog : service-national-universel (30 derniers jours, au 28 septembre 2026)

### Résumé
Ce mois-ci a été principalement consacré à un effort massif de sécurisation de la plateforme et à un nettoyage important des fonctionnalités obsolètes. Plusieurs anciens parcours (inscription, phase 1, représentants légaux) ont été retirés pour simplifier l'expérience, tandis que de nombreux correctifs ont été déployés pour renforcer la protection des données personnelles et la robustesse des accès.

### Évolutions fonctionnelles
- **Simplification du parcours utilisateur**
  - Décommissionnement de plusieurs parcours et écrans devenus obsolètes : tunnel d'inscription et de réinscription [#5358](https://github.com/betagouv/service-national-universel/issues/5358), écran "jeune affecté" [#5412](https://github.com/betagouv/service-national-universel/issues/5412), parcours des représentants légaux [#5357](https://github.com/betagouv/service-national-universel/issues/5357) et fonctionnalités d'inscription pour les structures [#5290](https://github.com/betagouv/service-national-universel/issues/5290).
  - Retrait des écritures liées à la phase 1 et des objectifs d'inscription [#5449](https://github.com/betagouv/service-national-universel/issues/5449).
- **Information utilisateur**
  - Ajout de bandeaux d'information concernant l'indisponibilité temporaire de la plateforme sur les pages de connexion et la base de connaissance [#5296](https://github.com/betagouv/service-national-universel/issues/5296) [#5289](https://github.com/betagouv/service-national-universel/issues/5289).

### Évolutions techniques
- **Sécurité et protection des données**
  - **Contrôle d'accès et étanchéité** : Renforcement massif des permissions pour prévenir les accès non autorisés (IDOR) et cloisonnement des données par rôle (agents, référents, structures) [#5302](https://github.com/betagouv/service-national-universel/issues/5302) [#5319](https://github.com/betagouv/service-national-universel/issues/5319) [#5342](https://github.com/betagouv/service-national-universel/issues/5342).
  - **Confidentialité (RGPD)** : Protection de la vie privée par le masquage des données personnelles (PII) et des secrets dans les journaux d'erreurs (Sentry) et les logs applicatifs [#5446](https://github.com/betagouv/service-national-universel/issues/5446) [#5431](https://github.com/betagouv/service-national-universel/issues/5431) [#5337](https://github.com/betagouv/service-national-universel/issues/5337). Suppression de l'outil de télémétrie Plausible [#5401](https://github.com/betagouv/service-national-universel/issues/5401).
  - **Authentification et sessions** : Sécurisation des jetons (invalidation des jetons exposés ou obsolètes) [#5451](https://github.com/betagouv/service-national-universel/issues/5451), protection contre les attaques CSRF [#5428](https://github.com/betagouv/service-national-universel/issues/5428) et durcissement de la gestion des cookies de session [#5406](https://github.com/betagouv/service-national-universel/issues/5406).
  - **Intégrité des échanges** : Protection contre les injections HTML [#5377](https://github.com/betagouv/service-national-universel/issues/5377), sécurisation des pièces jointes (analyse antivirus) [#5443](https://github.com/betagouv/service-national-universel/issues/5443) et assainissement des contenus des emails officiels [#5452](https://github.com/betagouv/service-national-universel/issues/5452).
- **Infrastructure et DevOps**
  - **Optimisation de la CI/CD** : Intégration des suites de tests du support dans la CI [#5436](https://github.com/betagouv/service-national-universel/issues/5436) et optimisation de la gestion du cache npm sur les runners pour accélérer les déploiements [#5327](https://github.com/betagouv/service-national-universel/issues/5327).
  - **Performance** : Optimisation de la consommation mémoire des tâches planifiées (cron) pour éviter les surcharges lors des mises à jour [#5448](https://github.com/betagouv/service-national-universel/issues/5448).

### Autres changements
- **Maintenance du système**
  - Nettoyage de la base de données et retrait de composants d'administration obsolètes (administration CLE, tables de répartition) [#5315](https://github.com/betagouv/service-national-universel/issues/5315) [#5356](https://github.com/betagouv/service-national-universel/issues/5356).
