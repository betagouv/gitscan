## Changelog : egapro (30 derniers jours, au 21 mai 2026)

### Résumé
Les dernières mises à jour d'EgaPro se concentrent sur l'amélioration des statistiques de déclaration, l'exposition de nouvelles données via l'API SUIT et la correction de plusieurs bugs d'interface utilisateur et de logique applicative. Des améliorations significatives ont également été apportées à l'infrastructure de pipeline et à la gestion des statuts de la démarche.

### Évolutions fonctionnelles
- Ajout de nouvelles statistiques :
    - Taux de déclaration [#3214](https://github.com/SocialGouv/egapro/issues/3214) [#3513](https://github.com/SocialGouv/egapro/issues/3513)
    - Délai moyen par étape [#3217](https://github.com/SocialGouv/egapro/issues/3521)
- L'API SUIT expose désormais l'historique des statuts [#3503](https://github.com/SocialGouv/egapro/issues/3503).
- Amélioration de la navigation et de l'affichage des étapes dans l'espace personnel [#3495](https://github.com/SocialGouv/egapro/issues/3495) et [#3485](https://github.com/SocialGouv/egapro/issues/3485).
- Gestion du statut "annulé" pour les déclarations [#3431](https://github.com/SocialGouv/egapro/issues/3431).
- Ajout de l'infrastructure pour l'envoi d'emails [#3466](https://github.com/SocialGouv/egapro/issues/3466).
- Ajout de colonnes de pourcentages dans la déclaration [#3405](https://github.com/SocialGouv/egapro/issues/3405).
- Page récapitulatif de la déclaration (lecture seule) [#3375](https://github.com/SocialGouv/egapro/issues/3375).

### Évolutions techniques
- Refonte du mock GIP-MDS pour supporter 5 tranches de taille d'effectif [#3497](https://github.com/SocialGouv/egapro/issues/3497).
- Amélioration du pipeline CI/CD :
    - Intégration de doc-writer agent et de la compétence /doc [#3409](https://github.com/SocialGouv/egapro/issues/3409).
    - Consolidation de la configuration, correction de bugs d'orchestration et ajout de rapports automatiques [#3423](https://github.com/SocialGouv/egapro/issues/3423) et [#3403](https://github.com/SocialGouv/egapro/issues/3403).
    - Ajout d'observabilité avec événements de phase, coût en direct et détection de blocages [#3410](https://github.com/SocialGouv/egapro/issues/3410).
    - Nettoyage automatique des worktrees et ajout de la compétence /open pour les tests PR locaux [#3345](https://github.com/SocialGouv/egapro/issues/3345).
- Mise en place d'un cache pour les données de déclaration afin d'améliorer la performance et de faciliter le retour en arrière [#3406](https://github.com/SocialGouv/egapro/issues/3406).
- Documentation de l'architecture et des fonctionnalités de la V2 [#3390](https://github.com/SocialGouv/egapro/issues/3390) et [#3389](https://github.com/SocialGouv/egapro/issues/3389).
- Amélioration de la gestion des logs et de la discipline de logging.

### Autres changements
- Correction de plusieurs problèmes d'alignement et d'accessibilité de l'interface utilisateur (UI) sur différentes pages (Mon Espace, Login, Déclaration) [#3344](https://github.com/SocialGouv/egapro/issues/3344), [#3340](https://github.com/SocialGouv/egapro/issues/3340), [#3371](https://github.com/SocialGouv/egapro/issues/3371), [#3361](https://github.com/SocialGouv/egapro/issues/3361), [#3330](https://github.com/SocialGouv/egapro/issues/3330).
- Suppression des seuils Q4 de l'API SUIT dans le cadre d'une migration [#3493](https://github.com/SocialGouv/egapro/issues/3493).
- Correction de bugs liés à la navigation et à l'affichage des étapes de la déclaration [#3492](https://github.com/SocialGouv/egapro/issues/3492), [#3486](https://github.com/SocialGouv/egapro/issues/3486), [#3384](https://github.com/SocialGouv/egapro/issues/3384), [#3266](https://github.com/SocialGouv/egapro/issues/3266).
- Amélioration de la gestion des erreurs et des messages d'erreur [#3383](https://github.com/SocialGouv/egapro/issues/3383).
- Correction de la déconnexion OIDC côté navigateur [#3347](https://github.com/SocialGouv/egapro/issues/3347).
- Correction de l'alignement des champs numériques [#3285](https://github.com/SocialGouv/egapro/issues/3285).
