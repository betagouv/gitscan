## Changelog : catalogi (30 derniers jours, au 29 octobre 2026)

### Résumé
Cette période a été marquée par une refonte de l'interface de consultation des logiciels, offrant une navigation plus fluide et une présentation plus claire. En parallèle, les mécanismes d'importation de données ont été considérablement renforcés pour mieux gérer les sources externes et garantir la précision des informations répertoriées.

### Évolutions fonctionnelles
- **Refonte de la page de détails des logiciels** : passage à un format de page unique avec une navigation latérale pour faciliter l'accès aux différentes sections.
- **Amélioration de l'expérience utilisateur** : optimisation de la navigation interne et restauration de contenus sur la page de détails.

### Évolutions techniques
- **Gestion des données et sources** :
    - Amélioration de l'importation des sources externes (forges de dépôts, gestion des identifiants et détection des doublons).
    - Mise en place d'une gestion de priorité des sources par catégorie.
    - Optimisation de la localisation via la fusion des textes provenant de sources externes par langue.
    - Amélioration de l'exportation des données au format Codemeta (ajout de version et export par dump de base de données).
- **Infrastructure et Qualité** :
    - Mise à jour de l'environnement de tests (Playwright) pour assurer la compatibilité avec Ubuntu 26.04.
    - Sécurisation de l'environnement de build par le verrouillage de la version Node.js.
    - Ajout de scripts de génération de données (seed) pour faciliter les tests et le développement.
    - Amélioration de la suite de tests end-to-end (e2e).

### Autres changements
- Nettoyage de code et ajustements de style.
