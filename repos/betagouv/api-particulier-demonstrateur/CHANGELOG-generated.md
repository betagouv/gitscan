## Changelog : api-particulier-demonstrateur (30 derniers jours, au 14 septembre 2026)

### Résumé
Les récentes évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment par l'ajout de messages d'information contextuels et l'optimisation de l'affichage des éléments d'interface (boutons, panneaux d'aide et alertes). Parallèlement, la stabilité du projet a été renforcée par une meilleure gestion des dépendances et une mise à jour de l'environnement de déploiement.

### Évolutions fonctionnelles
- **Information et guidage utilisateur** :
    - Ajout de messages d'information concernant la récupération automatique des justificatifs avant l'étape FranceConnect ([#6944](https://github.com/betagouv/api-particulier-demonstrateur/issues/6944)).
    - Déplacement du panneau d'information FranceConnect de la section "éligibilité" vers la page de "connexion" pour une meilleure pertinence.
    - Masquage automatique du panneau d'information FranceConnect pour les profils (personas) n'utilisant pas ce mode d'authentification.
- **Améliorations de l'interface (UI)** :
    - Correction de l'affichage des alertes pour éviter qu'elles ne soient masquées par le pied de page.
    - Ajustement de la largeur des boîtes d'aide (COG) pour assurer un alignement correct dans les colonnes.
    - Optimisation des espacements (boutons FranceConnect, textes d'aide au téléchargement) et correction de la ponctuation.

### Évolutions techniques
- **Infrastructure et CI/CD** :
    - Mise à jour de l'environnement d'intégration continue pour utiliser Node 24.
    - Automatisation des mises à jour de dépendances via un calendrier hebdomadaire.
    - Mise en place d'un gel des versions majeures des dépendances pour garantir la stabilité du projet.
- **Architecture et logique** :
    - Optimisation de la résolution des cas d'usage via le segment de l'URL (pathname).
    - Migration automatique des configurations suite à l'installation des paquets npm.

### Autres changements
- **Qualité du code et style** :
    - Mise à jour et reformatage de plusieurs layouts pour assurer la compatibilité avec Prettier 3.9.
