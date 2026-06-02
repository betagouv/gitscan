## Changelog : flux-retour-cfas (30 derniers jours, au 01 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration des fonctionnalités de collaboration et de suivi des CFA, notamment avec l'ajout de nouvelles stratégies d'envoi de campagnes, l'intégration d'indicateurs de collaboration et des corrections pour assurer la robustesse des données et des processus. Des améliorations ont également été apportées à l'infrastructure de déploiement et à la sécurité.

### Évolutions fonctionnelles
- Ajout de la préqualification WhatsApp pour les campagnes. [#4612](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4612)
- Implémentation d'une stratégie d'envoi de campagnes CFA en deux étapes. [#4611](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4611)
- Affichage des effectifs des moins de 16 ans comme hors-limite dans le tableau des CFA. [#4607](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4607)
- Ajout d'indicateurs de collaboration pour un suivi plus précis. [#4609](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4609)
- Création de nouvelles pages d'atterrissage (landing pages) pour l'inscription. [#4602](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4602)
- Correction des liens vers les pages d'inscription dans le footer des pages d'atterrissage. [#4608](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4608)
- Ajout d'informations sur l'effectif dans l'export de collaboration. [#4614](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4614)
- Activation d'un nouveau point de terminaison d'activation v2. [#4606](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4606)

### Évolutions techniques
- Mise en place d'une auto-révocation des clés API inutilisées pour renforcer la sécurité. [#4619](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4619)
- Réduction des champs projetés pour optimiser les performances. [#4618](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4618)
- Migration de l'outil de détection de secrets Talisman vers Gitleaks. [#4600](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4600)
- Amélioration de la chaîne de déploiement pour une plus grande homogénéité. [#4598](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4598)
- Correction du fichier `release.yml` pour améliorer le processus de publication. [#4604](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4604) et [#4603](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4603)
- Correction d'un problème de déduplication entraînant des erreurs. [#4599](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4599)

### Autres changements
- Correction d'un problème empêchant la gestion des dossiers orphelins inter-organismes dans les déclarations de rupture des CFA. [#4605](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4605)
- Restriction du nombre de collaborations administratives aux dossiers `acc_conjoint`. [#4613](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4613)
- Mise à jour des dépendances pour corriger des vulnérabilités de sécurité. [#4610](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4610)
- Ajout d'étiquettes permanentes sur la liste des "traites" et unification de l'étiquette CFA. [#4615](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4615)
- Activation de la collaboration et de la déclaration v2 pour 10 CMA de Nouvelle-Aquitaine. [#4597](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4597)
- Prévention des erreurs E11000 lors de la déduplication des enregistrements ML avec fusion de squatter. [#4601](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4601)
