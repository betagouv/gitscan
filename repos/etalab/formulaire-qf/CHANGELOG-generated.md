## Changelog : formulaire-qf (30 derniers jours, au 15 octobre 2026)

### Résumé
Les récentes évolutions se sont concentrées sur la fiabilisation des processus de test, l'amélioration de la confidentialité des données usagers et l'optimisation de l'environnement de développement pour les contributeurs.

### Évolutions fonctionnelles
- **Protection des données et confidentialité** : Amélioration de la sécurité des données en supprimant l'envoi des identités d'usagers et des détails de requêtes/réponses vers l'outil de suivi d'erreurs Sentry ([#393](https://github.com/etalab/formulaire-qf/pull/393)).

### Évolutions techniques
- **CI/CD** : Correction du pipeline d'intégration continue pour garantir l'exécution systématique des tests à chaque nouveau commit sur une pull request ([#397](https://github.com/etalab/formulaire-qf/pull/397)).
- **Compatibilité et correctifs** : 
    - Résolution de problèmes de déploiement liés à la compatibilité entre JSON 3 et Sprockets ([#398](https://github.com/etalab/formulaire-qf/pull/398)).
    - Correction d'une clé de version en double dans le format JSON 3 ([#391](https://github.com/etalab/formulaire-qf/pull/391)).
    - Typage de la version du quotient familial en chaîne de caractères pour assurer la cohérence des données.
- **Maintenance et base de données** : Préparation de la montée de version de GoodJob par l'application des migrations en attente ([#392](https://github.com/etalab/formulaire-qf/pull/392)).
- **Expérience développeur** : Mise en place de scripts pour faciliter l'utilisation de *worktrees* avec des bases de données et des ports isolés ([#394](https://github.com/etalab/formulaire-qf/pull/394)).

### Autres changements
- **Documentation** : Ajout du fichier `CLAUDE.md` répertoriant les commandes et les conventions de travail du dépôt.
- **Configuration** : Centralisation des paramètres de Logstasher dans un fichier de configuration dédié `logstasher.yml` ([#396](https://github.com/etalab/formulaire-qf/pull/396)).
