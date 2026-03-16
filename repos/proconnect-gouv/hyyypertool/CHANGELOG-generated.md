## Changelog : hyyypertool (30 derniers jours)

### Résumé
Cette version apporte des améliorations significatives à la gestion des équipes et des accès, ainsi qu'à la gestion des modérations et des domaines. Des corrections de bugs ont été implémentées pour améliorer la stabilité et l'expérience utilisateur. De plus, l'outil a été mis à jour avec les dernières versions de ses dépendances et des améliorations de sécurité ont été apportées.

### Évolutions fonctionnelles
- Ajout de la gestion des équipes avec contrôle d'accès basé sur les rôles [#1477](https://github.com/proconnect-gouv/hyyypertool/pull/1477).
- Possibilité de filtrer les services à exclure par leur nom [#1496](https://github.com/proconnect-gouv/hyyypertool/pull/1496).
- Ajout de la possibilité d'automatiser la vérification des domaines lors de l'ajout de domaines autorisés [#1433](https://github.com/proconnect-gouv/hyyypertool/pull/1433).
- Ajout de l'affichage de la tranche d'effectifs de l'unité légale dans le composant organisation [#1449](https://github.com/proconnect-gouv/hyyypertool/pull/1449).
- Amélioration de la gestion des modérations avec l'envoi de notifications via Crisp [#1441](https://github.com/proconnect-gouv/hyyypertool/pull/1441).
- Simplification du filtre de modérations [#1434](https://github.com/proconnect-gouv/hyyypertool/pull/1434).

### Évolutions techniques
- Refonte de la couche de données "hyperbase" [#867](https://github.com/proconnect-gouv/hyyypertool/pull/867).
- Refactorisation de la configuration et de la structure des middlewares [#1474](https://github.com/proconnect-gouv/hyyypertool/pull/1474).
- Suppression de l'intégration Zammad et du code associé [#1445](https://github.com/proconnect-gouv/hyyypertool/pull/1445).
- Suppression de Row-Level Security (RLS) dans hyyyperbase [#1475](https://github.com/proconnect-gouv/hyyypertool/pull/1475).
- Mise à jour des dépendances (Hono, pg, @gouvfr/dsfr, etc.).
- Amélioration de la sécurité avec l'ajout de Sentry pour le profiling et la surveillance des erreurs [#1406](https://github.com/proconnect-gouv/hyyypertool/pull/1406).
- Utilisation de node 24 pour la build.

### Autres changements
- Suppression du fichier `.eslintrc` [#1478](https://github.com/proconnect-gouv/hyyypertool/pull/1478).
- Correction de bugs liés à la gestion des membres liés et à l'affichage des tables [#1405](https://github.com/proconnect-gouv/hyyypertool/pull/1405), [#1430](https://github.com/proconnect-gouv/hyyypertool/pull/1430).
- Amélioration de l'accessibilité des tableaux [#1429](https://github.com/proconnect-gouv/hyyypertool/pull/1429).
- Correction de problèmes de flakiness dans les tests E2E [#1408](https://github.com/proconnect-gouv/hyyypertool/pull/1408).
- Mise à jour de la documentation et des configurations.
