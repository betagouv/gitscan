## Changelog : mobilic (30 derniers jours, au 26 octobre 2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur l'amélioration de la gestion des véhicules et la stabilisation de l'interface d'administration. L'expérience utilisateur a été affinée grâce à une meilleure gestion des tris, des formats d'immatriculation plus flexibles et une interface plus fluide lors du changement de société. Des améliorations de sécurité et de performance ont également été apportées pour garantir la fiabilité de la plateforme.

### Évolutions fonctionnelles
- **Gestion des véhicules** : 
    - Amélioration de la saisie et de l'affichage des plaques d'immatriculation (support des formats à 6-8 chiffres, des plaques militaires numériques et formatage cohérent). [#1002](https://github.com/MTES-MCT/mobilic/pull/1002), [#980](https://github.com/MTES-MCT/mobilic/pull/980)
    - Optimisation du tri des listes de véhicules par numéro d'immatriculation canonique.
- **Interface d'administration** : 
    - Amélioration de la fluidité lors du changement de société (affichage de squelettes de chargement, rafraîchissement automatique des filtres d'équipe et des données). [#1005](https://github.com/MTES-MCT/mobilic/pull/1005)
    - Correction de la pagination des jours de travail pour éviter les erreurs de chargement.
- **Contrôles et Incidents** : 
    - Amélioration de l'interface utilisateur pour la liste des incidents. [#997](https://github.com/MTES-MCT/mobilic/pull/997), [#996](https://github.com/MTES-MCT/mobilic/pull/996)
    - Ajout d'un registre de bugs de contrôle. [#957](https://github.com/MTES-MCT/mobilic/pull/957)
    - Mise en place d'un nouveau format d'exportation pour les contrôles. [#977](https://github.com/MTES-MCT/mobilic/pull/977)
    - Ajout du type de transport dans les formulaires de bulletin de contrôle.
- **Navigation et Interface** : 
    - Mise en place de la pagination pour la liste des activités. [#935](https://github.com/MTES-MCT/mobilic/pull/935)
    - Amélioration des filtres de statut et des filtres d'activités. [#991](https://github.com/MTES-MCT/mobilic/pull/991), [#970](https://github.com/MTES-MCT/mobilic/pull/970)
    - Optimisation de l'affichage des badges de notification (masqués lorsqu'ils sont vides ou en cours de chargement). [#983](https://github.com/MTES-MCT/mobilic/pull/983), [#979](https://github.com/MTES-MCT/mobilic/pull/979)
    - Clarification des formulaires : renommage de "Activités RSE" en "Activités tachygraphe". [#984](https://github.com/MTES-MCT/mobilic/pull/984)

### Évolutions techniques
- **Sécurité** : Mise à jour de Node.js pour corriger une vulnérabilité critique (CVE-2026-111497).
- **CI/CD** : 
    - Ajout d'une étape de build systématique avant le déploiement. [#968](https://github.com/MTES-MCT/mobilic/pull/968)
    - Intégration d'un scan de secrets (Gitleaks) dans le processus de pré-commit pour renforcer la sécurité du code. [#966](https://github.com/MTES-MCT/mobilic/pull/966)
- **Performance** : Réduction du nombre d'appels API lors de la consultation des détails d'une société dans l'administration. [#917](https://github.com/MTES-MCT/mobilic/pull/917)
- **Refactoring** : 
    - Simplification de la logique de tri des véhicules pour assurer une cohérence entre les tableaux et les sélecteurs. [#1004](https://github.com/MTES-MCT/mobilic/pull/1004)
    - Optimisation du routage pour la gestion des badges.

### Autres changements
- Nettoyage du code et correction de diverses alertes de qualité (SonarCloud et linting).
