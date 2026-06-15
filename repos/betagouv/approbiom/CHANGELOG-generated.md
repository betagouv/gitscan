## Changelog : approbiom (30 derniers jours, au 12 juin 2026)

### Résumé
Ce mois-ci, le projet approbiom a connu un développement rapide, passant d'un dépôt initialisé à une base solide pour la création de widgets pour Grist. L'accent a été mis sur la création de widgets de tableau et de carte interactifs, ainsi que sur la mise en place d'une infrastructure de build et de déploiement robuste.

### Évolutions fonctionnelles
- Ajout d'un widget de tableau permettant de sélectionner des colonnes et de filtrer les lignes. [#9](https://github.com/betagouv/approbiom/issues/9) et [#10](https://github.com/betagouv/approbiom/issues/10)
- Implémentation d'un widget de carte interactive affichant des données géographiques. [#11](https://github.com/betagouv/approbiom/issues/11)
- Possibilité de choisir les colonnes à afficher et leur ordre dans le widget tableau.
- Affichage du libellé des colonnes au lieu de leur identifiant dans le widget tableau.
- Ajout d'une barre de recherche permettant de filtrer les lignes du tableau.
- Création d'un menu déroulant pour l'édition des types de référence.
- Amélioration de la réactivité de l'affichage des départements sur la carte.

### Évolutions techniques
- Mise en place d'une chaîne CI/CD avec GitHub Actions pour la construction et le déploiement automatique.
- Configuration de l'environnement de développement pour servir une instance Grist en mode développement.
- Utilisation de Playwright pour les tests E2E, notamment pour le widget carte.
- Refactoring du code pour suivre les bonnes pratiques Vue.js (nommage des composants).
- Utilisation des types Grist Plugin API pour une meilleure intégration.
- Passage à une structure MPA (Multiple Page Application) avec Vite.
- Amélioration de la gestion des configurations et des variables d'environnement.

### Autres changements
- Correction de diverses erreurs de linting.
- Suppression de dossiers inutiles (docs, dist).
- Ajout d'un fichier `.nojekyll` pour éviter les problèmes de déploiement sur GitHub Pages.
- Documentation et commentaires ajoutés pour faciliter la compréhension du code.
