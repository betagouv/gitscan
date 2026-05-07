## Changelog : flux-retour-cfas (30 derniers jours, au 5 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration des fonctionnalités liées aux collaborations, notamment avec l'ajout de nouvelles collaborations ML/OFA et l'intégration de données associées dans les exports utilisateurs. Des corrections ont également été apportées pour améliorer la stabilité et la fiabilité de l'application, en particulier concernant la gestion des doublons et le processus de déploiement.

### Évolutions fonctionnelles
- Ajout de nouvelles collaborations ML/OFA. [#4558](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4558)
- Activation des collaborations v2 pour les CMA de Nouvelle-Aquitaine (10) et des Hauts-de-France (7). [#4597](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4597), [#4590](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4590)
- Intégration de Crisp sur la page CFA pour améliorer le support utilisateur. [#4596](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4596)
- Extension des colonnes d'export utilisateur pour inclure des informations géographiques pour plus de types d'organisations. [#4587](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4587)
- Ajout d'un nouveau processus d'onboarding. [#4586](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4586)
- Ajout de la gestion des feedbacks pour les collaborations. [#4585](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4585)
- Intégration des données ML dans les exports utilisateurs. [#4583](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4583)
- Ajout de colonnes de collaboration aux exports de traitement ML. [#4584](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4584)

### Évolutions techniques
- Correction de problèmes de doublons lors de la fusion des enregistrements ML avec les squatter. [#4601](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4601)
- Correction d'une erreur de déduplication. [#4599](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4599)
- Amélioration de l'homogénéisation de la chaîne de déploiement. [#4598](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4598)
- Correction du workflow de release. [#4604](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4604), [#4603](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4603)
- Correction de l'utilisation de la date pour l'ouverture des collaborations. [#4591](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4591)
- Mise à jour des habilitations. [#4594](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4594)
- Suppression de la modal et de la logique backend liées au feedback du classificateur. [#4582](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4582)

### Autres changements
- Ajout de nouveaux utilisateurs (Lucas). [#4593](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4593), [#4592](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4592)
- Correction de vulnérabilités de sécurité en mettant à jour les dépendances Handlebars et form-data. [#4589](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4589)
- Mise à jour de dépendances pour corriger des alertes de sécurité (Dependabot). [#4588](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4588)
