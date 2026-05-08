## Changelog : mission-transition-ecologique (30 derniers jours, au 7 mai 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la fiabilité des tests automatisés, la correction de vulnérabilités de sécurité et l'ajout de témoignages à la page "À propos" pour valoriser l'impact de la plateforme. Des mises à jour régulières des données des programmes et projets ont également été effectuées.

### Évolutions fonctionnelles
- Ajout de témoignages à la page "À propos" pour illustrer l'impact de la plateforme. [#2572](https://github.com/betagouv/mission-transition-ecologique/issues/2572)
- Amélioration de la gestion des réponses des formulaires dans les tests E2E. [#2590](https://github.com/betagouv/mission-transition-ecologique/issues/2590)

### Évolutions techniques
- Fiabilisation des tests E2E en utilisant des données de test runtime et en ajoutant des mécanismes anti-flakiness dans la CI. [#2590](https://github.com/betagouv/mission-transition-ecologique/issues/2590)
- Mise à jour de la commande Playwright pour utiliser `npx` pour l'exécution.
- Mise à jour de la configuration de Playwright.
- Correction d'une vulnérabilité de sécurité. [#2551](https://github.com/betagouv/mission-transition-ecologique/issues/2551)
- Extension des dates de validité dans les données de test `programs_tests.json` jusqu'en 2027.

### Autres changements
- Mises à jour régulières des données des programmes et projets. (plusieurs PRs automatisés)
