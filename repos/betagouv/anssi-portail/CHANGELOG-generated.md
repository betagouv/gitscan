## Changelog : anssi-portail (30 derniers jours, au 04 novembre 2026)

### Résumé
Ce mois a été marqué par un enrichissement majeur des contenus et des outils du portail. La simulation de hameçonnage a été considérablement étendue avec de nouveaux scénarios réalistes, tandis que la boîte à outils a été modernisée avec des fonctionnalités de prévisualisation et de nouveaux modèles de documents. Parallèlement, une refonte technique importante a permis de moderniser l'infrastructure et d'harmoniser l'interface utilisateur avec le Design System de l'État.

### Évolutions fonctionnelles
- **Simulation de hameçonnage** :
    - Ajout de nombreux nouveaux scénarios d'emails (ANSSI, banques, services publics comme La Poste ou amendes.gouv, etc.) avec leurs réponses associées.
    - Amélioration de l'expérience utilisateur : affichage des scores en fin de test, distinction visuelle des messages lus, et optimisation de l'interface pour mobile et tablette.
    - Mise en place d'un système de collecte des retours utilisateurs et de suivi des résultats.
- **Boîte à outils** :
    - Ajout de nouveaux modèles de documents personnalisables (gestion des mots de passe, listes d'activités, revue des droits d'accès, etc.).
    - Intégration d'une fonctionnalité de prévisualisation des documents (sous forme d'image ou de modale) avant téléchargement.
    - Ajout d'un module de retours utilisateurs directement sur les outils.
- **Contacts et annuaires** :
    - Enrichissement et mise à jour des données de contacts nationaux, régionaux et sectoriels.
- **Contenu et Web** :
    - Création de la page "Kit Relais" avec rendu côté serveur (SSR).
    - Mise en place d'un système d'avis et de retours sur les articles du blog.
    - Amélioration de la présentation des webinaires et des parcours de sécurisation.

### Évolutions techniques
- **Infrastructure et Toolchain** :
    - Migration de la stack vers Node.js 26.
    - Mise à jour de l'environnement Ruby et optimisation de la configuration CI/CD (utilisation de `.nvmrc`).
- **Interface Utilisateur (UI)** :
    - Passage à la version 2.0.0 du `@lab-anssi/ui-kit`.
    - Intégration native des composants du Design System (DSFR) pour les alertes et les notifications.
- **Architecture logicielle** :
    - Refactorisation massive des routes API pour une meilleure organisation (outils, annuaires, mini-tests).
    - Extraction et mutualisation de composants réutilisables (modales de prévisualisation, blocs de code, composants de thématiques).
    - Centralisation de la gestion des archives et de la manipulation des fichiers (XLSX, PDF).
- **Sécurité et Performance** :
    - Renforcement des politiques de sécurité du contenu (CSP) et gestion des blobs.
    - Optimisation du chargement des dépendances PDF et amélioration du rechargement à chaud (Hot Reload) pour le développement Svelte.

### Autres changements
- Nettoyage général du code et suppression de composants obsolètes (Jekyll).
- Amélioration de la qualité typographique (césure des mots, gestion des accents).
- Harmonisation du nommage des fichiers et des variables pour une meilleure maintenabilité.
