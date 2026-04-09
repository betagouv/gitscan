## Changelog : cdata (30 derniers jours, au 9 avril 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de l'interface utilisateur, la correction de bugs et la modernisation de la stack technologique. L'application a été mise à jour vers Nuxt 4.0 et 3.18, apportant des améliorations de performance et de stabilité. Des améliorations ont également été apportées à la recherche, à la gestion des ressources et à la page de modération.

### Évolutions fonctionnelles
- Ajout du support des "Topics" dans la recherche globale, permettant une recherche plus précise et ciblée. [#1030](https://github.com/datagouv/cdata/issues/1030)
- Amélioration de la page de modération avec des informations supplémentaires sur les previews. [#1021](https://github.com/datagouv/cdata/issues/1021)
- Ajout d'informations sur les définitions de catégories restreintes. [#1017](https://github.com/datagouv/cdata/issues/1017)
- Amélioration de l'affichage des ressources avec des informations sur les en-têtes CORS. [#954](https://github.com/datagouv/cdata/issues/954)
- Ajout de liens de téléchargement WFS sur la carte. [#972](https://github.com/datagouv/cdata/issues/972)
- Amélioration de l'affichage des URL de téléchargement du catalogue dans les statistiques. [#998](https://github.com/datagouv/cdata/issues/998)
- Mise à jour de la page d'accueil avec une nouvelle conception et description. [#981](https://github.com/datagouv/cdata/issues/981)
- Ajout d'informations sur les limitations de débit (rate limiting) pour les services de données. [#1005](https://github.com/datagouv/cdata/issues/1005)
- Amélioration de l'encodage des URI pour les oEmbeds. [#994](https://github.com/datagouv/cdata/issues/994)

### Évolutions techniques
- Mise à jour vers Nuxt 4.0 (minimal). [#1023](https://github.com/datagouv/cdata/issues/1023)
- Mise à jour vers Nuxt 3.18 et 3.17. [#1009](https://github.com/datagouv/cdata/issues/1009), [#1008](https://github.com/datagouv/cdata/issues/1008)
- Mise à jour de Node.js vers la version 24. [#1011](https://github.com/datagouv/cdata/issues/1011)
- Refactorisation pour supprimer les duplications entre les previews. [#1018](https://github.com/datagouv/cdata/issues/1018)
- Correction d'un bug empêchant la construction des assets en mode développement. [#1024](https://github.com/datagouv/cdata/issues/1024)
- Mise à jour des versions des actions CI/CD. [#1013](https://github.com/datagouv/cdata/issues/1013)
- Correction d'un problème de réactivité entre Nuxt et non-Nuxt. [#987](https://github.com/datagouv/cdata/issues/987)
- Amélioration du chargement initial du serveur Vite en mode développement. [#983](https://github.com/datagouv/cdata/issues/983)
- Suppression de code mort. [#1003](https://github.com/datagouv/cdata/issues/1003), [#982](https://github.com/datagouv/cdata/issues/982)

### Autres changements
- Correction d'une erreur d'affichage des valeurs manquantes pour les sujets (topics). [#1032](https://github.com/datagouv/cdata/issues/1032)
- Amélioration de la formulation pour les jeux de données liés aux schémas. [#1019](https://github.com/datagouv/cdata/issues/1019)
- Correction de problèmes de responsive design sur la liste des cartes et la hauteur de ReadMore. [#993](https://github.com/datagouv/cdata/issues/993), [#997](https://github.com/datagouv/cdata/issues/997)
- Correction de problèmes de validation pour les ressources communautaires. [#990](https://github.com/datagouv/cdata/issues/990)
- Publication des composants datagouv. [#985](https://github.com/datagouv/cdata/issues/985)
- Mise à jour de la version des composants. [#988](https://github.com/datagouv/cdata/issues/988)
- Correction d'un revert précédent. [#1029](https://github.com/datagouv/cdata/issues/1029)
- Tentative de correction des tests flaky. [#1028](https://github.com/datagouv/cdata/issues/1028), [#979](https://github.com/datagouv/cdata/issues/979)
