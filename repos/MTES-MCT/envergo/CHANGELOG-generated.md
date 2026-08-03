## Changelog : envergo (30 derniers jours, au 30 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à l'interface utilisateur, notamment concernant la gestion des haies et des dates de demande. Des corrections de bugs et des optimisations ont également été apportées pour améliorer la stabilité et la performance de la plateforme. Plusieurs fusions de branches témoignent d'un travail actif sur de nouvelles fonctionnalités et des corrections.

### Évolutions fonctionnelles
- Amélioration de l'affichage et de la validation des dates de demande, avec des messages d'alerte et des formulaires dédiés. [#1212](https://github.com/MTES-MCT/envergo/pull/1212)
- Ajout de la possibilité de relancer une procédure unique. [#1208](https://github.com/MTES-MCT/envergo/pull/1208)
- Amélioration de la gestion des haies, incluant l'affichage des types de haies, le calcul des coefficients et la gestion des cas sans haies. [#1217](https://github.com/MTES-MCT/envergo/pull/1217), [#1216](https://github.com/MTES-MCT/envergo/pull/1216)
- Ajout de textes d'aide et d'instructions pour la loi sur l'eau et les haies.
- Amélioration de la lisibilité du démonstrateur. [#1176](https://github.com/MTES-MCT/envergo/pull/1176)
- Gestion des dossiers multi-départementaux. [#1196](https://github.com/MTES-MCT/envergo/pull/1196)
- Fermeture des projets de pétitions. [#1180](https://github.com/MTES-MCT/envergo/pull/1180)
- Ajout d'un bouton de relance dans les résultats en dehors du département, conditionné par la configuration.

### Évolutions techniques
- Refactoring de la validation des formulaires et amélioration de la gestion des erreurs.
- Amélioration de l'API pour une meilleure gestion des données.
- Corrections de conflits de fusion et mises à jour des migrations.
- Optimisation du calcul de la densité autour des centroïdes.
- Amélioration de la gestion des exceptions et des erreurs.
- Mise à jour des tests (pytest, Playwright) et ajout de nouveaux tests pour garantir la qualité du code.
- Amélioration de la gestion des configurations.
- Correction d'un problème de condition de course dans l'évaluation des requêtes. [#1168](https://github.com/MTES-MCT/envergo/pull/1168)
- Intégration de Sentry pour le suivi des erreurs. [#1194](https://github.com/MTES-MCT/envergo/pull/1194)

### Autres changements
- Mise à jour de la documentation.
- Amélioration de la cohérence des textes et des messages.
- Corrections de style et de formatage du code.
- Suppression de code inutile et nettoyage du code.
- Mise à jour des dépendances (non listées ici, car mises à jour de routine).
