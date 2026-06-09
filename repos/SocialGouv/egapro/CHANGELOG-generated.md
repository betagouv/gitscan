## Changelog : egapro (30 derniers jours, au 8 juin 2026)

### Résumé
Les dernières semaines ont été marquées par des améliorations significatives de l'expérience utilisateur, notamment dans le parcours de déclaration de rémunération, ainsi que par des avancées importantes dans les statistiques et le suivi des déclarations. Des corrections de bugs et des optimisations techniques ont également été apportées pour améliorer la stabilité et la performance de la plateforme.

### Évolutions fonctionnelles
- Amélioration de l'étape 5 du parcours de déclaration de rémunération avec des corrections visuelles et un focus sur l'ajout d'informations. [#3538](https://github.com/SocialGouv/egapro/issues/3538) [#3589](https://github.com/SocialGouv/egapro/issues/3589)
- Amélioration de l'étape de revue (étape 6) avec des ajustements visuels et une meilleure mise en évidence des informations importantes. [#3540](https://github.com/SocialGouv/egapro/issues/3540) [#3588](https://github.com/SocialGouv/egapro/issues/3588)
- Intégration de l'historique des statuts de la déclaration dans l'application, permettant un meilleur suivi de l'avancement. [#3584](https://github.com/SocialGouv/egapro/issues/3584) [#3611](https://github.com/SocialGouv/egapro/issues/3611)
- Correction des URLs des emails de notification et refactorisation du système de templates d'emails. [#3606](https://github.com/SocialGouv/egapro/issues/3606)
- Affichage du récapitulatif de la déclaration sur la page de détail de l'administration. [#3437](https://github.com/SocialGouv/egapro/issues/3437) [#3590](https://github.com/SocialGouv/egapro/issues/3590)
- Refonte de l'interface d'administration avec un élargissement du layout et l'ajout de statistiques sur le dashboard. [#3566](https://github.com/SocialGouv/egapro/issues/3566) [#3586](https://github.com/SocialGouv/egapro/issues/3586)
- Ajout de nouvelles statistiques : distribution des scores publics, taux d'abandon par étape, et funnel de complétion. [#3551](https://github.com/SocialGouv/egapro/issues/3551), [#3218](https://github.com/SocialGouv/egapro/issues/3218) [#3546](https://github.com/SocialGouv/egapro/issues/3546), [#3222](https://github.com/SocialGouv/egapro/issues/3222) [#3545](https://github.com/SocialGouv/egapro/issues/3545), [#3214](https://github.com/SocialGouv/egapro/issues/3214) [#3513](https://github.com/SocialGouv/egapro/issues/3513)
- Ajout de la possibilité d'exporter l'historique des statuts via l'API SUIT. [#3472](https://github.com/SocialGouv/egapro/issues/3472) [#3503](https://github.com/SocialGouv/egapro/issues/3503)
- Gestion du statut "annulé" pour les déclarations. [#3133](https://github.com/SocialGouv/egapro/issues/3133) [#3431](https://github.com/SocialGouv/egapro/issues/3431)

### Évolutions techniques
- Ajout d'un agent "tu-dev" pour la création et l'exécution de tests unitaires et d'intégration. [#3620](https://github.com/SocialGouv/egapro/issues/3620)
- Refactorisation du système de cache avec une sauvegarde en base de données. [#3484](https://github.com/SocialGouv/egapro/issues/3484) [#3537](https://github.com/SocialGouv/egapro/issues/3537)
- Extraction du kit de templates React Email pour une meilleure organisation et réutilisation. [#3561](https://github.com/SocialGouv/egapro/issues/3561)
- Correction d'un problème de blocage de l'installation de Playwright lors des tests E2E. [#3591](https://github.com/SocialGouv/egapro/issues/3591)
- Amélioration de la configuration du pipeline CI/CD pour une meilleure discipline de logging et des rapports automatiques. [#3423](https://github.com/SocialGouv/egapro/issues/3423)
- Ajout de documentation sur l'architecture et les fonctionnalités de la version V2 d'EgaPro. [#3391](https://github.com/SocialGouv/egapro/issues/3391), [#3390](https://github.com/SocialGouv/egapro/issues/3390), [#3389](https://github.com/SocialGouv/egapro/issues/3389)

### Autres changements
- Suppression des tests E2E lors de la fusion des tâches vers les fonctionnalités épiques. [#3635](https://github.com/SocialGouv/egapro/issues/3635)
- Diverses corrections visuelles et améliorations de l'interface utilisateur. [#3589](https://github.com/SocialGouv/egapro/issues/3589), [#3588](https://github.com/SocialGouv/egapro/issues/3588), [#3553](https://github.com/SocialGouv/egapro/issues/3553), [#3554](https://github.com/SocialGouv/egapro/issues/3554), [#3557](https://github.com/SocialGouv/egapro/issues/3557), [#3559](https://github.com/SocialGouv/egapro/issues/3559), [#3552](https://github.com/SocialGouv/egapro/issues/3552), [#3549](https://github.com/SocialGouv/egapro/issues/3549), [#3548](https://github.com/SocialGouv/egapro/issues/3548)
- Désactivation de l'autocomplétion du navigateur sur tous les formulaires. [#3539](https://github.com/SocialGouv/egapro/issues/3539) [#3548](https://github.com/SocialGouv/egapro/issues/3548)
- Correction de la validation du champ vide et ajout d'une alerte GIP sur le premier pas du parcours. [#3544](https://github.com/SocialGouv/egapro/issues/3544)
- Amélioration de l'alignement des éléments de l'interface utilisateur. [#3525](https://github.com/SocialGouv/egapro/issues/3525) [#3554](https://github.com/SocialGouv/egapro/issues/3554), [#3526](https://github.com/SocialGouv/egapro/issues/3526) [#3552](https://github.com/SocialGouv/egapro/issues/3552)
