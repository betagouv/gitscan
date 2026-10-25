## Changelog : espace-membre-next (30 derniers jours, au 23 octobre 2026)

### Résumé
Ce mois-ci, les évolutions se sont concentrées sur la sécurisation et la fluidification de l'authentification (ProConnect et MFA), l'amélioration de l'accueil des nouveaux membres via une nouvelle checklist, et le lancement d'une première version de l'API REST pour faciliter les intégrations.

### Évolutions fonctionnelles
- **Authentification et sécurité** :
    - Amélioration du parcours de connexion ProConnect incluant le MFA avec transition par lien magique [#1569](https://github.com/betagouv/espace-membre-next/issues/1569).
    - Meilleure gestion des refus de connexion : affichage du motif de refus, possibilité de relancer la procédure et gestion des emails personnels [#1603](https://github.com/betagouv/espace-membre-next/issues/1603) [#1597](https://github.com/betagouv/espace-membre-next/issues/1597) [#1596](https://github.com/betagouv/espace-membre-next/issues/1596).
- **Expérience utilisateur et onboarding** :
    - Mise en place d'une checklist dédiée pour l'embarquement des nouveaux intrapreneur·es [#1580](https://github.com/betagouv/espace-membre-next/issues/1580).
- **API** :
    - Lancement de la version 1 de l'API REST avec support de clés d'API à portée restreinte [#1518](https://github.com/betagouv/espace-membre-next/issues/1518).
- **Gestion des services et formations** :
    - Amélioration de la synchronisation des adresses Dimail et de la réactivation automatique des boîtes mail [#1588](https://github.com/betagouv/espace-membre-next/issues/1588).
    - Corrections sur le module de formation : gestion de l'e-learning, des adresses en présentiel et de la logique des listes d'attente [#1558](https://github.com/betagouv/espace-membre-next/issues/1558) [#1564](https://github.com/betagouv/espace-membre-next/issues/1564).

### Évolutions techniques
- **CI/CD et Déploiement** :
    - Automatisation de la fusion (auto-merge) des Pull Requests d'export vers beta.gouv.fr [#1602](https://github.com/betagouv/espace-membre-next/issues/1602).
    - Correction du processus de déploiement pour l'application cron afin d'éviter le lancement des migrations en post-déploiement [#1595](https://github.com/betagouv/espace-membre-next/issues/1595).
- **Architecture et optimisation** :
    - Refactorisation de la gestion des tâches planifiées (cron) avec l'utilisation de créneaux fixes et de jobs déclarés directement dans le code [#1590](https://github.com/betagouv/espace-membre-next/issues/1590).
- **Tests** :
    - Renforcement de la suite de tests, notamment sur les processus de connexion par email et la synchronisation des spécifications de tests [#1566](https://github.com/betagouv/espace-membre-next/issues/1566) [#1594](https://github.com/betagouv/espace-membre-next/issues/1594).

### Autres changements
- **Documentation** : Ajout de l'onboarding développeur aux défis de la communauté [#1565](https://github.com/betagouv/espace-membre-next/issues/1565).
