## Changelog : benefriches (30 derniers jours, au 12 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'amélioration du calcul des impacts économiques et environnementaux des projets de reconversion de friches, notamment en affinant les données prises en compte pour le calcul du seuil de rentabilité et en intégrant les coûts de construction et de réhabilitation. L'interface utilisateur a également été améliorée, avec l'ajout de nouvelles visualisations et la correction de bugs pour une meilleure expérience utilisateur.

### Évolutions fonctionnelles
- Ajout d'une nouvelle vue "Résumé des impacts" avec des graphiques pour chaque bénéficiaire d'impact [#245d401](https://github.com/incubateur-ademe/benefriches/commit/245d401).
- Affichage des dépenses de construction et de réhabilitation dans la vue des caractéristiques du projet urbain [#02a2613](https://github.com/incubateur-ademe/benefriches/commit/02a2613).
- Ajout d'un onglet "Score de développement" (en version bêta) pour visualiser les impacts [#bcb431a](https://github.com/incubateur-ademe/benefriches/commit/bcb431a).
- Calcul du seuil de rentabilité avec prise en compte des coûts de transfert de propriété et des revenus locatifs [#61ae910](https://github.com/incubateur-ademe/benefriches/commit/61ae910).
- Ajout d'un endpoint pour calculer le coût de l'inaction sur une friche [#fae2976](https://github.com/incubateur-ademe/benefriches/commit/fae2976).
- Amélioration de l'affichage des dépenses de décontamination du sol dans le résumé du projet [#a18382f](https://github.com/incubateur-ademe/benefriches/commit/a18382f).
- Prise en compte des dépenses liées aux infrastructures routières et aux réseaux lors du calcul des impacts [#3a5c3e0](https://github.com/incubateur-ademe/benefriches/commit/3a5c3e0).
- Affichage de la surface totale du site sur l'étape des espaces verts publics [#be075fb](https://github.com/incubateur-ademe/benefriches/commit/be075fb).
- Pré-remplissage de la surface de plancher des nouveaux bâtiments lors de la création d'un projet urbain [#071dc5a](https://github.com/incubateur-ademe/benefriches/commit/071dc5a).

### Évolutions techniques
- Refactorisation de l'architecture API pour améliorer la maintenabilité et l'évolutivité [#3a3efa7](https://github.com/incubateur-ademe/benefriches/commit/3a3efa7).
- Amélioration des tests unitaires et d'intégration pour garantir la qualité du code [#277485a](https://github.com/incubateur-ademe/benefriches/commit/277485a).
- Mise en place d'un système de synchronisation quotidienne des abonnements à la newsletter à partir du CRM via un cron Scalingo [#91b0481](https://github.com/incubateur-ademe/benefriches/commit/91b0481).
- Amélioration de la configuration CI/CD pour optimiser les temps de build et de déploiement [#f12d312](https://github.com/incubateur-ademe/benefriches/commit/f12d312).
- Utilisation de variables d'environnement standardisées pour les flags de fonctionnalité dans l'application web [#f067c7f](https://github.com/incubateur-ademe/benefriches/commit/f067c7f).
- Refactorisation du code pour extraire des composants réutilisables et améliorer la modularité [#92404ae](https://github.com/incubateur-ademe/benefriches/commit/92404ae).

### Autres changements
- Mise à jour de la documentation pour refléter les nouvelles fonctionnalités et les modifications apportées [#4995672](https://github.com/incubateur-ademe/benefriches/commit/4995672).
- Correction de références de fichiers obsolètes dans la documentation CLAUDE.md [#8bf42b4](https://github.com/incubateur-ademe/benefriches/commit/8bf42b4).
- Mise à jour des dépendances mineures et correctives [#047c413](https://github.com/incubateur-ademe/benefriches/commit/047c413), [#397c36b](https://github.com/incubateur-ademe/benefriches/commit/397c36b), [#e5745e1](https://github.com/incubateur-ademe/benefriches/commit/e5745e1).
- Amélioration de la gestion des erreurs et des logs dans l'API [#ef5a2cd](https://github.com/incubateur-ademe/benefriches/commit/ef5a2cd).
- Ajout de tests unitaires pour les nouveaux composants et fonctionnalités [#3b74413](https://github.com/incubateur-ademe/benefriches/commit/3b74413).
