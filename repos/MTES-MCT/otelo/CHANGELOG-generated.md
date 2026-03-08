## Changelog : otelo (30 derniers jours)

### Résumé
Ce changelog résume les améliorations apportées à otelo au cours du dernier mois. Les développements se concentrent sur l'ajout de nouvelles fonctionnalités, notamment la gestion des sources de données, l'historique des simulations, l'exportation de données améliorée et la gestion des utilisateurs. Des corrections de bugs et des optimisations ont également été implémentées pour améliorer la stabilité et l'expérience utilisateur.

### Évolutions fonctionnelles
- Ajout d'une page de retour utilisateur [#16](https://github.com/MTES-MCT/otelo/pull/16).
- Implémentation de la suppression de groupes EPCI [#15](https://github.com/MTES-MCT/otelo/pull/15).
- Ajout de la gestion des sources de données [#4](https://github.com/MTES-MCT/otelo/pull/4).
- Possibilité d'exporter les résultats des simulations en image.
- Ajout d'un bouton d'exportation des résultats des simulations.
- Amélioration de l'affichage des statistiques et ajout de la liste des EPCI dans l'export.
- Ajout de la gestion des utilisateurs et amélioration de l'interface.
- Ajout d'une page 404 et actualisation automatique après déconnexion.
- Amélioration de l'affichage des logements vacants et secondaires.
- Correction de l'affichage des totaux cumulés pour les logements vacants et secondaires.
- Correction de l'arrondi de la taille des ménages.
- Correction de l'affichage des offres potentielles RS.
- Correction de l'affichage des graphiques récapitulatifs.
- Correction de l'export Excel pour les décimales.

### Évolutions techniques
- Migration vers une meilleure solution d'authentification (Better Auth) [#3](https://github.com/MTES-MCT/otelo/pull/3).
- Refonte de la gestion des utilisateurs.
- Ajout de tests unitaires basés sur Excel pour le moteur de calcul.
- Implémentation du versioning des données (datapack) [#23](https://github.com/MTES-MCT/otelo/pull/23).
- Ajout de l'historique des résultats des simulations [#10](https://github.com/MTES-MCT/otelo/pull/10) et [#13](https://github.com/MTES-MCT/otelo/pull/13).
- Amélioration de la gestion des millésimes dans les calculs de taux [#28](https://github.com/MTES-MCT/otelo/pull/28).
- Correction de l'injection du module CLI.
- Correction de la configuration des paramètres de millésime.
- Correction de la gestion des années de base.
- Amélioration de la gestion des erreurs lors de la migration de la base de données.
- Ajout de tests Prisma.
- Amélioration de la configuration Swagger pour les enums.
- Correction de la construction de l'application.
- Utilisation de Puppeteer pour gérer Chromium.

### Autres changements
- Ajout d'une page de changelog.
- Ajout d'un script postinstall pour Chromium.
- Suppression de la commande prune.
- Nettoyage du code et suppression des logs inutiles.
- Correction de fautes de frappe.
- Mise à jour des dépendances.
- Ajout d'un banner de feedback.
- Amélioration de la navigation du menu d'en-tête pour les utilisateurs connectés.
- Correction d'un problème de blocage de l'interface lors du défilement vers un élément spécifique.
- Ajout d'une limitation de la taille de page pour éviter les blocages.
- Ajout d'un fichier `.env` local.
- Ajout de tests pour le calcul des logements indécents.
