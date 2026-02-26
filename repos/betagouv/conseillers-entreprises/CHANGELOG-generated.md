## Changelog : conseillers-entreprises (30 derniers jours)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la correction de bugs, l'amélioration de l'expérience utilisateur (notamment dans la gestion des formulaires et des recherches), l'optimisation des performances et la préparation du service pour une meilleure sécurité et maintenabilité. Des efforts ont également été faits pour améliorer l'accessibilité et la conformité aux normes RGAA.

### Évolutions fonctionnelles
- Correction d'un bug où une erreur 404 pouvait se transformer en erreur 500 (#4294).
- Amélioration de la gestion des URL pour les sollicitations par email (#4288).
- Correction d'un problème empêchant la soumission de sollicitations sans code INSEE (#4269).
- Ajout d'un bandeau d'information configurable pour la page d'accueil (#4262).
- Amélioration de la recherche thématique des besoins (#4251).
- Ajout d'un onglet de suivi pour les antennes régionales (#4230).
- Unification de l'onglet d'optimisation et de veille (#4203).
- Amélioration de l'export CSV des sollicitations (#4229).
- Correction d'un problème de redirection après la soumission d'un formulaire (#4215).

### Évolutions techniques
- Refactorisation du code pour améliorer la lisibilité et la maintenabilité, notamment dans la gestion des filtres de recherche des besoins.
- Mise à jour des dépendances : Nokogiri (1.18.10 -> 1.19.1), Rack (3.2.4 -> 3.2.5), Webpack (5.103.0 -> 5.104.1).
- Intégration d'AppSignal pour le monitoring et le suivi des erreurs (#4265).
- Utilisation de gem.coop comme source de gems (#4232).
- Amélioration de la gestion des erreurs et des réponses HTTP (retour de 404 au lieu de lever des exceptions).
- Refactorisation de l'affichage du code INSEE avec un contrôleur Stimulus pour améliorer l'accessibilité et la validation.
- Ajout de tests pour améliorer la couverture du code et la robustesse des fonctionnalités.
- Suppression de code obsolète et de configurations inutiles.
- Amélioration de la pagination Kaminari (passage à 25 éléments par défaut).

### Autres changements
- Ajout d'un fichier `.vscode` pour les configurations VS Code (puis suppression pour éviter le tracking).
- Ajout d'une mention de sponsoring d'AppSignal dans le README.
- Ajout d'un `crawl-delay` dans le fichier `robots.txt` pour améliorer le respect des robots d'indexation.
- Ajout d'une notice de confidentialité dans le modal de personne.
- Suppression de la directive `local: true` dans les formulaires.
- Documentation de la variable d'environnement `STAGING_ENV`.
- Correction de typos et amélioration de la qualité du code.
