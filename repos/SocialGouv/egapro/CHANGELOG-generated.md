## Changelog : egapro (30 derniers jours, au 7 mai 2026)

### Résumé
Les dernières semaines ont été marquées par des améliorations significatives de l'expérience utilisateur, notamment sur les parcours de déclaration et l'interface d'administration. Des efforts importants ont également été consacrés à l'amélioration de l'architecture et de l'infrastructure du projet, avec l'intégration de nouveaux outils de caching et d'automatisation.

### Évolutions fonctionnelles
- Amélioration de l'interface utilisateur de "Mon Espace" avec un libellé plus court pour le CTA "Continuer" ([#3490](https://github.com/SocialGouv/egapro/issues/3490), [#3492](https://github.com/SocialGouv/egapro/issues/3492)).
- Correction de l'affichage des dates dans l'export des données ([#3486](https://github.com/SocialGouv/egapro/issues/3486)).
- Exposition de l'ID de déclaration dans l'API SUIT ([#3478](https://github.com/SocialGouv/egapro/issues/3481)).
- Recalcul des pourcentages à chaque étape de la déclaration pour garantir la cohérence des données ([#3475](https://github.com/SocialGouv/egapro/issues/3480)).
- Amélioration de la gestion du statut "annulé" pour les déclarations ([#3431](https://github.com/SocialGouv/egapro/issues/3431)).
- Ajout de la possibilité de pré-remplir les données de la déclaration à partir de la dernière soumission, notamment pour l'indicateur 7 ([#3246](https://github.com/SocialGouv/egapro/issues/3269)).
- Amélioration du parcours "mimoquage" avec des champs en lecture seule et une navigation simplifiée ([#3252](https://github.com/SocialGouv/egapro/issues/3252)).
- Ajout d'un lien vers les déclarations dans le menu latéral de l'administration ([#3275](https://github.com/SocialGouv/egapro/issues/3275)).
- Ajout d'un sitemap et d'un fichier robots.txt pour améliorer le référencement ([#3235](https://github.com/SocialGouv/egapro/issues/3235)).
- Correction de l'alignement et de l'accessibilité de plusieurs éléments de l'interface utilisateur, notamment les étapes de la déclaration et la page récapitulative ([#3320](https://github.com/SocialGouv/egapro/issues/3320), [#3325](https://github.com/SocialGouv/egapro/issues/3325), [#3324](https://github.com/SocialGouv/egapro/issues/3324)).

### Évolutions techniques
- Ajout d'une infrastructure pour la gestion des envois d'emails ([#3466](https://github.com/SocialGouv/egapro/issues/3466)).
- Intégration de Valkey, une couche de caching compatible Redis, pour améliorer les performances de Next.js ([#3228](https://github.com/SocialGouv/egapro/issues/3228)).
- Mise en place d'un pipeline d'automatisation avec un agent "doc-writer" et l'intégration d'une boucle épique ([#3409](https://github.com/SocialGouv/egapro/issues/3409)).
- Amélioration du pipeline CI/CD avec des corrections de configuration, une meilleure discipline de logging et un rapport d'état automatique ([#3423](https://github.com/SocialGouv/egapro/issues/3423)).
- Refactorisation de l'architecture pour l'ajout de colonnes de pourcentages dans la déclaration ([#3405](https://github.com/SocialGouv/egapro/issues/3405)).
- Amélioration de l'observabilité du pipeline avec des événements de phase, un suivi des coûts et une détection des blocages ([#3410](https://github.com/SocialGouv/egapro/issues/3410)).
- Implémentation d'un cache de déclaration pour améliorer la performance et faciliter le retour en arrière ([#3406](https://github.com/SocialGouv/egapro/issues/3406)).
- Correction de bugs dans l'orchestration du pipeline ([#3403](https://github.com/SocialGouv/egapro/issues/3403)).
- Mise en place d'un job Cron pour nettoyer les données d'audit en base de données ([#3270](https://github.com/SocialGouv/egapro/issues/3270)).
- Intégration de Tipimail pour l'envoi d'emails en production ([#3237](https://github.com/SocialGouv/egapro/issues/3238)).
- Ajout d'un composant gateway API ([#3304](https://github.com/SocialGouv/egapro/issues/3304)).

### Autres changements
- Documentation de l'architecture et des fonctionnalités de la version 2 d'EGAPRO ([#3390](https://github.com/SocialGouv/egapro/issues/3390), [#3389](https://github.com/SocialGouv/egapro/issues/3389)).
- Documentation des parcours utilisateurs de la version 2 d'EGAPRO ([#3391](https://github.com/SocialGouv/egapro/issues/3391)).
- Publication des documents dans le wiki GitHub ([#3408](https://github.com/SocialGouv/egapro/issues/3408)).
- Correction de divers problèmes d'alignement et d'accessibilité de l'interface utilisateur.
- Suppression de filtres inutiles dans l'administration.
