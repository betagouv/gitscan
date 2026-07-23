## Changelog : france-chaleur-urbaine (30 derniers jours, au 21 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment dans le cadre de la fonctionnalité "Chaleur Renouvelable" avec l'ajout de commentaires sur les demandes, une meilleure intégration des données du RNB et de la BDNB, et un redesign de l'interface. Des améliorations de performance ont également été apportées au tableau des demandes et à la gestion des données.

### Évolutions fonctionnelles
- Ajout d'un champ commentaire utilisateur sur les demandes de raccordement [#1274](https://github.com/betagouv/france-chaleur-urbaine/issues/1274).
- Amélioration de l'affichage mobile des autres solutions de chauffage.
- Redesign du bloc FranceRenov.
- Amélioration de la gestion de l'affichage des bâtiments sur la carte, avec un effet au survol.
- Pré-remplissage des informations de bâtiment pour simplifier la création de demandes.
- Ajout d'un champ type de radiateur obligatoire.
- Implémentation d'un bloc ECFR (Énergie, Climat, Forêt, Renouvelable).
- Amélioration de la sélection de bâtiment via le RNB.
- Ajout d'un effet au survol sur les bâtiments.
- Ajout de la possibilité d'étiqueter les utilisateurs (tags) pour une meilleure gestion.
- Amélioration de la gestion des organisations et ajout d'une API v2 correspondante.
- Ajout de la possibilité de filtrer globalement sur les colonnes du tableau des demandes.
- Ajout de la possibilité de mettre à jour le statut des demandes par les administrateurs.
- Ajout du maitre d'ouvrage aux réseaux en construction.
- Amélioration de l'affichage des boutons de modification/suppression pour les relances.
- Ajout d'un lien vers le formulaire de contact depuis la page "Mes demandes".
- Amélioration de la gestion des cookies pour les grandes tailles.
- Restauration de l'affichage de l'éligibilité sur les iframes legacy.
- Simplification des statuts autour du recontact.
- Ajout d'un méga-menu pour une meilleure organisation de l'administration.
- Réorganisation du dashboard admin avec toutes les pages.
- Ajout de la possibilité d'ajouter une plage d'IP pour la gestion des accès.

### Évolutions techniques
- Refactorisation de l'API PAC (Pompe à Chaleur).
- Utilisation du composant `Dialog` au lieu de `Modal`.
- Migration vers le nouveau composant MapLibre.
- Amélioration de la gestion des types et des erreurs.
- Suppression de dépendances inutilisées.
- Optimisation des performances du tableau des demandes.
- Mise à jour du package `publicodes`.
- Amélioration de la gestion des migrations de base de données.
- Utilisation de `ConfirmDialog` et des variantes de boutons pour une meilleure cohérence.
- Suppression de l'intégration Pipedrive et des notifications emails de l'équipe FCU.
- Amélioration du tracking des événements dans les iframes et formulaires.
- Ajout de tests unitaires et d'intégration.
- Correction de problèmes de typage.

### Autres changements
- Mise à jour de la documentation.
- Nettoyage du code et refactorisation de certains composants.
- Correction de bugs mineurs et améliorations de la qualité du code.
- Ajout de commentaires pour faciliter la maintenance.
- Ajustements graphiques et amélioration de l'expérience utilisateur.
- Mise à jour des données et des configurations.
- Suppression de tests obsolètes.
- Amélioration de la gestion des erreurs et des exceptions.
