## Changelog : monlogementetudiant (30 derniers jours, au 18 novembre 2026)

### Résumé
Ce mois a été marqué par une montée en puissance des outils d'aide à la décision et de la fiabilité du système. Les étudiants bénéficient d'une recherche plus intuitive, de nouveaux outils de simulation de budget et d'un système d'alertes plus intelligent. Les bailleurs disposent désormais de tableaux de bord statistiques enrichis pour suivre leurs contacts et leur activité. En coulisses, une refonte majeure de la gestion des tâches automatiques et un renforcement massif des tests de sécurité garantissent une plateforme plus robuste et performante.

### Évolutions fonctionnelles
- **Expérience Étudiant** :
    - Refonte de l'interface de recherche : nouvelle barre de filtres avec tags et curseur de prix stable, et utilisation du Plan IGN pour une meilleure précision cartographique.
    - Amélioration de la carte : affichage de clusters de marqueurs colorés et popups de prévisualisation.
    - Nouveaux outils de gestion : génération de budgets au format PDF avec graphiques de répartition des dépenses et réorganisation du menu de l'espace étudiant.
    - Système d'alertes enrichi : suggestions de logements à proximité dans les emails [#437](https://github.com/betagouv/monlogementetudiant/pull/437) et rappels automatiques lorsque les objectifs personnels dépassent leur échéance [#436](https://github.com/betagouv/monlogementetudiant/pull/436).
- **Gestion Bailleurs & Administration** :
    - Statistiques avancées : nouveaux tableaux de bord pour suivre la modération, les parcours de contact, l'utilisation des services et l'efficacité des emails de rappel.
    - Qualification des demandes : collecte de nouvelles informations sur le profil étudiant (études) directement dans les formulaires de contact.
    - Gestion des résidences : possibilité de saisir des loyers et des surfaces avec décimales, et gestion simplifiée des photos de résidence.
    - Export de données : ajout de fonctionnalités d'export CSV pour les statistiques de contact et les enquêtes sur les bourses.

### Évolutions techniques
- **Infrastructure & Tâches de fond** :
    - Migration majeure du système de tâches planifiées (cron) vers `graphile-worker` pour une gestion plus robuste des files d'attente et des exécutions.
    - Création d'un nouveau package dédié aux processus de fond (`apps/worker`) et mise en place d'un lanceur de commandes "one-off" sur Scalingo.
    - Passage de la stack locale et de la CI à PostgreSQL 18.
- **Qualité & Tests** :
    - Extension massive de la couverture de tests de bout en bout (E2E) avec Playwright, couvrant l'intégralité des parcours critiques (recherche, favoris, création de résidence, espace étudiant).
    - Optimisation des pipelines CI : réutilisation du cache des dépendances et parallélisation des tests d'intégration pour réduire les temps de build.
- **Performance & API** :
    - Optimisation de la synchronisation géographique : réduction du nombre d'appels API en regroupant les requêtes par département.
    - Amélioration de la réactivité de l'interface via le streaming des établissements à proximité.

### Autres changements
- **Documentation** : mise à jour des documentations techniques concernant l'API, les nouveaux processus de déploiement et le fonctionnement des tests E2E.
- **Maintenance** : nettoyage des images Docker pour optimiser l'espace de stockage et suppression des redirections inutiles vers WordPress.
