## Changelog : monitorenv (30 derniers jours, au 30 avril 2026)

### Résumé
Ce mois-ci, l'application monitorenv a bénéficié d'améliorations significatives en termes d'expérience utilisateur, notamment au niveau de la gestion des zones réglementaires, des aires de vigilances et des missions. Des corrections et des optimisations ont également été apportées pour améliorer la stabilité et la performance de l'application, ainsi que des ajouts concernant les données des navires.

### Évolutions fonctionnelles
- Ajout d'un bouton de réinitialisation sur les modales de mission, de rapports et du tableau de bord [#1234](https://github.com/MTES-MCT/monitorenv/issues/1234).
- Refonte de la table des missions pour la rendre plus extensible.
- Ajout de tags aux missions avec des informations sur l'action environnementale et la période.
- Amélioration de la gestion des zones réglementaires :
    - Ajout d'un filtre pour afficher les zones récentes.
    - Mise en évidence des zones récemment mises à jour ou créées.
    - Correction de bugs dans le formulaire de création/modification des zones réglementaires.
- Amélioration de la gestion des aires de vigilance :
    - Mise à jour du libellé "Drone".
    - Ajout de colonnes épinglées et de filtres.
    - Affichage des données dans un tableau avec des lignes extensibles.
- Ajout de la jauge de tonnage brut UMS aux navires.
- Amélioration de la visibilité de l'environnement sur les serveurs d'intégration ou de pré-production et suppression du feature flag associé.
- Ajout de la possibilité de mettre en évidence les nouvelles AMP (Aires Marines Protégées).

### Évolutions techniques
- Ajout de colonnes liées à la plongée lors d'opérations de contrôles conchylicoles.
- Ajout de tests unitaires pour les champs de plongée.
- Refactorisation du code pour améliorer la récupération des données des navires.
- Correction de type errors.
- Optimisation de l'indexation des données d'identification.
- Mise à jour de la gestion des timestamps pour les données des navires.
- Suppression de l'import inutile.
- Refactorisation du code pour améliorer la lisibilité et la maintenabilité.
- Désactivation du rebasage automatique pour Dependabot.
- Exclusions de `package.lock` de Dependabot.

### Autres changements
- Correction de tests E2E.
- Mise à jour de la favicon en production.
- Ajout d'un message d'avertissement pour les tags incomplets.
- Ajout d'un message d'avertissement pour les tags incomplets.
- Amélioration de la gestion des erreurs lors de la désérialisation des données.
- Ajout de vérifications de la présence du claim `organizational_unit` pour la sécurité.
- Correction de bugs mineurs et améliorations de la documentation.
- Mises à jour de dépendances (ol-mapbox-style, python-dotenv, pytest, cryptography, black).
