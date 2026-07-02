## Changelog : gestion-des-subventions-locales (30 derniers jours, au 01 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur avec une interface plus claire et réactive, notamment au niveau des filtres et de la navigation. Des optimisations de performance ont également été apportées, en particulier pour la génération de documents et la synchronisation des données avec DS. Enfin, des améliorations de la sécurité et du suivi des actions des utilisateurs ont été implémentées.

### Évolutions fonctionnelles
- Amélioration de l'interface de filtrage des projets : les filtres actifs sont maintenant affichés en permanence et la disposition a été repensée pour une meilleure ergonomie. [#759](https://github.com/betagouv/gestion-des-subventions-locales/issues/759)
- Génération de rapports PDF asynchrone : la génération des exports PDF est maintenant effectuée en arrière-plan via Celery, améliorant la réactivité de l'interface. [#764](https://github.com/betagouv/gestion-des-subventions-locales/issues/764)
- Correction du formulaire d'avis de la commission DETR. [#774](https://github.com/betagouv/gestion-des-subventions-locales/issues/774)
- Correction de la sélection de projets sur plusieurs pages. [#766](https://github.com/betagouv/gestion-des-subventions-locales/issues/766)
- Import de dossiers depuis tous les territoires gérés. [#749](https://github.com/betagouv/gestion-des-subventions-locales/issues/749)
- Affichage des informations de périmètre, des dates Turgot et du statut du report dans l'administration. [#748](https://github.com/betagouv/gestion-des-subventions-locales/issues/748)
- Ajout d'une entrée de menu dédiée pour les modèles de publipostage. [#750](https://github.com/betagouv/gestion-des-subventions-locales/issues/750)
- Unification de la page de détail d'un projet, pilotée par son état. [#753](https://github.com/betagouv/gestion-des-subventions-locales/issues/753)
- Possibilité d'importer des documents signés scannés via un chargement direct sur S3. [#739](https://github.com/betagouv/gestion-des-subventions-locales/issues/739)

### Évolutions techniques
- Mise en place d'un verrou Redis pour empêcher les synchronisations de dossiers DS concurrentes. [#740](https://github.com/betagouv/gestion-des-subventions-locales/issues/740)
- Optimisation de la compression des fichiers statiques avec WhiteNoise (gzip + Brotli). [#757](https://github.com/betagouv/gestion-des-subventions-locales/issues/757)
- Priorisation des tâches Celery en fonction du contexte d'appel. [#751](https://github.com/betagouv/gestion-des-subventions-locales/issues/751)
- Refactorisation de plusieurs composants pour utiliser des Class-Based Views (CBV) au lieu de Function-Based Views (FBV).
- Amélioration de la gestion des erreurs et des timeouts pour la génération de documents.
- Refactorisation de la gestion de l'historique des projets.
- Utilisation de l'importmap pour le cache-busting des fichiers JS.
- Suppression des rafraîchissements DS bloquants lors de l'ouverture de modales. [#743](https://github.com/betagouv/gestion-des-subventions-locales/issues/743)

### Autres changements
- Journalisation des événements de sécurité. [#770](https://github.com/betagouv/gestion-des-subventions-locales/issues/770)
- Ajout de tests unitaires et correction de tests existants.
- Mise à jour de la documentation.
- Journalisation des modifications des utilisateurs via l'admin Django. [#741](https://github.com/betagouv/gestion-des-subventions-locales/issues/741)
- Correction d'un test flaky et suppression d'un statut vide dans l'administration des projets. [#738](https://github.com/betagouv/gestion-des-subventions-locales/issues/738)
- Possibilité d'ajouter un fichier `justfile.local` pour les recettes personnelles. [#780](https://github.com/betagouv/gestion-des-subventions-locales/issues/780)
