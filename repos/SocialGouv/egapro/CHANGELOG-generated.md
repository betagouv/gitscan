## Changelog : egapro (30 derniers jours, au 7 mai 2026)

### Résumé
Les dernières semaines ont été marquées par des améliorations significatives de l'expérience utilisateur, notamment sur les étapes de la déclaration et dans l'interface d'administration. Des efforts importants ont également été consacrés à l'amélioration de la robustesse et de l'observabilité de la plateforme, ainsi qu'à l'intégration de nouvelles fonctionnalités pour la gestion des campagnes et des référents.

### Évolutions fonctionnelles
- Amélioration de l'interface utilisateur des étapes de déclaration (Effectifs, Récapitulatif, CSE) pour une meilleure conformité avec les maquettes Figma [#3320](https://github.com/SocialGouv/egapro/issues/3320), [#3325](https://github.com/SocialGouv/egapro/issues/3325), [#3324](https://github.com/SocialGouv/egapro/issues/3324).
- Ajout de colonnes de pourcentages dans la déclaration [#3379](https://github.com/SocialGouv/egapro/issues/3379).
- Implémentation de la gestion du statut "annulé" pour les déclarations [#3431](https://github.com/SocialGouv/egapro/issues/3133).
- Ajout d'une page de recherche publique pour les référents [#3234](https://github.com/SocialGouv/egapro/issues/3198).
- Mise en place d'un diagramme de progression de campagne dans l'interface d'administration [#3286](https://github.com/SocialGouv/egapro/issues/3286).
- Amélioration du "mimoquage" (pré-remplissage) des données de déclaration, avec lecture seule et navigation entre les étapes [#3252](https://github.com/SocialGouv/egapro/issues/3252).
- Ajout d'un cache de déclaration pour pré-remplir les données et permettre un retour en arrière [#3406](https://github.com/SocialGouv/egapro/issues/3205).
- Ajout d'une fonctionnalité pour lier les déclarations à des fichiers d'évaluation conjointe [#3226](https://github.com/SocialGouv/egapro/issues/3145).
- Amélioration de la gestion des avis du CSE avec un horodatage dédié [#3271](https://github.com/SocialGouv/egapro/issues/3271).
- Ajout d'un sitemap et d'un fichier robots.txt pour le SEO [#3235](https://github.com/SocialGouv/egapro/issues/3235).

### Évolutions techniques
- Refactorisation de la recherche de référents pour supprimer les filtres inutiles [#3281](https://github.com/SocialGouv/egapro/issues/3281), [#3282](https://github.com/SocialGouv/egapro/issues/3282).
- Mise en place d'une couche de cache Redis avec Valkey pour améliorer les performances [#3228](https://github.com/SocialGouv/egapro/issues/3228).
- Amélioration de la pipeline CI/CD avec des événements de phase, une détection des blocages et un rapport automatique [#3410](https://github.com/SocialGouv/egapro/issues/3410), [#3423](https://github.com/SocialGouv/egapro/issues/3423).
- Intégration d'un agent "doc-writer" pour la documentation et l'automatisation des tâches [#3409](https://github.com/SocialGouv/egapro/issues/3409).
- Mise en place d'une pipeline d'IA pour automatiser certaines tâches [#3305](https://github.com/SocialGouv/egapro/issues/3305).
- Amélioration de la gestion des logs et de l'observabilité [#3410](https://github.com/SocialGouv/egapro/issues/3410).
- Mise en place de l'envoi d'accusés de réception par email via Tipimail [#3237](https://github.com/SocialGouv/egapro/issues/3177).
- Correction de bugs liés à l'orchestration de la pipeline [#3403](https://github.com/SocialGouv/egapro/issues/3403).
- Correction d'un problème de déconnexion OIDC [#3347](https://github.com/SocialGouv/egapro/issues/3347).

### Autres changements
- Documentation de l'architecture V2 d'EGAPRO [#3390](https://github.com/SocialGouv/egapro/issues/3390).
- Documentation des fonctionnalités V2 d'EGAPRO [#3389](https://github.com/SocialGouv/egapro/issues/3389).
- Synchronisation des documents de la documentation avec la wiki GitHub [#3408](https://github.com/SocialGouv/egapro/issues/3408).
- Correction de problèmes d'alignement et d'accessibilité dans l'interface utilisateur [#3371](https://github.com/SocialGouv/egapro/issues/3320), [#3370](https://github.com/SocialGouv/egapro/issues/3325), [#3361](https://github.com/SocialGouv/egapro/issues/3324).
- Correction de bugs divers liés à la navigation et à l'affichage des données [#3384](https://github.com/SocialGouv/egapro/issues/3266), [#3383](https://github.com/SocialGouv/egapro/issues/3383).
