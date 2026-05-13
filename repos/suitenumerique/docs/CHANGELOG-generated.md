## Changelog : docs (30 derniers jours, au 12 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la stabilité, la performance et l'expérience utilisateur. Des corrections de bugs ont été apportées pour améliorer la fiabilité de l'application, notamment en matière de gestion des documents, de collaboration et de chargement des commentaires. Des optimisations ont été réalisées pour améliorer la réactivité de l'interface et la gestion des ressources. De plus, la compatibilité avec les dernières versions de certaines dépendances a été assurée, et des améliorations d'accessibilité ont été implémentées.

### Évolutions fonctionnelles
- Ajout d'un squelette de chargement pour le contenu afin d'améliorer l'expérience utilisateur pendant le chargement des documents [#2254].
- Fermeture de la connexion WebSocket lorsque l'utilisateur change d'onglet, optimisant ainsi l'utilisation des ressources [#2264].
- Ajout d'un lien vers la documentation dans le menu d'aide pour faciliter l'accès aux ressources d'aide [#2222].
- Intégration de Crisp pour le support utilisateur, accessible depuis le menu d'aide [#2222].
- Prise en charge de la création de sous-documents à partir de fichiers [#1987].

### Évolutions techniques
- Migration de l'outil de construction de paquets de `pip` vers `uv` pour améliorer la gestion des dépendances et la performance de construction.
- Mise à jour de l'image Nginx dans le Dockerfile vers la dernière version pour bénéficier des correctifs de sécurité et des améliorations de performance [#4fe508b].
- Utilisation d'un runner `arm64` pour la construction des images pour l'architecture `arm64` [#c72336a].
- Mise en place d'une stratégie de nouvelle tentative pour les verrous de table lors de la création de documents, améliorant ainsi la robustesse du système [#a47c351].
- Implémentation des en-têtes `etag` et `last_modified` pour la récupération de contenu, permettant une meilleure gestion du cache et une réduction de la bande passante [#68f1600].
- Refactorisation du module `core/utils.py` pour une meilleure organisation du code [#8f67b37].
- Mise à jour de Docspec vers la version 3.0.x et adaptation de l'API du convertisseur [#2220].
- Utilisation de Uvicorn pour exécuter l'application Django en environnement de développement [#ef93763].

### Autres changements
- Mise à jour des chaînes de traduction (i18n) [#4d68f39].
- Ignorer le fichier `uv.lock` dans la tâche de vérification orthographique [#325284c].
- Correction de quelques problèmes de stabilité des tests de bout en bout [#c525694].
- Amélioration de la gestion des erreurs 5xx et structuration des alertes pour une meilleure accessibilité [#31fea43, #9a5d81f].
- Correction de typos dans le fichier `contributing.md` [#30ed563].
- Ajout de tests pour vérifier la compatibilité avec les nouvelles versions des dépendances.
- Mise à jour des dépendances : `next` (v16.2.6), `axios` (v1.15.2), `lxml` (v6.1.0), `uuid` (v14).
- Suppression de la logique de suppression manuelle des accès depuis le hook de déplacement de document [#0a7aa58].
- Correction de la gestion des interlinkings en mode impression [#3701fe5].
- Amélioration de la gestion des couleurs en collaboration [#0f527a7].
- Ajout d'un favicon par défaut [#ff176d6].
- Factorisation des tests E2E dans un workflow séparé [#d933435].
- Ajout du flag `last-failed` uniquement si `last-run` est renseigné dans le workflow CI [#d68d7ee].
