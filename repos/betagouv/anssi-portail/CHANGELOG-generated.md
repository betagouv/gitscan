## Changelog : anssi-portail (30 derniers jours)

### Résumé
Ce mois-ci, le portail de l'ANSSI a connu des améliorations significatives, notamment l'ajout d'une section dédiée à la directive NIS2, avec des informations, une comparaison avec les normes ISO et une intégration de la demande de diagnostic cyber. Des optimisations ont également été apportées à la performance et à la maintenance du site, ainsi qu'à l'expérience utilisateur, avec des corrections de bugs et des améliorations de l'interface.

### Évolutions fonctionnelles
- Ajout d'une page dédiée à la directive NIS2, incluant une présentation, des informations et des liens utiles.
- Intégration de la demande de diagnostic cyber au sein de la section NIS2.
- Amélioration de l'affichage et de la navigation de la section NIS2, avec l'ajout d'onglets et d'une marelle.
- Affichage des guides non publiés masqués.
- Mise à jour du nombre d'organisations accompagnées sur la page Cyberdépart (passage à plus de 5000).
- Correction d'une typo dans l'adresse email de la page Contacts.
- Ajout d'une page de suivi de la santé des guides, permettant de vérifier la présence des fichiers et des images.
- Ajout de la mission "Réguler" de l'ANSSI.
- Amélioration de l'affichage du contenu et de la comparaison des exigences ISO et NIS2.
- Ajout de liens vers des nouvelles pages dans le pied de page.

### Évolutions techniques
- Mise à jour de plusieurs dépendances : `@lab-anssi/ui-kit` (versions 1.41.2 et 1.41.3), `axios`, `minimatch`, `qs`, `svelte`.
- Optimisation de la récupération des données et mise en cache des statistiques MAC.
- Refactoring du code pour améliorer la maintenabilité et la lisibilité.
- Utilisation de Knex pour la création de requêtes SQL pour Grist.
- Amélioration de la gestion des erreurs et des logs.
- Utilisation de variables d'environnement pour la configuration.
- Migration vers une nouvelle architecture pour la comparaison des guides.
- Amélioration de la performance de la requête SQL Grist.
- Correction de boucles Svelte.
- Suppression de styles CSS inutilisés.
- Utilisation de l'API Grist pour récupérer les exigences NIS2.

### Autres changements
- Mise à jour de la page statistiques.
- Amélioration des instructions d'installation.
- Correction de problèmes de typographie.
- Ajout de tests unitaires.
- Amélioration de la documentation.
- Modification du nom du site sur Google.
- Ajustements de style et d'interface utilisateur pour améliorer l'expérience utilisateur.
- Suppression de feature flags obsolètes.
- Correction de warnings et d'erreurs de linting.
- Modification de l'affichage des liens dans le menu tertiaire.
- Amélioration de la césure du titre des interlocuteurs.
- Ajout d'illustrations sur la page des collectivités.
- Modification du titre des 3 landings.
- Ajustement de l'espacement latéral du titre et de l'espace entre les éléments.
