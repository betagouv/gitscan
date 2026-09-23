## Changelog : benefriches (30 derniers jours, au 22 septembre 2026)

### Résumé
Ce mois-ci, bénéfriches a franchi une étape importante dans l'amélioration de l'expérience utilisateur avec un nouveau parcours d'accueil (onboarding) plus fluide et un assistant de modification de site nettement plus intuitif. La précision des analyses a également été renforcée par l'intégration de nouvelles données statistiques et l'actualisation des données foncières.

### Évolutions fonctionnelles
- **Amélioration de l'expérience utilisateur (UX) :**
    - Refonte complète du parcours d'onboarding avec un nouveau flux en 3 étapes.
    - Modernisation de l'assistant de modification de site (wizard) : ajout d'un indicateur d'état de sauvegarde, d'avertissements en cas de modifications non enregistrées et d'une navigation plus cohérente.
    - Ajout de points d'entrée directs pour "Modifier le site" depuis les pages de résumé et d'évaluation.
- **Précision des données et des calculs :**
    - Enrichissement des statistiques urbaines avec l'intégration des données de l'ANCT (Observatoire des territoires).
    - Mise à jour des données DVF avec les transactions de 2025 et ajout des données relatives aux terrains.
    - Affinement des algorithmes de calcul d'impact (zonage ABC) et optimisation des conditions de calcul pour éviter les résultats non significatifs.
- **Corrections d'interface :**
    - Amélioration de l'autocomplétion des adresses et de la gestion de la navigation lors de la saisie.
    - Corrections de textes et de mise en forme dans les descriptions de sites et de sols.

### Évolutions techniques
- **Refonte de l'architecture front-end :**
    - Migration massive des flux de création de sites (sites classiques, zones urbaines, sites express) vers un nouveau moteur de formulaires unifié (*wizard-form engine*).
    - Optimisation de la gestion des modales d'impact via les paramètres d'URL.
- **Évolutions de l'API et du backend :**
    - Ajout d'un endpoint de mise à jour des sites (`PUT /sites/:siteId`).
    - Amélioration de la robustesse de l'intégration CRM (gestion des erreurs, nettoyage des caractères spéciaux, synchronisation des contacts).
    - Augmentation des limites de requêtes (*rate limiting*) pour améliorer la disponibilité.
    - Mise en place d'un mécanisme de révocation des jetons d'authentification.
- **Qualité et Tests :**
    - Extension significative de la couverture de tests de bout en bout (E2E) sur les flux de mise à jour et d'inéligibilité.
    - Introduction de tests de régression pour l'accessibilité (ARIA snapshots) et le comportement métier.

### Autres changements
- **Documentation :** Fusion et simplification de la documentation des scripts API.
- **SEO & Web :** Ajout des balises de vérification pour Google Search Console.
- **Outils de développement :** Mise à jour des configurations pour les outils d'assistance au code (Claude/Codex).
