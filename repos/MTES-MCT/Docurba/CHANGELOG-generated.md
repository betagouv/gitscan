## Changelog : Docurba (30 derniers jours, au 26 mai 2026)

### Résumé
Les dernières semaines ont été marquées par des améliorations significatives de l'interface utilisateur, notamment concernant la gestion des procédures et des types de documents, ainsi que par des corrections de bugs pour une meilleure expérience utilisateur. Des efforts ont également été déployés pour améliorer la conformité aux exigences de la loi Huwart et pour optimiser l'infrastructure et les tests du projet.

### Évolutions fonctionnelles
- Possibilité de filtrer les types de procédures disponibles en fonction de leur date de début. [#340392a](https://github.com/MTES-MCT/Docurba/commit/340392a)
- Affichage d'une indication "avant/après Huwart" pour les types de procédures. [#b885455](https://github.com/MTES-MCT/Docurba/commit/b885455)
- La page de lecture PAC (Plan d'Aménagement et de Construction) est désormais publique. [#b53a072](https://github.com/MTES-MCT/Docurba/commit/b53a072)
- Amélioration de la gestion des événements, avec une liste mise à jour et une logique de gestion des options déplacée vers un plugin Nuxt. [#3c89a38](https://github.com/MTES-MCT/Docurba/commit/3c89a38), [#4e69d8e](https://github.com/MTES-MCT/Docurba/commit/4e69d8e), [#992c635](https://github.com/MTES-MCT/Docurba/commit/992c635)
- Correction d'un bug empêchant la création de PLU avec plusieurs communes. [#9553d70](https://github.com/MTES-MCT/Docurba/commit/9553d70)
- Correction d'un bug empêchant la récupération du dernier événement. [#ec819f1](https://github.com/MTES-MCT/Docurba/commit/ec819f1)
- Amélioration de la navigation en maintenant les filtres lors du changement de département. [#e90940a](https://github.com/MTES-MCT/Docurba/commit/e90940a)
- Synchronisation des champs de recherche avec les paramètres de l'URL. [#ab4cb4d](https://github.com/MTES-MCT/Docurba/commit/ab4cb4d)
- Redirection de l'utilisateur vers le tableau de bord après la récupération du mot de passe. [#a089e00](https://github.com/MTES-MCT/Docurba/commit/a089e00)

### Évolutions techniques
- Refactorisation de l'application `internal_api` et déplacement dans le répertoire `docurba`. [#05af439](https://github.com/MTES-MCT/Docurba/commit/05af439)
- Mise en place d'une gestion des erreurs plus robuste pour éviter les manipulations de propriétés de variables indéfinies. [#df116e1](https://github.com/MTES-MCT/Docurba/commit/df116e1)
- Ajout d'une colonne `started_before_huwart_law` dans le modèle `Procedure` pour indiquer si une procédure a débuté avant la loi Huwart. [#6f0b594](https://github.com/MTES-MCT/Docurba/commit/6f0b594)
- Simplification de la commande de gestion pour remplir le champ `started_before_huwart_law`. [#26d9488](https://github.com/MTES-MCT/Docurba/commit/26d9488)
- Mise à jour de la documentation de l'API pour inclure les topics des communes et des SCoT. [#e28b305](https://github.com/MTES-MCT/Docurba/commit/e28b305)
- Utilisation de FactoryBoy pour la création d'objets de test. [#2bc0c2a](https://github.com/MTES-MCT/Docurba/commit/2bc0c2a)
- Mise en place d'un Makefile pour simplifier les tâches de développement. [#77a8823](https://github.com/MTES-MCT/Docurba/commit/77a8823)
- Utilisation d'un environnement virtuel (venv). [#b333432](https://github.com/MTES-MCT/Docurba/commit/b333432)
- Mise à jour des dépendances : Django, djangorestframework, urllib3, ruff, pre-commit.

### Autres changements
- Suppression des événements de fin d'échéance pour se conformer à la loi Huwart. [#62f67e4](https://github.com/MTES-MCT/Docurba/commit/62f67e4)
- Déplacement de `TypeCollectivite` vers `core.enums`. [#a9ad3fb](https://github.com/MTES-MCT/Docurba/commit/a9ad3fb)
- Mise à jour du nom de la procédure lors de la mise à jour du type de document. [#5737491](https://github.com/MTES-MCT/Docurba/commit/5737491)
- Distinction des types EPCI `TypeCollectivite` des autres. [#399bc60](https://github.com/MTES-MCT/Docurba/commit/399bc60)
- Suppression de l'affichage dynamique de l'icône "i". [#359cc55](https://github.com/MTES-MCT/Docurba/commit/359cc55)
- Renommage du champ `ProcedureCommune` pour faciliter l'accès via l'ORM. [#28ef793](https://github.com/MTES-MCT/Docurba/commit/28ef793)
- Ajout d'un dossier `exports` ignoré par le système de contrôle de version. [#1df2ab7](https://github.com/MTES-MCT/Docurba/commit/1df2ab7)
- Mise à jour en masse du type de document des procédures de PLU à PLUi. [#0d6cf9a](https://github.com/MTES-MCT/Docurba/commit/0d6cf9a)
- Augmentation du plan Supabase et de la taille du disque pour résoudre les erreurs de mémoire récurrentes. [#1ed6e01](https://github.com/MTES-MCT/Docurba/commit/1ed6e01), [#f208f08](https://github.com/MTES-MCT/Docurba/commit/f208f08)
- Correction de conflits de migration. [#13d2489](https://github.com/MTES-MCT/Docurba/commit/13d2489)
- Ajout de la possibilité de modifier la colonne `soft_delete` de la procédure dans l'admin Django. [#d7bb24a](https://github.com/MTES-MCT/Docurba/commit/d7bb24a)
- Ajout de la possibilité d'exposer les topics des procédures dans l'API SCoT. [#f195396](https://github.com/MTES-MCT/Docurba/commit/f195396)
- Ajout de noms de routes pour pouvoir utiliser la fonction `reverse`. [#5508b7e](https://github.com/MTES-MCT/Docurba/commit/5508b7e)
- Correction de problèmes de sonar et retours de revue de code. [#5c714e7](https://github.com/MTES-MCT/Docurba/commit/5c714e7)
