## Changelog : Docurba (30 derniers jours, au 09/11/2026)

### Résumé
Ce mois-ci, Docurba a bénéficié d'une refonte majeure de l'interface de gestion des autorités territoriales et d'une amélioration significative de la gestion des procédures (noms, types et filtrage). L'expérience utilisateur est fluidifiée par de nouveaux indicateurs visuels et une gestion plus robuste des données, tandis que la sécurité et la structure de l'API ont été renforcées.

### Évolutions fonctionnelles
- **Gestion des autorités territoriales** : Refonte complète des pages de détails et des sous-pages ; mise en place d'une vue par défaut basée sur le profil utilisateur et intégration de GeoRisques comme page de données par défaut.
- **Amélioration de la gestion des procédures** : 
    - Affichage des commentaires de dépôt et des détails du nom des procédures directement dans les tableaux.
    - Ajout de nouveaux filtres, notamment pour le PLUi.
    - Intégration d'indicateurs visuels liés à la loi Huwart (affichage dans les en-têtes et indicateurs de date).
- **Expérience utilisateur (UX)** : 
    - Automatisation du calcul des noms de procédures dans les formulaires avec une meilleure gestion des erreurs.
    - Optimisation des modes d'édition par défaut (mode édition pour le cadre PAC) et masquage des sections vides dans les aperçus.
    - Amélioration de la gestion des droits pour les administrateurs PAC.

### Évolutions techniques
- **Backend (Django)** :
    - Refonte de la logique métier des procédures : centralisation du calcul des noms (`computed_name`), gestion optimisée des types de documents et des règles pour les procédures sectorielles.
    - Optimisation des performances via la mise en cache du périmètre des procédures.
    - Enrichissement de l'API interne pour exposer de nouvelles données (noms calculés, dates d'approbation) et améliorer le filtrage.
    - Migration et nettoyage des énumérations (`enums`) pour une meilleure structure du code.
- **Frontend (Nuxt)** :
    - Migration des appels API vers un plugin dédié pour une meilleure gestion de l'authentification et de l'URL de base.
    - Amélioration de la gestion des données territoriales (distinction entre codes INSEE et SIREN, restauration des champs région).
    - Sécurisation des requêtes Supabase (gestion de la casse pour les emails).
- **Infrastructure & CI/CD** :
    - Amélioration du cycle de vie des "Review Apps" (création et suppression).

### Autres changements
- Documentation de scripts internes.
- Nettoyage du code (suppression de commandes de gestion obsolètes, suppression de snapshots orphelins et mise en conformité Ruff).
