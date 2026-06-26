## Changelog : aides-jeunes (30 derniers jours, au 25 juin 2026)

### Résumé
Ce changelog présente les améliorations apportées au simulateur d'aides-jeunes au cours du dernier mois. Les principales évolutions concernent l'amélioration de l'outil de contribution simplifié, avec l'ajout d'une navigation latérale et la possibilité de sélectionner une institution. Des corrections de bugs ont également été apportées pour améliorer la stabilité et l'expérience utilisateur.

### Évolutions fonctionnelles
- **Outil de contribution simplifié :** Ajout d'une navigation latérale pour faciliter l'utilisation de l'outil [#5120](https://github.com/betagouv/aides-jeunes/pull/5120).
- **Outil de contribution simplifié :** Possibilité de sélectionner une institution lors de la contribution [#5133](https://github.com/betagouv/aides-jeunes/pull/5133).
- **Aide permis demandeur d'emploi :** Mise à jour de la configuration de l'aide "permis demandeur d'emploi" [#5151](https://github.com/betagouv/aides-jeunes/pull/5151).
- **Conditions générales :** Correction du libellé des conditions générales dans l'outil de contribution [#5149](https://github.com/betagouv/aides-jeunes/pull/5149).

### Évolutions techniques
- **Correction de bug :** Résolution d'un problème de mutation de tableau réactif dans la fonction de tri des ressources [#5155](https://github.com/betagouv/aides-jeunes/pull/5155).
- **Correction de bug :** Prévention des erreurs réseau non gérées lors du chargement des paramètres OpenFisca [#5157](https://github.com/betagouv/aides-jeunes/pull/5157).
- **Mises à jour de dépendances :** Mise à jour de plusieurs dépendances, incluant `js-yaml`, `jsonwebtoken`, `dsfr` et `axios` [#5145](https://github.com/betagouv/aides-jeunes/pull/5145), [#5143](https://github.com/betagouv/aides-jeunes/pull/5143) et corrections via `npm audit fix` [#5144](https://github.com/betagouv/aides-jeunes/pull/5144).
