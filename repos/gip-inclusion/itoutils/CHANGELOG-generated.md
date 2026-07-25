## Changelog : itoutils (30 derniers jours, au 21 juillet 2026)

### Résumé
Les récentes mises à jour d'itoutils se concentrent principalement sur la maintenance et la correction de bugs. Une amélioration notable concerne la gestion des erreurs dans l'intégration avec Nexus, permettant une meilleure traçabilité des problèmes. De nombreuses dépendances ont également été mises à jour pour bénéficier des dernières corrections et améliorations de sécurité.

### Évolutions fonctionnelles
- Correction d'un bug dans l'intégration avec Nexus : l'exception originale `httpx` est maintenant préservée lors de la journalisation des erreurs d'API, facilitant le débogage. [#5d5b571](https://github.com/gip-inclusion/itoutils/commit/5d5b571)

### Évolutions techniques
- Mise à jour de plusieurs dépendances :
    - `Django` : passage de la version 6.0.6 à 6.0.7
    - `jwcrypto` : passage de la version 1.5.7 à 1.5.8
    - `syrupy` : passage de la version 5.3.2 à 5.5.3
    - `django-datadog-logger` : passage de la version 0.9.0 à 0.9.1
    - `ruff` : mises à jour de la version 0.15.18 à 0.15.21 puis à 0.15.22
    - `setup-uv` : passage de la version 8.2.0 à 8.3.2
    - `gh-action-pypi-publish` : passage de la version 1.14.0 à 1.14.1
