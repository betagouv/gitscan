## Changelog : aides-agri (30 derniers jours)

### Résumé
Ce changelog présente les évolutions récentes du service aides-agri. Les dernières semaines ont été marquées par l'ajout d'une première version de la page de statistiques, des améliorations de l'interface d'administration et du parcours utilisateur, ainsi que des mises à jour de sécurité et de dépendances pour assurer la stabilité et la performance de la plateforme.

### Évolutions fonctionnelles
- Ajout d'une première version de la page de statistiques pour l'administration. (#387)
- Les bureaux valideurs peuvent désormais visualiser les aides avant leur publication. (#371)
- Amélioration du parcours v1 pour une meilleure expérience utilisateur. (#363)
- Mise à jour de la page des fonds d'urgence DNC pour refléter les informations les plus récentes. (#370)
- Correction mineure sur la page de résultats pour améliorer la présentation des informations. (#353)
- Adaptation de l'export CSV pour fonctionner correctement en mode minimal. (#341)
- Ajout d'une popup d'avertissement sur toutes les environnements sauf la production pour signaler un environnement de test. (#351)

### Évolutions techniques
- Amélioration du script de mises à jour pour faciliter la maintenance et les déploiements. (#381)
- Mise en place d'un "cooldown" pour les mises à jour automatiques de dépendances (dependabot) afin d'éviter des instabilités. (#374)
- Relance des tests E2E dans la CI pour garantir la qualité du code. (#350)
- Relance des mises à jour automatiques Javascript. (#345)

### Autres changements
- Mises à jour de plusieurs dépendances :
    - gunicorn (v25.0.1 -> v25.0.3 -> v25.1.0) (#367, #386)
    - ruff (0.14.14 -> 0.15.0 -> 0.15.1) (#362, #385)
    - coverage (7.13.2 -> 7.13.3 -> 7.13.4) (#344, #359, #383)
    - sentry-sdk (2.50.0 -> 2.51.0 -> 2.52.0) (#352, #364)
    - django-dsfr (3.3.0 -> 3.3.1) (#355)
    - faker (40.1.2 -> 40.4.0) (#366)
    - packaging (25.0 -> 26.0) (#340)
    - markdown (3.10 -> 3.10.1 -> 3.10.2) (#369, #382)
    - asgiref (3.11.0 -> 3.11.1) (#358)
    - django (5.2.10 -> 5.2.11) (#357)
    - gunicorn (23.0.0 -> 24.1.1) (#346)
    - cypress (15.7.0 -> 15.9.0) (#349)
    - esbuild (0.27.0 -> 0.27.2 -> 0.27.3) (#347, #375)
    - @sentry/browser (10.26.0 -> 10.34.0 -> 10.36.0 -> 10.37.0 -> 10.38.0) (#348, #354, #361, #373)
    - js-yaml (3.14.1 -> 3.14.2) (#379)
    - lodash & lodash-es (4.17.21 -> 4.17.23) (#377, #378)
    - tar-fs (3.1.0 -> 3.1.1) (#376)
    - qs & express (#380)
