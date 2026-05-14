## Changelog : flux-retour-cfas (30 derniers jours, au 12 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur avec l'ajout de nouvelles pages d'atterrissage, l'activation de la version 2 pour plusieurs CMA (Chambres de Métiers et de l'Artisanat) et des corrections de bugs liés à la gestion des données et des collaborations. Des améliorations de sécurité ont également été apportées en mettant à jour les dépendances.

### Évolutions fonctionnelles
- Ajout de nouvelles pages d'atterrissage et d'inscription génériques. [#4602](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4602)
- Affichage des effectifs de moins de 16 ans comme étant hors portée dans le tableau des CFA. [#4607](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4607)
- Activation de la version 2 de l'endpoint d'activation. [#4606](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4606)
- Ajout de Crisp (outil de chat) sur la page des CFA. [#4596](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4596)
- Nouvelle fonctionnalité d'onboarding ajoutée. [#4586](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4586)
- Ajout de la nouvelle collaboration ML/OFA. [#4558](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4558)
- Ajout de colonnes de collaboration au traitement export ML. [#4584](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4584)
- Ajout de feedbacks pour la collaboration. [#4585](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4585)

### Évolutions techniques
- Migration de l'outil de scan de secrets Talisman vers Gitleaks. [#4600](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4600)
- Correction de la chaîne de déploiement pour une homogénéisation. [#4598](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4598)
- Correction de bugs dans le fichier `release.yml` pour améliorer le processus de publication. [#4604](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4604), [#4603](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4603)
- Correction d'un problème d'e11000 lors de la déduplication des enregistrements ML avec fusion de squatter. [#4601](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4601)
- Correction d'une erreur de déduplication. [#4599](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4599)
- Correction de l'utilisation de la date incorrecte pour l'ouverture de la collaboration. [#4591](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4591)
- Adaptation des statistiques pour la collaboration. [#4595](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4595)
- Extension des colonnes d'exportation utilisateur pour inclure plus de types d'organisations. [#4587](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4587)

### Autres changements
- Correction des liens vers les pages d'atterrissage/inscription dans le footer générique. [#4608](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4608)
- Ajout de Lucas en tant qu'utilisateur. [#4593](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4593), [#4592](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4592)
- Mise à jour des habilitations. [#4594](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4594)
- Épinglage de `handlebars` et `form-data` pour corriger des CVE critiques. [#4589](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4589)
- Mise à jour des dépendances pour corriger les alertes de sécurité Dependabot. [#4588](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4588)
- Activation de la version 2 de la collaboration pour 7 CMA de la région HDF. [#4590](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4590)
- Activation de la version 2 de la collaboration pour 10 CMA de la région Nouvelle-Aquitaine. [#4597](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4597)
