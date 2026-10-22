## Changelog : api-subventions-asso (30 derniers jours, au 20 octobre 2026)

### Résumé
Ce mois a été principalement consacré à l'amélioration de l'expérience de recherche. Les utilisateurs bénéficient désormais d'une interface web plus riche (recherche avancée, historique, nouveaux affichages) et de résultats plus précis et complets grâce à l'intégration de nouvelles données et à une optimisation du moteur de recherche de l'API.

### Évolutions fonctionnelles
- **Amélioration de la recherche (Interface web) :**
    - Mise en place d'une recherche avancée [#4051](https://github.com/betagouv/api-subventions-asso/issues/4057).
    - Refonte visuelle de l'historique de recherche [#4050](https://github.com/betagouv/api-subventions-asso/issues/4058) et de l'affichage des résultats [#4044](https://github.com/betagouv/api-subventions-asso/issues/4059).
    - Ajout de la correction orthographique (spellcheck) dans les champs de saisie [#4051](https://github.com/betagouv/api-subventions-asso/issues/4051).
    - Corrections d'affichage sur les tags d'associations et les espacements [#4050](https://github.com/betagouv/api-subventions-asso/issues/4050).
- **Amélioration de l'API :**
    - Ajout du nom Sirene dans les résultats de recherche [#4061](https://github.com/betagouv/api-subventions-asso/issues/4065).
    - Correction de la gestion des identifiants RNA erronés pour les entités légales Sirene.
    - Amélioration de la robustesse de la recherche via une meilleure gestion de la casse des mots saisis.

### Évolutions techniques
- **Refactorisation et performance :**
    - Refonte complète du moteur de recherche de l'API [#4035](https://github.com/betagouv/api-subventions-asso/issues/4040).
    - Migration des composants frontend vers la nouvelle syntaxe "Svelte runes" pour optimiser la réactivité [#3969](https://github.com/betagouv/api-subventions-asso/issues/4011).
- **Tests et maintenance :**
    - Amélioration du fichier de test pour les tâches planifiées (cron) [#4047](https://github.com/betagouv/api-subventions-asso/issues/4063).
