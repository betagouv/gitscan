## Changelog : gestion-des-subventions-locales (30 derniers jours, au 06 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur de la page projet, avec une refonte de l'affichage des informations, l'ajout de nouvelles fonctionnalités comme la gestion des notes et des simulations, et une amélioration de la gestion des filtres. Des optimisations de performance ont également été apportées, notamment pour la génération de rapports PDF.

### Évolutions fonctionnelles
- **Page Projet :** Refonte majeure de la page projet avec l'ajout d'une nouvelle section "Simulations" et une unification de la navigation. [#775](https://github.com/betagouv/gestion-des-subventions-locales/issues/775)
- **Gestion des notes :** Ajout de la possibilité de créer, lire, mettre à jour et supprimer des notes directement sur la page projet.
- **Filtres :** Amélioration de l'interface des filtres avec l'ajout d'une barre d'onglets pour les filtres actifs et une disposition plus compacte. [#759](https://github.com/betagouv/gestion-des-subventions-locales/issues/759)
- **Assiette de financement :** Ajout d'un champ modifiable pour l'assiette de financement au niveau du projet et affichage d'un bloc d'état en lecture seule.
- **Dotations :** Amélioration de l'affichage des informations de dotation et ajout de badges d'état.
- **Avis de la commission DETR :** Correction du formulaire d'avis de la commission DETR. [#774](https://github.com/betagouv/gestion-des-subventions-locales/issues/774)
- **Actions en masse :** Correction d'un bug empêchant la réinitialisation de la sélection après une action en masse. [#771](https://github.com/betagouv/gestion-des-subventions-locales/issues/771)
- **Accessibilité :** Ajout de liens de contournement pour faciliter la navigation au clavier. [#777](https://github.com/betagouv/gestion-des-subventions-locales/issues/777)

### Évolutions techniques
- **Génération de PDF :** La génération des exports PDF est désormais asynchrone via Celery, améliorant ainsi les performances et la réactivité de l'application. [#764](https://github.com/betagouv/gestion-des-subventions-locales/issues/764)
- **Refactoring :** Refactorisation de plusieurs composants pour améliorer la maintenabilité et la lisibilité du code.
- **Sécurité :** Journalisation des événements de sécurité. [#770](https://github.com/betagouv/gestion-des-subventions-locales/issues/770)
- **Gestion des timeouts :** Le timeout Gunicorn est désormais configurable.
- **Limitation des requêtes :** Limitation du nombre de requêtes simultanées vers le proxy DS pour améliorer la stabilité. [#758](https://github.com/betagouv/gestion-des-subventions-locales/issues/758)

### Autres changements
- **Documentation :** Ajout de documentation pour les nouvelles fonctionnalités.
- **Tests :** Ajout et mise à jour de tests unitaires et d'intégration.
- **Configuration :** Possibilité d'utiliser un fichier `justfile.local` pour les recettes personnelles. [#780](https://github.com/betagouv/gestion-des-subventions-locales/issues/780)
- **Historique :** Enregistrement des événements DS dans l'historique du projet. [#755](https://github.com/betagouv/gestion-des-subventions-locales/issues/755)
