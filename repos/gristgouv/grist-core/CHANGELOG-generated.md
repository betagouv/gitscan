## Changelog : grist-core (30 derniers jours, au 2026-05-05)

### Résumé
Les dernières semaines ont été marquées par des améliorations significatives de l'expérience utilisateur, notamment dans la configuration initiale (Quick Setup) et la gestion des applications OAuth. Des corrections de bugs et des optimisations de performance ont également été apportées, ainsi que des traductions pour plusieurs langues. Des efforts ont été faits pour améliorer la sécurité et la robustesse de la plateforme.

### Évolutions fonctionnelles
- **Configuration initiale (Quick Setup):** Amélioration du processus de configuration initiale avec l'ajout de sections pour les sauvegardes et la configuration du serveur. [#2283](https://github.com/gristgouv/grist-core/issues/2283), [#2293](https://github.com/gristgouv/grist-core/issues/2293)
- **Authentification:** Ajout d'une interface pour la gestion des applications OAuth, permettant aux utilisateurs de connecter Grist à d'autres services. [#2285](https://github.com/gristgouv/grist-core/issues/2285)
- **Recherche:** La recherche dans les documents est désormais insensible à la casse et aux accents. [#2221](https://github.com/gristgouv/grist-core/issues/2221)
- **Menu contextuel:** Possibilité d'ouvrir le menu contextuel via des raccourcis clavier dans les widgets. [#2226](https://github.com/gristgouv/grist-core/issues/2226)
- **Nouvel enregistrement:** Amélioration de l'expérience utilisateur pour l'ajout de nouveaux enregistrements. [#2312](https://github.com/gristgouv/grist-core/issues/2312)
- **API:** Ajout d'un endpoint POST `/records/list` pour la gestion des enregistrements. [#2321](https://github.com/gristgouv/grist-core/issues/2321)
- **Permissions:** Affichage des options de permissions par défaut dans le panneau d'administration. [#2314](https://github.com/gristgouv/grist-core/issues/2314)

### Évolutions techniques
- **Refactoring:** Refactorisation du code pour améliorer la lisibilité et la maintenabilité, notamment au niveau des types `ISandbox`. [#2211](https://github.com/gristgouv/grist-core/issues/2211)
- **Tests:** Amélioration de la robustesse des tests, notamment en corrigeant des problèmes de "flakiness" et en adaptant les tests pour les nouvelles versions de Chrome. [#2214](https://github.com/gristgouv/grist-core/issues/2214), [#2300](https://github.com/gristgouv/grist-core/issues/2300), [#2320](https://github.com/gristgouv/grist-core/issues/2320)
- **Sécurité:** Correction d'un problème de gestion des origines opaques pour les requêtes CORS. [#2299](https://github.com/gristgouv/grist-core/issues/2299)
- **Gestion des sessions:** Amélioration de la gestion des sessions pour éviter la pollution lors de l'utilisation d'une clé API. [#2246](https://github.com/gristgouv/grist-core/issues/2246)
- **Dépendances:** Mise à jour de plusieurs dépendances, notamment `axios`, `fast-xml-parser`, `svgo`, `flatted`, `follow-redirects`, `dompurify`, `basic-ftp`, `@xmldom/xmldom` et `uuid`. (Ces mises à jour sont listées dans les commits mais ne sont pas détaillées ici).
- **Intégration continue:** Amélioration des tests et de l'intégration continue.

### Autres changements
- **Documentation:** Mise à jour de la documentation pour faciliter l'exécution des tests nbrowser en local. [#2214](https://github.com/gristgouv/grist-core/issues/2214)
- **Traductions:** Ajout et mise à jour de traductions en suédois, basque et hongrois.
- **Linting:** Ajout d'une règle ESLint pour améliorer la qualité du code et la cohérence des appels de traduction. [#2237](https://github.com/gristgouv/grist-core/issues/2237)
- **Nettoyage de code:** Diverses corrections et améliorations du code pour une meilleure maintenabilité.
