## Changelog : referentiel-applications (30 derniers jours, au 2026-10-30)

### Résumé
Ce mois-ci, le projet a franchi des étapes importantes en matière d'accessibilité numérique (conformité RGAA) et d'enrichissement des capacités d'exportation de données (Excel, PowerPoint). Le renforcement de la sécurité et l'introduction de nouvelles fonctionnalités, comme les résumés quotidiens par email et la synchronisation avec Grist, ont également été au cœur des développements.

### Évolutions fonctionnelles
- **Exports et rapports :**
    - Ajout de l'exportation des cartes produits vers PowerPoint [#2833](https://github.com/dnum-mi/referentiel-applications/issues/2833).
    - Amélioration de l'export Excel : ajout de la pagination [#2829](https://github.com/dnum-mi/referentiel-applications/issues/2829), identification du statut actuel des applications [#3082](https://github.com/dnum-mi/referentiel-applications/issues/3082), et meilleure stabilité lors des sessions longues ou des renouvellements de session [#3171](https://github.com/dnum-mi/referentiel-applications/issues/3171), [#3150](https://github.com/dnum-mi/referentiel-applications/issues/3150).
    - Exportation des stacks technologiques avec filtrage par fin de vie [#2921](https://github.com/dnum-mi/referentiel-applications/issues/2921).
- **Accessibilité (RGAA) et Expérience Utilisateur :**
    - Améliorations majeures de l'accessibilité : gestion du focus pour les tableaux [#3007](https://github.com/dnum-mi/referentiel-applications/issues/3007), annonce des états de chargement (AppLoader) aux lecteurs d'écran [#3037](https://github.com/dnum-mi/referentiel-applications/issues/3037), et optimisation globale des flux de travail [#2875](https://github.com/dnum-mi/referentiel-applications/issues/2875).
    - Interface : renommage des filtres personnels [#3104](https://github.com/dnum-mi/referentiel-applications/issues/3104), mise à jour de la terminologie (passage de "fins de vie" à "technologies") [#3099](https://github.com/dnum-mi/referentiel-applications/issues/3099), et intégration de la gestion des logos dans les mises à jour et imports [#3086](https://github.com/dnum-mi/referentiel-applications/issues/3086).
- **Nouvelles fonctionnalités :**
    - Mise en place d'un système de résumé quotidien par email avec gestion du fuseau horaire de Paris [#3098](https://github.com/dnum-mi/referentiel-applications/issues/3098).
- **Recherche et Données :**
    - Amélioration de la recherche globale avec respect des permissions technologiques [#3176](https://github.com/dnum-mi/referentiel-applications/issues/3176) et restauration de la recherche par source de données [#3055](https://github.com/dnum-mi/referentiel-applications/issues/3055).
    - Ajout de la cible de révision EcoIndex dans le modèle de conformité [#3172](https://github.com/dnum-mi/referentiel-applications/issues/3172).

### Évolutions techniques
- **Sécurité et Authentification :**
    - Correction de plusieurs vulnérabilités sur des dépendances critiques (qs, deepmerge, pnpm, etc.) [#3088](https://github.com/dnum-mi/referentiel-applications/issues/3088), [#3080](https://github.com/dnum-mi/referentiel-applications/issues/3080), [#2898](https://github.com/dnum-mi/referentiel-applications/issues/2898), [#2862](https://github.com/dnum-mi/referentiel-applications/issues/2862).
    - Durcissement de l'authentification : application des claims JWT de confiance [#3039](https://github.com/dnum-mi/referentiel-applications/issues/3039) et limitation de l'impersonation des administrateurs [#3029](https://github.com/dnum-mi/referentiel-applications/issues/3029).
    - Sécurisation des logs en masquant les tokens API dans les requêtes HTTP [#3018](https://github.com/dnum-mi/referentiel-applications/issues/3018).
- **Backend et Infrastructure :**
    - Implémentation de la synchronisation avec Grist, incluant une gestion des conflits et un service de verrouillage (GristSyncLockService) [#2876](https://github.com/dnum-mi/referentiel-applications/issues/2876), [#3087](https://github.com/dnum-mi/referentiel-applications/issues/3087).
    - Amélioration de l'observabilité via l'ajout de logs pour les appels API vers Loki [#3028](https://github.com/dnum-mi/referentiel-applications/issues/3028).
    - Optimisation du pipeline CI/CD pour la publication des images lors des releases [#3079](https://github.com/dnum-mi/referentiel-applications/issues/3079).
    - Mise en place d'un système de gestion des fonctionnalités bêta (feature flags) [#3034](https://github.com/dnum-mi/referentiel-applications/issues/3034), [#3042](https://github.com/dnum-mi/referentiel-applications/issues/3042).

### Autres changements
- **Documentation :**
    - Déplacement des décisions d'architecture dans le dossier de documentation dédié [#3089](https://github.com/dnum-mi/referentiel-applications/issues/3089).
    - Documentation des processus de détection et de revue humaine des corrélations [#2922](https://github.com/dnum-mi/referentiel-applications/issues/2922).
    - Mise à jour de la documentation Grafana [#3035](https://github.com/dnum-mi/referentiel-applications/issues/3035).
