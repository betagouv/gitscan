## Changelog : codebox (30 derniers jours, au 12 novembre 2026)

### Résumé
Ce mois a été marqué par une étape majeure : le projet change de nom, passant de `just-code` à `codebox`. Parallèlement, l'expérience utilisateur a été profondément remaniée avec un nouvel assistant de configuration (wizard) plus intuitif, une interface traduite en français et une gestion beaucoup plus robuste de la récupération des données et des secrets.

### Évolutions fonctionnelles
- **Rebranding majeur :** Changement de nom global du projet (`just-code` devient `codebox`) impactant le CLI, les modules et les chemins d'installation.
- **Nouvel assistant de configuration (Wizard) :** Refonte complète du processus d'initialisation avec un flux en plusieurs étapes (sélection des modèles, configuration de l'identité Git, intégration du jeton GitHub et récapitulatif interactif).
- **Amélioration de l'interface (TUI) :** 
    - Traduction française de nombreux messages de confirmation et d'introduction.
    - Optimisation de l'affichage (gestion du curseur lors du redimensionnement, meilleure visibilité des options de sélection).
- **Nouveaux harnais d'agents :** Support du harnais "Pi" comme seconde option pour les agents ([#176](https://github.com/etalab-ia/codebox/issues/176)).
- **Gestion de la sortie :** Ajout d'un écran de fin de session permettant de récupérer les modifications avant de quitter.
- **Statistiques d'usage :** Introduction d'un système de collecte de statistiques avec gestion explicite du consentement de l'utilisateur.

### Évolutions techniques
- **Mécanismes de récupération (Recovery) :** 
    - Implémentation d'un chemin de récupération pour les instances Microsandbox arrêtées ou mises à jour.
    - Amélioration de la résilience du workspace pour préserver le travail commité lors des rafraîchissements ou des erreurs.
- **Gestion des secrets et de la sécurité :**
    - Nouveau système de livraison des secrets approuvés directement dans le bac à sable (guest) via des fichiers `.env` ou le proxy Microsandbox.
    - Durcissement de la vérification des empreintes (digests) et des fichiers de configuration.
    - Intégration de détecteurs de secrets pour sécuriser l'environnement.
- **Gestion du Workspace et Git :** Amélioration de la détection des branches, de la synchronisation avec l'hôte et de la gestion des modifications lors de la reprise de session.
- **Infrastructure et Runtime :** 
    - Migration vers OpenCode v2.
    - Mises à jour régulières du runtime Microsandbox (v0.7.14).
    - Optimisation de la CI/CD (résolveurs DNS explicites pour les conteneurs Ubuntu).

### Autres changements
- **Documentation :** Mise à jour massive de la documentation technique, notamment sur les protocoles de qualification, la gestion des secrets et l'utilisation des VM (Lima).
- **Tests :** Extension importante de la couverture de tests de qualification pour inclure macOS (arm64), Linux et Windows.
