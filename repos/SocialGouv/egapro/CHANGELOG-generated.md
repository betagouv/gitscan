## Changelog : egapro (30 derniers jours, au 27 mai 2026)

### Résumé
Les dernières semaines ont été marquées par des améliorations significatives de l'expérience utilisateur, notamment au niveau de l'alignement visuel avec la charte graphique, de la gestion des erreurs et de la navigation. Des efforts importants ont également été consacrés à l'amélioration des statistiques et de l'export des données, ainsi qu'à l'optimisation de l'infrastructure et des pipelines de développement.

### Évolutions fonctionnelles
- Amélioration de l'alignement visuel de plusieurs éléments de l'interface utilisateur (ResourceBanner, étapes du formulaire, page récapitulative, etc.) pour correspondre aux maquettes Figma. [#3526](https://github.com/SocialGouv/egapro/issues/3526), [#3320](https://github.com/SocialGouv/egapro/issues/3320), [#3325](https://github.com/SocialGouv/egapro/issues/3325), [#3324](https://github.com/SocialGouv/egapro/issues/3324)
- Ajout d'une validation pour s'assurer que les champs ne sont pas vides dans l'étape "Effectifs" et alerte GIP sur le changement. [#3544](https://github.com/SocialGouv/egapro/issues/3544)
- Désactivation de l'autocomplétion du navigateur sur tous les formulaires pour améliorer la sécurité et la confidentialité des données. [#3539](https://github.com/SocialGouv/egapro/issues/3539)
- Amélioration de la navigation et des liens "Précédent" dans le parcours de déclaration. [#3485](https://github.com/SocialGouv/egapro/issues/3485), [#3266](https://github.com/SocialGouv/egapro/issues/3266)
- Ajout de nouvelles statistiques : taux de déclaration, taux d'abandon par étape, funnel de complétion, délai moyen par étape. [#3513](https://github.com/SocialGouv/egapro/issues/3513), [#3546](https://github.com/SocialGouv/egapro/issues/3546), [#3545](https://github.com/SocialGouv/egapro/issues/3545), [#3521](https://github.com/SocialGouv/egapro/issues/3521)
- Ajout de la gestion du statut "annulé" pour les déclarations. [#3431](https://github.com/SocialGouv/egapro/issues/3431)
- Ajout de l'infrastructure pour la gestion des envois d'emails (notifications). [#3466](https://github.com/SocialGouv/egapro/issues/3466)

### Évolutions techniques
- Refonte du système de cache avec sauvegarde en base de données pour améliorer les performances. [#3537](https://github.com/SocialGouv/egapro/issues/3537)
- Amélioration de l'orchestration des pipelines de développement et de l'observabilité. [#3423](https://github.com/SocialGouv/egapro/issues/3423), [#3410](https://github.com/SocialGouv/egapro/issues/3410)
- Mise en place d'un pipeline d'IA pour automatiser certaines tâches. [#3345](https://github.com/SocialGouv/egapro/issues/3345)
- Amélioration de la gestion des erreurs et de la journalisation. [#3559](https://github.com/SocialGouv/egapro/issues/3559)
- Expose l'ID de déclaration dans l'API SUIT. [#3481](https://github.com/SocialGouv/egapro/issues/3481)
- Amélioration de l'export des données via l'API SUIT, notamment en exposant l'historique des statuts. [#3503](https://github.com/SocialGouv/egapro/issues/3503)
- Suppression des seuils Q4 de l'API SUIT suite à une migration. [#3493](https://github.com/SocialGouv/egapro/issues/3493)

### Autres changements
- Documentation de l'architecture et des fonctionnalités de la version V2 d'EgaPro. [#3391](https://github.com/SocialGouv/egapro/issues/3391), [#3390](https://github.com/SocialGouv/egapro/issues/3390), [#3389](https://github.com/SocialGouv/egapro/issues/3389)
- Amélioration de la documentation du parcours utilisateur. [#3371](https://github.com/SocialGouv/egapro/issues/3371)
- Ajout de tests et d'améliorations de la qualité du code.
- Correction de problèmes mineurs d'interface utilisateur et d'accessibilité.
- Mise à jour des dépendances.
