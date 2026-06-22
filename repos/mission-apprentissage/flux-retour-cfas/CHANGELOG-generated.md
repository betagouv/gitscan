## Changelog : flux-retour-cfas (30 derniers jours, au 19 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'intégration avec des services tiers (Brevo, Tally, Sipa, WhatsApp), l'ajout de nouvelles fonctionnalités pour le suivi des CFA (notamment autour des campagnes et des effectifs), et des corrections de bugs pour assurer une meilleure stabilité et précision des données. Des migrations de serveurs ont également été effectuées.

### Évolutions fonctionnelles
- Ajout de la gestion des webinaires avec intégration du formulaire d'inscription Brevo. [#4627](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4627)
- Intégration des endpoints Sipa pour une meilleure gestion des données. [#4630](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4630)
- Possibilité d'activer la version 2 du système. [#4631](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4631)
- Ajout d'une fonctionnalité de préqualification WhatsApp. [#4612](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4612)
- Redirection vers Tally Survey pour les sondages. [#4622](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4622)
- Amélioration de la stratégie d'envoi des campagnes CFA avec une stratégie à deux envois. [#4611](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4611)
- Ajout d'informations sur l'effectif dans l'exportation des collaborations. [#4614](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4614)
- Ajout d'indicateurs de collaboration. [#4609](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4609)
- Correction du calcul des rapports. [#4637](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4637)
- Correction de l'import des voeux Affelnet. [#4632](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4632)
- Correction des données GEO et du formatage des données pour la synchronisation Brevo. [#4620](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4620)
- Correction d'un revert concernant le changement de colonnes SMS/TELEPHONE pour la sync Brevo. [#4626](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4626)
- Correction de l'affichage de "webinaire" au pluriel. [#4628](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4628)
- Corrections de l'outil V1. [#4633](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4633)

### Évolutions techniques
- Suppression des sous-modules `.infra/authorizations` et `.infra/inventories`. [#4634](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4634)
- Migration des serveurs `tdb-production` et `tdb-recette`. [#4636](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4635) et [#4636](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4636)
- Réduction des champs projetés pour optimiser les performances. [#4618](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4618)
- Auto-révocation des clés API inutilisées. [#4619](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4619)
- Restriction des comptages de collaboration admin aux dossiers `acc_conjoint`. [#4613](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4613)
- Protection des sous-routes `/admin` et `/france-travail`. [#4616](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4616)
- Unification du label CFA et affichage des tags permanents sur la liste des traités. [#4615](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4615)

### Autres changements
- Mise à jour des dépendances pour corriger des vulnérabilités de haute sévérité. [#4610](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4610)
