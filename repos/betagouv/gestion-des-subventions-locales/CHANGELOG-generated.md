## Changelog : gestion-des-subventions-locales (30 derniers jours, au 20 mai 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de la gestion des dossiers et des subventions, notamment en ce qui concerne l'intégration avec les Démarches Numériques (DN) et la gestion des notifications. Des optimisations de performance ont également été apportées, ainsi que des corrections de bugs et des améliorations de l'expérience utilisateur, notamment au niveau des filtres et de la navigation.

### Évolutions fonctionnelles
- **Gestion des dossiers:**
    - Possibilité de filtrer les dossiers par groupe instructeur via le proxy DS. [#723](https://github.com/betagouv/gestion-des-subventions-locales/issues/723)
    - Désactivation des dossiers supprimés/archivés depuis DS. [#716](https://github.com/betagouv/gestion-des-subventions-locales/issues/716)
    - Amélioration du formatage de l'adresse du demandeur dans les documents. [#718](https://github.com/betagouv/gestion-des-subventions-locales/issues/718)
    - Correction du dropdown de sélection de statut dans la page projet. [#717](https://github.com/betagouv/gestion-des-subventions-locales/issues/717)
    - Suppression du demandeur dupliqué au niveau du dossier, ne conservant que celui du dossier principal. [#670](https://github.com/betagouv/gestion-des-subventions-locales/issues/670)
- **Démarches Numériques (DN):**
    - Gestion correcte des démarches archivées. [#720](https://github.com/betagouv/gestion-des-subventions-locales/issues/720)
    - Possibilité de récupérer un dossier depuis DN via une action dans le BO. [#696](https://github.com/betagouv/gestion-des-subventions-locales/issues/696)
    - Utilisation des champs actifs d'une démarche DN. [#668](https://github.com/betagouv/gestion-des-subventions-locales/issues/668)
    - Amélioration du proxy DN pour éviter les timeouts Scalingo avec un heartbeat streamé. [#676](https://github.com/betagouv/gestion-des-subventions-locales/issues/676)
    - Restriction des champs Demarche et filtrage des dossiers supprimés dans le proxy DS. [#692](https://github.com/betagouv/gestion-des-subventions-locales/issues/692)
- **Notifications:**
    - Découplage de la notification de refus/classement du changement de statut. [#719](https://github.com/betagouv/gestion-des-subventions-locales/issues/719)
    - Possibilité de rendre le QR code de suivi optionnel sur les documents générés. [#720](https://github.com/betagouv/gestion-des-subventions-locales/issues/720)
    - Génération de documents en masse dans une modale et téléchargement via le stockage. [#712](https://github.com/betagouv/gestion-des-subventions-locales/issues/712)
    - Amélioration de la gestion des erreurs lors de la génération de notifications.
    - Possibilité de fermer la modale "Vous ne faites pas partie du groupe d'instructeurs". [#690](https://github.com/betagouv/gestion-des-subventions-locales/issues/690)
- **Filtres et Recherche:**
    - Ajout d'un filtre EPCI sur les pages projet, programmation et simulation. [#673](https://github.com/betagouv/gestion-des-subventions-locales/issues/673)
    - Ajout d'une recherche sur l'intitulé, la raison sociale et le numéro de dossier. [#701](https://github.com/betagouv/gestion-des-subventions-locales/issues/701)
    - Évaluation paresseuse des choix dans les FilterSet pour améliorer les performances. [#703](https://github.com/betagouv/gestion-des-subventions-locales/issues/703)
- **Interface Utilisateur:**
    - Ajout d'en-têtes de colonnes fixes lors du défilement des listes de projets, programmations et simulations. [#704](https://github.com/betagouv/gestion-des-subventions-locales/issues/704)
    - Ouverture du dropdown de statut sans casser les colonnes stickies. [#711](https://github.com/betagouv/gestion-des-subventions-locales/issues/711)

### Évolutions techniques
- Refactorisation de l'utilisation des managers `Active*Manager` vers des méthodes `queryset .active()`.
- Ajout d'un champ `is_active` sur `Dossier` et mise à jour des managers associés.
- Optimisation de la génération d'arrêtés/lettres en masse. [#714](https://github.com/betagouv/gestion-des-subventions-locales/issues/714)
- Mise à jour des dépendances vulnérables signalées par Dependabot. [#710](https://github.com/betagouv/gestion-des-subventions-locales/issues/710)
- Ajout de la librairie `django-query-counter` pour le suivi des requêtes SQL. [#671](https://github.com/betagouv/gestion-des-subventions-locales/issues/671)
- Amélioration de la gestion des erreurs GraphQL dans le proxy DS.
- Correction de l'URL du script HeatmapSessionRecording de Matomo. [#687](https://github.com/betagouv/gestion-des-subventions-locales/issues/687)
- Mise en place d'une commande `just release-dry-run` pour prévisualiser les releases. [#680](https://github.com/betagouv/gestion-des-subventions-locales/issues/680)
- Ajout de tests pour les branches hotfix. [#686](https://github.com/betagouv/gestion-des-subventions-locales/issues/686)

### Autres changements
- Documentation : introduction d'un fichier `AGENTS.md` pour guider les agents de code. [#715](https://github.com/betagouv/gestion-des-subventions-locales/issues/715)
- Documentation : ajout d'informations sur l'utilisation des branches hotfix pour le déploiement par tag. [#722](https://github.com/betagouv/gestion-des-subventions-locales/issues/722)
- Correction de la FAQ. [#707](https://github.com/betagouv/gestion-des-subventions-locales/issues/707)
- Amélioration du formatage de l'adresse dans les documents.
- Correction de bugs mineurs et améliorations de la qualité du code.
- Mise à jour des lock files et garde-fou CI contre la dérive. [#713](https://github.com/betagouv/gestion-des-subventions-locales/issues/713)
