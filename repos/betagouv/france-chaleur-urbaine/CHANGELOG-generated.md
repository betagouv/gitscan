## Changelog : france-chaleur-urbaine (30 derniers jours, au 29 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur, notamment avec l'intégration d'un nouveau formulaire de contact via l'ADEME Connect et la simplification du simulateur de raccordement. Des efforts importants ont également été réalisés pour améliorer la gestion des données, avec l'ajout d'informations sur les écoréseaux et des corrections de typage pour une meilleure fiabilité. Enfin, des mises à jour de l'interface utilisateur et de la documentation ont été effectuées.

### Évolutions fonctionnelles
- Intégration du formulaire de contact ADEME Connect [#1238](https://github.com/betagouv/france-chaleur-urbaine/pull/1238).
- Ajout d'un bouton "Réinitialiser" sur le formulaire de collecte d'informations.
- Amélioration de la gestion de l'état du formulaire de collecte, avec des messages de soumission plus clairs.
- Ajout d'un AB Test pour collecter des utilisateurs dans Airtable lors d'une demande de raccordement non éligible [#1234](https://github.com/betagouv/france-chaleur-urbaine/issues/1234).
- Simplification et refonte de la landing page du simulateur simplifié [#1215](https://github.com/betagouv/france-chaleur-urbaine/pull/1215).
- Ajout d'informations sur les écoréseaux, incluant leur source et un label spécifique sur la carte et la page réseau [#1224](https://github.com/betagouv/france-chaleur-urbaine/pull/1224) et [#1227](https://github.com/betagouv/france-chaleur-urbaine/pull/1227).
- Ajout de liens vers les formulaires de contact et les adresses email dans l'administration [#1226](https://github.com/betagouv/france-chaleur-urbaine/pull/1226).
- Amélioration de l'affichage des messages informatifs sur le simulateur coup de pouce.
- Mise à jour des conditions d'éligibilité à l'aide "Coup de pouce".

### Évolutions techniques
- Passage à Tailwind CSS pour la page City et le simulateur.
- Refactorisation du code du simulateur pour une meilleure maintenabilité.
- Utilisation de la méthode tertiaire pour les calculs Publicodes.
- Mise à jour du package Publicodes.
- Amélioration du typage de plusieurs composants et variables.
- Correction de conflits lors du chargement du popup via URL/LocalStorage [#1235](https://github.com/betagouv/france-chaleur-urbaine/pull/1235).
- Correction d'un bug lié à l'état du formulaire.
- Suppression de code inutile et simplification de certaines fonctions.
- Amélioration de la gestion des dépendances.
- Correction de tests unitaires.
- Amélioration de la gestion des emails (envoi depuis une adresse no-reply beta.gouv, harmonisation du style).

### Autres changements
- Mise à jour de la documentation sur la procédure de mise à jour des statistiques mensuelles.
- Correction de coquilles et amélioration du wording sur plusieurs pages.
- Mise à jour des statistiques d'avril.
- Suppression d'icônes de la section "Qui sommes-nous".
- Modification du texte concernant le budget dans la section "Qui sommes-nous".
- Ajout d'images et de nouveaux articles de contenu sur la page d'accueil.
- Mise à jour des images des différents chauffages.
- Ajout d'un script d'import des écoréseaux et des données correspondantes.
- Correction de l'encodage Markdown.
