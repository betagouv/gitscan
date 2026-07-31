## Changelog : gestion-des-subventions-locales (30 derniers jours, au 30 juillet 2026)

### Résumé
Cette période a été marquée par une refonte majeure de la page projet, incluant l'ajout d'une nouvelle section "Simulations", une amélioration de l'interface utilisateur et des corrections de bugs. Des fonctionnalités d'import de données et de gestion des notifications ont également été implémentées. Enfin, des améliorations techniques ont été apportées, notamment la migration vers `uv` pour la gestion des dépendances.

### Évolutions fonctionnelles
- **Page Projet :** Refonte complète de la page projet avec ajout d'un onglet "Simulations" pour gérer les simulations de subventions. [#775](https://github.com/betagouv/gestion-des-subventions-locales/issues/775)
- **Dotations :** Amélioration de l'affichage et du filtrage des dotations sur la page projet.  Possibilité de filtrer par double dotation et mise à jour des badges d'état.
- **Notifications :** Refonte de l'onglet notification avec une nouvelle interface utilisateur. [#783](https://github.com/betagouv/gestion-des-subventions-locales/issues/783)
- **Formulaire Projet :** Correction et amélioration du formulaire de création/édition de projet. [#784](https://github.com/betagouv/gestion-des-subventions-locales/issues/784)
- **Lettre de Refus :** Ajout d'un modèle de lettre de refus pour les demandes de subvention. [#785](https://github.com/betagouv/gestion-des-subventions-locales/issues/785)
- **Import COG :** Ajout d'une ligne de commande pour importer les données du COG (INSEE). [#782](https://github.com/betagouv/gestion-des-subventions-locales/issues/782)
- **Notes :** Ajout de la gestion des notes sur la page projet (création, lecture, modification, suppression).
- **Accessibilité :** Ajout de liens d'évitement pour améliorer l'accessibilité du site. [#777](https://github.com/betagouv/gestion-des-subventions-locales/issues/777)
- **Filtre Catégories :** Le filtre sur les catégories est maintenant affiché en permanence. [#776](https://github.com/betagouv/gestion-des-subventions-locales/issues/776)
- **Journalisation Sécurité :** Journalisation des événements de sécurité pour une meilleure traçabilité. [#770](https://github.com/betagouv/gestion-des-subventions-locales/issues/770)

### Évolutions techniques
- **Gestion des Dépendances :** Migration de `pip-tools` vers `uv` pour une gestion plus performante des dépendances. [#786](https://github.com/betagouv/gestion-des-subventions-locales/issues/786) et [#57ded1ff](https://github.com/betagouv/gestion-des-subventions-locales/commit/57ded1ff)
- **Refactoring :** Refactoring important du code de la page projet, notamment l'utilisation de Stimulus pour la gestion des interactions et la suppression de code obsolète.
- **Tests :** Ajout et mise à jour de tests unitaires pour assurer la qualité du code.
- **Django Lint :** Mise à jour et corrections suite à l'utilisation de `djlint`.

### Autres changements
- Amélioration de la documentation et du code pour une meilleure maintenabilité.
- Corrections de bugs mineurs et améliorations de l'interface utilisateur.
- Ajout d'une recette `justfile` locale pour les besoins personnels des développeurs.
