## Changelog : egapro (30 derniers jours, au 2026-06-04)

### Résumé
Les dernières semaines ont été marquées par d'importantes améliorations de l'expérience utilisateur, notamment au niveau de l'administration et du parcours de déclaration. Des efforts considérables ont également été déployés pour améliorer la robustesse de la plateforme, en particulier concernant la gestion des statuts, le cache et la pipeline CI/CD.  De nouvelles statistiques ont été ajoutées pour un meilleur suivi de l'utilisation de la plateforme.

### Évolutions fonctionnelles
- Intégration de l'historique des statuts dans l'application, permettant un suivi plus précis de l'avancement des déclarations. [#3584](https://github.com/SocialGouv/egapro/issues/3584) [#3611](https://github.com/SocialGouv/egapro/issues/3611)
- Affichage du récapitulatif de la déclaration sur la page de détail de l'administration. [#3437](https://github.com/SocialGouv/egapro/issues/3437) [#3590](https://github.com/SocialGouv/egapro/issues/3590)
- Amélioration des URLs des emails envoyés par le système de notifications. [#3606](https://github.com/SocialGouv/egapro/issues/3606)
- Refonte de l'interface d'administration : élargissement du layout et ajout de statistiques sur le dashboard. [#3566](https://github.com/SocialGouv/egapro/issues/3566) [#3586](https://github.com/SocialGouv/egapro/issues/3586)
- Ajout de nouvelles statistiques : distribution des scores publics, taux d'abandon par étape, funnel de complétion et taux de déclaration. [#3551](https://github.com/SocialGouv/egapro/issues/3551), [#3218](https://github.com/SocialGouv/egapro/issues/3218) [#3546](https://github.com/SocialGouv/egapro/issues/3546), [#3222](https://github.com/SocialGouv/egapro/issues/3222) [#3545](https://github.com/SocialGouv/egapro/issues/3545), [#3214](https://github.com/SocialGouv/egapro/issues/3214) [#3513](https://github.com/SocialGouv/egapro/issues/3513)
- Exposition de l'historique des statuts dans l'API SUIT. [#3472](https://github.com/SocialGouv/egapro/issues/3472) [#3503](https://github.com/SocialGouv/egapro/issues/3503)
- Gestion du statut "annulé" pour les déclarations. [#3133](https://github.com/SocialGouv/egapro/issues/3133) [#3431](https://github.com/SocialGouv/egapro/issues/3431)
- Amélioration de la validation du champ vide et ajout d'une alerte GIP sur onChange dans l'étape 1 du questionnaire. [#3544](https://github.com/SocialGouv/egapro/issues/3544)
- Correction de l'alignement de la typographie et du padding du menu "Mon espace". [#3525](https://github.com/SocialGouv/egapro/issues/3525) [#3554](https://github.com/SocialGouv/egapro/issues/3554)
- Correction de l'alignement de l'illustration ResourceBanner. [#3526](https://github.com/SocialGouv/egapro/issues/3526) [#3552](https://github.com/SocialGouv/egapro/issues/3552)

### Évolutions techniques
- Ajout d'un agent "tu-dev" pour la création et l'exécution de tests unitaires et d'intégration. [#3620](https://github.com/SocialGouv/egapro/issues/3620)
- Refactoring du système de notifications avec extraction du kit de templates React Email. [#3561](https://github.com/SocialGouv/egapro/issues/3561)
- Mise en place d'un système de cache avec sauvegarde en base de données. [#3484](https://github.com/SocialGouv/egapro/issues/3484) [#3537](https://github.com/SocialGouv/egapro/issues/3537)
- Correction d'un blocage dans l'installation de Playwright lors des tests E2E. [#3591](https://github.com/SocialGouv/egapro/issues/3591)
- Amélioration de la pipeline CI/CD : discipline de logging, détection des blocages et rapports automatiques. [#3423](https://github.com/SocialGouv/egapro/issues/3423)
- Amélioration de l'orchestration de la pipeline. [#3403](https://github.com/SocialGouv/egapro/issues/3403)
- Refonte du mock GIP-MDS pour supporter 5 buckets de personnel. [#3497](https://github.com/SocialGouv/egapro/issues/3497)

### Autres changements
- Documentation de l'architecture et des fonctionnalités de la V2 d'EgaPro. [#3390](https://github.com/SocialGouv/egapro/issues/3390), [#3389](https://github.com/SocialGouv/egapro/issues/3389)
- Documentation des parcours utilisateurs de la V2 d'EgaPro. [#3391](https://github.com/SocialGouv/egapro/issues/3391)
- Désactivation de l'autocomplétion du navigateur sur tous les formulaires. [#3539](https://github.com/SocialGouv/egapro/issues/3539) [#3548](https://github.com/SocialGouv/egapro/issues/3548)
- Ajout d'un agent "doc-writer" pour la documentation et intégration avec la boucle épique. [#3409](https://github.com/SocialGouv/egapro/issues/3409)
- Mise en place d'un mirroring de la documentation vers le wiki GitHub. [#3408](https://github.com/SocialGouv/egapro/issues/3408)
