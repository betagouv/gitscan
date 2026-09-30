## Changelog : demarche.numerique.gouv.fr (30 derniers jours, au 29/09/2026)

### Résumé
Ce mois a été marqué par un effort important sur la résilience du système et la sécurité des accès. La plateforme gère désormais mieux les indisponibilités des services externes (comme l'API Entreprise) en permettant aux usagers de poursuivre leurs démarches en "mode dégradé". La sécurité a été renforcée pour les profils sensibles (administrateurs et experts) via l'obligation d'utiliser ProConnect et l'introduction de la double authentification (MFA). Enfin, l'interface a bénéficié de nombreuses améliorations d'accessibilité et de nouveaux outils de filtrage pour les agents.

### Évolutions fonctionnelles
- **Résilience des données externes :** Mise en place d'un mode dégradé pour les champs dépendants de l'API Entreprise (SIRET/RNA). En cas d'échec de l'API, l'usager peut valider sa saisie et une tentative de synchronisation est programmée automatiquement [#14059](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/14059).
- **Gestion du consentement (AMI) :** Amélioration du parcours de consentement des usagers, incluant un nouveau bloc de suivi sur la page de soumission et une compatibilité avec les applications mobiles [#13755](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/13755).
- **Sécurité des accès :** 
    - Généralisation de l'usage de ProConnect pour les administrateurs et les experts [#13779](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/13779).
    - Renforcement de la sécurité des super-administrateurs avec l'obligation de MFA/OTP et un verrouillage automatique du compte après plusieurs échecs [#13936](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/13936).
- **Outils pour les instructeurs et administrateurs :** 
    - Ajout de filtres par période pour les colonnes de dates [#14092](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/14092).
    - Refonte visuelle de l'interface d'administration avec l'utilisation de nouvelles tuiles de configuration pour une meilleure lisibilité.
- **Accessibilité et Interface (UI) :** 
    - Amélioration de l'accessibilité des composants de sélection (combobox/select) pour les technologies d'assistance [#14099](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/14099).
    - Intégration et mise à jour du widget "Gaufre" (La Suite) pour supporter le mode sombre et améliorer l'interactivité [#13262](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/13262).
    - Correction de divers problèmes de typographie et d'affichage des badges.

### Évolutions techniques
- **Sécurité et Isolation :** Implémentation d'un système de "sandboxing" (isolation via subprocess) pour le traitement des images (libvips) et l'exécution de commandes, afin de protéger l'infrastructure des données malveillantes [#13854](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/13854).
- **Optimisation des performances :** 
    - Mise à jour vers Sidekiq 8 pour une meilleure gestion des tâches asynchrones [#13926](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/13926).
    - Optimisation des requêtes GraphQL via le préchargement (preloading) des données et le chargement à la demande des descripteurs de champs.
    - Amélioration des index de base de données pour accélérer la recherche et le suivi de l'inactivité des utilisateurs.
- **Refactoring et Architecture :** 
    - Migration massive de templates HAML vers ERB pour une meilleure maintenance.
    - Refonte de la logique de révision des dossiers pour assurer une meilleure intégrité des données lors des clones et des modifications.
    - Nettoyage du moteur de recherche en optimisant l'utilisation des `tsvectors`.
- **Infrastructure et CI/CD :** 
    - Mise à jour de la chaîne de CI pour utiliser Ubuntu 24.04.
    - Optimisation de la gestion des assets avec Vite et amélioration du cache des tests.

### Autres changements
- **Documentation :** Mise à jour de la documentation technique (`AGENTS.md`) et des guides de configuration des variables d'environnement.
- **Maintenance :** Nettoyage de code mort, suppression de vues obsolètes et de dépendances inutilisées.
