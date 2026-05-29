## Changelog : flux-retour-cfas (30 derniers jours, au 28 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration des fonctionnalités de collaboration et de déclaration, ainsi que sur l'ajout de nouvelles pages d'atterrissage pour faciliter l'inscription. Des corrections ont également été apportées pour améliorer la stabilité et la gestion des données, notamment concernant la déduplication et la gestion des erreurs.

### Évolutions fonctionnelles
- Ajout d'indicateurs de collaboration pour une meilleure visibilité sur l'activité. [#4609](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4609)
- Affichage des effectifs des moins de 16 ans comme hors-limite dans le tableau des CFA. [#4607](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4607)
- Ajout d'informations sur les effectifs dans l'export de collaboration. [#4614](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4614)
- Création de nouvelles pages d'atterrissage pour l'inscription et l'information. [#4602](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4602)
- Ajout de tags permanents sur la liste des "traites" et unification du libellé des CFA. [#4615](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4615)
- Ajout de Crisp (outil de chat) sur la page des CFA. [#4596](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4596)
- Activation de la version 2 de la collaboration et de la déclaration pour plusieurs CMA (Nouvelle Aquitaine et HDF). [#4597](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4597), [#4590](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4590)
- Ajout d'un endpoint d'activation pour la version 2. [#4606](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4606)

### Évolutions techniques
- Migration de l'outil de détection de secrets (Talisman) vers Gitleaks. [#4600](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4600)
- Amélioration de la chaîne de déploiement pour une meilleure homogénéisation. [#4598](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4598)
- Correction de problèmes liés à la déduplication des enregistrements ML. [#4601](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4601), [#4599](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4599)
- Correction d'une erreur lors de la gestion des ruptures d'organisme croisées. [#4605](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4605)
- Restriction des comptages de collaboration admin aux dossiers "acc_conjoint". [#4613](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4613)
- Protection des sous-routes "admin" et "france-travail". [#4616](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4616)

### Autres changements
- Correction des liens vers les pages d'inscription dans le footer. [#4608](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4608)
- Mise à jour des dépendances pour corriger des vulnérabilités de haute sévérité. [#4610](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4610)
- Corrections de la configuration du fichier `release.yml`. [#4604](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4604), [#4603](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4603)
