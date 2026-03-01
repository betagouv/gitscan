## Changelog : gestion-des-subventions-locales (30 derniers jours)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'interface utilisateur, notamment en rendant les tableaux plus lisibles et en ajoutant des colonnes d'informations pertinentes. Des améliorations ont également été apportées à la gestion des catégories de subventions (DETR/DSIL) et à la sécurité, avec l'ajout de l'authentification à deux facteurs pour les utilisateurs staff. Enfin, des corrections de bugs et des optimisations de performance ont été réalisées.

### Évolutions fonctionnelles
- Ajout de l'authentification à deux facteurs (OTP) pour les utilisateurs staff [#537](https://github.com/betagouv/gestion-des-subventions-locales/issues/537).
- Ajout d'un lien vers le D.N. dans les tableaux des dossiers, projets et programmations [#548](https://github.com/betagouv/gestion-des-subventions-locales/issues/548).
- Ajout d'une vidéo de démo sur la page d'aide [#526](https://github.com/betagouv/gestion-des-subventions-locales/issues/526).
- Ajout de colonnes dans la page liste des utilisateurs (BO) [#502](https://github.com/betagouv/gestion-des-subventions-locales/issues/502).
- Possibilité de compléter les dossiers reportés sans pièces via un formulaire dédié [#520](https://github.com/betagouv/gestion-des-subventions-locales/issues/520), [#496](https://github.com/betagouv/gestion-des-subventions-locales/issues/496).
- Affichage des catégories DETR/DSIL sur les pages dossier et projet, et ajout de la possibilité de les renseigner lors de la création d'un dossier sans pièces [#500](https://github.com/betagouv/gestion-des-subventions-locales/issues/500), [#491](https://github.com/betagouv/gestion-des-subventions-locales/issues/491), [#492](https://github.com/betagouv/gestion-des-subventions-locales/issues/492).
- Ajout des champs libres instructeurs dans les "Annotations" [#494](https://github.com/betagouv/gestion-des-subventions-locales/issues/494).
- Ajout du nombre de projets dans les listes de projets [#495](https://github.com/betagouv/gestion-des-subventions-locales/issues/495).

### Évolutions techniques
- Migration des tableaux vers la structure DSFR et application du nommage BEM [#544](https://github.com/betagouv/gestion-des-subventions-locales/issues/544).
- Refactorisation de l'interface utilisateur pour améliorer la lisibilité et la performance, notamment avec l'ajout de colonnes "sticky" et la suppression de code mort.
- Optimisation des performances des pages d'administration de Collegue et FieldMapping [#518](https://github.com/betagouv/gestion-des-subventions-locales/issues/518).
- Simplification de la modélisation : suppression de `FieldMappingForHuman` et renommage de `FieldMapping` [#493](https://github.com/betagouv/gestion-des-subventions-locales/issues/493).
- Déplacement de la relation entre Dossier et DossierData, et entre Demarche et Dossier, pour améliorer la structure de la base de données [#543](https://github.com/betagouv/gestion-des-subventions-locales/issues/543), [#536](https://github.com/betagouv/gestion-des-subventions-locales/issues/536).
- Ajout de la librairie django-axes pour la protection contre les attaques par force brute [#524](https://github.com/betagouv/gestion-des-subventions-locales/issues/524).
- Utilisation de `BaseModel` au lieu de `TimestampedModel` pour simplifier la modélisation.

### Autres changements
- Correction de bugs liés à la récupération des catégories DETR et DSIL, notamment pour les territoires non gérés [#549](https://github.com/betagouv/gestion-des-subventions-locales/issues/549), [#547](https://github.com/betagouv/gestion-des-subventions-locales/issues/547).
- Correction d'erreurs 404 après actualisation DN ou changement de dotation [#529](https://github.com/betagouv/gestion-des-subventions-locales/issues/529).
- Correction d'un test [#546](https://github.com/betagouv/gestion-des-subventions-locales/issues/546), [#533](https://github.com/betagouv/gestion-des-subventions-locales/issues/533).
- Suppression de code mort (processModal.js) [#534](https://github.com/betagouv/gestion-des-subventions-locales/issues/534).
- Ajout d'un filtre par arrondissement sur les pages Dossier et Projet du BO [#522](https://github.com/betagouv/gestion-des-subventions-locales/issues/522).
- Renommage de l'onglet "Annotations" en "Notes" [#507](https://github.com/betagouv/gestion-des-subventions-locales/issues/507).
- Correction de l'algo qui récupère les catégories DETR [#510](https://github.com/betagouv/gestion-des-subventions-locales/issues/510).
- Ajout d'une tâche pour rafraîchir tous les dossiers de toutes les démarches depuis DN [#538](https://github.com/betagouv/gestion-des-subventions-locales/issues/538).
- Ajout d'une tâche pour rafraîchir les dossiers d'une démarche depuis une date donnée [#533](https://github.com/betagouv/gestion-des-subventions-locales/issues/533).
- Suppression de la connexion par username/mdp [#523](https://github.com/betagouv/gestion-des-subventions-locales/issues/523).
- Ajout du lien Tchap [#506](https://github.com/betagouv/gestion-des-subventions-locales/issues/506).
- Correction de l'affichage des labels complets [#511](https://github.com/betagouv/gestion-des-subventions-locales/issues/511).
- Suppression de la suppression des dotations projets programmés [#521](https://github.com/betagouv/gestion-des-subventions-locales/issues/521).
- Correction de la gestion des catégories DETR pour les départements non trouvés [#547](https://github.com/betagouv/gestion-des-subventions-locales/issues/547).
- Correction de la création des catégories DETR lorsqu'elles ne sont pas trouvées [#547](https://github.com/betagouv/gestion-des-subventions-locales/issues/547).
