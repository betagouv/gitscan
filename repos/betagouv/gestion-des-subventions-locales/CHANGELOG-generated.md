## Changelog : gestion-des-subventions-locales (30 derniers jours, au 23 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la robustesse et de la performance de l'application, notamment au niveau de la synchronisation avec le DS (Dossier Simplifié), de la gestion des documents et de l'expérience utilisateur. Des corrections de bugs et des optimisations ont également été apportées pour améliorer la stabilité et la fluidité de l'outil.

### Évolutions fonctionnelles
- Possibilité de rechercher les dossiers par sous-chaîne du numéro de dossier. [#728](https://github.com/betagouv/gestion-des-subventions-locales/issues/728)
- Import des dossiers de tous les territoires gérés. [#749](https://github.com/betagouv/gestion-des-subventions-locales/issues/749)
- Possibilité de changer le statut de plusieurs projets en "refusé" ou "classé sans suite" en lot. [#726](https://github.com/betagouv/gestion-des-subventions-locales/issues/726)
- Amélioration de l'affichage des enveloppes budgétaires dans l'interface, avec masquage de la colonne d'actions sur certaines pages. [#752](https://github.com/betagouv/gestion-des-subventions-locales/issues/752)
- Possibilité de définir le nom du fichier PDF lors de la génération de notifications d'acceptation. [#736](https://github.com/betagouv/gestion-des-subventions-locales/issues/736)
- Ajout d'une entrée de menu dédiée pour le publipostage des modèles. [#750](https://github.com/betagouv/gestion-des-subventions-locales/issues/750)
- Affichage du périmètre, des dates Turgot et du statut du report dans l'interface d'administration. [#748](https://github.com/betagouv/gestion-des-subventions-locales/issues/748)
- Conservation des filtres et du tri lors de la navigation vers les documents de notification. [#725](https://github.com/betagouv/gestion-des-subventions-locales/issues/725)

### Évolutions techniques
- Limitation de chaque token du proxy DS à une seule requête simultanée pour améliorer la robustesse. [#758](https://github.com/betagouv/gestion-des-subventions-locales/issues/758)
- Ajout d'un verrou anti-concurrence sur la synchronisation des dossiers DS pour éviter les conflits. [#740](https://github.com/betagouv/gestion-des-subventions-locales/issues/740)
- Priorisation des tâches Celery en fonction du contexte d'appel pour optimiser les performances. [#751](https://github.com/betagouv/gestion-des-subventions-locales/issues/751)
- Augmentation du timeout Gunicorn à 120 secondes pour la génération de documents afin d'éviter les erreurs de timeout. [#763](https://github.com/betagouv/gestion-des-subventions-locales/issues/763)
- Refactorisation du code pour améliorer la structure et la maintenabilité, notamment au niveau de la gestion des projets, des notifications et de l'historique.
- Remplacement de certaines vues fonctionnelles (FBV) par des vues classes (CBV) pour une meilleure organisation du code. [#754](https://github.com/betagouv/gestion-des-subventions-locales/issues/754)
- Découpage du document GraphQL monolithique en fichiers plus petits et plus gérables. [#721](https://github.com/betagouv/gestion-des-subventions-locales/issues/721)
- Activation de la compression WhiteNoise (gzip + Brotli) des fichiers statiques pour améliorer les performances de chargement. [#757](https://github.com/betagouv/gestion-des-subventions-locales/issues/757)
- Ajout d'un identifiant de requête et d'une journalisation structurée sur le proxy DS pour faciliter le débogage. [#731](https://github.com/betagouv/gestion-des-subventions-locales/issues/731)

### Autres changements
- Correction de bugs mineurs liés à l'affichage des filtres, à la gestion des tableaux TipTap et à la perte du curseur sur les pages vides.
- Amélioration de la gestion des erreurs renvoyées par DN lors de la sauvegarde des curseurs.
- Ajout d'alertes email aux administrateurs sur les opérations sensibles. [#730](https://github.com/betagouv/gestion-des-subventions-locales/issues/730)
- Suppression des pages d'administration sur l'application. [#727](https://github.com/betagouv/gestion-des-subventions-locales/issues/727)
- Correction de tests flaky et amélioration de la couverture de test.
- Mise à jour de la documentation.
