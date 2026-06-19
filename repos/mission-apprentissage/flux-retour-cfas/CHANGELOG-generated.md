## Changelog : flux-retour-cfas (30 derniers jours, au 18 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'intégration avec des services tiers (Brevo, Tally Survey, Sipa, Affelnet), l'ajout de nouvelles fonctionnalités pour la gestion des collaborations et des webinaires, ainsi que des corrections de bugs et des optimisations de performance. Des migrations d'infrastructure ont également été réalisées.

### Évolutions fonctionnelles
- Ajout de la gestion des webinaires avec intégration du formulaire d'inscription Brevo. [#4627](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4627)
- Intégration des endpoints Sipa pour une meilleure gestion des données. [#4630](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4630)
- Possibilité d'activer la version 2 du système. [#4631](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4631)
- Correction d'un bug concernant l'import des vœux Affelnet. [#4632](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4632)
- Correction d'un bug lié à la synchronisation Brevo des numéros de téléphone (SMS). [#4626](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4626)
- Amélioration du formatage des données et de la détermination des données géographiques. [#4620](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4620)
- Ajout de la préqualification WhatsApp. [#4612](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4612)
- Ajout d'indicateurs de collaboration et d'informations sur l'effectif dans l'export de collaboration. [#4614](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4614)
- Redirection de l'URL `/sondage` vers Tally Survey. [#4622](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4622)
- Ajout d'une stratégie d'envoi en 2 étapes pour les campagnes CFA. [#4611](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4611)
- Affichage des tags permanents sur la liste des "traites" et unification du label CFA. [#4615](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4615)

### Évolutions techniques
- Suppression des sous-modules `.infra/authorizations` et `.infra/inventories`. [#4634](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4634)
- Migrations des serveurs `tdb-production` et `tdb-recette`. [#4636](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4636), [#4635](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4635)
- Réduction des champs projetés pour optimiser les performances. [#4618](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4618)
- Mise en place d'une révocation automatique des clés API inutilisées. [#4619](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4619)
- Restriction du comptage des collaborations administrateur aux dossiers `acc_conjoint`. [#4613](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4613)
- Protection des routes `/admin` et `/france-travail` avec des sous-routes. [#4616](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4616)

### Autres changements
- Correction de l'affichage de "webinaire" au pluriel ("webinaires"). [#4628](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4628)
- Mise à jour des dépendances pour corriger des vulnérabilités de sécurité. [#4610](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4610)
- Correction d'un bug dans l'outil V1. [#4633](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4633)
- Correction du routage de la redirection WhatsApp pour qu'elle passe par `/api`. [#4623](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4623)
