## Changelog : ComparIA (30 derniers jours, au 2026-04-15)

### Résumé
Ce mois-ci, ComparIA a connu des améliorations significatives en termes de déploiement, de robustesse et de fonctionnalités. L'installation via Docker a été simplifiée, la détection de spam a été améliorée grâce à l'intégration de Gemini, et de nouveaux modèles de langage ont été ajoutés au catalogue, tandis que certains modèles obsolètes ont été archivés. Des efforts importants ont également été consacrés à l'optimisation des performances et à la mise en place d'une meilleure surveillance.

### Évolutions fonctionnelles

*   **Installation Docker simplifiée:** Une méthode d'installation Docker autonome avec Caddy a été ajoutée, facilitant le déploiement de ComparIA.  [#429](https://github.com/betagouv/ComparIA/pull/429)
*   **Amélioration de la détection de spam:** La détection de spam et de contenu inapproprié a été améliorée en utilisant le modèle Gemini au lieu d'expressions régulières, et les résultats sont maintenant persistés en base de données. [#398](https://github.com/betagouv/ComparIA/pull/398)
*   **Ajout de nouveaux modèles:** Les modèles Gemma 4 26B A4B et Gemma 4 31B ont été ajoutés au catalogue. [#425](https://github.com/betagouv/ComparIA/pull/425), [#426](https://github.com/betagouv/ComparIA/pull/426), [#418](https://github.com/betagouv/ComparIA/pull/418)
*   **Archivage de modèles obsolètes:** Les modèles olmo-3-32b-think, LFM 2 8B A1B et Gemini 3 Pro ont été archivés car ils ne sont plus disponibles ou pertinents. [#428](https://github.com/betagouv/ComparIA/pull/428), [#424](https://github.com/betagouv/ComparIA/pull/424), [#426](https://github.com/betagouv/ComparIA/pull/426)
*   **Ajout de Captcha:** Ajout d'un Captcha Altcha pour protéger les endpoints de l'arène. [#384](https://github.com/betagouv/ComparIA/pull/384)
*   **Limitation du taux de requêtes:** Implémentation d'une limitation du taux de requêtes pour la sélection de modèles personnalisés afin de prévenir les abus. [#384](https://github.com/betagouv/ComparIA/pull/384)

### Évolutions techniques

*   **Refonte du calcul des classements:** Le calcul des classements des modèles a été refactorisé pour utiliser Redis comme cache et s'appuyer sur des données provenant de la base de données, améliorant ainsi les performances et la fiabilité.
*   **Instrumentation et monitoring:** Ajout d'une instrumentation complète avec Prometheus et Loki pour une meilleure surveillance et un débogage plus facile.
*   **Amélioration de l'infrastructure Docker:** Refactorisation de la configuration Docker, simplification des pipelines CI/CD et correction de problèmes liés à la base de données.
*   **Mise à jour des dépendances:** Mise à jour de plusieurs dépendances, notamment jsdom, eslint et les paquets npm/yarn.
*   **Refactorisation du code:** Refactorisation significative du code, notamment dans les modules liés aux données, aux classements et à l'accès à la base de données.
*   **Correction de bugs:** Correction de plusieurs bugs liés à la base de données, aux logs et à la configuration de l'environnement.

### Autres changements

*   **Documentation:** Amélioration de la documentation concernant l'installation Docker et le processus d'initialisation de la base de données.
*   **Traduction:** Mise à jour des traductions en Estonien et en Danois via Weblate.
*   **Nettoyage du code:** Suppression de code obsolète et simplification de la configuration.
*   **Mise à jour des modèles:** Mise à jour de la liste des modèles disponibles et archivage des modèles obsolètes.
*   **Amélioration des logs:** Ajout de logs plus précis et informatifs.
*   **Configuration de Dependabot:** Optimisation de la fréquence de mise à jour des dépendances par Dependabot.
