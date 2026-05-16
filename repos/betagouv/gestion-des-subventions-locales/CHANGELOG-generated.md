## Changelog : gestion-des-subventions-locales (30 derniers jours, au 15 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment au niveau des simulations et des notifications. Des corrections de bugs et des optimisations de performance ont également été apportées, ainsi que des améliorations de la gestion des documents et du proxy vers les Démarches Numériques.

### Évolutions fonctionnelles
- Possibilité de filtrer les projets, programmations et simulations par EPCI. [#673](https://github.com/betagouv/gestion-des-subventions-locales/issues/673)
- Ajout d'une FAQ pour aider les utilisateurs. [#672](https://github.com/betagouv/gestion-des-subventions-locales/issues/672)
- Amélioration de l'affichage des documents dans l'onglet "Notifications". [#665](https://github.com/betagouv/gestion-des-subventions-locales/issues/665)
- Possibilité de changer le statut de plusieurs simulations en lot. [#661](https://github.com/betagouv/gestion-des-subventions-locales/issues/661)
- Affichage de la priorité du dossier lorsqu'il est déposé plusieurs fois par le même demandeur. [#675](https://github.com/betagouv/gestion-des-subventions-locales/issues/675)
- Autorisation des tabulations dans les arrêtés et lettres de notification. [#705](https://github.com/betagouv/gestion-des-subventions-locales/issues/705)
- Amélioration de l'affichage des documents de l'autre dotation dans l'onglet Programmation. [#694](https://github.com/betagouv/gestion-des-subventions-locales/issues/694)
- Correction de l'affichage de la date de notification. [#695](https://github.com/betagouv/gestion-des-subventions-locales/issues/695)
- Possibilité de fermer la modale "Vous ne faites pas partie du groupe d'instructeurs". [#690](https://github.com/betagouv/gestion-des-subventions-locales/issues/690)
- Ajout de titres de colonnes fixes lors du défilement des listes de projets, programmations et simulations. [#704](https://github.com/betagouv/gestion-des-subventions-locales/issues/704)
- Ajout d'une recherche sur les intitulés, raisons sociales et numéros de dossier dans les listes de projets, programmations et simulations. [#701](https://github.com/betagouv/gestion-des-subventions-locales/issues/701)
- Amélioration de l'interface pour la génération de documents en masse, avec déplacement dans une modale. [#697](https://github.com/betagouv/gestion-des-subventions-locales/issues/697)
- Possibilité de générer des arrêtés et des lettres simultanément.
- Choix du format d'exportation pour les documents (arrêté, lettre).
- Ajout de QR codes pour rattacher automatiquement les scans signés aux documents. [#709](https://github.com/betagouv/gestion-des-subventions-locales/issues/709)

### Évolutions techniques
- Refactorisation du proxy vers les Démarches Numériques pour améliorer la performance et la robustesse.
- Amélioration de la gestion des erreurs et des timeouts dans le proxy DN.
- Mise à jour des dépendances pour corriger des vulnérabilités. [#710](https://github.com/betagouv/gestion-des-subventions-locales/issues/710) et [#703](https://github.com/betagouv/gestion-des-subventions-locales/issues/703)
- Amélioration de la performance des filtres en utilisant des requêtes paresseuses.
- Ajout de tests pour empêcher les requêtes HTTP non mockées.
- Correction de problèmes liés aux tags de release et aux notes de version.
- Ajout d'une commande `just release-dry-run` pour prévisualiser les releases.
- Amélioration de la gestion des statuts en masse pour les simulations.
- Utilisation de managers pour les FieldMapping.
- Ajout de la librairie django-query-counter.

### Autres changements
- Correction de typos et améliorations de la mise en page des arrêtés et lettres.
- Mise à jour de la documentation.
- Correction de l'URL du script HeatmapSessionRecording de Matomo. [#687](https://github.com/betagouv/gestion-des-subventions-locales/issues/687)
- Correction de la récupération des profils DN en permettant la modification de l'adresse email. [#700](https://github.com/betagouv/gestion-des-subventions-locales/issues/700)
- Ajout d'une action dans l'interface d'administration pour récupérer un dossier depuis DN. [#696](https://github.com/betagouv/gestion-des-subventions-locales/issues/696)
- Suppression du Demandeur (doublon) pour ne conserver que le demandeur au niveau du dossier. [#670](https://github.com/betagouv/gestion-des-subventions-locales/issues/670)
- Mise à jour de l'enveloppe lors de la modification des montants des projets acceptés. [#674](https://github.com/betagouv/gestion-des-subventions-locales/issues/674)
- Correction de l'affichage du statut du projet dans l'onglet notifications.
- Suppression des simulations hors-périmètre lorsque le périmètre du dossier a changé.
- Correction de l'affichage des documents.
- Correction de la date affichée.
- Amélioration de la gestion des erreurs dans la génération de documents.
- Correction d'un bug lié à l'ouverture du dropdown de statut. [#711](https://github.com/betagouv/gestion-des-subventions-locales/issues/711)
