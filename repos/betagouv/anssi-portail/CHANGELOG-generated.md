## Changelog : anssi-portail (30 derniers jours, au 10 novembre 2026)

### Résumé
Ce mois a été marqué par une montée en puissance des outils de sensibilisation et de l'accompagnement. Le portail a vu le déploiement de nouveaux tests de simulation de hameçonnage plus complets et une refonte majeure de la "Boîte à outils", qui propose désormais des modèles de documents personnalisables et un système de retour utilisateur. L'annuaire des contacts a également été enrichi pour offrir une meilleure précision géographique et sectorielle.

### Évolutions fonctionnelles
- **Simulation de hameçonnage** :
    - Déploiement de nouveaux scénarios de tests en production.
    - Amélioration de l'expérience utilisateur sur mobile et tablette.
    - Ajout de fonctionnalités de suivi : affichage des scores, distinction visuelle des messages lus/non-lus et possibilité de laisser un avis après le test.
    - Mise à disposition de composants web externes pour faciliter l'intégration des tests sur d'autres sites.
- **Boîte à outils** :
    - Ajout de nouveaux modèles de documents et procédures (Recensement, Revue des droits d'accès, Modification de mots de passe, etc.).
    - Mise en place d'un système de prévisualisation des documents (via modale) avant téléchargement.
    - Évolution terminologique : les "tutoriels" sont désormais appelés "procédures".
    - Intégration d'un module de collecte des retours utilisateurs pour chaque outil.
- **Contacts et annuaires** :
    - Mise à jour et enrichissement des données de contact (niveaux national, régional et sectoriel).
    - Amélioration de l'affichage des cartes de contacts.
- **Contenu et navigation** :
    - Création d'une nouvelle page dédiée au "Kit Relais".
    - Amélioration des parcours de sécurisation et des redirections vers les pages de diagnostic.

### Évolutions techniques
- **Infrastructure et Environnement** :
    - Migration de la stack vers Node.js 26 et PostgreSQL 18.
    - Amélioration de la gestion des environnements métier et simplification des tests.
- **Architecture et Backend** :
    - Refonte complète du système de signalement des erreurs (séparation du traitement HTTP et du contrat de signalement).
    - Réorganisation massive des routes de l'API (outils, mini-tests, annuaires) pour une meilleure maintenabilité.
    - Optimisation de la gestion des middlewares et de la configuration de sécurité (CSP).
- **Interface et Design (UI/UX)** :
    - Mise à jour majeure du kit d'interface (`@lab-anssi/ui-kit` passage en v2.x).
    - Généralisation de l'utilisation des composants du Design System (DSFR) pour les alertes, les notifications et les uploads.
    - Optimisation du rendu côté serveur (SSR) et alignement avec le rendu client (HMR) pour Svelte.
- **Qualité et Toolchain** :
    - Amélioration de la robustesse des tests et de la gestion des dépendances.

### Autres changements
- **Qualité du code (Linting)** : Mise en place de nouvelles règles de normalisation typographique (gestion des espaces insécables) sur l'ensemble des fichiers (Markdown, Svelte, HTML, Jekyll).
- **Nettoyage** : Réorganisation de la structure des dossiers, suppression des commentaires inutiles et renommage de fichiers pour plus de clarté.
