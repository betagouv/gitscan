## Changelog : ma-cantine (30 derniers jours, au 22 octobre 2026)

### Résumé
Ce mois-ci a été marqué par une préparation intensive de la campagne de télédéclaration 2026, avec l'intégration de nouveaux indicateurs et une interface de saisie simplifiée. Parallèlement, la plateforme a considérablement renforcé sa traçabilité des données et sa sécurité pour mieux accompagner les acteurs de la restauration.

### Évolutions fonctionnelles
- **Télédéclaration** : Optimisation de l'expérience de saisie avec l'ajout du remplissage automatique, de boutons de saisie rapide et d'une gestion dynamique des erreurs en temps réel [#7384, #7377, #7323, #7174, #7175].
- **Télédéclaration** : Mise à jour pour la campagne 2026 incluant de nouveaux champs obligatoires (origine, circuit court, local, pêche durable, fermier) et une meilleure gestion des étapes [#7326, #7325, #7180, #7148, #7230].
- **Télédéclaration** : Amélioration du suivi et de la synthèse (nouveaux graphiques EGalim, macarons de progression, récapitulatifs des volets et affichage des coûts repas) [#7361, #7343, #7369, #7355, #7176].
- **Diagnostics** : Enrichissement des indicateurs de performance avec de nouveaux calculs de pourcentages par origine, circuit court et local [#7364, #7345].
- **Utilisateurs & Sécurité** : Simplification de la gestion des comptes (suppression du champ "username") et renforcement de la protection contre les attaques XSS et la divulgation d'informations lors de la récupération de compte [#7228, #7397, #7396, #7395, #7393].

### Évolutions techniques
- **Traçabilité** : Mise en place d'un nouveau modèle de journalisation (EventLog) pour suivre précisément les imports, les appels API et les tâches asynchrones [#7311, #7321, #7322].
- **Data & ETL** : Optimisation des pipelines de données via dbt (utilisation de la commande `COPY` pour accélérer les transferts) et nettoyage des anciens exports devenus obsolètes [#7207, #7360, #7357, #7358].
- **Data & ETL** : Exportation des journaux d'événements vers le data warehouse pour analyse [#7354].
- **OAuth2** : Extension du système d'applications pour permettre l'association d'un nom d'entreprise [#7248, #7251].
- **CI/CD** : Amélioration des performances de la chaîne de tests (parallélisation des vCPU) et création d'une CI dédiée à dbt [#7240, #7162].
- **Base de données** : Optimisation de l'historique via le regroupement (squash) des migrations de la base de données [#7402].

### Autres changements
- **Documentation** : Mise à jour de la documentation de l'API (Swagger) et des guides d'onboarding pour les développeurs [#7302, #7247, #7259].
