## Changelog : anssi-portail (30 derniers jours, au 16 novembre 2026)

### Résumé
Ce mois-ci, le portail a franchi une étape importante dans l'enrichissement de ses outils de sensibilisation et d'accompagnement. Les simulations de hameçonnage sont devenues plus complètes, plus interactives et peuvent désormais être intégrées sur des sites externes. La boîte à outils s'est également étoffée avec de nouveaux modèles pratiques, tandis qu'un système de collecte d'avis utilisateurs a été déployé pour mieux mesurer l'efficacité des parcours de sécurisation.

### Évolutions fonctionnelles
- **Simulations de hameçonnage** : 
    - Enrichissement des scénarios avec de nouveaux modèles d'emails (ANSSI, Banque Postale, CPF, etc.) et l'intégration de leurs réponses.
    - Amélioration de l'expérience de test : affichage des scores, feedback visuel immédiat (bonnes/mauvaises réponses), et adaptation de l'interface aux mobiles et tablettes.
    - Déploiement de composants web (WebC) permettant d'intégrer les tests de hameçonnage sur des sites tiers.
- **Boîte à outils** : 
    - Ajout de nombreux nouveaux modèles de documents (RACI, revue des droits d'accès, revue des comptes utilisateurs, gestion des mots de passe, etc.).
    - Intégration d'un module de retour utilisateur permettant de soumettre des avis directement depuis les outils.
    - Ajout d'une fonctionnalité de prévisualisation des contenus (sous forme d'image ou de modale).
- **Parcours de sécurisation** : Mise en place d'un système de collecte d'avis utilisateurs automatique à différentes étapes clés (obtention de badge, complétion du parcours, etc.).
- **Améliorations diverses** : 
    - Optimisation de la recherche entreprise (recherche plus flexible).
    - Corrections sur les filtres de recherche, l'affichage du centre d'aide et le mode maintenance.
    - Mise à jour des informations de contact et des statistiques de diagnostics.

### Évolutions techniques
- **Infrastructure & CI/CD** : 
    - Migration de la stack vers Node.js 26 et PostgreSQL 18.
    - Remplacement de `s3cmd` par la CLI AWS officielle pour les processus d'intégration continue.
    - Optimisation de l'environnement de développement via Nix et simplification de la gestion des paquets Node.js/pnpm.
- **Architecture & Sécurité** : 
    - Refonte du système de gestion des erreurs : séparation du signalement des erreurs et de leur traitement HTTP pour une meilleure robustesse.
    - Renforcement de la sécurité via l'ordonnancement des politiques CSP et la correction d'une vulnérabilité sur `body-parser`.
    - Refactorisation de la gestion du stockage de session et encapsulation du `sessionStorage`.
- **Qualité de code & UI** : 
    - Mise à jour et centralisation du Design System (`@lab-anssi/ui-kit`).
    - Normalisation de la typographie (gestion des espaces insécables) sur l'ensemble du projet (Markdown, Svelte, HTML, Jekyll).
    - Amélioration des performances de rendu serveur (Svelte) et de la gestion des ressources XLSX.

### Autres changements
- Nettoyage de code : suppression de nombreux "feature flags" obsolètes (notamment liés à NIS2) et de propriétés inutilisées.
- Mise à jour des contenus éditoriaux et correction de divers textes et diacritiques pour une meilleure qualité de rédaction.
