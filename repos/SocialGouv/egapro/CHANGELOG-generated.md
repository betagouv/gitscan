## Changelog : egapro (30 derniers jours, au 2026-06-02)

### Résumé
Les dernières semaines ont été marquées par une refonte significative de l'interface d'administration (admin) d'EgaPro, avec l'ajout de tableaux de bord statistiques et d'informations récapitulatives sur les déclarations. Des améliorations ont également été apportées à l'expérience utilisateur, notamment au niveau de la validation des formulaires, de l'alignement visuel et de la gestion des statuts de déclaration. Enfin, des efforts ont été déployés pour optimiser les performances et la robustesse de la plateforme, notamment au niveau du cache et de la gestion des notifications.

### Évolutions fonctionnelles
- Ajout d'un récapitulatif de la déclaration sur la page de détail de l'administration. [#3437](https://github.com/SocialGouv/egapro/issues/3437) et [#3590](https://github.com/SocialGouv/egapro/issues/3590)
- Refonte de l'interface d'administration avec un layout élargi et l'ajout de tableaux de bord statistiques. [#3566](https://github.com/SocialGouv/egapro/issues/3566) et [#3586](https://github.com/SocialGouv/egapro/issues/3586)
- Ajout de statistiques sur la distribution des scores publics. [#3551](https://github.com/SocialGouv/egapro/issues/3551)
- Ajout de statistiques sur le taux d'abandon par étape. [#3218](https://github.com/SocialGouv/egapro/issues/3218) et [#3546](https://github.com/SocialGouv/egapro/issues/3546)
- Ajout de statistiques sur le funnel de complétion. [#3222](https://github.com/SocialGouv/egapro/issues/3222) et [#3545](https://github.com/SocialGouv/egapro/issues/3545)
- Ajout de statistiques sur le taux de déclaration. [#3214](https://github.com/SocialGouv/egapro/issues/3214) et [#3513](https://github.com/SocialGouv/egapro/issues/3513)
- Ajout de statistiques sur le délai moyen par étape. [#3217](https://github.com/SocialGouv/egapro/issues/3217) et [#3521](https://github.com/SocialGouv/egapro/issues/3521)
- Amélioration de l'étape "quartile" de la déclaration de rémunération avec des corrections visuelles. [#3553](https://github.com/SocialGouv/egapro/issues/3553)
- Gestion du statut "annulé" pour les déclarations. [#3431](https://github.com/SocialGouv/egapro/issues/3431)
- Correction des URLs des emails dans les notifications et refactorisation du système de templates. [#3606](https://github.com/SocialGouv/egapro/issues/3606)

### Évolutions techniques
- Refactorisation du système de cache avec sauvegarde en base de données. [#3484](https://github.com/SocialGouv/egapro/issues/3484) et [#3537](https://github.com/SocialGouv/egapro/issues/3537)
- Extraction du kit de templates React Email pour les notifications. [#3561](https://github.com/SocialGouv/egapro/issues/3561)
- Correction d'un blocage dans l'installation de Playwright en CI. [#3591](https://github.com/SocialGouv/egapro/issues/3591)
- Désactivation de l'autocomplétion du navigateur sur tous les formulaires. [#3539](https://github.com/SocialGouv/egapro/issues/3539) et [#3548](https://github.com/SocialGouv/egapro/issues/3548)
- Amélioration de l'orchestration des agents et de la gestion des erreurs. [#3403](https://github.com/SocialGouv/egapro/issues/3403) et [#3423](https://github.com/SocialGouv/egapro/issues/3423)
- Mise en place d'une meilleure observabilité du pipeline avec des événements, un suivi des coûts et une détection des blocages. [#3410](https://github.com/SocialGouv/egapro/issues/3410)
- Amélioration de la gestion des statuts de la démarche. [#3379](https://github.com/SocialGouv/egapro/issues/3379) et [#3405](https://github.com/SocialGouv/egapro/issues/3405)

### Autres changements
- Documentation de l'architecture et des fonctionnalités de la V2 d'EgaPro. [#3389](https://github.com/SocialGouv/egapro/issues/3389) et [#3390](https://github.com/SocialGouv/egapro/issues/3390)
- Documentation des parcours utilisateurs de la V2 d'EgaPro. [#3391](https://github.com/SocialGouv/egapro/issues/3391)
- Améliorations de l'alignement visuel et de l'accessibilité de certains éléments de l'interface. [#3525](https://github.com/SocialGouv/egapro/issues/3525), [#3526](https://github.com/SocialGouv/egapro/issues/3526), [#3535](https://github.com/SocialGouv/egapro/issues/3535), [#3475](https://github.com/SocialGouv/egapro/issues/3475), [#3320](https://github.com/SocialGouv/egapro/issues/3320) et [#3325](https://github.com/SocialGouv/egapro/issues/3325)
- Corrections de bugs mineurs et améliorations de la robustesse de la plateforme.
- Ajout d'un agent doc-writer et intégration avec le pipeline. [#3409](https://github.com/SocialGouv/egapro/issues/3409)
- Correction de la gestion des dates dans l'API SUIT. [#3486](https://github.com/SocialGouv/egapro/issues/3486)
- Amélioration du processus de logout OIDC. [#3347](https://github.com/SocialGouv/egapro/issues/3347)
