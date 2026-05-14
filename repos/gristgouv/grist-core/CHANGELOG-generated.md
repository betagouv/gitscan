## Changelog : grist-core (30 derniers jours, au 2026-05-05)

### Résumé
Les dernières semaines ont été marquées par des améliorations significatives de l'expérience utilisateur, notamment dans la configuration initiale (Quick Setup) et la gestion des applications OAuth. Des corrections de bugs et des optimisations de performance ont également été apportées, ainsi que des mises à jour de dépendances pour assurer la sécurité et la stabilité du projet.

### Évolutions fonctionnelles
- **Configuration initiale :** Amélioration du processus de configuration initiale avec l'ajout de sections pour les sauvegardes et la configuration du serveur. [#2283](https://github.com/gristlabs/grist-core/issues/2283), [#2293](https://github.com/gristlabs/grist-core/issues/2293)
- **OAuth :** Implémentation de l'interface utilisateur et de l'API pour l'enregistrement et la gestion des applications OAuth, permettant une intégration plus facile avec d'autres services. [#2246](https://github.com/gristlabs/grist-core/issues/2246), [#2285](https://github.com/gristlabs/grist-core/issues/2285)
- **API :** Ajout d'un endpoint POST `/records/list` pour la création de listes d'enregistrements. [#2299](https://github.com/gristlabs/grist-core/issues/2299)
- **Widgets :** Le widget calendrier se charge maintenant à partir d'un plugin spécifique, favorisant les widgets intégrés. [#2262](https://github.com/gristlabs/grist-core/issues/2262)
- **Recherche :** La recherche dans un document est désormais insensible à la casse et aux accents. [#2221](https://github.com/gristlabs/grist-core/issues/2221)
- **Menu contextuel :** Possibilité d'ouvrir le menu contextuel via des raccourcis clavier dans les widgets. [#2226](https://github.com/gristlabs/grist-core/issues/2226)
- **Permissions par défaut :** Affichage des options de permissions par défaut dans le panneau d'administration. [#2314](https://github.com/gristlabs/grist-core/issues/2314)

### Évolutions techniques
- **Pyodide :** Mise à jour de Pyodide de la version 0.23.4 à la version 0.28.1. [#1754](https://github.com/gristlabs/grist-core/issues/1754)
- **Tests :** Amélioration de la robustesse des tests, notamment en corrigeant des problèmes de synchronisation et en ajustant les délais d'attente. [#2214](https://github.com/gristlabs/grist-core/issues/2214), [#2320](https://github.com/gristlabs/grist-core/issues/2320)
- **Refactoring :** Refactorisation du code pour améliorer la lisibilité et la maintenabilité, notamment au niveau des types `ISandbox`. [#2211](https://github.com/gristlabs/grist-core/issues/2211)
- **CI/CD :** Ajustements de la configuration CI/CD pour améliorer la stabilité et la performance des tests. [#2267](https://github.com/gristlabs/grist-core/issues/2267)
- **Gestion des sessions :** Prévention des modifications de sessions provenant de sessions préforkées dans la vérification de l'accès granulaire. [#2297](https://github.com/gristlabs/grist-core/issues/2297)
- **Docker :** Correction pour permettre à Grist de redémarrer sans supprimer le socket d'écoute. [#2265](https://github.com/gristlabs/grist-core/issues/2265)

### Autres changements
- **Traduction :** Mises à jour des traductions suédoises, basques et hongroises.
- **Documentation :** Adaptation de la documentation pour exécuter les tests nbrowser localement. [#2214](https://github.com/gristlabs/grist-core/issues/2214)
- **Dépendances :** Mises à jour de plusieurs dépendances, notamment `axios`, `fast-xml-parser`, `svgo`, `flatted`, `follow-redirects`, `dompurify`, `basic-ftp`, `@xmldom/xmldom` et `uuid`.
- **Linting :** Ajout d'une règle ESLint pour s'assurer que les appels à la fonction de traduction `t` sont corrects. [#2237](https://github.com/gristlabs/grist-core/issues/2237)
- **Nettoyage de code :** Diverses corrections et améliorations mineures du code.
