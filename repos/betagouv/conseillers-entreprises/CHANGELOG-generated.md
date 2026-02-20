## Changelog : conseillers-entreprises (30 derniers jours)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'accessibilité du site (conformité RGAA), l'ajout de nouvelles fonctionnalités pour le suivi des antennes régionales, et l'amélioration de la gestion des données, notamment avec l'intégration du code INSEE et la correction de bugs liés à la recherche et à la création de diagnostics. Des optimisations techniques et des mises à jour de dépendances ont également été réalisées.

### Évolutions fonctionnelles
- Ajout d'un onglet de suivi des antennes régionales, permettant de visualiser des informations et des statistiques sur les activités de conseil (#4230).
- Amélioration de la gestion du code INSEE dans les formulaires et la recherche d'entreprises, avec l'intégration de la gem `decoupage-administratif` (#4214).
- Correction d'un bug empêchant la suppression d'experts ayant des missions en cours (#4199).
- Amélioration de la gestion des erreurs lors de la création de diagnostics (#4214).
- Ajout d'un bandeau d'information configurable pour afficher des messages importants sur certaines pages (#4262).
- Ajout d'un message de confidentialité dans la modale de présentation des personnes (#4263).
- Correction d'un crash dans l'interface d'administration lors de la gestion des thèmes des landing pages régionales (#4268).
- Ajout d'un support pour l'intégration d'AppSignal pour le monitoring et le suivi des performances (#4265, #4278).

### Évolutions techniques
- Mise à jour de plusieurs dépendances, notamment webpack, lodash, rack et d'autres packages npm/yarn (#4245, #4270, #4231, #4203).
- Refactorisation du code pour améliorer la lisibilité et la maintenabilité, notamment dans la gestion des formulaires et des requêtes API (#4214).
- Amélioration de la couverture de tests avec l'ajout de tests RSpec et l'intégration de SimpleCov pour le suivi de la couverture de code (#4257).
- Utilisation de gem.coop comme source de gems Ruby (#4232).
- Suppression de code obsolète et de configurations inutiles (#4253, #4266).
- Migration vers une nouvelle approche pour la gestion des codes INSEE, améliorant la précision et la performance (#4214).
- Amélioration de la gestion des erreurs et des retours d'information à l'utilisateur (#4250).
- Ajout de TimeDurationService::Years pour faciliter les calculs de durée (#4224).

### Autres changements
- Ajout d'un fichier `.vscode` pour les paramètres de l'éditeur VS Code (supprimé du tracking git ensuite) (#4277, #4278).
- Mise à jour de la documentation README avec des informations sur AppSignal (#4278).
- Ajout d'un crawl-delay dans le fichier robots.txt pour améliorer le respect des robots d'indexation (#4228).
- Correction de typos et amélioration de la qualité du code (#4233, #4256).
- Amélioration de l'accessibilité du site web pour répondre aux critères RGAA (Référentiel Général d'Accessibilité pour les Administrations) (#4214).
- Suppression de la possibilité d'utiliser `local: true` dans les formulaires (#4253, #4266).
- Désactivation de robots dans l'environnement de staging (#4239).
