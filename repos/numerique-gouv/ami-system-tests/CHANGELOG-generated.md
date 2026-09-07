## Changelog : ami-system-tests (30 derniers jours, au 02 septembre 2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur la stabilisation de la suite de tests et l'optimisation de la chaîne de validation (CI/CD). Les tests sont désormais plus robustes face aux instabilités de l'interface (notamment sur la gestion du code d'accès) et le système de reporting a été modernisé pour offrir une meilleure visibilité sur les résultats de chaque branche.

### Évolutions fonctionnelles
- **Amélioration de la fiabilité des tests** :
    - Optimisation de la gestion du "code d'accès" (ajout de tentatives de réessai, gestion des délais d'apparition et contournement par cookie pour réduire la fragilité).
    - Renforcement de la robustesse de la page d'accueil (meilleure gestion des URL avec hash et tolérance aux variations de texte comme les apostrophes typographiques).
- **Corrections de sélecteurs** :
    - Mise à jour des sélecteurs pour la webapp, notamment pour FranceConnect et le bouton "Suivi".
    - Ajustement de la gestion des popups de code d'accès sur la webapp.
- **Tests mobiles** :
    - Enrichissement des rapports avec des métadonnées plus précises (épics, stories, tags).
    - Essai de tests Android via un APK buildé.

### Évolutions techniques
- **Modernisation du reporting** :
    - Migration vers Allure 3 pour un reporting plus performant.
    - Mise en place de l'isolation des rapports par Pull Request et de la gestion de l'historique des résultats.
- **Optimisation de la CI/CD (GitHub Actions)** :
    - Découplage du cycle de tests par rapport aux déploiements Scalingo : utilisation de l'API GitHub pour vérifier le statut des déploiements au lieu d'attendre Scalingo directement.
    - Flexibilité accrue : possibilité de configurer les suites de tests, de cibler l'environnement d'une branche spécifique et de sauter l'étape de vérification Scalingo lors de déclenchements manuels.
    - Mise à jour des versions des GitHub Actions et amélioration de la gestion des secrets.
- **Performance et environnement** :
    - Optimisation de la taille de la fenêtre Chrome Headless pour mieux correspondre à la SPA.
    - Création de cibles de build spécifiques pour optimiser la génération des rapports et résoudre des problèmes de téléchargement de drivers sur macOS.

### Autres changements
- **Documentation** : Mise à jour des documents d'architecture (ADR) concernant le découplage de la CI et l'adoption d'Allure 3.
- **Maintenance du code** :
    - Nettoyage important du code mort (variables de branche inutilisées, attentes Scalingo obsolètes).
    - Amélioration de la qualité des logs avec l'ajout de commandes de debug pour faciliter le diagnostic.
    - Correction de problèmes d'échappement dans les scripts shell.
