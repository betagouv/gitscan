## Changelog : mission-transition-ecologique (30 derniers jours, au 7 mai 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la fiabilité des tests automatisés, notamment les tests de bout en bout (E2E), et sur la mise à jour régulière des données des programmes d'aides à la transition écologique. Des ajustements techniques ont également été apportés pour assurer la compatibilité et la bonne exécution des outils de test.

### Évolutions fonctionnelles
- Amélioration de la fiabilité des tests E2E grâce à l'utilisation de données de test générées dynamiquement et à la réduction des faux échecs dans l'environnement d'intégration continue. [#2590](https://github.com/betagouv/mission-transition-ecologique/issues/2590)
- Extension des dates de validité des données de test dans le fichier `programs_tests.json` jusqu'en 2027 pour assurer la pérennité des tests.

### Évolutions techniques
- Mise à jour de la commande Playwright pour utiliser `npx` afin d'assurer une exécution correcte des tests.
- Amélioration de la configuration de Playwright et de la gestion des réponses des formulaires dans les tests.
- Mise à jour des dépendances et des données des programmes et projets via les workflows automatisés.

### Autres changements
- Mises à jour régulières des données des programmes et des projets via les workflows automatisés (plusieurs mises à jour).
