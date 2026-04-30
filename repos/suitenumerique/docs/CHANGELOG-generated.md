## Changelog : docs (30 derniers jours, au 2026-04-29)

### Résumé
Les 30 derniers jours ont été marqués par des améliorations significatives de la robustesse et de la performance de Docs, notamment au niveau de la gestion du contenu et de l'intégration avec les services externes. Des corrections de bugs ont été apportées pour améliorer l'expérience utilisateur, en particulier concernant l'interlinking et la gestion des erreurs. Des optimisations ont également été réalisées sur l'infrastructure et les tests.

### Évolutions fonctionnelles
- Ajout d'un lien vers la documentation dans le menu d'aide. [#2222](https://github.com/suitenumerique/docs/issues/2222)
- Amélioration de la gestion des liens internes (interlinking) avec une meilleure expérience utilisateur et correction de bugs. [#2170](https://github.com/suitenumerique/docs/issues/2170), [#2213](https://github.com/suitenumerique/docs/issues/2213)
- Mise en place d'un support hors-ligne pour le contenu via un Service Worker, incluant la mise en cache du contenu et des métadonnées.
- Ajout d'un easter egg sur la création d'emojis dans les documents. [#2155](https://github.com/suitenumerique/docs/issues/2155)
- Possibilité de configurer l'URI de la requête d'authentification forward. [#2241](https://github.com/suitenumerique/docs/issues/2241)
- Amélioration de l'ordre d'affichage des documents épinglés (par date de mise à jour). [#2028](https://github.com/suitenumerique/docs/issues/2028)

### Évolutions techniques
- Mise à jour de l'image Nginx dans le Dockerfile vers la dernière version.
- Refonte de l'architecture de la gestion du contenu avec un endpoint dédié pour les mises à jour, l'utilisation d'ETag et de `Last-Modified` pour la mise en cache.
- Suppression de l'endpoint `descendants` obsolète.
- Mise à niveau de la librairie `docspec` vers la version 3.0.0 et adaptation de l'API de conversion. [#2220](https://github.com/suitenumerique/docs/issues/2220)
- Amélioration de la configuration du logger en mode debug pour l'environnement "feature".
- Utilisation d'Uvicorn pour exécuter l'application Django en environnement de développement.
- Refactorisation des tests E2E pour une meilleure organisation et une exécution plus rapide.
- Ajout de permissions au workflow CI pour une sécurité accrue.
- Amélioration de la gestion des erreurs 5xx avec une redirection vers une page dédiée et une structure d'alerte améliorée. [#2128](https://github.com/suitenumerique/docs/issues/2128)
- Amélioration de l'accessibilité des résultats de recherche de documents. [#2122](https://github.com/suitenumerique/docs/issues/2122)

### Autres changements
- Correction de tests unitaires et E2E instables.
- Corrections de typos dans la documentation (contributing.md).
- Mise à jour des dépendances JavaScript et Python (hors mises à jour de sécurité).
- Ajout d'un checklist IA dans le template de pull request.
- Mise à jour des chaînes de traduction.
- Correction de problèmes de style et d'erreurs ESLint.
- Ajout d'un favicon par défaut.
- Validation des emojis pour les réactions. [#2208](https://github.com/suitenumerique/docs/issues/2208)
- Suppression des paramètres UTM.
- Correction de bugs liés à la gestion des espaces blancs dans les URLs CORS.
- Interdiction de restaurer un document non supprimé.
- Prévention du déplacement d'un document vers son propre descendant ou vers lui-même.
- Amélioration de la gestion des erreurs lors de l'importation de CSV.
- Correction de problèmes de compatibilité avec les instances E2E.
- Ajout d'un flag `last-failed` aux tests E2E.
- Mise à jour des dépendances `blocknote` vers la version 0.47.3.
