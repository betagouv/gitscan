## Changelog : france-chaleur-urbaine (30 derniers jours, au 25 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des permissions et des accès, l'ajout de nouvelles fonctionnalités de suivi et d'analyse (notamment avec PostHog), et des corrections pour optimiser l'expérience utilisateur et la performance de la plateforme. Des améliorations ont également été apportées à la gestion des données et à l'intégration avec des services externes comme ADEME Connect.

### Évolutions fonctionnelles
- Ajout d'un nouveau système de permissions plus granulaire, incluant des rôles (CCRT, ALEC) et une gestion des accès simplifiée.
- Amélioration de l'interface d'administration pour la gestion des permissions et des utilisateurs.
- Intégration d'ADEME Connect via iframe.
- Ajout d'un bandeau d'information concernant une future indisponibilité du service.
- Amélioration de la gestion des relances et des notes sur les réseaux.
- Ajout d'une fonctionnalité de recherche par ID SNCU dans les statistiques.
- Affichage de la colonne "has_PDP" dans l'administration des demandes.
- Ajout d'une FAQ accessible depuis la page d'accueil.
- Amélioration du formulaire de création d'utilisateur par un administrateur.
- Ajout d'un bouton pour réaffecter facilement les demandes.
- Ajout d'une fonctionnalité de sauvegarde des presets dans l'URL pour une expérience utilisateur plus cohérente.
- Amélioration de la visibilité des demandes à traiter et affectées.
- Ajout d'un lien direct vers la correction des permissions pour un gestionnaire.

### Évolutions techniques
- Mise en place d'un cache au niveau des tuiles pour améliorer la performance de la carte.
- Refactor de la gestion des permissions et des routes.
- Ajout d'un module de métriques avec une API Prometheus pour le monitoring.
- Migration des comptes métropoles.
- Optimisation des performances du listing des demandes.
- Amélioration du typage et du code dans plusieurs composants.
- Suppression de code obsolète et nettoyage général du code.
- Ajout de tests pour les routes territoires.
- Uniformisation du tracking PostHog entre différents composants (Card, Link, Button).
- Ajout de nombreux événements de tracking PostHog pour mieux comprendre le comportement des utilisateurs.
- Utilisation de composants UI/Link au lieu de next/link.
- Mise à jour et simplification de la configuration des variables d'environnement.

### Autres changements
- Ajout d'un script pour dropper des tables à distance.
- Ajout d'un script pour mettre à jour les réseaux via un répertoire.
- Ajout d'un script de migration des notes de tags.
- Suppression des presets "haut potentiel" et "dans PDP".
- Ajout d'un fichier `.claudeignore`.
- Correction de plusieurs erreurs de typage et d'indentation.
- Amélioration de la documentation et des commentaires.
- Suppression de crons inutiles.
- Ajout de commandes pour analyser les réseaux.
- Ajout d'un message d'information pour les utilisateurs provenant de Pacoupa.
- Amélioration du texte sous les liens pour plus de clarté.
- Ajout d'un petit délai pour une meilleure gestion du scroll sur l'accordéon de la FAQ.
