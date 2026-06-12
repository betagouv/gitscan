## Changelog : egapro (30 derniers jours, au 8 juin 2026)

### Résumé
Les dernières semaines ont été marquées par des améliorations significatives de l'expérience utilisateur, notamment dans les étapes de déclaration de la rémunération et de la revue des données. Des efforts importants ont également été consacrés à l'amélioration de la performance et de la stabilité de la plateforme, ainsi qu'à l'ajout de nouvelles statistiques et fonctionnalités pour l'administration.

### Évolutions fonctionnelles
- Amélioration de l'étape 5 de la déclaration de rémunération avec des corrections visuelles et une meilleure gestion du focus sur l'ajout d'informations. [#3538](https://github.com/SocialGouv/egapro/issues/3589)
- Correction de l'affichage de l'étape 6 (revue) avec un arrière-plan noir et une typographie améliorée. [#3540](https://github.com/SocialGouv/egapro/issues/3588)
- Ajout de l'historique des statuts d'une déclaration dans l'application. [#3584](https://github.com/SocialGouv/egapro/issues/3611)
- Correction des URLs des emails de notification et refactorisation du système de templates. [#3606](https://github.com/SocialGouv/egapro/issues/3606)
- Affichage du récapitulatif de la déclaration sur la page de détail de l'administration. [#3437](https://github.com/SocialGouv/egapro/issues/3590)
- Amélioration de la validation du champ vide et ajout d'une alerte GIP sur l'étape 1 (effectifs). [#3544](https://github.com/SocialGouv/egapro/issues/3544)
- Amélioration de l'espacement entre les actions de formulaire et le contenu. [#3535](https://github.com/SocialGouv/egapro/issues/3549)
- Désactivation de l'autocomplétion du navigateur sur tous les formulaires. [#3539](https://github.com/SocialGouv/egapro/issues/3548)
- Ajout de nouvelles statistiques : taux de déclaration, délai moyen par étape, taux d'abandon par étape, funnel de complétion et distribution des scores publics. [#3551](https://github.com/SocialGouv/egapro/issues/3551), [#3218](https://github.com/SocialGouv/egapro/issues/3546), [#3222](https://github.com/SocialGouv/egapro/issues/3545), [#3214](https://github.com/SocialGouv/egapro/issues/3513), [#3217](https://github.com/SocialGouv/egapro/issues/3521)
- Ajout de l'historique des statuts dans l'API SUIT pour l'export. [#3503](https://github.com/SocialGouv/egapro/issues/3503)
- Amélioration de l'affichage des labels d'étape pour les différents statuts du parcours de conformité. [#3495](https://github.com/SocialGouv/egapro/issues/3495)

### Évolutions techniques
- Ajout d'un agent `tu-dev` pour la création de tests unitaires et d'intégration. [#3620](https://github.com/SocialGouv/egapro/issues/3620)
- Refactorisation du système de cache avec une sauvegarde en base de données. [#3484](https://github.com/SocialGouv/egapro/issues/3537)
- Extraction du kit de templates React Email pour les notifications. [#3561](https://github.com/SocialGouv/egapro/issues/3561)
- Correction d'un blocage lors de l'installation de Playwright dans les tests E2E. [#3591](https://github.com/SocialGouv/egapro/issues/3591)
- Suppression des tests E2E lors de la fusion des tâches vers les fonctionnalités épiques. [#3635](https://github.com/SocialGouv/egapro/issues/3635)
- Correction d'un problème de migration silencieuse en incrémentant le numéro de migration. [#3559](https://github.com/SocialGouv/egapro/issues/3559)

### Autres changements
- Ajout d'outils de planification et de dimensionnement de sprint. [#3644](https://github.com/SocialGouv/egapro/issues/3644)
- Alignement visuel du `CompanyBanner` avec Figma. [#3532](https://github.com/SocialGouv/egapro/issues/3573)
- Alignement de la typographie et du padding du dropdown "Mon espace" avec Figma. [#3525](https://github.com/SocialGouv/egapro/issues/3554)
- Alignement de l'illustration de `ResourceBanner` à droite. [#3526](https://github.com/SocialGouv/egapro/issues/3552)
- Documentation de l'architecture et des fonctionnalités de EGAPRO V2. [#3391](https://github.com/SocialGouv/egapro/issues/3390), [#3389](https://github.com/SocialGouv/egapro/issues/3389)
