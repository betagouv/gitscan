## Changelog : lab-anssi-lib (30 derniers jours, au 27 juillet 2026)

### Résumé
Cette version apporte des améliorations à l'intégration avec le CMS Crisp, notamment l'exposition des dates de création, modification et publication du contenu. Des corrections de typage et des mises à jour de sécurité ont également été intégrées. La configuration du projet a été revue pour intégrer Renovate, un outil d'automatisation des mises à jour de dépendances.

### Évolutions fonctionnelles
- L'adaptateur Crisp expose désormais les dates de création, modification et publication du contenu. [#3fe4044](https://github.com/betagouv/lab-anssi-lib/commit/3fe4044)
- Correction d'un problème de typage dans les mocks de test. [#3fe4044](https://github.com/betagouv/lab-anssi-lib/commit/3fe4044)

### Évolutions techniques
- Ajout d'une configuration Renovate pour la gestion automatisée des dépendances. [#2608928](https://github.com/betagouv/lab-anssi-lib/commit/2608928)
- Mise à jour de la version de la librairie. [#da6cf5a](https://github.com/betagouv/lab-anssi-lib/commit/da6cf5a), [#eea034b](https://github.com/betagouv/lab-anssi-lib/commit/eea034b)
- Mises à jour de sécurité pour les dépendances Axios et qs. [#3f67320](https://github.com/betagouv/lab-anssi-lib/commit/3f67320), [#86dec17](https://github.com/betagouv/lab-anssi-lib/commit/86dec17)
- Suppression des exceptions pour Axios et QS. [#d4050ab](https://github.com/betagouv/lab-anssi-lib/commit/d4050ab), [#110f63f](https://github.com/betagouv/lab-anssi-lib/commit/110f63f)

### Autres changements
- Améliorations de la sécurité du CI/CD : validation des configurations et désactivation des identifiants `git` des dépôts clonés. [#c51472b](https://github.com/betagouv/lab-anssi-lib/commit/c51472b), [#bb4d55d](https://github.com/betagouv/lab-anssi-lib/commit/bb4d55d)
