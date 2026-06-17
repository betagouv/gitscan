## Changelog : a-just (30 derniers jours, au 16 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment sur la page Panorama avec l'ajout de tests automatisés et l'amélioration de l'aide à la navigation. Des corrections et des améliorations ont également été apportées au cockpit, notamment concernant l'affichage des données et la gestion des dates. Des mises à jour de l'extracteur de données et des tests associés ont également été réalisées.

### Évolutions fonctionnelles
- Amélioration de la gestion de la saisie de date dans les composants `aj-date-select` et `aj-date-select-blue` : possibilité de saisie manuelle et utilisation du clavier tout en conservant le sélecteur de date.
- Ajout de la possibilité de filtrer les contentieux sur la page Panorama et de vérifier la complétude des données.
- Amélioration de l'affichage des données et de l'aide à la navigation sur la page Panorama avec l'ajout d'un "pas à pas" (IntroJS).
- Ajout de la possibilité de masquer le bouton "Qu'est-ce que c'est ?" pour les utilisateurs sans droit d'édition des ressources humaines.
- Amélioration de l'affichage des entrées et sorties dans le composant `ReferentielCalculatorComponent` sur le cockpit.
- Correction de l'affichage des dates dans le cockpit.
- Mise à jour des règles ASA (Absence, Suspension, Autorisation).
- Correction de l'affichage des agents dans les colonnes "Arrivées" et "Départs" des changements d'effectifs.
- Correction de l'affichage des contentieux avec des données à compléter sur la page Panorama.
- Amélioration de l'affichage des tooltips sur le cockpit.

### Évolutions techniques
- Refactorisation du workflow GitHub Actions pour simplifier les déploiements.
- Mise à jour de la configuration de Cypress.
- Correction de problèmes liés à la configuration de Redis en Docker.
- Amélioration de la gestion des variables d'environnement dans les tests Cypress.
- Mise à jour de l'extracteur de données.
- Ajout de CSP security.
- Suppression de fichiers et de workflows inutilisés (sandbox, nightly-sandbox).

### Autres changements
- Mise à jour des fichiers de nomenclature [#564](https://github.com/betagouv/a-just/issues/564).
- Correction de bugs mineurs et améliorations de la qualité du code.
- Ajout de logs pour faciliter le débogage.
- Mise à jour de la version du projet.
- Synchronisation des origines.
- Correction d'un problème de duplication d'agent.
- Correction d'un bug lié à la projection des données.
- Correction de l'état de chargement dans le composant `PopinEditActivitiesComponent`.
- Ajout de permissions pour la mise à jour du panorama.
