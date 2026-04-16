## Changelog : eva-serveur (30 derniers jours, au 15 avril 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de l'expérience utilisateur, notamment dans la gestion des structures, des utilisateurs et des restitutions d'évaluation. Des efforts importants ont également été consacrés à la modernisation de l'interface utilisateur avec l'adoption du Design System Fr (DSFR) et à l'optimisation des performances. Des corrections de bugs et des améliorations de sécurité ont également été apportées.

### Évolutions fonctionnelles
- Amélioration de la gestion des structures : possibilité de créer des structures sans SIRET pour les super-admins, correction de bugs liés à la modification du SIRET et du code postal, anonymisation des données sensibles des structures supprimées. [#2345](lien vers issue/PR si applicable)
- Géolocalisation des structures : intégration de geo.api.gouv.fr pour une géolocalisation plus précise et fiable.
- Gestion des invitations : amélioration de la gestion des invitations, notamment pour les structures existantes, avec une page dédiée pour les invitations invalides.
- Restitutions d'évaluation : amélioration de l'affichage des restitutions, notamment pour les évaluations Eva Pro, avec l'intégration des offres de services des OPCO.
- Parcours utilisateurs : amélioration du parcours d'inscription et d'invitation, avec une meilleure gestion des alertes et des informations affichées.
- Gestion des OPCO : ajout de la possibilité de rattacher des parcours types aux OPCO, et de gérer les IDCC.
- Export des évaluations : correction d'un bug lié à la limite d'export des évaluations.

### Évolutions techniques
- Mise à jour des dépendances : actualisation de Rails, ActiveAdmin, Devise et d'autres dépendances pour bénéficier des dernières corrections et améliorations de sécurité.
- Migration vers le DSFR : remplacement progressif des composants Bootstrap par des composants du Design System Fr (DSFR) pour une meilleure cohérence visuelle et une maintenance simplifiée.
- Refactoring du code : refactoring de plusieurs parties du code, notamment le contrôleur des structures et la gestion des évaluations, pour améliorer la lisibilité, la maintenabilité et les performances.
- Amélioration des tests : ajout de nouveaux tests et amélioration des tests existants pour garantir la qualité du code.
- Anonymisation des données : amélioration de l'anonymisation des données des utilisateurs supprimés.
- Optimisation des performances : optimisation de l'affichage de l'index des évaluations Eva Pro.
- Suppression de code obsolète : suppression de code et de fichiers inutilisés.

### Autres changements
- Documentation : mise à jour de la documentation pour refléter les changements apportés.
- Configuration : ajout d'une variable d'environnement pour la limite d'export des évaluations.
- Correction de bugs mineurs : correction de divers bugs mineurs affectant l'interface utilisateur et le comportement de l'application.
- Amélioration de la gestion des messages flash et des styles CSS.
- Harmonisation du wording de certains éléments de l'interface utilisateur.
