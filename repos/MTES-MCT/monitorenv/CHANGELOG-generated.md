## Changelog : monitorenv (30 derniers jours, au 12 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des zones de vigilance, des domaines réglementaires et des missions, avec une attention particulière portée à l'expérience utilisateur et à la qualité du code. Des corrections de bugs et des optimisations techniques ont également été apportées pour améliorer la stabilité et la performance de l'application.

### Évolutions fonctionnelles
- **Zones de vigilance :**
    - Ajout de filtres pour les zones de vigilance, permettant un affichage plus pertinent des données. [#ddbb570](https://github.com/MTES-MCT/monitorenv/issues/ddbb570)
    - Mise en place d'une table avec des lignes extensibles pour une meilleure visualisation des détails. [#6430d0f](https://github.com/MTES-MCT/monitorenv/issues/6430d0f)
    - Tri par date de création par défaut. [#ad07290](https://github.com/MTES-MCT/monitorenv/issues/ad07290)
- **Missions :**
    - Refonte de la table des missions pour la rendre extensible et plus claire. [#c424cf9](https://github.com/MTES-MCT/monitorenv/issues/c424cf9)
    - Ajout de tags aux missions avec des actions environnementales et des périodes. [#d225a21](https://github.com/MTES-MCT/monitorenv/issues/d225a21)
    - Ajout d'un bouton de réinitialisation sur les modales de mission, rapport et tableau de bord. [#153e04a](https://github.com/MTES-MCT/monitorenv/issues/153e04a)
- **Domaines réglementaires :**
    - Amélioration du flux de mise à jour des domaines réglementaires de CACEM. [#a392cbf](https://github.com/MTES-MCT/monitorenv/issues/a392cbf)
    - Suppression de code obsolète lié aux domaines réglementaires. [#f92eefc](https://github.com/MTES-MCT/monitorenv/issues/f92eefc)
- **Contrôle conchylicole :** Ajout de colonnes liées à la plongée lors d'opérations de contrôle conchylicole. [#29b6535](https://github.com/MTES-MCT/monitorenv/issues/29b6535)
- **Recherche :** Correction de la requête de recherche dans la carte. [#ad1ef22](https://github.com/MTES-MCT/monitorenv/issues/ad1ef22)

### Évolutions techniques
- **Dépendances :** Mise à jour de plusieurs dépendances, notamment Cypress (14.5.3 -> 15.14.2), @sentry/browser (8.54.0 -> 10.51.0) et diverses autres bibliothèques.
- **CI/CD :**
    - Mise à jour de l'action Docker pour la CI/CD (version 3 -> 4). [#5851bbe](https://github.com/MTES-MCT/monitorenv/issues/5851bbe)
    - Configuration de Dependabot pour exclure `package.lock` et éviter les mises à jour inutiles. [#22391f0](https://github.com/MTES-MCT/monitorenv/issues/22391f0)
- **Refactoring :**
    - Refactoring de la table des missions pour améliorer l'extensibilité. [#b52e3b4](https://github.com/MTES-MCT/monitorenv/issues/b52e3b4)
    - Refactoring du code lié aux domaines réglementaires. [#dc18b7b](https://github.com/MTES-MCT/monitorenv/issues/dc18b7b)
- **Tests :** Correction de tests unitaires et E2E. [#8938264](https://github.com/MTES-MCT/monitorenv/issues/8938264)
- **Authentification :** Amélioration de la logique de vérification des utilisateurs et des permissions. [#0a92d3e](https://github.com/MTES-MCT/monitorenv/issues/0a92d3e)

### Autres changements
- Ajout de tags au dépôt. [#7651fcc](https://github.com/MTES-MCT/monitorenv/issues/7651fcc)
- Correction de fautes de frappe dans le README. [#5bd4eb4](https://github.com/MTES-MCT/monitorenv/issues/5bd4eb4)
- Ajout d'une validation sur les cas d'utilisation de patch. [#6728627](https://github.com/MTES-MCT/monitorenv/issues/6728627)
- Suppression du mot "New" pour les domaines réglementaires. [#0b78f1d](https://github.com/MTES-MCT/monitorenv/issues/0b78f1d)
- Amélioration de la visibilité de l'environnement sur les serveurs d'intégration ou de pré-production. [#23a0420](https://github.com/MTES-MCT/monitorenv/issues/23a0420)
- Ajout d'un favicon correct en production. [#b91332f](https://github.com/MTES-MCT/monitorenv/issues/b91332f)
- Correction de l'URL du favicon. [#24ee410](https://github.com/MTES-MCT/monitorenv/issues/24ee410)
- Ajout d'un message d'avertissement pour la complétion des tags. [#d68436c](https://github.com/MTES-MCT/monitorenv/issues/d68436c)
- Mise à jour du label "Drone" pour l'unité de contrôle. [#459f193](https://github.com/MTES-MCT/monitorenv/issues/459f193)
- Suppression du drapeau de fonctionnalité "Regulatory areas". [#23a0420](https://github.com/MTES-MCT/monitorenv/issues/23a0420)
