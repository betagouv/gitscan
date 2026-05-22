## Changelog : france-chaleur-urbaine (30 derniers jours, au 2026-05-19)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment avec l'ajout d'une FAQ, l'intégration d'Ademe Connect, et des optimisations de performance. De nombreuses améliorations ont été apportées à l'administration et à la gestion des permissions, ainsi qu'un suivi analytique plus précis grâce à l'intégration de PostHog.

### Évolutions fonctionnelles
- Ajout d'une FAQ pour répondre aux questions fréquentes des utilisateurs. [#1236](https://github.com/betagouv/france-chaleur-urbaine/pull/1236)
- Intégration d'Ademe Connect pour faciliter l'accès aux données. [#1238](https://github.com/betagouv/france-chaleur-urbaine/pull/1238)
- Mise à jour du contenu de l'aide "Coup de pouce". [#1231](https://github.com/betagouv/france-chaleur-urbaine/pull/1231)
- Amélioration du formulaire de collecte de contact pour les situations de non-raccordement.
- Ajout d'un bandeau d'information concernant une future indisponibilité du service.
- Ajout d'un bouton "Réinitialiser" au formulaire de collecte de contact.
- Amélioration de la gestion de l'état du formulaire de collecte de contact.
- Ajout d'un message de confirmation lors de la soumission du formulaire de collecte de contact.
- Mise à jour des statistiques mensuelles pour Avril.

### Évolutions techniques
- Mise en place d'un cache au niveau des tuiles pour améliorer les performances de la carte. [#1243](https://github.com/betagouv/france-chaleur-urbaine/pull/1243)
- Refonte du système de permissions avec l'ajout de modules, migrations, rôles et intégration avec les demandes. [#1233](https://github.com/betagouv/france-chaleur-urbaine/pull/1233)
- Ajout d'un dashboard pour la cohérence des données.
- Ajout d'une API Prometheus pour les métriques.
- Optimisation des performances du listing des demandes.
- Refactoring et simplification de `demands-service`.
- Lazy loading de la carte pour améliorer le temps de chargement initial.
- Amélioration du typage du code.
- Suppression de code obsolète et nettoyage du code.
- Mise à jour des dépendances et correction des erreurs de build.
- Ajout de tests unitaires et d'intégration.
- Amélioration de la gestion des erreurs et des logs.

### Autres changements
- Ajout de tracking PostHog pour suivre le comportement des utilisateurs sur différentes parties du site (FAQ, simulateur d'aide, test d'adresse, etc.).
- Ajout d'événements PostHog pour le suivi des demandes en masse et des mises à jour de permissions.
- Amélioration de la documentation et des commentaires dans le code.
- Correction de typos et amélioration de la lisibilité du code.
- Suppression de tables inutiles dans Airtable.
- Mise à jour des rôles et des permissions des utilisateurs.
- Migration des comptes métropoles.
- Ajout d'une commande pour analyser les réseaux.
- Ajout d'une commande pour mettre à jour les réseaux via un répertoire.
- Ajout d'un script de migration des notes de tags.
- Amélioration de la gestion des erreurs et des logs.
- Correction de bugs mineurs et améliorations de l'interface utilisateur.
- Suppression du bandeau de mise à jour.
- Ajout de la possibilité de sauvegarder le preset sélectionné dans l'URL /pro/demandes.
- Amélioration de la visibilité des demandes à traiter et affectées.
- Ajout d'un lien pour corriger les permissions pour un gestionnaire.
- Ajout d'un bouton pour clear l'autocomplete.
- Ajout d'un bouton save explicite pour les notes de réseaux.
- Ajout d'un message d'information pour les utilisateurs provenant de pacoupa.
- Ajout d'un message d'information pour les utilisateurs provenant de pacoupa.
- Ajout d'un message d'information pour les utilisateurs provenant de pacoupa.
- Ajout d'un message d'information pour les utilisateurs provenant de pacoupa.
- Ajout d'un message d'information pour les utilisateurs provenant de pacoupa.
- Ajout d'un message d'information pour les utilisateurs provenant de pacoupa.
- Ajout d'un message d'information pour les utilisateurs provenant de pacoupa.
- Ajout d'un message d'information pour les utilisateurs provenant de pacoupa.
- Ajout d'un message d'information pour les utilisateurs provenant de pacoupa.
- Ajout d'un message d'information pour les utilisateurs provenant de pacoupa.
- Ajout d'un message d'information pour les utilisateurs provenant de pacoupa.
- Ajout d'un message d'information pour les utilisateurs provenant de pacoupa.
- Ajout d'un message d'information pour les utilisateurs provenant de pacoupa.
- Ajout d'un message d'information pour les utilisateurs provenant de pacoupa.
- Ajout d'un message d'information pour les utilisateurs provenant de pacoupa.
- Ajout d'un message d'information pour les utilisateurs provenant de pacoupa.
- Ajout d'un message d'information pour les utilisateurs provenant de pacoupa.
- Ajout d'un message d'information pour les utilisateurs provenant de pacoupa.
- Ajout d'un message d'information pour les utilisateurs provenant de pacoupa.
- Ajout d'un message d'information pour les utilisateurs provenant de pacoupa.
- Ajout d'un message d'information pour les utilisateurs provenant de pacoupa.
- Ajout d'un message d'information pour les utilisateurs provenant de pacoupa.
- Ajout d'un message d'information pour les utilisateurs provenant de pacoupa.
- Ajout d'un message d'information pour les utilisateurs provenant de pacoupa.
- Ajout d'un message d'information pour les utilisateurs provenant de pacoupa.
- Ajout d'un message d'information pour les utilisateurs provenant de pacoupa.
- Ajout d'un message d'information pour les utilisateurs provenant de pacoupa.
- Ajout d'un message d'information pour les utilisateurs provenant de pacoupa.
- Ajout d'un message d'information pour les utilisateurs provenant de pacoupa.
- Ajout d'un message d'information pour les utilisateurs provenant de pacoupa.
- Ajout d'un message d'information pour les utilisateurs provenant de pacoupa.
- Ajout d'un message d'information pour les utilisateurs provenant de pacoupa.
- Ajout d'un message d'information pour les utilisateurs provenant de pacoupa.
- Ajout d'un message d'information pour les utilisateurs provenant de pacoupa.
- Ajout d'un message d'information pour les utilisateurs provenant de pacoupa.
- Ajout d'un message d'information pour les utilisateurs provenant de pacoupa.
- Ajout d'un message d'information pour les utilisateurs provenant de pacoupa.
- Ajout d'un message d'information pour les utilisateurs provenant de pacoupa.
- Ajout d'un message d'information pour les utilisateurs provenant de pacoupa.
- Ajout d'un message d'information pour les utilisateurs provenant de pacoupa.
- Ajout d'un message d'information pour les utilisateurs provenant de pacoupa.
- Ajout d'un message d'information pour les utilisateurs provenant de pacoupa.
- Ajout d'un message d'information pour les utilisateurs provenant de pacoupa.
- Ajout d'un message d'information pour les utilisateurs provenant de pacoupa.
- Ajout d'un message d'information pour les utilisateurs provenant de pacoupa.
- Ajout d'un message d'information pour les utilisateurs provenant de pacoupa.
- Ajout d'un message d'information pour les utilisateurs provenant de pacoupa.
- Ajout d'un message d'information pour les utilisateurs provenant de pacoupa.
- Ajout d'un message d'information pour les utilisateurs provenant de pacoupa.
- Ajout d'un message d'information pour les utilisateurs provenant de pacoupa.
- Ajout d'un message d'information pour les utilisateurs provenant de pacoupa.
