## Changelog : gestion-des-subventions-locales (30 derniers jours, au 2026-05-19)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment au niveau de la gestion des documents, des filtres et des statuts des dossiers. Des optimisations techniques ont également été apportées pour améliorer la performance et la stabilité de l'application, en particulier concernant l'intégration avec les Démarches Numériques et la gestion des erreurs.

### Évolutions fonctionnelles
- Amélioration du formatage de l'adresse du demandeur dans les documents générés. [#718](https://github.com/betagouv/gestion-des-subventions-locales/issues/718)
- Correction du dropdown de sélection de statut dans la page projet. [#717](https://github.com/betagouv/gestion-des-subventions-locales/issues/717)
- Génération de l'export de documents en fin d'assistant et téléchargement via le stockage sécurisé. [#712](https://github.com/betagouv/gestion-des-subventions-locales/issues/712)
- Autorisation des tabulations dans les arrêtés/lettres de notification. [#705](https://github.com/betagouv/gestion-des-subventions-locales/issues/705)
- Correction de la FAQ. [#707](https://github.com/betagouv/gestion-des-subventions-locales/issues/707)
- Ouverture du dropdown de statut sans casser les colonnes stickies. [#711](https://github.com/betagouv/gestion-des-subventions-locales/issues/711)
- Ajout de filtres de recherche sur les listes de projets, simulations et programmations. [#701](https://github.com/betagouv/gestion-des-subventions-locales/issues/701)
- Ajout d'un filtre EPCI sur les pages projet, programmation et simulation. [#673](https://github.com/betagouv/gestion-des-subventions-locales/issues/673)
- Changement de statut en lot sur la page de simulation. [#661](https://github.com/betagouv/gestion-des-subventions-locales/issues/661)
- Affichage de la priorité du dossier si plusieurs ont été déposés par le même demandeur. [#675](https://github.com/betagouv/gestion-des-subventions-locales/issues/675)
- Mise en place d'une FAQ initiale. [#672](https://github.com/betagouv/gestion-des-subventions-locales/issues/672)
- Possibilité de fermer la modale "Vous ne faites pas partie du groupe d'instructeurs". [#690](https://github.com/betagouv/gestion-des-subventions-locales/issues/690)
- Ajout de titres de colonnes visibles au scroll dans les listes. [#704](https://github.com/betagouv/gestion-des-subventions-locales/issues/704)
- Amélioration de la gestion des documents signés avec rattachement automatique des scans signés par QR code. [#709](https://github.com/betagouv/gestion-des-subventions-locales/issues/709)

### Évolutions techniques
- Optimisation de la génération d'arrêtés/lettres en masse. [#714](https://github.com/betagouv/gestion-des-subventions-locales/issues/714)
- Correction d'un problème de N+1 requests.
- Mise à jour des dépendances vulnérables signalées par Dependabot. [#710](https://github.com/betagouv/gestion-des-subventions-locales/issues/710)
- Allègement de la requête GraphQL vers les Démarches Numériques pour éviter les timeouts. [#691](https://github.com/betagouv/gestion-des-subventions-locales/issues/691)
- Stream d'un heartbeat pour éviter les timeouts Scalingo du proxy DS. [#676](https://github.com/betagouv/gestion-des-subventions-locales/issues/676)
- Amélioration de la gestion des erreurs et des logs.
- Refactoring de la génération de documents en masse pour utiliser une modale. [#697](https://github.com/betagouv/gestion-des-subventions-locales/issues/697)
- Évaluation paresseuse des choix dans les FilterSet pour améliorer la performance. [#703](https://github.com/betagouv/gestion-des-subventions-locales/issues/703)
- Ajout de la librairie django-query-counter pour le profiling des requêtes SQL. [#671](https://github.com/betagouv/gestion-des-subventions-locales/issues/671)
- Mise à jour du proxy DN pour gérer les champs actifs d'une démarche et filtrer les dossiers supprimés. [#692](https://github.com/betagouv/gestion-des-subventions-locales/issues/692)

### Autres changements
- Introduction d'un fichier `AGENTS.md` pour guider les agents de code. [#715](https://github.com/betagouv/gestion-des-subventions-locales/issues/715)
- Réalignement des lock files et garde-fou CI contre la dérive. [#713](https://github.com/betagouv/gestion-des-subventions-locales/issues/713)
- Ajout de tests CI pour les branches hotfix/*
- Correction de typos CSS.
- Amélioration de la documentation et des messages d'erreur.
- Suppression du Demandeur (doublon) pour ne conserver que le demandeur au niveau du dossier. [#670](https://github.com/betagouv/gestion-des-subventions-locales/issues/670)
- Retrait du dotation_projet des simulations hors-périmètre lorsque le périmètre du dossier a changé. [#663](https://github.com/betagouv/gestion-des-subventions-locales/issues/663)
