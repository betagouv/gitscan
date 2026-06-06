## Changelog : flux-retour-cfas (30 derniers jours, au 5 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des données des CFA, notamment en vue de la synchronisation avec Brevo, l'ajout de nouvelles fonctionnalités pour le suivi des rendez-vous WhatsApp et des sondages, ainsi que des corrections et optimisations diverses pour améliorer la stabilité et l'expérience utilisateur. Des améliorations ont également été apportées aux landing pages et à l'export de données collaboratives.

### Évolutions fonctionnelles
- Ajout de la redirection vers un sondage Tally Survey via la route `/sondage` [#4622](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4622).
- Préqualification pour WhatsApp est maintenant disponible [#4612](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4612).
- Ajout d'informations sur l'effectif dans l'export collaboratif [#4614](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4614).
- Affichage des tags permanents sur la liste des "traites" et unification du label CFA [#4615](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4615).
- Ajout d'indicateurs de collaboration [#4609](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4609).
- Ajout de nouvelles landing pages pour l'inscription et l'information [#4602](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4602).
- Affichage des effectifs des moins de 16 ans comme hors-limite dans le tableau des CFA [#4607](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4607).
- Nouvelle version de l'endpoint d'activation (v2) [#4606](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4606).
- Gestion des ruptures de déclaration inter-organismes pour les CFA [#4605](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4605).
- Modification du nom de la colonne `TELEPHONE` en `SMS` pour la synchronisation avec Brevo [#4624](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4624).
- Correction d'un revert concernant le changement de colonnes SMS -> TELEPHONE pour la synchronisation Brevo [#4626](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4626).

### Évolutions techniques
- La redirection des rendez-vous WhatsApp est maintenant servie via `/api` pour permettre le routage par Nginx [#4623](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4623).
- Optimisation des champs projetés pour réduire la charge [#4618](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4618).
- Mise en place d'une stratégie d'envoi de campagnes CFA en deux étapes [#4611](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4611).
- Auto-révocation des clés API inutilisées [#4619](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4619).
- Protection des routes `/admin` et `/france-travail` [#4616](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4616).
- Migration de l'outil de détection de secrets `talisman` vers `gitleaks` [#4600](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4600).
- Amélioration du formatage des données et de la détermination des données GEO à partir des labels [#4620](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4620).

### Autres changements
- Mise à jour des dépendances pour corriger des vulnérabilités de sécurité critiques [#4610](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4610).
- Correction des liens vers les landing pages dans le footer générique [#4608](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4608).
- Restriction du comptage des collaborations admin aux dossiers `acc_conjoint` [#4613](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4613).
