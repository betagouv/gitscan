## Changelog : catalogi (30 derniers jours, au 29 octobre 2026)

### Résumé
Ce mois-ci, le projet a connu une évolution majeure de son interface utilisateur, notamment avec une refonte de la page de détails des logiciels pour offrir une navigation plus fluide. Parallèlement, d'importants travaux ont été menés sur la fiabilité de l'importation des données et sur l'amélioration des capacités d'exportation (Codemeta), garantissant une meilleure gestion des sources externes.

### Évolutions fonctionnelles
- **Refonte de l'affichage des logiciels** : La page de détails d'un logiciel passe désormais sur un format "page unique" avec une navigation latérale pour faciliter la consultation des différentes sections.
- **Amélioration de l'ergonomie** : Optimisation de la navigation entre les sections et restauration de contenus sur la page de détails.

### Évolutions techniques
- **Gestion et importation des données** :
    - Amélioration de la logique d'importation pour mieux gérer les sources externes (fusion des textes localisés par langue, gestion des priorités par catégorie de source).
    - Automatisation de la création de sources de forges à partir d'identifiants de dépôts.
    - Renforcement de la déduplication des données pour éviter les doublons lors de la découverte de liens logiciels (gestion des identifiants Zenodo, CNLL, etc.).
    - Ajout d'une fonctionnalité d'exportation des données au format Codemeta via un dump de la base de données.
- **Infrastructure et Qualité** :
    - **Sécurité** : Verrouillage de la version Node.js (24.22.1) pour répondre aux mises à jour de sécurité d'octobre 2026.
    - **Tests** : Mise à jour de Playwright pour assurer la compatibilité avec Ubuntu 26.04 et extension des tests de bout en bout (e2e) pour couvrir le nouveau parcours utilisateur.
    - **Développement** : Ajout d'un script de génération de données de test (`db:seed`) à la racine du projet.

### Autres changements
- Nettoyage du code et ajustements de style (Prettier).
- Mise à jour de la bibliothèque de composants UI (`@codegouvfr/react-dsfr`).
