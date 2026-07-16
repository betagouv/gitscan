## Changelog : flux-retour-cfas (30 derniers jours, au 15 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'intégration de nouvelles sources de données (SIPA, Brevo), l'amélioration de la synchronisation des données et la correction de plusieurs bugs affectant l'interface utilisateur et l'import de données. Des migrations d'infrastructure ont également été réalisées.

### Évolutions fonctionnelles
- Ajout du filtre "ville" à la liste des jeunes en rupture dans l'outil de Machine Learning [#4641](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4641).
- Distinction des dossiers collaborateur lors de l'export [#4646](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4646).
- Activation de la tâche cron quotidienne pour l'envoi de messages WhatsApp de pré-qualification à 18h30 [#4647](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4647).
- Amélioration de l'intégration de Brevo (synchronisation) [#4643](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4643).
- Ajout des endpoints SIPA pour l'intégration de données [#4630](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4630).
- Possibilité d'activer la version 2 (v2) [#4631](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4631).

### Évolutions techniques
- Migration des serveurs `tdb-production` et `tdb-recette` [#4636](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4636) et [#4635](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4635).
- Suppression des sous-modules `.infra/authorizations` et `.infra/inventories` [#4634](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4634).
- Ajout d'un limiteur de débit unifié pour l'API [#4617](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4617).
- Modification du calcul des rapports [#4637](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4637).

### Autres changements
- Corrections de typographie dans les emails [#4645](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4645).
- Modification de la formulation dans l'email d'accès OFA [#4644](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4644).
- Corrections diverses de l'outil (V1, V2, V3) [#4633](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4633), [#4638](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4638) et [#4639](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4639).
- Renforcement de la vérification du numéro de téléphone des collaborateurs côté backend [#4640](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4640).
- Correction de l'import des vœux Affelnet [#4632](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4632).
- Alignement du bandeau "Souhaite un RDV" et de la liste dans la vue Machine Learning [#4642](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4642).
