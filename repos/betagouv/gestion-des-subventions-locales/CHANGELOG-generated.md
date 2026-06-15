## Changelog : gestion-des-subventions-locales (30 derniers jours, au 12 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la performance, l'import de documents, l'expérience utilisateur et la robustesse de l'application. Des optimisations ont été apportées pour accélérer le traitement des tâches et la compression des fichiers statiques. L'import de documents a été simplifié et amélioré, notamment pour les documents signés. L'interface utilisateur a été affinée avec des corrections de bugs et des améliorations de l'affichage.

### Évolutions fonctionnelles
- Possibilité d'importer des dossiers de tous les territoires gérés. [#749](https://github.com/betagouv/gestion-des-subventions-locales/issues/749)
- Ajout d'une page dédiée au publipostage avec un menu pour les modèles. [#750](https://github.com/betagouv/gestion-des-subventions-locales/issues/750)
- Possibilité de changer le statut de plusieurs projets en "refusé" ou "classé sans suite" en lot. [#726](https://github.com/betagouv/gestion-des-subventions-locales/issues/726)
- Amélioration du formatage de l'adresse du demandeur dans les documents générés. [#718](https://github.com/betagouv/gestion-des-subventions-locales/issues/718)
- Correction du dropdown de sélection de statut dans la page projet. [#717](https://github.com/betagouv/gestion-des-subventions-locales/issues/717)
- Possibilité de spécifier le nom du fichier PDF lors de la génération de notifications d'acceptation. [#720](https://github.com/betagouv/gestion-des-subventions-locales/issues/720)
- Ajout d'une option pour rendre le QR code de suivi optionnel sur les documents générés. [#720](https://github.com/betagouv/gestion-des-subventions-locales/issues/720)
- Amélioration de l'affichage des enveloppes sur les pages de programmation et de simulation (masquage de la colonne d'actions). [#752](https://github.com/betagouv/gestion-des-subventions-locales/issues/752)
- Unification de la page de détail d'un projet, pilotée par son état. [#753](https://github.com/betagouv/gestion-des-subventions-locales/issues/753)
- Affichage du périmètre, des dates Turgot et du report dans l'admin. [#748](https://github.com/betagouv/gestion-des-subventions-locales/issues/748)
- Possibilité d'importer en masse des documents signés scannés via un upload direct sur S3. [#739](https://github.com/betagouv/gestion-des-subventions-locales/issues/739)

### Évolutions techniques
- Activation de la compression WhiteNoise (gzip + Brotli) des fichiers statiques pour améliorer les performances. [#757](https://github.com/betagouv/gestion-des-subventions-locales/issues/757)
- Priorisation des tâches Celery en fonction du contexte d'appel pour une meilleure gestion des ressources. [#751](https://github.com/betagouv/gestion-des-subventions-locales/issues/751)
- Refactorisation du code pour améliorer la structure et la maintenabilité, notamment au niveau de la gestion des projets et de l'import de documents.
- Amélioration de la gestion des erreurs lors de la synchronisation des dossiers depuis DN.
- Ajout d'un verrou anti-concurrence sur la synchronisation des dossiers DS pour éviter les conflits. [#740](https://github.com/betagouv/gestion-des-subventions-locales/issues/740)
- Découplage de la notification de refus/classement du changement de statut. [#719](https://github.com/betagouv/gestion-des-subventions-locales/issues/719)
- Optimisation de la génération d'arrêtés/lettres en masse. [#714](https://github.com/betagouv/gestion-des-subventions-locales/issues/714)
- Suppression des rafraîchissements DS bloquants à l'ouverture des modales. [#743](https://github.com/betagouv/gestion-des-subventions-locales/issues/743)

### Autres changements
- Ajout d'un fichier `AGENTS.md` pour partager des conseils et des bonnes pratiques avec les agents de code. [#715](https://github.com/betagouv/gestion-des-subventions-locales/issues/715)
- Documentation : usage des branches hotfix pour le déploiement par tag. [#722](https://github.com/betagouv/gestion-des-subventions-locales/issues/722)
- Correction de bugs mineurs et améliorations de la qualité du code.
- Ajout de logs pour les actions des utilisateurs via l'admin Django. [#741](https://github.com/betagouv/gestion-des-subventions-locales/issues/741)
- Correction d'un test flaky lié à la création de collègues. [#738](https://github.com/betagouv/gestion-des-subventions-locales/issues/738)
- Correction de la perte du curseur des dossiers supprimés sur les pages vides. [#742](https://github.com/betagouv/gestion-des-subventions-locales/issues/742)
- Correction du décochage silencieux des filtres de type `ModelMultipleChoiceFilter`. [#737](https://github.com/betagouv/gestion-des-subventions-locales/issues/737)
