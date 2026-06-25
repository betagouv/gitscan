## Changelog : acces-cible (30 derniers jours, au 24 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la correction de bugs, l'amélioration de la gestion des données et l'ajout d'une nouvelle fonctionnalité pour faciliter l'intégration avec le JDMA. Des optimisations techniques ont également été apportées, notamment concernant les tests et la configuration Docker.

### Évolutions fonctionnelles
- Ajout d'un widget JDMA pour faciliter l'intégration avec ce service [#569](https://github.com/betagouv/acces-cible/issues/569).
- Configuration du bouton JDMA via des variables d'environnement [#578](https://github.com/betagouv/acces-cible/issues/578).
- Correction d'un bug empêchant l'import CSV de gérer correctement les tags, évitant ainsi les doublons [#577](https://github.com/betagouv/acces-cible/issues/577).
- Normalisation de l'URL des sites pour assurer une cohérence des données [#576](https://github.com/betagouv/acces-cible/issues/576).

### Évolutions techniques
- Mise à jour de la configuration Docker pour utiliser le Dockerfile officiel [#547](https://github.com/betagouv/acces-cible/issues/547).
- Amélioration des mocks pour les tests Axe afin d'assurer une meilleure couverture et fiabilité [#586](https://github.com/betagouv/acces-cible/issues/586).
- Suppression d'une version personnalisée d'Omniauth au profit de la version officielle [#587](https://github.com/betagouv/acces-cible/issues/587).
- Suppression des colonnes `url` et `current` de la table `audits` [#582](https://github.com/betagouv/acces-cible/issues/582) et [#580](https://github.com/betagouv/acces-cible/issues/580).
- Ajout d'un header `User-Agent` personnalisé pour les requêtes [#601](https://github.com/betagouv/acces-cible/issues/601).

### Autres changements
- Mise à jour de la documentation concernant les en-têtes de la page d'aide [#602](https://github.com/betagouv/acces-cible/issues/602).
