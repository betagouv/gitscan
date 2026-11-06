## Changelog : ami-system-tests (30 derniers jours, au 30 octobre 2026)

### Résumé
Ce mois a été marqué par une modernisation profonde de l'infrastructure de tests. Le projet a migré vers une nouvelle version majeure de son moteur de test (WebdriverIO 10) et a totalement repensé son système d'automatisation (CI/CD) pour gagner en fiabilité et en clarté. Ces changements permettent de mieux valider les parcours utilisateurs sur mobile (iOS/Android) et sur le web, tout en offrant des rapports d'erreurs beaucoup plus précis pour les développeurs.

### Évolutions fonctionnelles
*Note : S'agissant d'un dépôt de tests, ces évolutions concernent la couverture et la fiabilité des scénarios de validation.*

- **Élargissement de la couverture Webapp** : Intégration de nouveaux parcours de tests pour l'agenda, le profil utilisateur, les services et le suivi des démarches.
- **Amélioration des tests mobiles** :
    - Renforcement de la validation des notifications (push natifs et centre de notifications) sur Android et iOS.
    - Meilleure gestion des scénarios d'onboarding (choix des zones géographiques et gestion du consentement).
    - Fiabilisation des parcours d'authentification FranceConnect sur les plateformes mobiles.
- **Précision des scénarios** : Refonte de la nomenclature des tests pour mieux distinguer les tests de "fumée" (smoke), les parcours utilisateurs complets et les cas d'usage spécifiques.

### Évolutions techniques
- **Migration majeure** : Passage à WebdriverIO 10, incluant la mise à jour des sélecteurs vers les standards natifs du framework. [#82](https://github.com/numerique-gouv/ami-system-tests/pull/82)
- **Refonte de la CI/CD (GitHub Actions)** :
    - Mise en place d'un système de commentaires automatisés sur les Pull Requests pour un meilleur suivi des résultats.
    - Migration du reporting : remplacement d'Allure par des rapports JUnit enrichis, incluant des liens directs vers les traces Sentry en cas d'échec.
    - Optimisation de la gestion des secrets et des artefacts pour plus de sécurité et de performance.
    - Standardisation des environnements d'exécution (utilisation d'images Ubuntu 24.04 figées).
- **Architecture des tests** :
    - Refactorisation massive des *Page Objects* et des *Locators* pour supporter nativement la distinction entre les contextes Web, Android et iOS.
    - Simplification du design global (principe KISS) pour réduire la complexité du code de test.
    - Optimisation des performances : réduction des commandes WebDriver inutiles et gestion plus intelligente des rechargements de pages.
- **Gestion des plateformes et outils** :
    - **Appium** : Simplification de l'installation des drivers et meilleure gestion des émulateurs/simulateurs.
    - **Outil `just`** : Refonte complète de l'interface en ligne de commande pour simplifier le lancement des tests et la gestion des appareils.
    - **Gestion des sessions** : Amélioration de la capacité des tests à revenir à un état initial stable (accueil de l'application) après chaque scénario.

### Autres changements
- **Documentation** : Mise à jour massive de la documentation technique (README, CONTRIBUTING, modèles de tests) et ajout de notes d'architecture (ADR).
- **Nettoyage** : Suppression de nombreux scripts obsolètes, de workflows d'exemple et de code mort.
- **Configuration** : Standardisation de la gestion des variables d'environnement via des fichiers `.env` structurés.
