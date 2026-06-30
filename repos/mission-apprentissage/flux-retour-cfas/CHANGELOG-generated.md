## Changelog : flux-retour-cfas (30 derniers jours, au 29 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'intégration avec des outils tiers (Brevo, Sipa, Tally Survey, WhatsApp) et la correction de plusieurs bugs affectant l'outil. Des migrations de serveurs ont également été réalisées. L'objectif est d'offrir une meilleure expérience utilisateur et d'optimiser le suivi des données d'apprentissage pour les CFA.

### Évolutions fonctionnelles
- Intégration de formulaires d'inscription Brevo directement dans les pages webinaires [#4627](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4627).
- Redirection des liens `/sondage` vers Tally Survey [#4622](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4622).
- Ajout de points de terminaison Sipa pour l'intégration de données [#4630](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4630).
- Pré-qualification WhatsApp pour faciliter la prise de rendez-vous [#4612](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4612).
- Possibilité d'activer la version 2 de certaines fonctionnalités [#4631](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4631).
- Amélioration de la stratégie d'envoi des campagnes CFA avec une approche en deux étapes [#4611](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4611).
- Correction de l'import des vœux Affelnet [#4632](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4632).
- Correction du calcul du reporting [#4637](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4637).
- Correction de l'affichage des webinaires (passage de "webinaire" à "webinaires") [#4628](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4628).
- Correction du formattage des données et de la détermination des données GEO [#4620](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4620).
- Corrections diverses de l'outil (V1, V2, V3) [#4633](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4633), [#4638](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4638), [#4639](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4639).

### Évolutions techniques
- Migration des serveurs `tdb-production` et `tdb-recette` [#4636](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4635), [#4635](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4636).
- Suppression des sous-modules `.infra/authorizations` et `.infra/inventories` [#4634](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4634).
- Suppression de champs de projection inutiles pour optimiser les performances [#4618](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4618).
- Mise en place d'une auto-révocation des clés API inutilisées [#4619](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4619).
- Correction d'une erreur de mapping de colonnes pour la synchronisation Brevo (SMS -> TELEPHONE, puis retour à TELEPHONE) [#4624](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4624), [#4626](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4626).
- Redirection du lien WhatsApp RDV sous `/api` pour permettre le routage par Nginx [#4623](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4623).

### Autres changements
- Aucun changement significatif à signaler.
