## Changelog : ocr-api (30 derniers jours, au 5 juillet 2026)

### Résumé
Cette mise à jour apporte des corrections de sécurité importantes, des améliorations de la performance et de la stabilité de l'API, notamment au niveau de l'initialisation de PaddleOCR et de la gestion des caches. De nouvelles fonctionnalités comme la génération de markdown ont été ajoutées, et le reporting d'erreurs a été amélioré grâce à l'intégration de Sentry.

### Évolutions fonctionnelles
*   Ajout de la génération de documents au format Markdown.
*   Intégration de Sentry pour le reporting des erreurs au niveau de l'API, du worker et de l'interface utilisateur ([#398](https://github.com/IA-Generative/ocr-api/issues/398)).

### Évolutions techniques
*   Mise à jour de l'initialisation de PaddleOCR pour une meilleure performance et stabilité.
*   Ajout de la variable d'environnement `TORCHINDUCTOR_CACHE_DIR` aux Dockerfiles pour optimiser l'utilisation du cache.
*   Corrections et stabilisations des tests, notamment pour le SDK ([#399](https://github.com/IA-Generative/ocr-api/issues/399)).
*   Correction de failles de sécurité identifiées par Dependabot et d'autres analyses de sécurité.
*   Amélioration de la méthode `batch_predict` dans PaddleOCR pour une meilleure lisibilité et formatage.

### Autres changements
*   Corrections de la configuration CI/CD pour les releases.
*   Mise à jour de la version de l'API à 0.12.6.
*   Nettoyage et refactoring du code.
