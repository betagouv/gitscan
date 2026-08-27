## Changelog : gestion-des-subventions-locales (30 derniers jours, au 27 août 2026)

### Résumé
Ce mois-ci, l'outil a été enrichi de fonctionnalités de gestion de masse, notamment pour la génération de lettres de refus, et d'un système de notification plus visible et sécurisé. L'interface utilisateur a également été modernisée pour offrir une navigation plus fluide et une meilleure accessibilité.

### Évolutions fonctionnelles
- **Gestion des notifications** : 
    - Ajout de badges et de statuts de notification directement dans les listes de projets et l'onglet dédié pour une meilleure visibilité.
    - Sécurisation du workflow : empêche désormais la génération ou l'import de documents lorsqu'un projet est en cours de notification [#790].
- **Automatisation documentaire** :
    - Possibilité de générer et de télécharger en masse des lettres de refus ou de classement sans suite [#833].
    - Ajout de la possibilité d'uploader des documents lors de la génération de lettres de refus [#832].
    - Nouveau bouton permettant de télécharger l'ensemble des documents générés en une seule fois [#802].
- **Expérience utilisateur** :
    - Amélioration de la réactivité des formulaires (zonage, budgets) grâce à l'intégration de HTMX.
    - Ajout d'indicateurs de chargement lors de la sauvegarde des formulaires pour une meilleure perception du traitement.

### Évolutions techniques
- **Performances** :
    - Optimisation de l'onglet de notification par la suppression de requêtes SQL redondantes (problème de N+1) [#840].
    - Allègement du contexte de données chargé pour les différents onglets de la page projet [#842].
- **Accessibilité (A11y)** :
    - Amélioration de l'accessibilité pour les lecteurs d'écran via la protection des emojis et des icônes décoratives avec l'attribut `aria-hidden` [#778].
- **Architecture et Refactoring** :
    - Migration de plusieurs formulaires vers une infrastructure de fragments partagés utilisant HTMX.
    - Réorganisation de la structure des fichiers du projet (déplacement de modules vers des sous-répertoires dédiés).
    - Refactorisation de plusieurs composants pour utiliser des "inclusion tags" et des mixins, améliorant la maintenabilité du code.

### Autres changements
- **Configuration et outils** :
    - Mise en place de Dependabot pour l'automatisation de la mise à jour des dépendances.
    - Ajustements de l'environnement de développement (outils `uv` et `precommit`).
    - Nettoyage de scripts internes et de la structure de fichiers.
