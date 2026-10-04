## Changelog : benefriches (30 derniers jours, au 02/10/2026)

### Résumé
Ce mois-ci, bénéfriches a franchi une étape importante dans l'amélioration de l'expérience utilisateur avec un nouveau parcours d'accueil (onboarding) et un assistant de mise à jour de site plus intuitif et sécurisé. Les capacités de simulation ont été enrichies par l'introduction d'un nouveau score de développement et une mise à jour majeure des données de référence (statistiques ANCT, données DVF et zonages urbains), garantissant des analyses d'impact plus précises et actualisées.

### Évolutions fonctionnelles
- **Parcours utilisateur & Interface :**
    - Refonte complète du parcours d'onboarding avec un nouveau flux en 3 étapes.
    - Amélioration de l'assistant de mise à jour des sites : ajout de sous-groupes, gestion de l'état de sauvegarde, avertissements en cas de modifications non enregistrées et possibilité de modifier les zones urbaines personnalisées.
    - Ajout de liens de modification directe dans les étapes du résumé de site.
- **Calculs & Données :**
    - Intégration d'un nouveau "score de développement" calculé à partir des impacts du projet.
    - Mise à jour massive des données de référence : intégration des statistiques de l'Observatoire des Territoires (ANCT), des transactions DVF 2025 et des nouveaux zonages urbains (ABC/ALDO).
    - Optimisation des calculs d'impact (augmentation de la valeur foncière locale et kilomètres évités) selon les nouveaux critères de zonage.
- **Corrections :**
    - Correction de l'affichage des surfaces de zones humides dans les modales de régulation de l'eau.
    - Amélioration de la gestion des contacts CRM (nettoyage automatique des caractères interdits dans les noms).

### Évolutions techniques
- **Architecture & State Management :**
    - Migration de la gestion d'état Redux dans l'application web (passage de `createSlice` à `createReducer`).
    - Refactorisation de l'API pour aligner les fichiers de cas d'utilisation et d'adaptateurs sur les conventions du projet.
- **Qualité & Tests :**
    - Renforcement de la qualité du code via l'intégration d'Oxlint (nouvelles règles de convention API et de gestion des imports).
    - Augmentation de la couverture de tests de bout en bout (E2E) sur les flux de mise à jour de site et les scénarios d'inéligibilité.
- **Infrastructure & Intégration :**
    - Amélioration de la robustesse de la connexion au CRM Connect (validation des configurations et récupération des contacts lors d'interruptions de service).
    - Mise en place d'un script de prévisualisation autonome pour les emails de cycle de vie.

### Autres changements
- **Documentation :** Mise à jour de la documentation technique concernant le nouveau référentiel du score de développement.
- **Outils de développement :** Optimisation et configuration des agents IA (Codex/Claude) pour l'assistance au développement et la revue de code.
- **Nettoyage :** Suppression de compétences et de scripts obsolètes dans les outils internes.
