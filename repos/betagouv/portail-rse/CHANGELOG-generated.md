## Changelog : portail-rse (30 derniers jours, au 23 octobre 2026)

### Résumé
Ce mois a été marqué par le déploiement majeur de la deuxième version (v2) de l'analyse par intelligence artificielle, offrant des capacités de synthèse plus poussées et de nouveaux modes d'export. Parallèlement, des efforts importants ont été consacrés au renforcement de la sécurité de la plateforme et à l'optimisation des outils de développement pour garantir une meilleure stabilité.

### Évolutions fonctionnelles
- **Lancement de l'analyse IA v2** : introduction d'un nouvel onglet dédié pour visualiser les analyses de nouvelle génération, avec des explications claires pour distinguer les résultats de la v1 et de la v2.
- **Nouvelles capacités d'export** : possibilité d'exporter les synthèses de l'analyse IA v2 au format Excel (.xlsx).
- **Amélioration de l'expérience utilisateur (UX)** :
    - Optimisation de l'affichage des résultats IA dans la section VSME.
    - Homogénéisation des icônes des onglets de synthèse.
    - Amélioration de la clarté du vocabulaire (passage de "Enjeux de durabilité" à "ESRS").
    - Correction de l'affichage des colonnes dans la partie CSRD.
- **Interface** : ajout des partenaires dans le pied de page du portail.
- **Fiabilité** : amélioration des messages d'erreur lors de l'authentification (OIDC) pour une meilleure compréhension par l'utilisateur.

### Évolutions techniques
- **Intelligence Artificielle** : architecture revue pour permettre le lancement de l'analyse v2 de manière totalement indépendante de la v1.
- **Performance** : mise en place d'un système de cache pour les indicateurs de rapport, réduisant significativement le nombre de requêtes nécessaires.
- **Sécurité** :
    - Mise à jour de Django et des certificats de sécurité.
    - Renforcement des contrôles d'accès sur certaines URL et sur les fragments de données liés au statut des analyses IA.
- **Infrastructure & Data** :
    - Migration vers une instance Metabase dédiée avec sa propre base de données.
    - Exportation des données de l'analyse IA v2 vers Metabase.
- **Qualité du code & CI/CD** :
    - Remplacement de la suite d'outils de formatage (Black, autoflake, etc.) par **Ruff** pour une exécution plus rapide.
    - Mise à jour et optimisation de la configuration des hooks de pré-commit.
- **Refactoring** : restructuration du code pour gérer la coexistence des versions d'analyse (v1/v2) via un renommage explicite des attributs et des méthodes.

### Autres changements
- **Documentation** : mise à jour de la documentation concernant la gestion des exceptions pour l'interface d'administration.
- **Configuration** : ajustements des commandes de déploiement (scalingo) et de la gestion des formats de date.
