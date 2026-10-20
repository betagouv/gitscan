## Changelog : espace-membre-next (30 derniers jours, au 19 octobre 2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur la sécurisation des accès via l'amélioration du parcours d'authentification (ProConnect et MFA) et l'ouverture de l'écosystème grâce à une nouvelle API REST. Des corrections importantes ont également été apportées à la gestion des formations, des formulaires de demande et de la synchronisation des adresses e-mail professionnelles.

### Évolutions fonctionnelles
- **Authentification et sécurité** :
    - Amélioration du parcours de connexion ProConnect, incluant la gestion du MFA par lien magique [#1569] et la possibilité de relancer une session après un refus [#1597].
    - Meilleure gestion des adresses e-mail lors de la connexion (distinction entre e-mail personnel et principal) [#1596].
- **Gestion des formations** :
    - Corrections sur le module e-learning, la gestion des adresses pour le présentiel et la logique des listes d'attente pour les sessions sans limite [#1558, #1564].
- **Services et formulaires** :
    - Optimisation des formulaires de demandes d'OPS [#1554] et d'accès Ségur [#1553].
    - Mise à jour de la navigation vers les services et correction des événements de calendrier [#1545, #1547].
- **Communication** :
    - Amélioration de la synchronisation, du statut et de la réactivation des adresses Dimail [#1588].

### Évolutions techniques
- **API et Intégration** :
    - Lancement de l'API v1 REST avec support de clés d'API à portée restreinte pour plus de sécurité [#1518].
- **Infrastructure et Automatisation** :
    - Refonte de l'architecture des tâches planifiées (cron) avec des créneaux fixes déclarés dans le code pour une meilleure stabilité [#1590].
    - Corrections liées au déploiement et à la syntaxe des tâches cron sur Scalingo [#1595, #1555].
- **Qualité et Tests** :
    - Renforcement de la couverture de tests, notamment sur la connexion par e-mail [#1566] et la resynchronisation des tests unitaires imbriqués [#1594].

### Autres changements
- Amélioration de la documentation des alertes avec l'ajout de liens vers les référents techniques [#1544].
- Ajout de l'onboarding pour les développeurs dans le cadre des challenges communautaires [#1565].
