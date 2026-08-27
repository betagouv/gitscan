## Changelog : Aidants_Connect (30 derniers jours, au 25 août 2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur l'amélioration majeure de l'accessibilité numérique de la plateforme et l'optimisation de l'interface pour les référents d'organisation, notamment via l'ajout de nouveaux indicateurs visuels et de raccourcis de navigation.

### Évolutions fonctionnelles
- **Optimisation de l'accueil des référents** : Ajout de tuiles d'accès rapide et de badges "à finaliser" pour mieux guider les utilisateurs dans leurs tâches [#1794].
- **Accompagnement à la configuration** : Mise en place de badges incitant les référents à configurer les thématiques administratives de leur organisation [#1790].
- **Gestion des rôles** : Introduction du label "co-référent".

### Évolutions techniques
- **Accessibilité (A11y)** : Travail de fond sur la structure sémantique et l'accessibilité de l'ensemble de l'application (en-tête, pied de page, menus de navigation, formulaires de création de mandat et pages de ressources) via l'utilisation de balises HTML5 et d'attributs ARIA [#1797, #1809].
- **Modèle de données** : Évolution du modèle `Organisation` avec l'ajout du champ `demarches_configured_at` pour le suivi de la configuration.
- **Tests** : Renforcement de la fiabilité de la suite de tests, incluant des tests d'accessibilité, des tests d'API et de modèles, ainsi que la correction de plusieurs régressions de tests [#1808].
- **Interface et Style** : Refactorisation du CSS et du SCSS du formulaire de création de mandat pour améliorer la mise en page, l'alignement et la maintenabilité du code.

### Autres changements
- **Nettoyage** : Suppression de migrations en double et de tests redondants pour alléger le dépôt.
