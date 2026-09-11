## Changelog : quefairedemesobjets (30 derniers jours, au 11 septembre 2026)

### Résumé
Ce mois-ci, le projet a connu des avancées significatives visant à améliorer la fluidité de l'expérience utilisateur (nouvelles cartes, formulaires enrichis) et à renforcer la robustesse de l'infrastructure. Les efforts se sont concentrés sur l'optimisation des performances du site, la sécurisation des accès et la stabilisation des environnements de déploiement et de test.

### Évolutions fonctionnelles
- **Interface & Expérience utilisateur**
  - Intégration d'une carte sur mesure au sein d'une fenêtre modale [#3071](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3071).
  - Ajout d'un champ de localisation dans le formulaire de contact pour enrichir les données collectées [#3300](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3300).
  - Amélioration de l'orientation des visiteurs sur les pages de contenu "Sites Conformes" [#3238](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3238).
  - Possibilité de configurer le texte indicatif (placeholder) du champ de recherche [#3198](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3198).
- **Corrections de bugs**
  - Résolution d'une erreur 500 lors de l'ajout de redirections de synonymes [#3200](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3200).
  - Correction d'un objet manquant dans les modales de partage des pages produits [#3174](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3174).
  - Amélioration de la qualité des données Open Data en interdisant les lignes vides dans les propositions de services [#3311](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3311).

### Évolutions techniques
- **Performance & Optimisation**
  - Optimisation des configurations Nginx et Gunicorn pour améliorer la réactivité du serveur [#3373](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3373).
  - Optimisation de la gestion des connexions à la base de données via l'application de `CONN_MAX_AGE` [#3364](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3364).
  - Utilisation des workers `gthread` de Gunicorn pour une meilleure gestion de la charge [#3362](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3362).
- **Infrastructure & Data**
  - Migration des bases de données Airflow et mise en place de Metabase sur Scaleway [#3384](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3384).
  - Mise à jour majeure d'Apache Airflow vers la version 3.3.1 [#3351](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3351).
  - Mise à jour du provider Scaleway pour Terragrunt [#3320](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3320).
  - Résolution de problèmes d'ordre d'exécution des tâches de calcul des acteurs [#3366](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3366).
- **Sécurité**
  - Mise en place d'une procédure de rotation des mots de passe [#3382](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3382).
  - Création d'utilisateurs Metabase en mode lecture seule pour limiter les risques [#3317](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3317).
  - Application de correctifs de sécurité divers [#3350](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3350).
- **CI/CD & DevOps**
  - Stabilisation des environnements de "preview" (correction des erreurs de déploiement et gestion de l'URL de base) [#3302](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3302), [#3353](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3353).
  - Correction d'un blocage sur la création de nouveaux buckets de preview [#3367](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3367).
- **Monitoring & Tests**
  - Ajout d'un pipeline de monitoring (DAG) pour le proxy Posthog [#3374](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3374).
  - Amélioration de la robustesse des tests de bout en bout (E2E) [#3294](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3294).
- **Refactoring**
  - Nettoyage des imports de fonctions utilitaires Django dans les fichiers Airflow [#3271](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3271).
  - Amélioration du contrôleur d'A/B testing [#3123](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3123).

### Autres changements
- **Maintenance & Configuration**
  - Nettoyage du dépôt : suppression de fichiers inutiles (`uv.lock`) [#3270](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3270) et mise à jour du `.gitignore` pour les caches npm [#55f9fdc](https://github.com/incubateur-ademe/quefairedemesobjets/issues/55f9fdc).
  - Ajustement de la configuration de Dependabot pour exclure certaines versions de TypeScript [#3375](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3375).
