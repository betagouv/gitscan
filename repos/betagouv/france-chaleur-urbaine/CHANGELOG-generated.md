## Changelog : france-chaleur-urbaine (30 derniers jours, au 4 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des permissions, la performance de l'application, et l'expérience utilisateur, notamment dans l'administration des données et la gestion des demandes. Des corrections et des refactorings importants ont été effectués pour rendre l'application plus robuste et plus facile à maintenir.

### Évolutions fonctionnelles
- **Gestion des permissions :** Refonte complète du système de permissions avec introduction de modules, migrations, rôles et intégration dans la gestion des demandes. Ajout d'un rôle "CCRT".
- **Administration des réseaux :**
    - Ajout d'un dashboard pour la cohérence des données.
    - Possibilité d'affecter des permissions en masse via des IDs.
    - Amélioration de l'affichage des permissions en construction.
    - Ajout d'un bouton pour corriger les permissions d'un gestionnaire.
    - Possibilité de consulter et modifier les notes associées aux réseaux.
- **Statistiques :**
    - Élargissement de la page de statistiques par réseau pour une meilleure visualisation.
    - Affichage de la puissance dans les statistiques par réseau.
    - Ajout de colonnes spécifiques à l'export des statistiques par réseau.
- **Demandes :**
    - Amélioration du workflow d'affectation au réseau.
    - Affichage de l'email dans la demande de réaffectation.
    - Amélioration de la visibilité des demandes à traiter et affectées.
    - Possibilité de filtrer les demandes par statut (non réalisable pour les demandes non éligibles).
    - Affichage d'un badge "ville différente" dans l'administration.
    - Correction de l'affectation des demandes dans PDP.
- **Interface utilisateur :**
    - Amélioration de l'affichage mobile de la page d'accueil.
    - Ajout d'un bouton "clear" dans l'autocomplete.
    - Suppression du bandeau de mise à jour.
    - Amélioration des alignements et du style de certains éléments.
- **Autres :**
    - Mise à jour des contacts (remplacement de Laetitia par Léa, suppression du lien RDV 1-1 d'Erwan).
    - Intégration d'ADEME Connect.

### Évolutions techniques
- **Performance :**
    - Lazy loading de la carte pour améliorer les performances.
    - Optimisation du rendu de la carte.
    - Amélioration des performances du listing des demandes (réduction du temps de chargement).
    - Mise en cache des tuiles cartographiques.
- **Infrastructure :**
    - Ajout d'un module metrics avec une API Prometheus.
    - Ajout de commandes pour analyser et mettre à jour les réseaux via un répertoire.
    - Ajout d'un script pour dropper des tables à distance.
- **Code :**
    - Refactoring important de `demands-service`.
    - Utilisation de helpers HTTP.
    - Utilisation des variables d'environnement via la configuration.
    - Suppression de code inutile et simplification de certaines fonctions.
    - Amélioration du typage TypeScript.
    - Migration vers des pratiques de programmation fonctionnelle.
    - Suppression de l'API pour récupérer les demandes.
- **Tests :**
    - Ajout de tests pour les routes territoires.
    - Refactoring des tests existants.

### Autres changements
- Ajout de documentation et de commentaires dans le code.
- Mise à jour des FAQ pour les gestionnaires.
- Suppression de tables et de crons inutiles dans Airtable.
- Ajout d'événements de tracking PostHog pour améliorer l'analyse de l'utilisation de l'application.
- Correction de bugs divers et amélioration de la stabilité de l'application.
- Ajout d'un fichier `.claude/` (ignoré par Git).
- Mise à jour des dépendances (non listées ici).
