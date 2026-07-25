## Changelog : inclusion-connect (30 derniers jours, au 24 juillet 2026)

### Résumé
Les récentes évolutions d'inclusion-connect se concentrent sur l'amélioration de la flexibilité de la configuration, notamment en mode démonstration, et sur la stabilisation de l'infrastructure via des mises à jour de dépendances et des corrections de CI/CD. Une amélioration de la gestion des domaines OIDC a également été apportée.

### Évolutions fonctionnelles
- Possibilité de choisir le prénom et le nom lors de l'utilisation du mode démonstration. [#190af3c](https://github.com/gip-inclusion/inclusion-connect/commit/190af3c)
- Amélioration de la configuration OIDC : autorise l'utilisation de caractères génériques dans le domaine. [#4181e6e](https://github.com/gip-inclusion/inclusion-connect/commit/4181e6e)
- Modification des URI de redirection par défaut dans les tests pour une meilleure cohérence. [#3971fa7](https://github.com/gip-inclusion/inclusion-connect/commit/3971fa7)

### Évolutions techniques
- Intégration de l'outil `djlint` pour l'analyse statique du code et l'amélioration de la qualité. [#0e39f2b](https://github.com/gip-inclusion/inclusion-connect/commit/0e39f2b)
- Épinglage des versions des actions GitHub pour une meilleure reproductibilité des builds CI/CD. [#3cc3e7e](https://github.com/gip-inclusion/inclusion-connect/commit/3cc3e7e)
- Mises à jour de plusieurs dépendances (Django, Sentry, Faker, etc.) pour bénéficier des dernières corrections de bugs et améliorations de sécurité.

### Autres changements
- Rétractation temporaire de l'ajout d'une bannière de démonstration. [#f1ec916](https://github.com/gip-inclusion/inclusion-connect/commit/f1ec916)
