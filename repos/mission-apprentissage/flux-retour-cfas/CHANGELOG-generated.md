## Changelog : flux-retour-cfas (30 derniers jours, au 11 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des collaborations, notamment avec l'activation de la version 2 pour plusieurs CMA (Conseils Métropolitains d'Apprentissage), et l'ajout de nouvelles fonctionnalités liées à l'export de données et à l'onboarding. Des corrections de bugs ont également été apportées pour assurer la stabilité et la fiabilité de la plateforme.

### Évolutions fonctionnelles
- Activation de la version 2 des collaborations et des déclaraisons pour 10 CMA de Nouvelle-Aquitaine [#4597](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4597).
- Activation de la version 2 des collaborations et des déclaraisons pour 7 CMA de Hauts-de-France [#4590](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4590).
- Ajout de Crisp pour le support utilisateur directement sur la page des CFA [#4596](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4596).
- Extension des colonnes d'export des utilisateurs pour inclure plus de types d'organisations [#4587](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4587).
- Ajout d'un nouveau processus d'onboarding [#4586](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4586).
- Ajout de la nouvelle collaboration ML/OFA [#4558](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4558).
- Ajout de colonnes de collaboration à l'export du traitement ML [#4584](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4584).
- Ajout de la possibilité de donner des feedbacks sur les collaborations [#4585](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4585).
- Correction d'un problème empêchant l'ouverture correcte des collaborations avec la date appropriée [#4591](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4591).
- Correction d'un problème de duplication d'enregistrements ML [#4601](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4601) et [#4599](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4599).
- Correction de la gestion des organismes orphelins dans les déclarations de rupture de CFA [#4605](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4605).

### Évolutions techniques
- Migration de l'outil de scan de secrets Talisman vers Gitleaks [#4600](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4600).
- Homogénéisation de la chaîne de déploiement [#4598](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4598).
- Corrections du fichier `release.yml` pour améliorer le processus de publication [#4603](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4603) et [#4604](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4604).
- Mise à jour des habilitations pour améliorer la sécurité [#4594](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4594).
- Épingle des versions de `handlebars` et `form-data` pour corriger des vulnérabilités critiques [#4589](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4589).

### Autres changements
- Ajout de nouveaux utilisateurs (Lucas) [#4592](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4592) et [#4593](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4593).
- Mise à jour des dépendances pour corriger des alertes de sécurité (via Dependabot) [#4588](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4588).
