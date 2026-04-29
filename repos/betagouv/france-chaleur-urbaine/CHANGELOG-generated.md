## Changelog : france-chaleur-urbaine (30 derniers jours, au 28 avril 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de l'expérience utilisateur, notamment sur le simulateur de raccordement, la page "Qui sommes-nous" et la gestion des données des réseaux de chaleur. Des corrections de bugs et des optimisations techniques ont également été apportées pour améliorer la stabilité et la performance de la plateforme. L'ajout de la gestion des écoréseaux est une nouveauté importante.

### Évolutions fonctionnelles
- **Simulateur de raccordement :** Refonte complète du simulateur, incluant une nouvelle interface utilisateur, une meilleure gestion des calculs et des conditions d'éligibilité, et une intégration avec la nouvelle version de publi.codes. [#1234](https://github.com/betagouv/france-chaleur-urbaine/issues/1234)
- **Page "Qui sommes-nous" :** Mise à jour du contenu et du design de la page, avec notamment la suppression des icônes de l'équipe et une clarification du budget. [#1232](https://github.com/betagouv/france-chaleur-urbaine/issues/1232)
- **Gestion des écoréseaux :** Ajout de la gestion des écoréseaux, incluant l'importation de données, l'affichage sur la carte et dans les listes de réseaux, et l'ajout d'une colonne dédiée dans l'administration. [#1224](https://github.com/betagouv/france-chaleur-urbaine/issues/1224)
- **Collecte de contact non raccordable :** Amélioration du formulaire de collecte de contact pour les utilisateurs non raccordables, incluant un bouton de réinitialisation et une gestion améliorée de l'état du formulaire. [#1236](https://github.com/betagouv/france-chaleur-urbaine/issues/1236)
- **Aide "Coup de pouce" :** Mise à jour des conditions d'attribution de l'aide "Coup de pouce". [#1231](https://github.com/betagouv/france-chaleur-urbaine/issues/1231)
- **Tableau des réseaux de chaleur :** Ajout de filtres et de colonnes supplémentaires au tableau des réseaux de chaleur dans l'administration.
- **Emails :** Amélioration du style et de l'encodage des emails, avec l'ajout du logo ADEME.

### Évolutions techniques
- **Refactoring du code :** Plusieurs refactorings ont été effectués pour améliorer la lisibilité et la maintenabilité du code, notamment dans les modules de simulation et de gestion des adresses.
- **Mise à jour des dépendances :** Mise à jour des dépendances du projet, incluant remark-directive-rehype et typescript. [#1229](https://github.com/betagouv/france-chaleur-urbaine/issues/1229)
- **Amélioration des tests :** Correction de bugs dans les tests et ajout de nouveaux tests pour améliorer la couverture du code.
- **Optimisation des images :** Conversion des images au format WebP pour réduire leur taille et améliorer les performances.
- **Utilisation de Tailwind CSS :** Migration progressive vers Tailwind CSS pour le style de certains composants.
- **Gestion des erreurs :** Amélioration de la gestion des erreurs et des messages d'erreur affichés à l'utilisateur.

### Autres changements
- **Documentation :** Mise à jour de la documentation pour refléter les changements apportés au projet.
- **Statistiques :** Mise à jour des statistiques mensuelles.
- **Configuration :** Modifications de la configuration pour améliorer la sécurité et la performance.
- **Linting et formatage :** Application de règles de linting et de formatage pour assurer la cohérence du code.
- **Suppression de code inutile :** Suppression de code obsolète ou inutile pour simplifier le projet.
- **Correction de coquilles et d'erreurs typographiques.**
- **Amélioration du tracking Matomo et Posthog.**
- **Correction de bugs mineurs et améliorations de l'interface utilisateur.**
