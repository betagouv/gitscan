## Changelog : gestion-des-subventions-locales (30 derniers jours, au 2026-04-23)

### Résumé
Ce mois-ci, l'application a bénéficié d'améliorations significatives en termes de fonctionnalités, de performance et de qualité du code. Les utilisateurs bénéficieront notamment de nouveaux filtres de recherche, d'une meilleure gestion des simulations de subventions, d'une interface utilisateur plus intuitive et de corrections de bugs. Des optimisations techniques ont également été apportées pour améliorer la stabilité et la maintenabilité de l'application.

### Évolutions fonctionnelles
- Ajout d'une FAQ pour aider les utilisateurs à trouver des réponses à leurs questions. [#672](https://github.com/betagouv/gestion-des-subventions-locales/issues/672)
- Possibilité de modifier en masse le statut des projets sur la page de simulation. [#661](https://github.com/betagouv/gestion-des-subventions-locales/issues/661)
- Amélioration de la mise en page des arrêtés et lettres. [#659](https://github.com/betagouv/gestion-des-subventions-locales/issues/659)
- Ajout de filtres pour la catégorie DETR/DSIL, le budget vert, la dotation sollicitée, le dossier complet, le zonage et la contractualisation. [#642](https://github.com/betagouv/gestion-des-subventions-locales/issues/642), [#640](https://github.com/betagouv/gestion-des-subventions-locales/issues/640), [#634](https://github.com/betagouv/gestion-des-subventions-locales/issues/634)
- Affichage de l'EPCI sur la page projet. [#615](https://github.com/betagouv/gestion-des-subventions-locales/issues/615)
- Affichage des colonnes Zonage et Contractualisation dans les listes de projets. [#599](https://github.com/betagouv/gestion-des-subventions-locales/issues/599)
- Récupération et affichage des cofinancements. [#595](https://github.com/betagouv/gestion-des-subventions-locales/issues/595)
- Possibilité de sauvegarder les filtres de simulation. [#650](https://github.com/betagouv/gestion-des-subventions-locales/issues/650)
- Correction de l'affichage du statut du projet dans l'onglet notifications et du lien "Annulation" dans la création/modification d'un arrêté/lettre. [#665](https://github.com/betagouv/gestion-des-subventions-locales/issues/665)
- Correction de l'affichage des cofinancements sur la page projet. [#643](https://github.com/betagouv/gestion-des-subventions-locales/issues/643)
- Correction de la réouverture des modales de statut avec contenu obsolète. [#621](https://github.com/betagouv/gestion-des-subventions-locales/issues/621)

### Évolutions techniques
- Mise en place d'un script HeatmapSessionRecording de Matomo pour l'analyse du comportement des utilisateurs. [#666](https://github.com/betagouv/gestion-des-subventions-locales/issues/666)
- Refactorisation des filtres projet pour une meilleure organisation et simplification. [#610](https://github.com/betagouv/gestion-des-subventions-locales/issues/610)
- Optimisation des requêtes et des prefetch/select_related pour améliorer les performances. [#611](https://github.com/betagouv/gestion-des-subventions-locales/issues/611)
- Utilisation de SQLite en mémoire pour les tests CI afin d'accélérer l'exécution des tests. [#596](https://github.com/betagouv/gestion-des-subventions-locales/issues/596)
- Ajout d'un workflow de déploiement en production via GitHub Actions. [#647](https://github.com/betagouv/gestion-des-subventions-locales/issues/647)
- Amélioration de la sécurité avec des corrections de potentielles failles XSS.
- Mise à jour de la configuration de Content Security Policy (CSP) pour Matomo.
- Refactorisation du code pour utiliser des propriétés au lieu de calculs dans les méthodes.
- Centralisation des constantes liées aux colonnes de tableaux.
- Remplacement des agrégats ProjetService par ProjetQuerySet.totals().

### Autres changements
- Ajout d'une tâche de nettoyage des projets programmés sur des enveloppes antérieures. [#655](https://github.com/betagouv/gestion-des-subventions-locales/issues/655)
- Ajout d'une action pour programmer les projets acceptés 2026 vers l'enveloppe 2025. [#654](https://github.com/betagouv/gestion-des-subventions-locales/issues/654)
- Correction de l'utilisation de l'adresse complète au lieu de la reconstruction de l'adresse sur une seule ligne. [#669](https://github.com/betagouv/gestion-des-subventions-locales/issues/669)
- Ajout d'un script pour sauvegarder régulièrement le code source chiffré. [#626](https://github.com/betagouv/gestion-des-subventions-locales/issues/626)
- Backport de la branche `main` vers `develop`. [#646](https://github.com/betagouv/gestion-des-subventions-locales/issues/646)
- Mise à jour de la documentation et des instructions de déploiement.
