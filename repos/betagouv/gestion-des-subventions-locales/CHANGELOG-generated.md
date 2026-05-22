## Changelog : gestion-des-subventions-locales (30 derniers jours, au 20 mai 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de l'expérience utilisateur, notamment au niveau de la gestion des dossiers et des notifications. Des optimisations ont également été apportées à l'intégration avec les Démarches Numériques (DN) et à la performance globale de l'application. Plusieurs corrections de bugs et améliorations de la documentation ont également été réalisées.

### Évolutions fonctionnelles
- Possibilité de filtrer les dossiers par groupe instructeur dans le proxy DS. [#723](https://github.com/betagouv/gestion-des-subventions-locales/issues/723)
- Amélioration de la gestion des dossiers archivés provenant de Démarches Numériques. [#716](https://github.com/betagouv/gestion-des-subventions-locales/issues/716)
- Découplage de la notification de refus/classement du changement de statut d'un dossier. [#719](https://github.com/betagouv/gestion-des-subventions-locales/issues/719)
- Possibilité de rendre le QR code de suivi optionnel sur les documents générés. [#720](https://github.com/betagouv/gestion-des-subventions-locales/issues/720)
- Ajout d'un filtre EPCI sur les pages projet, programmation et simulation. [#673](https://github.com/betagouv/gestion-des-subventions-locales/issues/673)
- Affichage de la priorité du dossier si plusieurs ont été déposés par le même demandeur. [#675](https://github.com/betagouv/gestion-des-subventions-locales/issues/675)
- Mise en place d'une FAQ pour aider les utilisateurs. [#672](https://github.com/betagouv/gestion-des-subventions-locales/issues/672)
- Amélioration du formatage de l'adresse du demandeur dans les documents. [#718](https://github.com/betagouv/gestion-des-subventions-locales/issues/718)
- Correction du dropdown de sélection de statut dans la page projet. [#717](https://github.com/betagouv/gestion-des-subventions-locales/issues/717)
- Génération de l'export de documents en fin d'assistant et téléchargement via le stockage. [#712](https://github.com/betagouv/gestion-des-subventions-locales/issues/712)
- Ajout de titres de colonnes fixes (sticky headers) dans les listes de projets, programmations et simulations. [#704](https://github.com/betagouv/gestion-des-subventions-locales/issues/704)
- Possibilité de rechercher des dossiers par intitulé, raison sociale et numéro de dossier. [#701](https://github.com/betagouv/gestion-des-subventions-locales/issues/701)
- Correction pour permettre la fermeture de la modale "Vous ne faites pas partie du groupe d'instructeurs". [#690](https://github.com/betagouv/gestion-des-subventions-locales/issues/690)

### Évolutions techniques
- Refactorisation de l'utilisation des managers `Active*Manager` par des méthodes `queryset .active()`.
- Ajout d'un champ `is_active` sur les dossiers et mise à jour des managers associés.
- Optimisation de la génération d'arrêtés/lettres en masse. [#714](https://github.com/betagouv/gestion-des-subventions-locales/issues/714)
- Amélioration de la gestion des erreurs et des timeouts avec le proxy Démarches Numériques (DS).
- Mise à jour des dépendances vulnérables signalées par Dependabot. [#710](https://github.com/betagouv/gestion-des-subventions-locales/issues/710)
- Ajout de la librairie `django-query-counter` pour l'analyse des requêtes SQL. [#671](https://github.com/betagouv/gestion-des-subventions-locales/issues/671)
- Amélioration de la gestion des erreurs GraphQL dans le proxy DS. [#678](https://github.com/betagouv/gestion-des-subventions-locales/issues/678)
- Correction de la configuration CI pour les branches hotfix. [#686](https://github.com/betagouv/gestion-des-subventions-locales/issues/686)

### Autres changements
- Documentation : introduction d'un fichier `AGENTS.md` pour guider les agents de code. [#715](https://github.com/betagouv/gestion-des-subventions-locales/issues/715)
- Documentation : ajout d'informations sur l'utilisation des branches hotfix pour le déploiement par tag. [#722](https://github.com/betagouv/gestion-des-subventions-locales/issues/722)
- Ajout du script HeatmapSessionRecording de Matomo. [#666](https://github.com/betagouv/gestion-des-subventions-locales/issues/666)
- Correction de l'URL du script HeatmapSessionRecording de Matomo. [#687](https://github.com/betagouv/gestion-des-subventions-locales/issues/687)
- Suppression des logs verbeux de `fontTools` en production. [#684](https://github.com/betagouv/gestion-des-subventions-locales/issues/684)
- Correction de l'affichage de la date de notification. [#695](https://github.com/betagouv/gestion-des-subventions-locales/issues/695)
- Autorisation des tabulations dans les arrêtés/lettres de notification. [#705](https://github.com/betagouv/gestion-des-subventions-locales/issues/705)
- Correction de la FAQ. [#707](https://github.com/betagouv/gestion-des-subventions-locales/issues/707)
- Correction de l'affichage des documents de l'autre dotation dans l'onglet Programmation. [#674](https://github.com/betagouv/gestion-des-subventions-locales/issues/674)
- Utilisation de l'adresse complète plutôt que reconstruite sur une ligne. [#669](https://github.com/betagouv/gestion-des-subventions-locales/issues/669)
- Mise à jour des modèles dans le formulaire de génération de documents en masse. [#706](https://github.com/betagouv/gestion-des-subventions-locales/issues/706)
