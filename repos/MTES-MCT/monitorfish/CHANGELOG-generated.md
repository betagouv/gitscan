## Changelog : monitorfish (30 derniers jours, au 30 juillet 2026)

### Résumé
Cette période a été marquée par des améliorations significatives sur les formulaires de contrôle (M1 et M3), notamment en termes d'ergonomie et de gestion des champs facultatifs. Des corrections de bugs ont été apportées concernant l'affichage des groupes de navires, la gestion des alertes de position et la performance des requêtes AIS. De nouvelles fonctionnalités ont été implémentées, comme la duplication de signalements et l'ajout de la prise en compte des navires sous charte dans les groupes prioritaires.

### Évolutions fonctionnelles
- Possibilité de dupliquer un signalement (#5290).
- Ajout de la prise en compte des navires sous charte dans les groupes prioritaires (#5289, #5270).
- Correction du problème de troncature du calendrier de fin de mission (#5269).
- Amélioration de l'affichage des groupes de navires et des signalements dans le contrôle report.
- Correction de bugs concernant l'archivage automatique des alertes de position (#5322).
- Correction de bugs sur les use-cases backend et assainissement du `ControllersExceptionHandler` (#5323).
- Correction de plusieurs bugs concernant les missions, le rafraîchissement des préavis, les avaries et les couleurs des groupes de navires (#5320).
- Correction du comportement du bouton "centrer sur la carte" dans la vue liste des signalements (#5128).
- Correction d'un bug lié aux clics multiples pour saisir le poids des espèces dans le tableau (#5317).
- Correction de l'affichage des groupes prioritaires pour les unités externes (#5314).
- Ajout d'une case "cibles prioritaires" au formulaire de création et de modification d'un groupe (#5310).
- Correction d'un crash dans le gestionnaire de survol des lignes d'espèces (#5271).
- Amélioration du comportement du bouton "afficher sur la carte" pour les signalements (#5273).
- Correction de bugs sur les formulaires M1 et M3 (e-ISR) : affichage des champs facultatifs, logique d'applicabilité, ajout des champs armateur (#5257, #5168, #5245).
- Mise à jour de la REG UE pour les avaries VMS (#5241).

### Évolutions techniques
- Optimisation de la requête des dernières positions AIS pour améliorer les performances (#5300).
- Correction du scraper Legipeche pour gérer les pages non visitées (#5268).
- Suppression de la dépendance `ktlint` et correction des violations restantes (#5261).
- Remplacement des imports wildcard par des imports explicites.
- Suppression de code obsolète et amélioration de la structure du code.
- Refactoring du code pour améliorer la lisibilité et la maintenabilité.
- Mise à jour de la librairie `postcss` dans le frontend (#5302).

### Autres changements
- Ajout de commentaires et documentation pour clarifier le code.
- Amélioration des tests Cypress pour une meilleure couverture et fiabilité.
- Mise à jour des descriptions des nouvelles fonctionnalités.
- Corrections de linting et de style de code.
- Ajout d'une section sur le box-sizing dans le fichier `CONTRIBUTING.md`.
- Suppression de fichiers de configuration inutiles.
