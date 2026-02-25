## Changelog : aides-agri (30 derniers jours)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'interface d'administration pour une meilleure gestion des aides, notamment en permettant aux bureaux valideurs de prévisualiser les aides avant publication. Des corrections et ajustements ont également été apportés au parcours utilisateur et à la page de résultats. Enfin, de nombreuses dépendances ont été mises à jour pour bénéficier des dernières corrections de sécurité et améliorations de performance.

### Évolutions fonctionnelles
- Ajout d'une page de statistiques pour l'administration (#387).
- Les bureaux valideurs peuvent désormais visualiser les aides avant leur publication (#371).
- Ajustement du parcours v1 pour une meilleure expérience utilisateur (#363).
- Mise à jour de la page des fonds d'urgence DNC (#370).
- Correction mineure sur la page de résultats (#353).
- Ajout d'une popup d'avertissement sur les environnements de test (#351).

### Évolutions techniques
- Mise à jour de la configuration de dependabot pour limiter la fréquence des mises à jour automatiques (#374).
- Amélioration du script de mises à jour pour plus de robustesse (#381).
- Relance des tests E2E dans la CI pour garantir la qualité du code (#350).
- Relance des mises à jour automatiques Javascript (#345).

### Autres changements
- Mises à jour de nombreuses dépendances :
    - gunicorn (25.0.1 -> 25.1.0, 24.1.1 -> 25.0.1, 23.0.0 -> 24.1.1)
    - ruff (0.14.14 -> 0.15.0, 0.15.0 -> 0.15.1)
    - coverage (7.13.2 -> 7.13.3, 7.13.3 -> 7.13.4)
    - sentry-sdk (2.50.0 -> 2.51.0, 2.51.0 -> 2.52.0)
    - faker (4.0.1.2 -> 4.0.4.0)
    - asgiref (3.11.0 -> 3.11.1)
    - django (5.2.10 -> 5.2.11)
    - django-dsfr (3.3.0 -> 3.3.1)
    - @sentry/browser (10.26.0 -> 10.34.0, 10.34.0 -> 10.36.0, 10.36.0 -> 10.37.0, 10.37.0 -> 10.38.0)
    - cypress (15.7.0 -> 15.9.0)
    - esbuild (0.27.0 -> 0.27.2, 0.27.2 -> 0.27.3)
    - js-yaml (3.14.1 -> 3.14.2)
    - lodash (4.17.21 -> 4.17.23)
    - lodash-es (4.17.21 -> 4.17.23)
    - tar-fs (3.1.0 -> 3.1.1)
    - qs et express (mises à jour non spécifiées)
    - markdown (3.10.1 -> 3.10.2)
