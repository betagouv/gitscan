## Changelog : mission-transition-ecologique (30 derniers jours, au 29 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la fiabilité des tests automatisés, l'ajout de témoignages sur la page "À propos" et l'intégration d'un script pour afficher des informations sur les entreprises via leur numéro SIRET. Des mises à jour de sécurité et des corrections concernant l'exécution des tests Playwright ont également été apportées. Enfin, les jeux de données des programmes et projets ont été mis à jour.

### Évolutions fonctionnelles
- Ajout de témoignages sur la page "À propos" pour illustrer l'impact de la plateforme. [#2572](https://github.com/betagouv/mission-transition-ecologique/issues/2572)
- Intégration d'un script permettant d'afficher des informations sur une entreprise à partir de son numéro SIRET via un iframe. [#2571](https://github.com/betagouv/mission-transition-ecologique/issues/2571)

### Évolutions techniques
- Amélioration de la fiabilité des tests E2E (end-to-end) en utilisant des données de test générées dynamiquement et en ajoutant des mécanismes pour réduire les faux échecs (anti-flakiness) dans la CI. [#2590](https://github.com/betagouv/mission-transition-ecologique/issues/2590)
- Mise à jour de la commande Playwright pour utiliser `npx` pour l'exécution, assurant une meilleure compatibilité et gestion des versions.
- Mise à jour de la configuration de Playwright et amélioration de la gestion des réponses des formulaires.
- Mise à jour de sécurité. [#2551](https://github.com/betagouv/mission-transition-ecologique/issues/2551)

### Autres changements
- Mise à jour régulière des jeux de données des projets et des programmes. (plusieurs commits)
