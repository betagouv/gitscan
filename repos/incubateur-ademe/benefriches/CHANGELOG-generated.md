## Changelog : benefriches (30 derniers jours, au 7 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur dans la création et l'analyse de projets de reconversion de friches. Des améliorations ont été apportées au calcul des impacts économiques, à la visualisation des données et à la gestion des dépenses liées aux projets urbains. Des corrections de bugs et des optimisations techniques ont également été réalisées pour améliorer la stabilité et la performance de l'application.

### Évolutions fonctionnelles
- Ajout d'un onglet "Score de développement" sur la page des impacts pour une évaluation plus fine des projets.
- Amélioration de la visualisation de l'allocation des surfaces dans les formulaires de projets urbains.
- Ajout de la prise en compte des coûts de construction et de réhabilitation dans le bilan économique des projets.
- Affichage des dépenses liées à la réutilisation et à la construction de bâtiments dans la vue des caractéristiques des projets urbains.
- Ajout d'un onglet "Résumé" sur la page des impacts, présentant une vue d'ensemble des indicateurs clés.
- Utilisation de couleurs pour les graphiques de niveau de seuil de rentabilité pour une meilleure lisibilité.
- Ajout d'un endpoint API pour calculer le coût de l'inaction sur une friche.
- Amélioration de la gestion des données de réutilisation des bâtiments dans les projets urbains.
- Ajout de tous les modèles de projets existants dans l'étape de sélection du modèle de projet de démonstration.
- Correction du calcul dans l'onglet de seuil de rentabilité lors de la modification de la période d'évaluation.
- Correction de l'affichage des coûts évités de décontamination des sols lorsque le total est nul.

### Évolutions techniques
- Refactorisation du code pour extraire et réutiliser des composants communs, notamment pour la gestion des surfaces.
- Amélioration de la couverture des tests d'intégration pour l'API, notamment pour la gestion des fonctionnalités des projets de reconversion.
- Mise à jour des dépendances (Vitest, Axios, etc.) pour bénéficier des dernières corrections et améliorations.
- Amélioration de la configuration de l'environnement de développement avec des variables d'environnement plus claires.
- Amélioration du pipeline CI/CD avec des contrôles de santé après le déploiement et une gestion des secrets plus sécurisée.
- Utilisation de variables d'environnement standardisées pour les flags de fonctionnalités.
- Ajout de commentaires et documentation pour faciliter la compréhension du code et de l'infrastructure.

### Autres changements
- Mise à jour de la documentation pour inclure des informations sur les endpoints publics de l'API.
- Correction de la configuration de la directive d'images CSP pour inclure OpenStreetMap.
- Mise à jour de la page légale.
- Suppression de fichiers inutiles et amélioration de la structure du projet.
- Correction de problèmes mineurs d'importation de modules.
- Ajout de tests unitaires pour la vue de résultat de création de projet.
- Correction de bugs liés à la navigation inverse dans les dépenses des projets urbains.
- Amélioration de la gestion des types de structures des parties prenantes dans la vue SQL des impacts.
- Correction de l'affichage des marqueurs sur la carte dans l'onglet de résumé des impacts.
- Correction de l'initialisation des données de réutilisation des bâtiments lors de la mise à jour des projets urbains.
